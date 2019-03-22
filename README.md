# PySAP_SL

> Automation module for source list in SAP

This automation module has been created to ease the creation of automation script for source list in SAP.

It can perform creation, modification, deletion and extraction task for source list.

The module leverage SAP GUI Scripting API in order to perform action in SAP.

## Installation

You can install the package through pip by using the below command :
```
pip install PySAP_SL 
```
Then you will have to modify the configuration file (should be found under path_to_Python_directory/Lib/site-packages/PySAP_SL) and add the name of your SAP system, the date format and the default value for source list.

I highly recommend you to run test in safe environnement before using PySAP_SL in a production environment.
Test are stored in the file test.py located in the path_to_Python_directory/Lib/site-packages/PySAP_SL/ directory, you can run them by simply go to this directory and run ```python -m unittest```

## Usage example

```
import PySAP_SL

app = PySAP_SL.SapSession("E1P300")
sl =  PySAP_SL.SL("10005465","2006",app)

sl_data = {'Vendor' : 'ICP1010', 'POrg' : 1000, 'Vendor Plant' : '1010', 'Fixed' : True}
sl.update_data(sl_data)

sl.delete_sl(delete_all=True)
sl.create_sl()

sl_data = {'Vendor' : 'ICP1010', 'POrg' : 1000, 'Vendor Plant' : '1010', 'Fixed' : False}
sl.update_data(sl_data)

sl.update_sl()
```

## Meta

Yacine BEKKA – [Linkedin](https://www.linkedin.com/in/yacine-bekka-519b79146) – yacinebekka@yahoo.fr

Distributed under MIT license. See ``LICENSE`` for more information.
