# Trellogy

<blockquote>Trello handling module using Trello REST API</blockquote>

## Purpose

Trello is an amazing tool that has multiple features to handle complicated workflows and enrich my life. Trello initially popped up to me as a recommendation from my office colleagues. Trello successfully settled down in our office workflow, which maximizes the efficiency.
After using it for a couple of months, I thought I could also make use of it in handling personal tasks as well. I was a big fan of Franklin Planner back in the old days, right until I migrated myself into the digital world. Believing Trello can be a perfect fit for this matter, I tested jotting down things on the Trello every day.
It didn't take long to figure out that it is such a time-consuming job to create lists, rename them to future dates accordingly, and duplicate same cards over and over. Of course, I knew the core (and perhaps most handy) function called 'Butler' that can assist handling tedious task. But it wasn't a perfect solution that can cover all my sophisticated needs. Hence I came up of the idea of creating a simple Python module that wraps up the Trello REST API, and then write some codes that can fulfill automated jobs.

## Quick Use

```python
from trellogy import Trellogy

# Initialize:
trello = Trellogy(key=TRELLO_API_KEY,
                  token=TRELLO_API_TOKEN,
                  board_id=BOARD_ID,
                  trash_id=TRASH_BOARD_ID)

# Get lists from the board:
trello_lists = trello.get_lists() # list of <trello.List>

# Get cards from a list:
trello_cards = trello.cards # list of <trello.Card>

# Get first card from the list:
sample_card = trello_cards[0]

# Title of the card:
print(sample_card.name)

# Description of the card:
print(sample_card.desc)
```

## Quick Explanation

### Mandatory: ACCESS_KEY, ACCESS_TOKEN, BOARD_ID

Basically, in order to use this module, you need **ACCESS KEY**, **ACCESS TOKEN**, and **BOARD ID**. Key and token is necessary in order to control your board via API. You can get your key and token from [here](https://trello.com/app-key).
Board ID is the id of the board that you are trying to manage. You can get your board ID by adding **.json** to your board_url. For example, if your board URL is **https://trello.com/b/RANDOM_ID/SAMPLE_NAME**, go to **https://trello.com/b/RANDOM_ID/SAMPLE_NAME.json** and you'll see your board ID on the first line of the JSON data.

### Optional: TRASH_BOARD_ID

Also, you can give **TRASH BOARD ID** as a parameter. Since the Trello does not let us directly remove data from the board via API, a way to detour this is to create a board and move all the unnecessasry lists or cards to it, as if you are tossing junk files to a trash bin.

If you do not set trash_id when initializing Trellogy class, you may have restrctions using a couple of methods e.g. delete_list(), delete_card().
