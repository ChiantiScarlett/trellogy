from .components import List, Card
from .error import InvalidAPIError, NoListFoundError


class Trellogy:
    def __init__(self, API_KEY, API_TOKEN, board_id, trash_id=None):
        self.board_id = board_id
        self.trash_id = trash_id

    def create_list(self, title) -> Card:
        pass

    def read_list(self, list_id: str) -> List:
        pass

    def read_lists(self) -> list:
        pass

    def create_card(self) -> Card:
        pass

    def read_card(self, card_id: str) -> Card:
        pass
