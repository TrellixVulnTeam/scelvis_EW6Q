"""Setup the SCViz Dash application.

Note that before importing this module, you will have to configure the settings in ``.settings``.  See this module's
docstring for more information.
"""

import os.path

import dash

from .__init__ import __version__
from .layout import HOME_BRAND, layout
from . import callbacks

#: Path to assets.
ASSETS_FOLDER = os.path.join(os.path.dirname(__file__), "assets")


#: The Dash application to run.
app = dash.Dash(
    __name__,
    assets_folder=ASSETS_FOLDER,
    # external_stylesheets=["/%s/bootstrap.min.css" % ASSETS_ROUTE, "/%s/scviz.css" % ASSETS_ROUTE],
)

# Set app title
app.title = "SCViz v%s" % __version__

# Serve assets locally
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

# Setup the application's main layout.
app.layout = layout

# Register the callbacks with the app.
callbacks.register_page_content(app)
callbacks.register_page_brand(app)
