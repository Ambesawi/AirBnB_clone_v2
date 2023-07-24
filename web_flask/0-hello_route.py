#!/usr/bin/python3
<<<<<<< HEAD
"""class Flask"""
from flask import Flask
"""class Flask"""


app = Flask(__name__)
=======
"""
Flask App that integrates with AirBnB static HTML Template
"""
from flask import Flask, render_template, url_for
from models import storage
import uuid;

# flask setup
app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'

>>>>>>> 55dbaaf8ddc8b3673ab8e95e193703af7dbc98d8

# begin flask page rendering
@app.teardown_appcontext
def teardown_db(exception):
    """
    after each request, this method calls .close() (i.e. .remove()) on
    the current SQLAlchemy Session
    """
    storage.close()

<<<<<<< HEAD
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """displays text
    Returns:
        text
    """
    return "Hello HBNB!"
=======
>>>>>>> 55dbaaf8ddc8b3673ab8e95e193703af7dbc98d8

@app.route('/0-hbnb')
def hbnb_filters(the_id=None):
    """
    handles request to custom template with states, cities & amentities
    """
    state_objs = storage.all('State').values()
    states = dict([state.name, state] for state in state_objs)
    amens = storage.all('Amenity').values()
    places = storage.all('Place').values()
    users = dict([user.id, "{} {}".format(user.first_name, user.last_name)]
                 for user in storage.all('User').values())
    return render_template('0-hbnb.html',
                           cache_id=uuid.uuid4(),
                           states=states,
                           amens=amens,
                           places=places,
                           users=users)

if __name__ == "__main__":
<<<<<<< HEAD
    app.run(host='0.0.0.0', port=5000)
=======
    """
    MAIN Flask App"""
    app.run(host=host, port=port)
>>>>>>> 55dbaaf8ddc8b3673ab8e95e193703af7dbc98d8
