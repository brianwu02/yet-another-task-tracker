from flask import Flask, jsonify, abort, request, make_response, url_for
from flask.ext.restful import Api, Resource, reqparse, fields, marshal
from flask.ext.httpauth import HTTPBasicAuth

from modules.database import db_session
from modules.models import Note

from datetime import datetime # just to get it working.

app = Flask(__name__, static_url_path = '')
api = Api(app)
auth = HTTPBasicAuth()

@app.teardown_appcontext
def shutdown_session(exception=None):
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
