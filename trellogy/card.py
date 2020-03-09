from urllib.request import quote
from .error import TrellogyError, NotEnoughParamsError
from .component import Component


class Card(Component):
    def __init__(self, **kwargs):
        _attributes = ['id', 'closed', 'name', 'desc', 'labels']
        super().__init__(**kwargs, _attributes=_attributes)

    def update(self, name=None, closed=None, desc=None, labels=None):

        name = self._name if name is None else name
        closed = self._closed if closed is None else closed
        desc = self._desc if desc is None else desc
        labels = self._labels if labels is None else labels

        # Update labels
        labels_id = ",".join([label.id for label in labels])
        self.req('PUT', '/cards/{}'.format(self._id),
                 name=name, closed=self.bool_to_str[closed],
                 desc=quote(desc), idLabels=labels_id)

        # name = self._name if not name else name
        # closed = {True: 'true', False: 'false'}[
        #     self._closed] if not closed else closed
        # board_id = self._board_id if not board_id else board_id
        # position = self._position if not position else position

        # self.req('PUT', '/lists/{}'.format(self._id),
        #          name=name, closed=closed,
        #          board_id=board_id, position=position)

    def delete(self):
        pass
        # self.req('DELETE', '/labels/{}'.format(self._id))

    @property
    def cards(self):
        if self._cards is None:
            self.read()

        return self._cards

    def read(self):
        path = '/lists/{LIST_ID}/cards'.format(LIST_ID=self._id)
        response = self.req('GET', path, fields='all')

        print(response)
