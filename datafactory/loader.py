import json

import config


def loadDrugs():
    fin = open(config.DRUGBANK_FILE)
    drugNames = set()
    while True:
        line = fin.readline()
        if line == "":
            break
        parts = line.strip().split("||")
        name = parts[0]
        if config.INCHIKEY_REQUIRED:
            inchiKey = parts[4].strip()
            if len(inchiKey) < 2:
                continue

        if len(name) >= config.DRUGNAME_MIN_LENGTH:
            continue
        drugNames.add(name.capitalize())
        if config.FULL_DRUGNAME_LIST:
            synNames = parts[-2].split("|")
            synNames = [n.capitalize() for n in synNames]
            for synName in synNames:
                drugNames.add(synName.capitalize())

            saltNames = parts[-1].split("|")
            saltNames = [n.capitalize() for n in saltNames]
            for saltName in saltNames:
                drugNames.add(saltName.capitalize())
    fin.close()
    return sorted(list(drugNames))


def loadDrugMap(*args):
    fin = open(config.DRUGBANK_FILE)
    drugInfoMap = {}
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
        if config.INCHIKEY_REQUIRED:
            if len(inchiKey) < 2:
                continue

        synNames = parts[-2].split("|")
        synNames = [n.capitalize() for n in synNames]

        saltNames = parts[-1].split("|")
        saltNames = [n.capitalize() for n in saltNames]

        drugNameMap[drugName] = drugName
        for synName in synNames:
            drugNameMap[synName] = drugName
        for saltName in saltNames:
            drugNameMap[saltName] = drugName
        info = {"drugName": drugName,
                "inchiKey": inchiKey,
                "drugBankID": drugbankId,
                "smile": smile,
                "synNames": synNames,
                "saltNames": saltNames
                }
        drugInfoMap[drugName] = info
    fin.close()
    return drugInfoMap, drugNameMap


def getAllDrugNames(*args):
    drugs = loadDrugs()
    allDrugNames = json.dumps(drugs)
    return allDrugNames
