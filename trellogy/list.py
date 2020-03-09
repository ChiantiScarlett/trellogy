from .error import TrellogyError, NotEnoughParamsError
from .component import Component
from .card import Card
from .label import Label


class List(Component):
    def __init__(self, **kwargs):
        _attributes = ['id', 'board_id', 'name', 'closed', 'position']
        super().__init__(**kwargs, _attributes=_attributes)

    def update(self, name=None, closed=None, board_id=None, position=None):
        if name is None and closed is None and \
                board_id is None and position is None:
            raise TrellogyError(
                'Need to give at least one parameter of the followings: ' +
                'name, closed, board_id, position')

        name = self._name if not name else name
        closed = self._closed if not closed else closed
        board_id = self._board_id if not board_id else board_id
        position = self._position if not position else position

        self.req('PUT', '/lists/{}'.format(self._id),
                 name=name, closed=self.bool_to_str[closed],
                 idBoard=board_id, pos=position)

    def delete(self):
        self.req('DELETE', '/labels/{}'.format(self._id))

    @property
    def cards(self):
        path = '/lists/{LIST_ID}/cards'.format(LIST_ID=self._id)
        response = self.req('GET', path, fields='all')

        cards = []
        for card in response:
            labels = []
            for label in card['labels']:
                labels.append(Label(key=self._key,
                                    token=self._token,
                                    board_id=self._board_id,
                                    id=label['id'],
                                    color=label['color'],
                                    name=label['name']
                                    ))

            cards.append(Card(key=self._key, token=self._token,
                              board_id=self._board_id,
                              list_id=self._id,
                              id=card['id'],
                              closed=card['closed'],
                              name=card['name'],
                              desc=card['desc'],
                              labels=labels
                              ))
        return cards
