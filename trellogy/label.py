from .error import TrellogyError, NotEnoughParamsError
from .component import Component


class Label(Component):
    def __init__(self, **kwargs):
        _attributes = ['id', 'board_id', 'name', 'color']
        super().__init__(**kwargs, _attributes=_attributes)

    def update(self, name=None, color=None):
        if name is None and color is None:
            raise TrellogyError('Need to give either name or color value.')

        if not name:
            name = self._name
        if not color:
            color = self._color

        colors = ['yellow', 'purple', 'blue', 'red', 'green', 'orange',
                  'black', 'sky', 'pink', 'lime', 'null']
        if color.lower() not in colors:
            raise TrellogyError('`color` should be one of the followings: ' +
                                '[yellow, purple, blue, red, green, ' +
                                'orange, black, sky, pink, lime, null].')

        self.req('PUT', '/labels/{}'.format(self._id),
                 name=name, color=color)

    def delete(self):
        self.req('DELETE', '/labels/{}'.format(self._id))
