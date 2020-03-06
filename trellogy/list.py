from .component import Component


class List(Component):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        attributes = ['name', 'closed', 'board_id', 'position']
        self.initialize_attributes(attributes, kwargs)
