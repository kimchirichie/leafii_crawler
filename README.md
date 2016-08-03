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

### statistical_parsing.py functions:

```
get_all_urls()
```
Returns a list of all the urls users have submitted

```
insert_word(str word)
```
 Inserts a word into the database with a count of zero, and returns true, unless it already exists, in which case it returns false.

```
count_words(str url)
```
Not currently finished

```
count_total_words()
```
Counts the total number of words in the database and returns an integer value

```
count_distinct_words()
```
Counts the number of distinct words in the database which have appeared at least once, and returns an integer value

```
average_count()
```
Calculates the average number of repititions a words has in the database and returns an integer value

```
std_count()
```
Calculates the standard deviation of the number of repititions a words has in the database and returns an integer value

```
order_keywords()
```
Returns a list of all the keywords in the database which have appeared at least once, in descending order of their repitions, displaying both the keywords and the number of times they've appeared


```
calculate_keywords(int total_words)
```
Not currently finished
