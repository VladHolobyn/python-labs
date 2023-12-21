import os
from app import create_app


if __name__ == '__main__':
    config_name = os.environ.get('CONFIG','default')
    create_app(config_name).run()
