# Python Library and CLI tool for working with the Uploadfiles.io API.

[![Uploadfiles.io](https://i.imgur.com/7mRrOkc.png)](https://uploadfiles.io)

# Features:
  - Pure Python3 solution 
  - Easy Install
  - Easy Interactions with Uploadfiles.io
  - Built in test funcitons

Customization quick start
-------------------------

To use ufile as the start of a new project, do the following, preferably in
a virtual environment. Clone the repo.

.. code-block:: console

    git https://github.com/osteth/ufile-tools.git
    cd ufile-tools
    
Then install locally.

    pip install
    py.test

Finally, give the command line program a try.

    ufile --help

### Usage
The ufile put command is used to upload a file you your Uploadfiles.io account. 
```sh
$ ufile out -f <file to upload>
```
The ufilesdown command is used to download a file from you Uploadfiles.io account. 
```sh
$ ufile get -s <SLUG> -p <SAVE PATH>
```
ufiles down can be used with or without a save path specified. if no save path is specified,the file will be save to the current directory using the slug as the filename. 

License
----

MIT


