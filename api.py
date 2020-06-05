import os;
import json;
from flask import Flask, request, send_from_directory, abort
from flask_cors import CORS
from dotenv import load_dotenv
from postal.parser import parse_address

load_dotenv()

app = Flask(__name__, static_url_path='/static')
CORS(app)
app.config['DEBUG'] = True

@app.route('/parseAddress', methods=['POST'])
def home():
    req_data = request.get_json()
    validateInput(req_data)
    result = parseAddress(req_data['address'])
    return json.dumps(result)

@app.route('/demo', methods=['GET'])
def demo():
     return app.send_static_file('index.html')

@app.route('/sampleData', methods=['GET'])
def sampleData():
     return app.send_static_file('sampleData.json')

if __name__ == '__main__':
    app.run(port=os.environ["PORT"])

def validateInput(req_data):
    # checks for incoming json and address key, if not then returns 400 bad request
    if req_data is None:
        abort(400)
    if 'address' not in req_data:
        abort(400)

def parseAddress(address):
    # parses address string with libpostal and returns as dictionary
    result = parse_address(address)
    dict = {k: v for (v, k) in result}
    return renameDictKeys(dict)

def renameDictKeys(dict):
    # renames libpostal result dictionary keys with predefined keys
    renameKeysDict = {
        'road': "street",
        'house_number': "housenumber",
    }
    for oldKey, newKey in renameKeysDict.items():
        if oldKey in dict:
            dict[newKey] = dict.pop(oldKey)
              
    return dict

