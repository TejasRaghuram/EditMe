import json


def get_data():
    """
    Retrieves the data from the data.json file.

    Returns:
    dict or False: The data if the data.json file exists, False otherwise.
    """
    try: 
        with open('data.json', 'r') as file:
            data = json.load(file)
    except:
        return False

    return data

def get_essay(username):
    """
    Retrieves the essay writing of a given username from the data.json file.

    Parameters:
    username (str): The username to retrieve the essay writing for.

    Returns:
    str or False: The essay writing if the username exists in the data.json file, False otherwise.
    """
    data = get_data()
    if data == False:
        return False
    if username in data:
        return data[username]['Essay']
    else:
        return False

def pending(email):
    """
    Retrieves the pending status of a given email from the data.json file.

    Parameters:
    email (str): The email to retrieve the pending status for.

    Returns:
    bool or False: The pending status if the email exists in the data.json file, False otherwise.
    """
    data = get_data()
    if data == False:
        return False
    if email in data:
        return data[email]['Pending']
    else:
        return False

def get_assigned(email):
    """
    Retrieve the assigned value for a given email from the data.

    Args:
        email (str): The email address to retrieve the assigned value for.

    Returns:
        bool: The assigned value for the given email if it exists in the data, otherwise False.
    """
    data = get_data()
    if data == False:
        return False
    if email in data:
        return data[email]['Assigned']
    else:
        return False

def set_essay(email, essay):
    """
    Set the essay for a given email in the data dictionary and save it to a JSON file.

    Args:
        email (str): The email address of the user.
        essay (str): The essay content to be set.

    Returns:
        None
    """
    data = get_data()
    data[email]['Essay'] = essay

    with open('data.json', 'w') as file:
        json.dump(data, file)

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
