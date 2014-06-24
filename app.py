from flask import Flask, jsonify, abort, request, make_response, url_for
from flask.ext.restful import Api, Resource, reqparse, fields, marshal
from flask.ext.httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy

from modules.database import db_session
from modules.models import Note, Base

from datetime import datetime # just to get it working.

from modules.database import init_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://test:password@192.168.1.24/testdb'
db = SQLAlchemy(app)

api = Api(app)
auth = HTTPBasicAuth()

@app.before_first_request 
def setup():
    print("This frs")
    Base.metadata.drop_all(bind=db.engine)
    Base.metadata.create_all(bind=db.engine)

@app.route('/add')
def add():
    note = Note('some data', datetime.now())
    db.session.add(note)
    db.session.commit()
    return note

@app.route('/')
def root():
    notes = db.session.query(Note).all()
    return u"<br>".join([u"{0}: {1}".format(note.note, note.timestamp) for note in notes])


@app.teardown_appcontext
def shutdown_session(exception=None):
    print("this is being called")
    db.session.remove()
    db_session.remove()


@auth.error_handler
def unauthorized():
    return make_response(jsonify(
        {'message': 'Unauthorized Access'}), 403)

task_fields = {
        'note': fields.String,
        'uri': fields.Url('note')
        }

class NoteAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('note', type=str, required=True,
                help='No note provided', location='json')

        super(NoteAPI, self).__init__()

        def get(self):
            """GET all notes"""

        def post(self):
            args = self.reqparse.parse_args()
            
            note = Note(args['note'], datetime.now())
            db_session.add(note)
            db_session.commit()

            return {'note': marshal(note, task_fields) }, 201


api.add_resource(NoteAPI, '/todo/v1/notes', endpoint='notes')


if __name__ == "__main__":
    app.run(debug=True)
