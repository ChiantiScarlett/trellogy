# Trellogy Documentation

[toc]

## trellogy.Trellogy

### [method] :: create_list(title, pos="bottom")

- **Description:** Create list to the Trello board.
- **Parameters:**
  - **title** (str):  Name for the list
  - **pos** (str): Position of the list. `top`, `bottom`, or a positive floating point number

- **Returns**: &lt;Trellogy.List&gt; object

### [method] :: get_list(list_id)

- **Description:** Createa <Trellogy.List> object based on the list ID
- **Parameters:**
  - **list_id** (str): ID of the Trello list
- **Returns**: <Trellogy.List> object

### [method] :: get_lists()

- **Description:** Read lists from  the Trello  board.

- **Parameters:** None

- **Returns**: list of <Trellogy.List> objects

  

## trellogy.List

### [method] :: update(**kwargs)

- **Description:** Update property of the Trello list.
- **Parameters:**
  - **name** (str): New name for the list
  - **closed** (bool): Whether the list should be closed (archived)
  - **idBoard** (str): ID of a board the list should be moved to
  - **pos** (str): New position for the list: `top`, `bottom`, or a positive floating point number
  - **subscribed** (bool): Whether the active member is subscribed to this list 

- **Returns**: New &lt;Trellogy.List&gt; object

### [method] :: archive()

- **Description:** Archive Trello list.
- **Parameters:** None
- **Returns**: None

### [method] :: delete()

- **Description:** Move Trello list to `TRASH_BOARD`.
- **Parameters:** None
- **Returns**: None