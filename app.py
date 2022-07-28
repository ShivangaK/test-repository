from flask import Flask
from flask_restful import Api
from db import db

from Scripts.section6.resources.item import Item, ItemsList
from Scripts.section6.resources.userresource import UserResource
from Scripts.section6.resources.storeresource import StoreResource, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle://gp:gp@172.23.208.12:1521/orcl'
# oracle://gp:gp@172.23.208.12:1521/orcl  sqlite:///data.db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemsList,'/items')
api.add_resource(UserResource,'/user')
api.add_resource(StoreResource,'/store/<string:name>')
api.add_resource(StoreList,'/stores')


if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
