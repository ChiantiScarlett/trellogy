from .error import NotEnoughParamsError


class Component:
    def __init__(self, **kwargs):
        if 'key' not in kwargs.keys():
            raise NotEnoughParamsError('key')
        if 'token' not in kwargs.keys():
            raise NotEnoughParamsError('token')
        if 'id' not in kwargs.keys():
            raise NotEnoughParamsError('id')
        self._key = kwargs['key']
        self._token = kwargs['token']
        self._id = kwargs['id']

    def initialize_attributes(self, attributes, kwargs):
        for attribute in attributes:
            setattr(self, attribute, None)

        for key in kwargs:
            setattr(self, key, kwargs[key])
