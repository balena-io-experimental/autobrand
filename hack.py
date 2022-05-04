from flask import Flask, render_template, request, redirect, url_for


import time

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/run", methods = ['POST'])
def run():
    if request.method == 'POST':
      repo = request.form['repo_url']
      # clone repo
      # get readme
      # start transformer chain
      print(repo)

      time.sleep(15)
      return redirect(url_for('index'))