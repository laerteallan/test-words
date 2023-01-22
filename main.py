from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from src.routes import register_app
app = Flask(__name__)
SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = '/static/swagger.json'  # Our API url (can of course be a local resource)

register_app(app)

swagger_blue = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        "app_name": "Test Word"
    }
)
app.register_blueprint(swagger_blue, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run()
