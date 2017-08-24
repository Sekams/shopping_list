from flask import Flask

# Initialize the app
app = Flask(__name__, instance_relative_config=True)

# Load the views
from app import views

app.config['SECRET_KEY'] = "this-is-secret"

# Load the config file
app.config.from_object('config')

if __name__ == '__main__':
    app.run()
    