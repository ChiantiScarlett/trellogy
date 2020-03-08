from .error import TrellogyError, NotEnoughParamsError
from .component import Component


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
        closed = {True: 'true', False: 'false'}[
            self._closed] if not closed else closed
        board_id = self._board_id if not board_id else board_id
        position = self._position if not position else position

        self.req('PUT', '/lists/{}'.format(self._id),
                 name=name, closed=closed,
                 board_id=board_id, position=position)

    def delete(self):
        self.req('DELETE', '/labels/{}'.format(self._id))
