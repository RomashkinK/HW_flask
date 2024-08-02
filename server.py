
from flask import Flask, jsonify, request
from flask.views import MethodView
from models import Advertisement, Session
from sqlalchemy.exc import IntegrityError

app = Flask('app')


class AdvertismentView(MethodView):
    def get(self, advertisement_id):
        with Session() as session:
            advertisment = session.get(Advertisement, advertisement_id)
            if advertisment is None:
                raise Exception()
            return jsonify({
                'id': advertisment.id,
                'title': advertisment.title,
                'description': advertisment.description,
                'creation_datetime': advertisment.creation_datetime,
                'owner': advertisment.owner
            })
    
    def post(self):
        json_data = request.json
        with Session() as session:
            advertisment = Advertisement(**json_data)
            session.add(advertisment)
            try:
                session.commit()
            except IntegrityError as err:
                raise err
            return jsonify({
                'id': advertisment.id,
                'title': advertisment.title,
                'description': advertisment.description,
                'creation_datetime': advertisment.creation_datetime,
                'owner': advertisment.owner
            })
    
    def patch(self, advertisment_id):
        json_data = request.json
        with Session() as session:
            advertisment = session.get(Advertisement, advertisment_id)
            if advertisment is None:
                raise Exception()
            for key, value in json_data.items():
                setattr(advertisment, key, value)
            session.add(advertisment)
            session.commit()
            return jsonify({
                'id': advertisment.id,
                'title': advertisment.title,
                'description': advertisment.description,
                'creation_datetime': advertisment.creation_datetime,
                'owner': advertisment.owner
            })
                

    def delete(self, advertisment_id):
        with Session() as session:
            advertisment = session.get(Advertisement, advertisment_id)
            if advertisment is None:
                raise Exception()
            session.delete(advertisment)
            session.commit()
            return jsonify({'status': 'deleted'})
        
app.add_url_rule(
    '/advertisment/<int:advertisment_id>', 
    view_func=AdvertismentView.as_view('with_id'),
    methods=['GET','PATCH','DELETE'])

app.add_url_rule(
    '/advertisment',
    view_func=AdvertismentView.as_view('create_advertisment'),
    methods=['POST'])

app.run()
