from flask import Flask

# Initialize the app
app = Flask(__name__, instance_relative_config=True)

# Load the config file
app.config.from_object('heroku_config')

# Load the views
from app import views

if __name__ == "__main__":
    app.run()