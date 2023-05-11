from flask import Flask
from flask_restful import Api
from app.routes import example_route

# Create an instance of the BigQuery client



app = Flask(__name__)
api = Api(app)

# Register blueprints
app.register_blueprint(example_route, url_prefix='/api')

if __name__ == '__main__':
    app.run()
