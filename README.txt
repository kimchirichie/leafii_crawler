Instructions on Parser:

***Note***: Whenever you are running the parser more than once, make sure to remove the
            collections: keywords_coll, skill_coll, degree_coll, in your terminal before
            running again. Otherwise, you will have duplicate keys in the database

1. Open your terminal, and go into the directory that contains the .py files

2. Make sure to pip install pymongo, and pdfminder. In a later build, this will all
   be done for you, but for now pip install this.

2.2 If you are running Windows, grab the .tar or .zip files, and extract the folder
    containing the .py files for the library, into wherever you installed Python.
    Find the folder called, "site-packages", and just extract the folder in there

3. Type in your terminal, "python createSearchable.py"


4. Let it run, this python file will create a database of skills and degree keywords.
   It only needs to be run once, so never run it again

5. Now run "python testDB.py", and watch for any errors that shouldn't be there. For
   instance if you know that a website should be working, and it gives an error, "Error
   in html", make a note of it.

6. Your database should have the keywords inputted in now, and you're good to go.

For more information, or bugs please contact us @:
support@leafii.com
