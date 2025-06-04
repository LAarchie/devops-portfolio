from flask import Flask
from .routes import main
from flask_cors import CORS

def create_app():
    """
    Create and configure the Flask application.

    This function initializes the Flask app, applies CORS settings to allow
    requests from the frontend running at http://localhost:8080, and registers
    the main blueprint containing API routes.

    Returns:
        Flask: The configured Flask application instance.
    """
    
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "http://localhost:8080"}})
    app.register_blueprint(main)
    return app
