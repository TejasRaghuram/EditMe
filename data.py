import json


def get_essay(username):
    try: 
        with open('data.json', 'r') as file:
            data = json.load(file)
    except:
        return False

    if username in data:
        return data[username]['Essay']['writing']
    else:
        return False


# Given an email address, this function returns the user status(pending)
def pending(email):
    return False

# Given an email address, this function returns the email of the person assigned to the user
def get_assigned(email):
    return ""

# Given an email and an essay, this function will update the essay that the user currently has
# This function returns the success of the operation
def set_essay(email, essay):
    return False

# Given an email, this function will change their status to pending(set boolean to true)
# This function returns the success of the operation
def set_pending(email):
    return False

# This function checks the database to see if two people are pending, and if they are, assigns them to each other
def assign():
    return False


"""

The methods in this file are to be implemented by Vignesh Saravanakumar

Start by creating a new branch called "data-dev"
Commit often, and add concise, professional commit messages
They should have all "important" words capitalized, such as the following:
"Implemented the getData Function"
You can see the messages of existing commits for more examples

This application is a platform that allows students to have their college essays peer reviewed

To start, create a MongoDB database to hold the user data

Each user should have the following attributes:
Email(string storing email)
Prompt(string storing the prompt the user is writing for)
Essay(string storing the user's essay)
Pending(boolean storing whether a user needs to be assigned an essay)
Assigned(string storing the email of the person the user has been assigned[null if no one])

Specific instructions detailing what each function does can be found above the function
Delete them after completing the corresponding function

Delete this message after the work is done, just before merging

More functions may or may not need to be added as the project progresses
If more are needed, you will be contacted

Have fun!

"""