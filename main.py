from taipy import Gui

prompt = "prompt"
essay = "essay"
state = "state"

index = f"""
<|Welcome to EditMe!|text|class_name=text|>

<|Your Essay:|text|class_name=text|>

<|{prompt}|text|class_name=text|>

<|{essay}|text|class_name=text|> 

<|{state}|text|class_name=text|>

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

custom_theme = {
  "palette": {
    "background": {"default": "#becdf0"},
    "primary": {"main": "#324164"}
  }
}

Gui(pages=pages, css_file="./styles.css").run(theme=custom_theme)