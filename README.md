<p> In this repository, we are going to import data from an CSV file into an existing django model. We use visual studio to write the python scripts with Python 3.9.4 version.</p>
<br>
<p>First we need to clean the data.</p>
<p>Our data contain a single column called 'NUMDOS|NUMDOSVERLING|ANCART|FILIERE|ETAPE|VERLING|FORMAT'</p>
<p>We are going to separate it with the symbol '|' to obtain 7 new colomuns with their values: norme/data_cleaning.py</p>
<br>
<h3>Steps to upload csv file:</h3>
<ul>
  <li>Create a virtual environment<br><code>py -m venv venv</code></li>
  <li>Activate the virtual environment<br><code>venv/Scripts/activate</code></li>
  <li>Install Django<br><code>pip install django</code></li>
  <li>Build a project Django admin start project<br><code>django-admin startproject core .</code></li>
  <li>Build a project Django admin start app called norme<br><code>django-admin startapp norme</code></li>
  <li>Build a model from data. We are going to create a new class called Norme in the following path<br><code>norme/models.py</code></li>
  <li>Register our application into core/settings.py so it finds our new model 'norme'</li>
  <li>Apply the migrations files to create the tables in the database<br><code>manage.py makemigrations</code> <br><code>manage.py migrate</code></li>
  <li>Install extension SQLite in visual studio</li>
  <li>Download sqlite.exe from website sqlite.org/download.html (for example: for windows) then drag that into our project. We use that to access our database and load up our csv file.</li>
  <li>Run sqlite.exe file and then select the database 'db.sqlite3' we want to work with<br><code>sqlite.exe db.sqlite3</code></li>
  <li>Load up our csv file into the database<br><code>.mode csv</code><br><code>.import data_cleaning.csv norme_norme</code></li>
</ul>
