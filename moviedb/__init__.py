import json
import os

from flask import Flask


def create_app(config_filename: str = 'config.dev.jason')->Flask:
    app = Flask(__name__,
                    instance_relative_config=True,
                    static_folder = 'static',
                    template_folder = 'templates'
                    )
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    try:
        app.config.from_file(config_filename, load=json.load)
        app.logger.debug('Config loaded')
    except FileNotFoundError:
        app.logger.error("Arquivo nao encontrado")
        exit(1)


    return app