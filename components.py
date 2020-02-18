class List:
    def __init__(self, list_id):
        self.id = list_id


class Card:
    def __init__(self, card_id):
        self.id = card_id
        self.title = None
        self.members = None
        self.labels = None
        self.attachments = None
        self.due = None
        self.dueComplete = None
        self.idAttachmentCover = None
