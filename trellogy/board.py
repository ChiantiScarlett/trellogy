from .error import TrellogyError
from .component import Component
from .list import List
import requests


class Board(Component):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._name = None

    def create_list(self):
        pass

    @property
    def lists(self):
        response = requests.get(
            'https://api.trello.com/1/boards/' +
            '{BOARD_ID}/lists?key={KEY}&token={TOKEN}'.format(
                BOARD_ID=self._id, KEY=self._key, TOKEN=self._token
            ))
        if response.status_code != 200:
            raise TrellogyError(response.text)

        lists = []
        for list_item in response.json():
            lists.append(
                List(key=self._key,
                     token=self._token,
                     id=list_item['id'],
                     name=list_item['name'],
                     closed=list_item['closed'],
                     board_id=list_item['idBoard'],
                     position=list_item['pos']
                     ))
        return lists
