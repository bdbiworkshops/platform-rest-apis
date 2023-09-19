from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.app_context().push()
db = SQLAlchemy(app)

# TODO: define columns

class Account(db.Model):
    pass

db.create_all()


# TODO: write routes

     
# Run app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
