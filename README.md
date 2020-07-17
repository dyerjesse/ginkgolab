# ginkgolab
ginkgo fitness app for data and fitness nuts a like.

If you don't already have pip installed:
$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

If you don't already have python2 installed:

next install pandas 
$ pip install pandas

Clone ginkgolab
$ git clone git@github.com:dyerjesse/ginkgolab.git

Clone fitparse mod to fitparse
$ git clone git@github.com:artcompiler/fitparse.git

Enter fitparse directory
$ cd fitparse

Clone fitparse and install dependencies
$ git clone git@github.com:dtcooper/python-fitparse.git
$ cd python-fitparse
$ python setup.py install

Take a .fit and place it in users/fitparse/data directory.

$ cd ../tools

Open t.py in editor

$ open t.py

Modify the read file to the name of your fit file to match that of the fit file you added in the data directory

$ fitfile = FitFile('./data/*YOURFILENAME*.fit')

Run t.py using python 2 from the tools directory

$ python2 t.py

Enter the ginkgolab.
cd ginkgolab/app

Run convert.py with your own '*file.json' 
