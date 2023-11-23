from taipy import Gui

index = """
# This is the home page
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