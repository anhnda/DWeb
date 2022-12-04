import os
from cache.MemCache import MemCache

C_DIR = os.path.dirname(os.path.abspath(__file__))


DRUGBANK_FILE = "%s/resource/DrugBankNameX.txt" % C_DIR
DRUGNAME_MIN_LENGTH = 10