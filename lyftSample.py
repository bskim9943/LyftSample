from flask import Flask, request
import json

#intialize app
app = Flask(__name__)

#set route to test and use post method
@app.route('/test', methods=['Post'])

#function to process JSON object
def processJSON():
    #request string
    string_to_cut = request.json['string_to_cut']
    #pass string to string function
    return_string = stringCut(string_to_cut)
    #return string output
    json_return = {"return_string": return_string}
    #return jwon
    return json.dumps(json_return)

#function to get every 3rd letter in string
def stringCut(string):
    #intialize count and result
    count = 0
    result = []
    for letter in string:
        #count every letter in string
        count += 1
        #if count reaches 3, add to result and reset count
        if count == 3:
            result.append(letter)
            count = 0
    #return result
    return "".join(result)
    
if __name__ == '__main__':
    app.run(debug=True, port=5000)
