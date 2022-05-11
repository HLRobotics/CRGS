#@author:Er.Akhil P Jacob
#HLEngine Environmental settings
import subprocess
import sys
import time
def setup_libraries():
    print("\n[ WELCOME TO CRGS System based SWARM Technology Installation Wizard ]")
    time.sleep(1)
    print("\n[ INKER ROBOTICS SOLUTION Private Limited 2021]")
    time.sleep(1)
   
    print("\n[ Note:It is recommended to close all other applications including Editors or IDE's on installation ]")
    from xml.dom import minidom
    mydoc = minidom.parse('payload_setup.xml')
    payload = mydoc.getElementsByTagName('payload')    
    xfile=open("log.txt","w")
    xfile.write("")
    xfile.close()    
    for elem in payload:
        print(elem.firstChild.data)
        package = str(elem.firstChild.data)
        try:
            print("[ SWARM : Please Wait ......  ]")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        except:
            print("[ SWARM: Installation failed.... ]")
            xfile=open("log.txt","a")
            xfile.write(package)
            xfile.close()
    print('[***** ENJOY *****]')



setup_libraries()
