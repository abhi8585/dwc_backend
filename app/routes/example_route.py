from flask import Blueprint
from app.resources.example_resource import ExampleResource
from app.resources.sample_resource import SampleResource

# Create a blueprint for the route
example_route = Blueprint('example_route', __name__)

# Add resource(s) to the blueprint
example_resource = ExampleResource()
sample_resource = SampleResource()

# Define routes
example_route.add_url_rule('/example', view_func=example_resource.as_view('example'))
example_route.add_url_rule('/sample', view_func=sample_resource.as_view('sample'))
