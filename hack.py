from flask import Flask, render_template, request, redirect, url_for
import os, json, shutil

app = Flask(__name__,static_url_path='', 
            static_folder='assets')


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/run", methods = ['POST'])
def run():
    if request.method == 'POST':
      repo = request.form['repo_url']

      # STEP 1 - README-GETTER
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

      # STEP 2 - SENTIMENT-ANALYSIS

      # get output.json from readme-getter and feed to sentiment-analysis

      readme_getter_file = json.load(open('./readme-getter/output/output.json'))

      sentiment_analysis_input_contract_data = {
        "input": {
          "contract": readme_getter_file['results'][0]['contract'],
          "transformerContract": {
                  "type": "transformer",
                  "handle": "readme2sentiment"
              },
          "artifactPath": "foobar"
        }
      }

      with open('./sentiment-analysis/input.json', 'w') as f:
        f.write(json.dumps(sentiment_analysis_input_contract_data))

      # start sentiment-analysis
      print("Executing sentiment analysis ...")

      # change to transformer directory so docker runs in proper context
      os.chdir('./sentiment-analysis')

      os.system("./run.sh")

      print("sentiment analysis done ...")

      os.chdir(root)

      # STEP 3 - COLORS-ON-A-PLATE

      # get output.json from sentiment-analysis and feed to colors-on-a-plate

      sentiment_analysis_file = json.load(open('./sentiment-analysis/output/output.json'))

      colors_on_a_plate_input_contract_data = {
        "input": {
          "contract": sentiment_analysis_file['results'][0]['contract'],
          "transformerContract": {
                  "type": "transformer",
                  "handle": "sentiment2colors"
              },
          "artifactPath": "foobar"
        }
      }

      with open('./colors-on-a-plate/input.json', 'w') as f:
        f.write(json.dumps(colors_on_a_plate_input_contract_data))

      # start colors-on-a-plate
      print("Serving up colors on a plate ...")

      # change to transformer directory so docker runs in proper context
      os.chdir('./colors-on-a-plate')

      os.system("./run.sh")

      print("Colors served ...")

      os.chdir(root)

      # STEP 4 - NAME GENERATOR
      print("Thinking up a name...")

      colors_on_a_plate_file = json.load(open('./colors-on-a-plate/output/output.json'))
      output_colors = colors_on_a_plate_file['results'][0]['contract']['data']

      os.chdir('./krea-brain')

      with open('./artifacts/prefix_file.txt', 'w') as f:
        f.write(output_colors['primaryName'] + ' ' + output_colors['complementaryName'] + ' ' + output_colors['contrastAdjustedName'] + ' ' + readme_getter_file['results'][0]['contract']['data']['content'])

      os.system("./run.sh")

      print("Named!")

      os.chdir(root)


      # STEP 5 - LOGO GENERATOR
      print("Designing a snazzy logo...")

      with open('./krea-brain/artifacts/suggestion.txt') as f:
        brand_name = f.readlines()

      os.chdir('./gitbrander')

      with open('./input.txt', 'w') as f:
        f.write('logo' + brand_name[0] + ' in a circle')

      with open('./colors.json', 'w') as f:
        f.write(json.dumps(output_colors))

      os.system("./run.sh")

      print("Logo done!")

      os.chdir(root)

      # STEP 6 - Display the output artifacts on the page (name, logo, colors)
      
      # get name from name-generator
    


      # copy icon to assets folder
      shutil.copyfile('gitbrander/output/icon.png', 'assets/icon.png')

      return redirect('/?name=' +  brand_name[0])


