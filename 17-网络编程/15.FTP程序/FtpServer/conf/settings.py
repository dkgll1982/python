import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

USER_HOME = "%s/home" % BASE_DIR
LOG_DIR = "%s/log" % BASE_DIR
LOG_LEVEL = "DEBUG"

ACCOUNT_FILE = "%s/conf/accounts.cfg" % BASE_DIR

<<<<<<< HEAD
HOST = "127.0.0.1"
=======
HOST = "0.0.0.0"
>>>>>>> 8c71f90a755f435117c304b5b10d4370e123be32
PORT = 9999

