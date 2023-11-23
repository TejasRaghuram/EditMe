from taipy import Gui
from taipy.gui import Html

index = Html("""
    <h1>This is the home page</h1>
""")

register = Html("""
    <h1>This is the register page</h1>
""")

login = Html("""
    <h1>This is the login page</h1>
""")

pages = {
    'index': index,
    'register': register,
    'login': login,
}

Gui(pages=pages, css_file="./styles.css").run(dark_mode=True)