# ginkgolab
ginkgo fitness app for data and fitness nuts a like.

If you don't already have python 3 installed go to https://www.python.org/downloads/ and download the version best suited for your OS.

If you don't already have python2 installed go to https://www.python.org/downloads/release/python-272/ and download the version best suited for your OS.

If you don't already have pip installed:

$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

next install pandas using pip

$ pip install pandas

Clone ginkgolab into your users directory

$ git clone git@github.com:dyerjesse/ginkgolab.git

Enter Ginkgolab directory

cd ginkgolab

Clone artcompiler mod of fitparse

$ git clone git@github.com:artcompiler/fitparse.git

Enter fitparse directory

$ cd fitparse

Clone fitparse and install dependencies

$ git clone git@github.com:dtcooper/python-fitparse.git

$ cd python-fitparse

$ python setup.py install

Go back one directory

$ cd ..

Take a .fit and place it in users/fitparse/data directory.
 
$ cd data

Take a step back

$ cd..

Enter the tools directory

$ cd ../tools

Open t.py in editor

$ open t.py

Modify the read file to the name of your fit file to match that of the fit file you added in the data directory

$ fitfile = FitFile('./data/*YOURFILENAME*.fit')

Run t.py and dump the file to a JSON using :

$ python2 t.py > "YOUROURFILE.json"

Copy the exported json you named which is now located in the tools directory t.py.

$ cd ../../

Enter app directory

$ cd app

Open convert.py

$ open convert.py

Change the Read json line to:

$ data = pd.read_json(r'YOURFILENAME.json')

Save convert.py and run

$ python convert.py
