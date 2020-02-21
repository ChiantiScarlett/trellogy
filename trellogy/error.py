class TrellogyError(Exception):
    def __init__(self, message):
        self._message = message

    def __str__(self):
        return self._message


class NotEnoughParamsError(Exception):
    def __init__(self, key):
        self._key = key

    def __str__(self):
        return "Value for the key `{}` was not given.".format(self._key)


class InvalidKeyTokenError(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "Invalid API KEY or API TOKEN."


class InvalidBoardIDError(Exception):
    def __init__(self, board_id):
        self.board_id = board_id

    def __str__(self):
        return "No board was found by the id `{}`.".format(self.board_id)


class InvalidListIDError(Exception):
    def __init__(self, list_id):
        self.list_id = list_id

    def __str__(self):
        return "No list was found by the id `{}`.".format(self.list_id)


class InvalidCardIDError(Exception):
    def __init__(self, card_id):
        self.card_id = card_id

    def __str__(self):
        return "No card was found by the id `{}`.".format(self.card_id)
