import json

# TODO: Implement mongoDB
# TODO: Implement create() function

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

def create():
    # TODO: 
    pass

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
        return data[email]['Pending Status']
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

def set_pending(email):
    """
    Set the pending status for a given email in the data dictionary and save it to a JSON file.

    Args:
        email (str): The email address of the user.

    Returns:
        None
    """
    data = get_data()
    data[email]['Pending Status'] = True

    with open('data.json', 'w') as file:
        json.dump(data, file)

def assign():
    needs_review = []  # People needing their essays to be reviewed
    reviewers = []     # People available to review an essay
    data = get_data()

    # Identifying people needing review and available reviewers
    for person in data:
        if data[person]['Pending Status']:
            needs_review.append(person)
        if data[person]['Assigned'] == "":
            reviewers.append(person)

    # Check if there are enough reviewers
    if not reviewers:
        return False

    # Assign reviewers to people needing review
    for person in needs_review:
        for reviewer in reviewers:
            if person != reviewer:
                data[person]['Assigned'] = reviewer
                data[reviewer]['Pending Status'] = False
                reviewers.remove(reviewer)
                break

    # Update data.json with the new assignments
    try:
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)
        return True
    except IOError:
        return False
