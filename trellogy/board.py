from .error import TrellogyError, NotEnoughParamsError
from .component import Component
from .label import Label
from .list import List


class Board(Component):
    def __init__(self, **kwargs):
        _attributes = []
        super().__init__(**kwargs, _attributes=_attributes)

    @property
    def labels(self):
        path = '/boards/{BOARD_ID}/labels'.format(BOARD_ID=self._id)
        response = self.req('GET', path)
        labels = []
        for label in response:
            labels.append(Label(key=self._key,
                                token=self._token,
                                id=label['id'],
                                board_id=label['idBoard'],
                                name=label['name'],
                                color=label['color']))
        return labels

    def create_label(self, name=None, color=None):
        if name is None:
            raise NotEnoughParamsError('name')
        if color is None:
            raise NotEnoughParamsError('color')

        colors = ['yellow', 'purple', 'blue', 'red', 'green', 'orange',
                  'black', 'sky', 'pink', 'lime', 'null']
        if color.lower() not in colors:
            raise TrellogyError('`color` should be one of the followings: ' +
                                '[yellow, purple, blue, red, green, ' +
                                'orange, black, sky, pink, lime, null].')

        response = self.req('POST', '/labels',
                            name=name, color=color.lower(), idBoard=self._id)

        return Label(key=self._key,
                     token=self._token,
                     id=response['id'],
                     board_id=response['idBoard'],
                     name=response['name'],
                     color=response['color'])

    def create_list(self, name, position='bottom'):
        if name is None:
            raise NotEnoughParamsError('name')

        response = self.req('POST', '/boards/{}/lists'.format(self._id),
                            name=name, pos=position)

        return List(key=self._key, token=self._token, id=response['id'],
                    position=response['pos'], closed=response['closed'])
