import os
from app import create_app

config_name = os.environ.get('CONFIG','default')
app = create_app(config_name)
