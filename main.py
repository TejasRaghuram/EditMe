from taipy import Gui

prompt = "prompt"
essay = "essay"
status = "status"

index = f"""
# Welcome to EditMe!

## Your Essay:
**{prompt}**
<br />
{essay} 

## {status}
<|Edit Essay|button|>
"""

register = """
# This is the register page
"""

login = """
# This is the login page
"""

pages = {
    'index': index,
    'register': register,
    'login': login,
}   

Gui(pages=pages, css_file="./styles.css").run(dark_mode=True)