from flask import Flask, render_template, request, redirect, url_for
import os, json

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/run", methods = ['POST'])
def run():
    if request.method == 'POST':
      repo = request.form['repo_url']

      # write input.json to readme-getter 

      readme_getter_input_contract_data = {
        "input": {
          "contract": {
                  "type": "repourl",
                  "data": {
                      "url": repo
                  }
              },
          "transformerContract": {
                  "type": "transformer",
                  "handle": "repourl2readme"
              },
              "artifactPath": "foobar"
        }
    }

      with open('./readme-getter/input.json', 'w') as f:
        f.write(json.dumps(readme_getter_input_contract_data))

      # keep track of project root dir
      root = os.getcwd()

      print("Executing readme-getter ...")

      # change to transformer directory so docker runs in proper context
      os.chdir('./readme-getter')

      os.system("./run.sh")

      print("readme-getter done ...")

      os.chdir(root)

      # get output.json from readme-getter and feed to sentiment-analysis

      readme_getter_file = json.load(open('./readme-getter/output/output.json'))

      readme_getter_contract = readme_getter_file['results'][0]['contract']

      # write readme text 

      with open('./sentiment-analysis/input/input.md', 'w') as f:
        f.write(readme_getter_contract['data']['text'])

      # start sentiment-analysis
      print("Executing sentiment analysis ...")

      # change to transformer directory so docker runs in proper context
      os.chdir('./sentiment-analysis')

      os.system("./run.sh")

      print("sentiment analysis done ...")

      os.chdir(root)

      return redirect(url_for('index'))