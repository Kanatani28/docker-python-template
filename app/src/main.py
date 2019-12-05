from flask import Flask
from flask_restplus import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://test:test@sample_db:3306/dc_db?charset=utf8'
db = SQLAlchemy(app)
api = Api(app)

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        
        return {'hello': 'world'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)