from flask import Flask, jsonify, request
from flask_cors import CORS
import os

# Start the app and setup the static directory for the html, css, and js files.
app = Flask(__name__, static_url_path='', static_folder='static')
CORS(app)

# This is your 'database' of scripts with their blocking info.
# You can store python dictionaries in the format you decided on for your JSON
   # parse the text files in script_data to create these objects - do not send the text
   # files to the client! The server should only send structured data in the sallest format necessary.
scripts = []

### DO NOT modify this route ###
@app.route('/')
def hello_world():
    return 'Theatre Blocking root route'

### DO NOT modify this example route. ###
@app.route('/example')
def example_block():
    example_script = "O Romeo, Romeo, wherefore art thou Romeo? Deny thy father and refuse thy name. Or if thou wilt not, be but sworn my love And I’ll no longer be a Capulet."

    # This example block is inside a list - not in a dictionary with keys, which is what
    # we want when sending a JSON object with multiple pieces of data.
    return jsonify([example_script, 0, 41, 4])


''' Modify the routes below accordingly to 
parse the text files and send the correct JSON.'''

## GET route for script and blocking info
@app.route('/script/<int:script_id>')
def script(script_id):
    # right now, just sends the script id in the URL
    data = read_text(str(script_id))
    actor_data = read_csv("actors.csv")
    actor = ""
    result = []



    for i in range(2, len(data)):
        j = i - 2 + 1
        actors={}
        for k in actor_data.keys():
            actor = actor_data[k]
            if actor in data[j].keys():
                actors[k] = [actor, data[j][actor]]
        result.append([data["script"], data[j]['chart_start'], data[j]['chart_end'], data["script"][int(data[j]['chart_start']):int(data[j]['chart_end'])], actors])
   
    return jsonify(result)


## POST route for replacing script blocking on server
# Note: For the purposes of this assignment, we are using POST to replace an entire script.
# Other systems might use different http verbs like PUT or PATCH to replace only part
# of the script.
@app.route('/script', methods=['POST'])
def addBlocking():
    # right now, just sends the original request json
    return jsonify(request.json)



# added, helper function for file processing
def read_text(filenum):
    with open('/app/script_data/hamlet'+filenum+'.txt') as script:
        blank = 0
        data = {}
        line = script.readline()
        data["file_number"] = line.strip()
        while line:
            if line == "\n":
                blank += 1
            elif blank == 1:
                data["script"] = line.strip()
            elif blank == 2:
                comma_spt = line.split(",")
 
                dot_spt=comma_spt[0].split(".")
                part_number = int(dot_spt[0].strip())
                data[part_number] = {}
                data[part_number]["chart_start"] = dot_spt[1].strip()
                data[part_number]["chart_end"] = comma_spt[1].strip()
                
                for i in range (2 , len(comma_spt)):
                    #data[i-2]["actor"] =  comma_spt[i].split("-")[0].strip()
                    #data[i-2]["position"] = comma_spt[i].split("-")[1].strip()
                    data[part_number][comma_spt[i].split("-")[0].strip()]=comma_spt[i].split("-")[1].strip()
            line = script.readline()
  
    return data
# added, help function for file processing

import csv
def read_csv(filename):
    #'actors.csv'
    with open("/app/"+filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        actor = {}
        for row in csv_reader:
           actor[int(row[0])]=row[1]
    return actor




if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=os.environ.get('PORT', 80))

