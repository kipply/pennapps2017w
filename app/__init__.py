from flask import Flask 
from flask_compress import Compress

app = Flask(__name__) # Create the Flask app 
Compress(app) # Gzip compression for faster load times

from app import views # Import views.py at end. Importing at top lines causes import loop error.

