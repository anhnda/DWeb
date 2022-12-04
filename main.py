import json

from flask import Flask, send_from_directory
from datafactory.initMemCache import initMemCache
import utils
memCache = initMemCache()


app = Flask(__name__, static_folder="static")


@app.route("/")
def index():
    return send_from_directory("static", "index.html")


@app.route("/get/drugs")
def get_drugs():
    allDrugNames = memCache.getValueByName("allDrugNames")
    print(allDrugNames)
    return allDrugNames


@app.route("/get/druginfo/<drugname>")
def get_druginfo(drugname):
    drugname = str(drugname)
    allDrugInfo = memCache.getValueByName("drugMap")
    drugInfo = utils.get_dict(allDrugInfo, drugname, None)
    if drugInfo is None:
        drugInfo = {"drugname": "Not found"}
    v = json.dumps(drugInfo)
    return v
