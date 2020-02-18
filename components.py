class List:
    def __init__(self, list_id):
        self.id = list_id

    def to_json(self):
        """
        Convert data to JSON object:
        """
        pass


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
