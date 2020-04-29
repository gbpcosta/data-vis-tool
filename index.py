import pandas as pd
import tensorflow as tf

from app import app
import app_callbacks
import app_layout
import logging

logging.basicConfig(level=logging.DEBUG)

app.layout = app_layout.define_layout()

if __name__ == '__main__':
    app.run_server(debug=True)
