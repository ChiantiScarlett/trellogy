from .components import List, Card
from .error import TrellogyError, InvalidListIDError
import requests


class Trellogy:
    def __init__(self, key, token, board_id, trash_id=None):
        self._key = key
        self._token = token
        self._board_id = board_id
        self._trash_id = trash_id

    def create_list(self, title: str, position='bottom') -> List:
        response = requests.post(
            'https://api.trello.com/1/boards/' +
            '{BOARD_ID}/lists?name={TITLE}&pos={POSITION}&key={KEY}&token={TOKEN}'.format(
                BOARD_ID=self._board_id,
                TITLE=title, POSITION=position,
                KEY=self._key, TOKEN=self._token,
            )
        )
        if response.status_code != 200:
            raise TrellogyError(response.json()['message'])

        return response.json()

    def get_lists(self) -> list:
        response = requests.get(
            'https://api.trello.com/1/boards/' +
            '{BOARD_ID}/lists?key={KEY}&token={TOKEN}'.format(
                BOARD_ID=self._board_id, KEY=self._key, TOKEN=self._token
            ))
        if response.status_code != 200:
            raise InvalidListIDError

        lists = []
        for list_item in response.json():
            lists.append(
                List(key=self._key, token=self._token, board_id=self._board_id,
                     trash_id=self._trash_id, list_id=list_item['id'],
                     name=list_item['name']))
        return lists

    def get_list(self, list_id: str) -> List:
        pass

    def create_card(self) -> Card:
        pass

    def read_card(self, card_id: str) -> Card:
        pass
