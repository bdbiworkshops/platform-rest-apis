from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.app_context().push()
db = SQLAlchemy(app)

class Account(db.Model):
    name = db.Column(db.String(80), unique=False, nullable=False)
    username = db.Column(db.String(80), primary_key=True, unique=True, nullable=False)
    email = db.Column(db.String(80), unique=False, nullable=False)

    def __init__(self, name, username, email):
        self.name = name
        self.username = username
        self.email = email


db.create_all()


@app.route('/accounts/<username>', methods=['GET'])
def get_account(username):
    account = Account.query.get(username)
    del account.__dict__['_sa_instance_state']
    return jsonify(account.__dict__)


@app.route('/accounts/', methods=['POST'])
def create_account():
  body = request.get_json()
  db.session.add(Account(body['name'], body['username'], body['email']))
  db.session.commit()
  return "account created"


@app.route('/accounts/<username>', methods=['DELETE'])
def delete_account(username):
    db.session.query(Account).filter_by(username=username).delete()
    db.session.commit()
    return "account deleted"

     
# Run app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
