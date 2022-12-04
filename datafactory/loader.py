import json

import config


def loadDrugs():
    fin = open(config.DRUGBANK_FILE)
    drugNames = []
    while True:
        line = fin.readline()
        if line == "":
            break
        parts = line.strip().split("||")
        name = parts[0]
        if len(name) >= config.DRUGNAME_MIN_LENGTH:
            continue
        drugNames.append(name.capitalize())
    fin.close()
    return drugNames


def loadDrugMap(*args):
    fin = open(config.DRUGBANK_FILE)
    drugNameMap = {}
    while True:
        line = fin.readline()
        if line == "":
            break
        parts = line.strip().split("||")
        name = parts[0]
        if len(name) >= config.DRUGNAME_MIN_LENGTH:
            continue
        drugName = name.capitalize()
        inchiKey = parts[4]
        drugbankId = parts[2]
        smile = parts[5]
        otherNames = parts[-2].split("|")
        otherNames = [n.capitalize() for n in otherNames]
        info = {"drugName": drugName,
                "inchiKey": inchiKey,
                "drugBankID": drugbankId,
                "smile": smile,
                "otherNames": otherNames
                }
        drugNameMap[drugName] = info
    fin.close()
    return drugNameMap


def getAllDrugNames(*args):
    drugs = loadDrugs()
    allDrugNames = json.dumps(drugs)
    return allDrugNames
