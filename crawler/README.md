# Leafii - Web Crawler

Here are somethings it can do:

 * Connect to database & query users
 * Parse out website for keywords
 * Detect PDF's & parse them

To use the module, run virtual environment :+1:

```bash 
$ sudo apt-get install python-pip
$ sudo pip install virtualenv
$ cd ./path/to/repo
$ source ./bin/activate
$ pip install -r requirements.txt
```

### How to use API:

To use the crawler to parse localhost database:

```bash
$ python crawler/createSearchables.py
$ python crawler/testDB.py
```
