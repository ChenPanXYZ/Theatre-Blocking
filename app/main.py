from flask import Flask, jsonify, request
from flask_cors import CORS
import os, csv

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
        result.append([data["script"], data[j]['chart_start'], data[j]['chart_end'], actors])
   
    return jsonify(result)


## POST route for replacing script blocking on server
# Note: For the purposes of this assignment, we are using POST to replace an entire script.
# Other systems might use different http verbs like PUT or PATCH to replace only part
# of the script.
@app.route('/script', methods=['POST'])
def addBlocking():
    # right now, just sends the original request json

    data = request.get_json()
    filenum = data['scriptNum']
    blocks = data['blocks']

    filename = find_script(filenum)
    if filename is not None:

        with open("/app/script_data/" + filename, "w") as f:
            f.write(filenum + '\n\n')
            # Need to get FULL Script first.
            fullScript = ""
            for i in range(0, len(blocks)):
                rowBlockText = blocks[i]['text'] # We don't want "     "
                fullScript+= rowBlockText[1: len(rowBlockText) - 1]
            f.write(fullScript+ '\n\n')
            start = 0
            end = 0
            for i in range(0, len(blocks)):
                part_num = blocks[i]['part']
                rowBlockText = blocks[i]['text'] # We don't want "     "
                end += len(rowBlockText) - 2
                actors = blocks[i]['actors']
                f.write(str(part_num)+'. '+str(start)+', '+str(end - 1)+', ')
                for actor_index in range(0, len(actors)):
                    actor = actors[actor_index]
                    f.write(actor[0]+'-'+actor[1])
                    if actor_index != (len(actors) - 1):
                        f.write(', ')
                    else:
                        f.write('\n')
                start = end
            f.close()
    return jsonify(request.json)


## POST route for replacing script blocking on server
# Note: For the purposes of this assignment, we are using POST to replace an entire script.
# Other systems might use different http verbs like PUT or PATCH to replace only part
# of the script.
@app.route('/actor', methods=['POST'])
# def checkRemovability(actorName, actors):
#     for actor in actors:
#         if actorName == actor[0]:
#             return True
#     return False
def changeActor():
    # right now, just sends the original request json
    data = request.get_json()
    filenum = data['scriptNum']
    blocks = data['blocks']
    newActor = data['newActor']
    addOrRemove = data['type']
    alreadyIn = False
    filename = find_script(filenum)
    # if not(checkRemovability(newActor, blocks[0]['actors'])):
    #     return jsonify([])
    if filename is not None:
        if addOrRemove == "add":
            add_name_csv(newActor, 'actors.csv')
        with open("/app/script_data/" + filename, "w") as f:

            f.write(filenum + '\n\n')
            # Need to get FULL Script first.
            fullScript = ""
            for i in range(0, len(blocks)):
                rowBlockText = blocks[i]['text'] # We don't want "     "
                fullScript += rowBlockText[1: len(rowBlockText) - 1]
            f.write(fullScript+ '\n\n')
            start = 0
            end = 0
            for i in range(0, len(blocks)):
                part_num = blocks[i]['part']
                rowBlockText = blocks[i]['text'] # We don't want "     "
                end += len(rowBlockText) - 2
                actors = blocks[i]['actors']
                f.write(str(part_num)+'. '+str(start)+', '+str(end - 1))
                if len(actors) == 0 and addOrRemove == "remove":
                    f.write('\n')
                elif len(actors) == 0 and addOrRemove == "add":
                    f.write(', ' + newActor + '-' + '0\n')
                else:
                    for actor_index in range(0, len(actors)):
                        actor = actors[actor_index]
                        if newActor == actor[0]:
                            alreadyIn = True
                        if (actor_index == (len(actors) - 1) and addOrRemove == "remove" and newActor == actor[0]):
                            # To be removed is the last
                            f.write('\n')
                        elif not(actor_index != (len(actors) - 1) and addOrRemove == "remove" and newActor == actor[0]):
                            f.write(', ' + actor[0] + '-' + actor[1])
                            if actor_index == (len(actors) - 1) and not(addOrRemove == "remove"):
                                if not(alreadyIn):
                                    f.write(', ' + newActor + '-' + '0\n')
                                else:
                                    f.write('\n')
                            elif actor_index == (len(actors) - 1):
                                f.write('\n')

                start = end
            f.close()
    return jsonify(request.json)



# added, helper function for file processing
def find_script(filenum):
    ''' Helper function used to get file names of the text files with the file number
    @param str filenum: a filenum indicating the script number
    '''
    for filename in os.listdir('app/script_data/'):
        with open('app/script_data/'+filename, "r") as script:
            if script.readline().strip('\n') == filenum:
                return filename
    return None

def read_text(filenum):
    ''' Helper function used to read information from the provided text files with the file number
    @param str filenum: a filenum indicating the script number
    '''
    data = {}
    filename = find_script(filenum)
    if filename is not None:
        with open('/app/script_data/'+filename, "r") as script:
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
                        data[part_number][comma_spt[i].split("-")[0].strip()]=comma_spt[i].split("-")[1].strip()
                line = script.readline()
  
    return data
# added, help function for file processing

def read_csv(filename):
    '''Helper function used to read actor names from the csv file
    @param str filename: the name of the csv file
    '''

    with open("/app/"+filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        actor = {}
        for row in csv_reader:
           actor[int(row[0])]=row[1]
    return actor
    
def add_name_csv(actor_name,file_name):
    with open("/app/" + file_name,"r+") as csv_file:
        exist = False
        for line in csv_file:
            if line.split(",")[1].strip() == actor_name:
                exist = True
            last_num = line.split(",")[0].strip()
        if not exist:
            csv_file.write(str(int(last_num)+1)+","+actor_name+"\n")





if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=os.environ.get('PORT', 80))