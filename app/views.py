from app import app
from flask import render_template, redirect, request, url_for
from htmlmin.minify import html_minify

@app.route('/')
def index(): 
  # Do something 
  return html_minify(render_template('index.html'))