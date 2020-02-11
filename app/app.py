from flask import Flask, render_template, make_response
from flask import redirect, request, jsonify, url_for


app = Flask(__name__)
app.secret_key = 's3cr3t'
app.debug = True