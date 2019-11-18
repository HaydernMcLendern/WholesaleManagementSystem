WholesaleManagementSystem

Instructions to run:

Install Python 3 on your device

Once installed, run
```
pip install Flask
```
and
```
pip install pymysql
```
in your command prompt

To connect it with your local database, edit this block in __init__.py
```
MYSQL_HOST='localhost',
        MYSQL_USER='yoursqluseraccount',
        MYSQL_PASS='yoursqluseraccountpassword',
        MYSQL_DB='yourdatabasename',
```
with your appropriate database connection information.

To run, click the run.bat file and load up http://127.0.0.1:5000 in your web browser. 


