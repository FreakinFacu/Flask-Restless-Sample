import flask
import flask.ext.sqlalchemy
import flask.ext.restless

# Create the Flask application and the Flask-SQLAlchemy object.
app = flask.Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/orders'
db = flask.ext.sqlalchemy.SQLAlchemy(app)

class Orders(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    status   = db.Column(db.String(255))
    quantity = db.Column(db.Integer)
    model    = db.Column(db.String(255))
    name     = db.Column(db.String(255))
    address  = db.Column(db.String(255))
    city     = db.Column(db.String(255))
    state    = db.Column(db.String(2))
    zip      = db.Column(db.String(10))

# Create the database tables.
db.create_all()

# Create the Flask-Restless API manager.
manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)


manager.create_api(Orders, methods=['GET', 'POST'], url_prefix='', collection_name='order')

# start the flask loop
app.run()