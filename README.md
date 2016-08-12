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
$ sudo pip install -r requirements.txt
```

### How to use API:

***Note*** Make sure database is running while using the package

To use the crawler to parse localhost database:

```bash
$ python -m crawler/scripts/createSearchable
$ python -m crawler/scripts/reparse
```

***Note***: If you are running Windows, grab the .tar or .zip files, and extract the folder
			containing the .py files for the library, into wherever you installed Python.
			Find the folder called, "site-packages", and just extract the folder in there