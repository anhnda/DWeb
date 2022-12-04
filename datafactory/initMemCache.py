from cache.MemCache import getMemCache

def initMemCache():
    # Set all drugNames
    memCache = getMemCache()
    from datafactory.loader import getAllDrugNames
    memCache.setValueByName("allDrugNames", getAllDrugNames())

    # Set drug name map:
    from datafactory.loader import loadDrugMap
    memCache.setValueByName("drugMap", loadDrugMap())
    return memCache

initMemCache()