from .error import InvalidKeyTokenError, InvalidListIDError, NotEnoughParamsError
import requests


class List:
    def __init__(self, **kwargs):
        try:
            self._key = kwargs['key']
            self._token = kwargs['token']
            self._board_id = kwargs['board_id']
            self._trash_id = kwargs['trash_id']
            self._id = kwargs['list_id']
            self._name = kwargs['name']
        except KeyError as error:
            raise NotEnoughParamsError(error.__str__())

        self._cards = None

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

    def read(self):
        url = 'https://api.trello.com/1/lists/' + \
            '{LIST_ID}/cards?fields=all&key={KEY}&token={TOKEN}'
        response = requests.get(url.format(
            LIST_ID=self._id, KEY=self._key, TOKEN=self._token
        ))
        if response.status_code != 200:
            raise InvalidListIDError

        self._cards = response.json()

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
