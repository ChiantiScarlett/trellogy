# trellogy

Trello Automation Project



```python
from trellogy.components import Board, List, Card
from trellogy.automation import Automator
```



```python
class List:
  self.id = None
  self.title = None
  self.labels = None
  self.attachments = None
  
class Card:
  self.id = None
  self.title = None
  self.members = None
  self.labels = None
  self.attachments = None
  self.due = None
  self.dueComplete = None
  self.idAttachmentCover = None
```







```python
trellogy = Trellogy(board_id="BOARD_ID", trash_id="TRASH_BIN_ID")

# Create
new_list = trellogy.create_list(title="TITLE")
new_list.update()

# Read single list
single_list = trellogy.read_list(list_id="LIST_ID")

# Read existing lists
trello_lists = trellogy.read_lists()
for trello_list in trello_lists:
  print(trello_list.id)

```



from trellogy



- class List
- class Card
- 









- Trellogy()
- trellogy.create_list(title, position)
- trellogy.read_list(list_id)
- trellogy.update_list(list_id, **params)
- trellogy.delete_list(list_id)
- trellogy.archive_list(list_id)
- trellogy.create_card(title, position, list_id)
- trellogy.update_card(card_id, **params)
- trellogy.delete_card(card_id)
- trellogy.archive_card(card_id)