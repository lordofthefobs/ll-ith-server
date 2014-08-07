"""
Define controller mappings.

Uses a factory method to apply routes to the app.
It would also be possible to use blueprints.
"""


def create_routes(app):
    @app.route("/")
    def index():
        """
        Example: use value from application configuration as page content.
        """
        return app.config['MESSAGE']
