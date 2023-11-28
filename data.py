import json
from MongoDBManager import MongoDBManager

# TODO: Fix Assign Error

MongoDB = MongoDBManager()

def create(username):
    """
    Generates a default JSON structure for a given username.

    Parameters:
    username (str): The username to generate the default JSON for.

    Returns:
    dict: The default JSON structure for the given username.
    """
    new = {
        username: {
            "Pending Status": True,
            "Assigned": "",
            "Essay": {
                "prompt": None,
                "writing": None
            }
        }
    }
    try:
        MongoDB.write({**MongoDB.read(), **new})
        return True
    except:
        print("Error: Could not open MongoDB")
        return False

def get_essay(username):
    """
    Retrieves the essay writing of a given username from the data.json file.

    Parameters:
    username (str): The username to retrieve the essay writing for.

    Returns:
    str or False: The essay writing if the username exists in the data.json file, False otherwise.
    """
    try:
        data = MongoDB.read()
    except:
        print("Error: Could not open MongoDB")
        return False
    if data == False:
        print("Error: Could not open MongoDB")
        return False
    if username in data:
        return data[username]['Essay']
    else:
        print("Error: Username does not exist")
        return False


def get_assigned(email):
    """
    Retrieve the assigned value for a given email from the data.

    Args:
        email (str): The email address to retrieve the assigned value for.

    Returns:
        bool: The assigned value for the given email if it exists in the data, otherwise False.
    """
    try:
        data = MongoDB.read()
    except:
        print("Error: Could not open MongoDB")
        return False
    if data == False:
        print("Error: Could not open MongoDB")
        return False
    if email in data:
        return data[email]['Assigned']
    else:
        print("Error: Email does not exist")
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
    try:
        data = MongoDB.read()
    except:
        print("Error: Could not open MongoDB")
        return False
    data[email]['Essay']['writing'] = essay

    try:
        MongoDB.write(data)
        return True
    except:
        print("Error: Could not write to MongoDB")
        return False

def set_prompt(email, prompt):
    """
    Set the prompt for a given email in the data dictionary and save it to a JSON file.

    Args:
        email (str): The email address of the user.
        prompt (str): The prompt content to be set.

    Returns:
        None
    """
    try:
        data = MongoDB.read()
    except:
        print("Error: Could not open MongoDB")
        return False
    data[email]['Essay']['prompt'] = prompt

    try:
        MongoDB.write(data)
        return True
    except:
        print("Error: Could not write to MongoDB")
        return False

def set_pending(email):
    """
    Set the pending status for a given email in the data dictionary and save it to a JSON file.

    Args:
        email (str): The email address of the user.

    Returns:
        None
    """
    try:
        data = MongoDB.read()
    except:
        print("Error: Could not open MongoDB")
        return False
    data[email]['Pending Status'] = True

    try:
        MongoDB.write(data)
        return True
    except:
        print("Error: Could not write to MongoDB")
        return False

def get_pending(email):
    """
    Retrieves the pending status of a given email from the data.json file.

    Parameters:
    email (str): The email to retrieve the pending status for.

    Returns:
    bool or False: The pending status if the email exists in the data.json file, False otherwise.
    """
    try:
        data = MongoDB.read()
    except:
        print("Error: Could not open MongoDB")
        return False
    if data == False:
        print("Error: Could not open MongoDB")
        return False
    if email in data:
        return data[email]['Pending Status']
    else:
        print("Error: Email does not exist")
        return False

def get_essay(email):
    """
    Retrieve the essay for a given email from the data.

    Args:
        email (str): The email address to retrieve the essay for.

    Returns:
        str: The essay for the given email if it exists in the data, otherwise False.
    """
    try:
        data = MongoDB.read()
    except:
        print("Error: Could not open MongoDB")
        return False
    if data == False:
        print("Error: Could not open MongoDB")
        return False
    if email in data:
        return data[email]['Essay']
    else:
        print("Error: Email does not exist")
        return False
    
def get_prompt(email):
    """
    Retrieve the prompt for a given email from the data.

    Args:
        email (str): The email address to retrieve the prompt for.

    Returns:
        str: The prompt for the given email if it exists in the data, otherwise False.
    """
    try:
        data = MongoDB.read()
    except:
        print("Error: Could not open MongoDB")
        return False
    if data == False:
        print("Error: Could not open MongoDB")
        return False
    if email in data:
        return data[email]['Essay']['prompt']
    else:
        print("Error: Email does not exist")
        return False

def assign():
    needs_review = []  # People who need someone to review their essays
    reviewers = []     # People available to review an essay

    try:
        data = MongoDB.read()
    except:
        print("Error: Could not open data.json")
        return False

    # People who need review have a pending status of True
    for email in data:
        if data[email]['Pending Status']:
            needs_review.append(email)
    
    # People who are available to review have no value in 'Assigned'
    for email in data:
        if data[email]['Assigned'] == "":
            reviewers.append(email)

    # If there are no people who need review, return True
    if len(needs_review) == 0:
        return True
    if len(reviewers) == 0:
        print("Error: No reviewers available")
        return False
    if len(needs_review) == len(reviewers) and len(needs_review) == 1:
        print("Error: Only one person available to review, and they are the one who needs review")
        return False
    for email in needs_review:
        for reviewer in reviewers:
            if email != reviewer:
                data[email]['Assigned'] = reviewer
                data[reviewer]['Assigned'] = email

                try:
                    MongoDB.write(data)
                    return True
                except:
                    print("Error: Could not open data.json")
                    return False


# Example Usage
# print(create("Vignesh"))
# print(create("Tejas"))
# print(create("Aryan"))
# print(create("John"))

# # Set Essay
# print(set_essay("Vignesh", "This is a test essay"))
# print(set_essay("Tejas", "This is a test essay"))
# print(set_essay("Aryan", "This is a test essay"))

# # Set Prompt
# print(set_prompt("Vignesh", "This is a test prompt"))
# print(set_prompt("Tejas", "This is a test prompt"))
# print(set_prompt("Aryan", "This is a test prompt"))

# # Get Pending
# print("Pending: " + str(get_pending("Vignesh")))
# print("Pending: " + str(get_pending("Tejas")))
# print("Pending: " + str(get_pending("Aryan")))

# # Get Essay
# print("Essay: " + str(get_essay("Vignesh")))
# print("Essay: " + str(get_essay("Tejas")))
# print("Essay: " + str(get_essay("Aryan")))

# # Get Prompt
# print("Prompt: " + str(get_prompt("Vignesh")))
# print("Prompt: " + str(get_prompt("Tejas")))
# print("Prompt: " + str(get_prompt("Aryan")))

# # Get Assigned
# print("Assigned: " + str(get_assigned("Vignesh")))
# print("Assigned: " + str(get_assigned("Tejas")))
# print("Assigned: " + str(get_assigned("Aryan")))


# # Assign
# print("Assign: " + str(assign()))

# # Get Assigned
# print("Assigned: " + get_assigned("Vignesh"))
# print("Assigned: " + get_assigned("Tejas"))
# print("Assigned: " + get_assigned("Aryan"))


# If you want to clear the database
# print(MongoDB.write({}))
