import os
from flask import Flask

# Create instance of app
# __name__is a built in Python varialbe Flask needs
# # locate templates and static files
app = Flask(__name__)


# A decorator is a way of wrapping functions, / is root directory


@app.route("/")
def index():
    return "Hello, World"


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)

