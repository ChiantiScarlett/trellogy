from urllib.request import quote
from .error import TrellogyError, NotEnoughParamsError
from .component import Component
from .attachment import Attachment


class Card(Component):
    def __init__(self, **kwargs):
        _attributes = ['id', 'closed', 'name', 'desc', 'labels']
        super().__init__(**kwargs, _attributes=_attributes)

    def update(self, name=None, closed=None, desc=None, labels=None, board_id=None):

        name = self._name if name is None else name
        closed = self._closed if closed is None else closed
        desc = self._desc if desc is None else desc
        labels = self._labels if labels is None else labels
        board_id = self._board_id if board_id is None else board_id

        # Update labels
        labels_id = ",".join([label.id for label in labels])
        self.req('PUT', '/cards/{}'.format(self._id),
                 name=name, closed=self.bool_to_str[closed],
                 desc=quote(desc), idLabels=labels_id, idBoard=board_id)

    def archive(self):
        self.update(closed=True)

    def unarchive(self):
        self.update(closed=False)

    @property
    def attachments(self):
        path = '/cards/{CARD_ID}/attachments'.format(CARD_ID=self._id)
        response = self.req('GET', path)

        attachments = []
        for attachment in response:
            attachments.append(Attachment(key=self._key, token=self._token,
                                          card_id=self._id,
                                          id=attachment['id'],
                                          size=attachment['bytes'],
                                          name=attachment['name'],
                                          url=attachment['url']))
        return attachments
