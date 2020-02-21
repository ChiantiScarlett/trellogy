from .error import (TrellogyError,
                    NotEnoughParamsError, InvalidParamError)
import requests


class List:
    def __init__(self, **kwargs):
        try:
            self._key = kwargs['key']
            self._token = kwargs['token']
            self._idTrash = kwargs['idTrash']
            self._id = kwargs['id']
            self._name = kwargs['name']
            self._closed = kwargs['closed']
            self._idBoard = kwargs['idBoard']
            self._pos = kwargs['pos']

        except KeyError as error:
            raise NotEnoughParamsError(error.__str__())

        self._cards = None

    @property
    def idTrash(self):
        return self._idTrash

    @property
    def idBoard(self):
        return self._idBoard

    @property
    def closed(self):
        return self._closed

    @property
    def pos(self):
        return self._pos

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def cards(self):
        if self._cards is None:
            self.read()

        return self._cards

    def delete(self):
        self.update(idBoard=self._idTrash)

    def archive(self):
        url = 'https://api.trello.com/1/lists/' + \
            '{LIST_ID}/closed?value=true&key={KEY}&token={TOKEN}'
        response = requests.put(url.format(
            LIST_ID=self._id,
            KEY=self._key,
            TOKEN=self._token
        ))
        if response.status_code != 200:
            raise TrellogyError(response.text)

    def read(self):
        url = 'https://api.trello.com/1/lists/' + \
            '{LIST_ID}/cards?fields=all&key={KEY}&token={TOKEN}'
        response = requests.get(url.format(
            LIST_ID=self._id, KEY=self._key, TOKEN=self._token
        ))
        if response.status_code != 200:
            raise TrellogyError(response.text)

        self._cards = response.json()

    def update(self, **kwargs):
        VALID_KEYS = ['name', 'closed', 'idBoard', 'pos', 'subscribed']
        for key in kwargs.keys():
            if key not in VALID_KEYS:
                raise InvalidParamError(key)

        url = 'https://api.trello.com/1/lists/' + \
            '{LIST_ID}?key={KEY}&token={TOKEN}'.format(
                LIST_ID=self._id, KEY=self._key, TOKEN=self._token
            )

        params = map(lambda key: "{}={}".format(
            key, kwargs[key]), kwargs.keys())

        response = requests.put("&".join([url]+list(params)))

        if response.status_code != 200:
            print(response)

    def __repr__(self):
        return "<class 'trellogy.List'>"

    def __str__(self):
        return self._name


class Card:
    def __init__(self, card_id, trash_board=None):
        self._id = card_id
        self._title = None
        self._members = None
        self._labels = None
        self._attachments = None
        self._due = None
        self._dueComplete = None
        self._idAttachmentCover = None

    def to_json(self):
        """
        Convert current attributes to JSON object:
        """
        pass

    def update(self, **kwargs):
        """
        Update attributes according to kwargs:
        """
        pass

    def archive(self):
        """
        Archive this card:
        """
        pass

    def delete(self):
        """
        Move this card to the trash_board:
        """
        pass
