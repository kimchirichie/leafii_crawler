# Leafii Web Crawler

To use the module, you must have python virtualenv:

```
$ sudo apt-get install python-pip  # for debian/ubuntu
$ sudo pacman -S python-pip # for arch
```

Download & cd to directory:

```
$ git clone git@github.com:sinr0202/leafii_crawler
$ cd leafii_crawler
```

Activate the virtualenv

```
$ source ./bin/activate
```

Install the required modules

```
$ pip install -r requirements.txt
```

### How to use API:

To use the crawler to parse localhost database:

```bash
$ python crawler/createSearchables.py
$ python crawler/testDB.py
```

***Note***: Whenever you are running the parser more than once, make sure to remove the
            collections: keywords_coll, skill_coll, degree_coll, in your terminal before
            running again. Otherwise, you will have duplicate keys in the database


***Note***: If you are running Windows, grab the .tar or .zip files, and extract the folder
			containing the .py files for the library, into wherever you installed Python.
			Find the folder called, "site-packages", and just extract the folder in there