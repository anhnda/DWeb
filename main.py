import json

from flask import Flask, send_from_directory
from datafactory.initMemCache import initMemCache
import utils

memCache = initMemCache()

app = Flask(__name__, static_url_path='',
            static_folder='static',
            template_folder='templates')



@app.route("/")
def index():
    return send_from_directory("static", "index.html")


@app.route("/get/drugs")
def get_drugs():
    allDrugNames = memCache.getValueByName("allDrugNames")
    # print(allDrugNames)
    return allDrugNames


@app.route("/get/druginfo/<drugname>")
def get_druginfo(drugname):
    drugname = str(drugname)
    drugName = drugname.lower().capitalize()
    drugNameMap = memCache.getValueByName("drugNameMap")
    drugNameMapped = utils.get_dict(drugNameMap, drugName, None)

    if drugNameMapped is not None:
        allDrugInfo = memCache.getValueByName("drugInfoMap")
        drugInfo = utils.get_dict(allDrugInfo, drugNameMapped, None)
        assert drugInfo is not None
        drugInfo["drugName"] = drugName

    else:
        drugInfo = {"drugName": "Not found", "searchName": drugName}
    v = json.dumps(drugInfo)
    return v
