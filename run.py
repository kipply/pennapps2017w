#!/usr/bin/env python3

from app import app
from flask import Flask

if __name__ == '__main__': # If it is being run directly, otherwise __name__ would be the name of the module
  try:
    context = ()
    print("Running HTTPS")
    app.run(host='0.0.0.0', port=443, debug=True, ssl_context=context) 
  except Exception as e:
    print("Running HTTP")
    app.run(host='0.0.0.0', port=80, debug=True)