from .error import TrellogyError
from .component import Component
from .label import Label


class Board(Component):
    def __init__(self, **kwargs):
        _attributes = []
        super().__init__(**kwargs, _attributes=_attributes)

    @property
    def labels(self):
        path = '/boards/{BOARD_ID}/labels'.format(BOARD_ID=self._id)
        response = self.req(path)
        labels = []
        for label in response:
            labels.append(Label(key=self._key,
                                token=self._token,
                                id=label['id'],
                                board_id=label['idBoard'],
                                name=label['name'],
                                color=label['color']))
        return labels
