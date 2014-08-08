"""
Define controller mappings.

Uses a factory method to apply routes to the app.
It would also be possible to use blueprints.
"""

from flask.ext.cors import cross_origin
from flask import jsonify, request
import json

def create_routes(app):
    @app.route("/")
    def index():
        """
        Example: use value from application configuration as page content.
        """
        return app.config['MESSAGE']

    @app.route("/devices/list", methods=["GET", "POST"])
    @cross_origin(headers=['Content-Type'])
    def device_list():
    	return json.dumps(app.device_manager.get_devices())

    @app.route("/device/update/<int:device_id>", methods=["GET", "POST"])
    @cross_origin(headers=['Content-Type'])
    def update_device(device_id):
        device_name = request.form["device_name"]
        # app.device_manager.update_device(device_id, device_name)
        return "{}"