from splitwise import Splitwise
from splitwise.expense import Expense
from splitwise.user import ExpenseUser
from splitwise.group import Group
from dotenv import dontenv_values

x = dotenv_values(".env")
SPLITWISE_CONSUMER_KEY = x['SPLITWISE_CONSUMER_KEY']
SPLITWISE_CONSUMER_SECRET = x['SPLITWISE_CONSUMER_SECRET']
SPLITWISE_API_KEY = x['SPLITWISE_API_KEY']

s = Splitwise(SPLITWISE_CONSUMER_KEY,SPLITWISE_CONSUMER_SECRET, api_key=SPLITWISE_API_KEY)

#I set this for a specific group I wanted to create splits for. You can change this to whatever group you want.
def get_members():

    groups = s.getGroups()
    for i in groups:
        if i.name == "E 2095":
            group_id = i.id
            break
    members = i.members
    return members

def create_split(paid_by, user_ids, cost, description):
    cost = round(cost/len(user_ids), 2)*round(len(user_ids), 2)
    expense = Expense()
    expense.setCost(cost)
    expense.setDescription(description)
    users = [ExpenseUser() for user in user_ids]
    if paid_by not in user_ids:
        users.append(ExpenseUser())
        users[-1].setId(paid_by)
        users[-1].setPaidShare(cost)
    else:
        users[user_ids.index(paid_by)].setPaidShare(cost)
    for user in range(len(user_ids)):
        users[user].setId(user_ids[user])
        users[user].setOwedShare(cost/len(user_ids))

    expense.setUsers(users)    
    expense.setGroupId(42557871)
    added_expense = s.createExpense(expense)
    return added_expense
