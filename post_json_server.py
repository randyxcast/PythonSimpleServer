from flask import Flask
from flask import request
from flask import abort
import json

app = Flask(__name__)

# function with route /test and POST method
@app.route('/test', methods=['POST'])
def cut_string():
    try:
        # get string parameter from POST resquest
        string_to_cut = request.json['string_to_cut'] 
    except:
        # abort since the key 'string_to_cut' wasn't found 
        print('Error: The POST request key was not found.')
        abort(400)
    
    # let's get the string length
    string_len = len(string_to_cut)
    # variable to store the cut string
    string_third_chars = ""

    # check if string has at least 3 characters
    if(string_len >= 3):
        # start loop at char 3 and increment by 3
        for x in range(2, string_len, 3):
            # store the third letter
            string_third_chars += string_to_cut[x]

        # store the cut string in json format with key 'return_string'
        json_st = {'return_string':string_third_chars}
    else:
        # string has less than 3 characters, return the original
        print("Warning: String does not have at least 3 characters.")
        json_st = {'return_string_original':string_to_cut}

    # return in json format
    return json.dumps(json_st)

if __name__ == '__main__':
    # run app in localhost port 8000
    app.run(port=8000, host='localhost', debug=True)