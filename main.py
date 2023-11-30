from taipy import Gui

prompt = "prompt"
essay = "essay"
state = "state"

index = f"""
<|Welcome to EditMe!|text|class_name=text title|>

<|Your Essay:|text|class_name=text subtitle|>

<|{prompt}|text|class_name=text bold|>

<|{essay}|text|class_name=text regular|> 

<|{state}|text|class_name=text subtitle|>

<|Edit Essay|button|class_name=button|>
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

custom_theme = {
  "palette": {
    "background": {"default": "#becdf0"},
    "primary": {"main": "#324164"}
  }
}

Gui(pages=pages, css_file="./styles.css").run(theme=custom_theme)