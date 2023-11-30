from taipy import Gui

prompt = "prompt"
essay = "essay"
state = "state"

index = f"""
<|Welcome to EditMe!|text|>

<|Your Essay:|text|>

<|{prompt}|text|>

<|{essay}|text|> 

<|{state}|text|>

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