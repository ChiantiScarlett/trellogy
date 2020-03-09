from .error import TrellogyError, NotEnoughParamsError
from .component import Component


class Attachment(Component):
    def __init__(self, **kwargs):
        _attributes = ['id', 'card_id', 'size', 'name', 'url']
        super().__init__(**kwargs, _attributes=_attributes)

    def delete(self):
        path = '/cards/{CARD_ID}/attachments/{ATTACHMENT_ID}'\
            .format(CARD_ID=self._card_id, ATTACHMENT_ID=self._id)
        self.req('DELETE', path)
