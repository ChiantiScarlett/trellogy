# Trellogy Documentation

   * [Trellogy Documentation](#trellogy-documentation)
      * [trellogy.Trellogy](#trellogytrellogy)
         * [[method] :: create_list(title, pos="bottom")](#method--create_listtitle-posbottom)
         * [[method] :: get_list(list_id)](#method--get_listlist_id)
         * [[method] :: get_lists()](#method--get_lists)
      * [trellogy.List](#trellogylist)
         * [[method] :: update(**kwargs)](#method--updatekwargs)
         * [[method] :: archive()](#method--archive)
         * [[method] :: delete()](#method--delete)
         * [[properties]](#properties)
      * [trellogy.Card](#trellogycard)
         * [[method] :: update(**kwargs)](#method--updatekwargs-1)
         * [[method] :: archive()](#method--archive-1)
         * [[method] :: delete()](#method--delete-1)
         * [[properties]](#properties-1)





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

### [properties]

- **idTrash** (str): The ID of the TRASH_BOARD
- **idBoard** (str): The ID of the parent board
- **closed** (bool): Boolean whether the list has been closed or not
- **pos** (float): Position of the card in the board
- **id** (str): The ID of the list
- **name** (str): The name of the list
- **cards** (list): The cards of the list





## trellogy.Card

### [method] :: update(**kwargs)

- **Description:** Update property of the Trello list.
- **Parameters:**
  - **desc**(str): The description for the card. Up to 16384 chars.
  - **closed**(bool): Whether the card is closed (archived). Note: Archived lists and boards do not cascade archives to cards.
  - **idMembers**(list): An array of member IDs that are on this card
  - **idAttachmentCover**(str): The id of the attachment selected as the cover image, if one exists
  - **idList**(list): The ID of the list the card is in
  - **idLabels**(list): An array of label IDs that are on this card
  - **idBoard**(str): The ID of the board the card is on
  - **pos**(float): Position of the card in the list
  - **due**(date): The due date on the card, if one exists
  - **dueComplete**(bool): Whether the due date has been marked complete
  - **subscribed**(bool): Whether this member is subscribed to the card
  - **address**(str): Address of card location
  - **locationName**(str): Name of card location
  - **coordinates**(object): Either a comma-separated string in the format latitude,longitude or an object containing keys for `latitude` and `longitude` whose values are numbers between -180 and 180.
  
- **Returns**: New &lt;Trellogy.List&gt; object

### [method] :: archive()

- **Description:** Archive Trello card.
- **Parameters:** None
- **Returns**: None

### [method] :: delete()

- **Description:** Move Trello card to `TRASH_BOARD`.
- **Parameters:** None
- **Returns**: None

### [properties]

- **attachments**
- **idTrash**
- **id**
- **address**
- **checkItemStates**
- **closed**
- **coordinates**
- **creationMethod**
- **dateLastActivity**
- **desc**
- **descData**
- **dueReminder**
- **idBoard**
- **idLabels**
- **idList**
- **idMembersVoted**
- **idShort**
- **idAttachmentCover**
- **limits**
- **locationName**
- **manualCoverAttachment**
- **name**
- **pos**
- **shortLink**
- **isTemplate**
- **badges**
- **dueComplete**
- **due**
- **idChecklists**
- **idMembers**
- **labels**
- **shortUrl**
- **subscribed**
- **url**
- **cover**