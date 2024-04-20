import sys, os
from pyunpack import Archive
import zipfile
import tarfile
#import unrar

def setwd():
    usrdir = (sys.argv[1])
    os.chdir( os.getcwd() + '/' + usrdir)
    
def extractor():
    setwd()
    for file in os.listdir(os.getcwd()):
        print("[file] - {}".format(file))
    try:
        if py7zr.is_7zfile(file):
            with py7zr.SevenZipFile("test.7z", 'r') as seven:
                seven.extractall()
            print("[7z] - {}".format(seven))
            
            
        #TODO: fix library error for unrar
        #if unrar.rarfile.testrar():
            #with unrar.rarfile.RarFile("test.rar", 'r') as rar:
               # rar.testrar()
                #rar.namelist()
                #rar.extractall()
            #print("extracted:")
            #print(rar)
              
        if zipfile.is_zipfile(file):
            try: 
                with zipfile.ZipFile(file) as zip:
                    print("[zip] - {}".format(zip))
                    zip.extractall()
            except zipfile.BadZipFile as error:
                print(error)
                pass
        
        if tarfile.is_tarfile(file):
            try:
                with tarfile.open(file) as tar:
                    print("[tar] - {}".format(tar))
                    tar.extractall()
            except tarfile.TarError as error:
                print(error)
                pass
    # until recursion, skip a subdirectory and catch the error
    except IsADirectoryError as direrror:
        print("[skipped] - {}".format(direrror))
   
     

extractor()
print("scan complete")