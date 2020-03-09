from .error import TrellogyError, NotEnoughParamsError
from .component import Component
from .card import Card
from .label import Label
from .list import List


class TrashBin(Component):
    def __init__(self, **kwargs):
        _attributes = []
        super().__init__(**kwargs, _attributes=_attributes)

    def add(self, TrellogyComponent):
        if type(TrellogyComponent) in [List, Card]:
            print("adding")
            return TrellogyComponent.update(board_id=self._id)

        raise TrellogyError('TrashBin can only add List or Card component.')

    @property
    def name(self):
        path = '/boards/{BOARD_ID}/name'.format(BOARD_ID=self._id)
        response = self.req('GET', path)
        return response['_value']
