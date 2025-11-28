"""
Main Flask application entry point.
"""
from flask import Flask, render_template
from flask_cors import CORS
from app.routes.api import api_bp


def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)
    
    # Enable CORS for frontend access
    CORS(app)
    
    # Register blueprints
    app.register_blueprint(api_bp)
    
    # Serve the main page
    @app.route('/')
    def index():
        return render_template('index.html')
    
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=8000, debug=True)
