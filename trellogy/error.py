class InvalidAPIError(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "Invalid API KEY or API TOKEN."


class NoCardFoundError(Exception):
    def __init__(self, board_id):
        self.board_id = board_id

    def __str__(self):
        return "No board was found by the id `{}`.".format(self.board_id)


class NoListFoundError(Exception):
    def __init__(self, list_id):
        self.list_id = list_id

    def __str__(self):
        return "No list was found by the id `{}`.".format(self.list_id)


class NoCardFoundError(Exception):
    def __init__(self, card_id):
        self.card_id = card_id

    def __str__(self):
        return "No card was found by the id `{}`.".format(self.card_id)
