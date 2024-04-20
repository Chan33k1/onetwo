import sys
import os
from pyunpack import Archive
import zipfile
import tarfile

def setwd():
    usrdir = sys.argv[1]
    os.chdir(os.getcwd() + '/' + usrdir)

def extractor():
    setwd()
    for file in os.listdir(os.getcwd()):
        print("[file] - {}".format(file))
        try:
            if file.endswith(".7z"):
                Archive(file).extractall()
                print("[7z] - {}".format(file))
            elif zipfile.is_zipfile(file):
                with zipfile.ZipFile(file) as zip:
                    zip.extractall()
                print("[zip] - {}".format(file))
            elif tarfile.is_tarfile(file):
                with tarfile.open(file) as tar:
                    tar.extractall()
                print("[tar] - {}".format(file))
            else:
                print("[skipped] - Unsupported file format: {}".format(file))
        except Exception as error:
            print(error)
            pass

extractor()
print("scan complete")
