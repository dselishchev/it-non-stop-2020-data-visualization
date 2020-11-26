import dash

from layout import get_layout

dash_app = dash.Dash('My Awesome Data Visualization App')
dash_app.title = 'My Awesome Data Visualization App'
dash_app.layout = get_layout()

app = dash_app.server
