# Python Simple Server

This is a small web application in Python which does the following:
1. Accept a POST request to the route “/test”, which accepts one argument “string_to_cut”
2. Return a JSON object with the key “return_string” and a string containing every third letter from the original string

(e.g.) If you POST {"string_to_cut": "HelloWorld"}, it will return: {"return_string": "lWl"}.

To run the file we need to create a set up a Local Programming Environment for Python 3 and install flask. Asuming Python3 and Pip is installed we can do the following:
1. Open terminal and go to the directory containing the python file
2. Run the next command to create a local programing environment: 
   $ python3 -m venv my_env
3. Run the next command to activate the environment: 
   $ source my_env/bin/activate
4. Run the next command to install flask: 
   $ pip install flask
   
Note: make sure the environment is activated before running the file ($ source my_env/bin/activate).
   
Now, we can test the server:
1. Run the python file:
   $ python3 post_json_server.py
2. Open a new terminal window and run the curl POST request:
   $ curl -X POST http://localhost:8000/test --data '{"string_to_cut": "HelloWorld"}' -H 'Content-Type: application/json'
   
"string_to_cut" is the string which the program will cut every third letter. If the string is less than 3 characters then the program will return the orginal string
