<p> In this repository, we are going to import data from an CSV file into an existing django model and create REST API Using Core Django to retrieve data. We use visual studio to write the python scripts with Python 3.9.4 version.</p>
<br>
<p>First we need to clean the data.</p>
<p>Our data contain a single column called <code>'NUMDOS|NUMDOSVERLING|ANCART|FILIERE|ETAPE|VERLING|FORMAT'</code></p>
<p>We are going to separate it with the symbol '|' to obtain 7 new colomuns with their values: <code>norme/data_cleaning.py</code></p>
<br>There are no columns with the same values and there are no duplicate values.
<br>
<h3>Steps to upload csv file:</h3>
<ul>
  <li>Create a virtual environment<br><code>py -m venv venv</code></li>
  <li>Activate the virtual environment<br><code>venv/Scripts/activate</code></li>
  <li>Install Django<br><code>pip install django</code></li>
  <li>Build a project Django admin start project<br><code>django-admin startproject core .</code></li>
  <li>Build a project Django admin start app called norme<br><code>django-admin startapp norme</code></li>
  <li>Build a model from data. We are going to create a new class called Norme in the following path<br><code>norme/models.py</code></li>
  <li>Register our application into <code>core/settings.py</code> so it finds our new model <code>norme</code></li>
  <li>Apply the migrations files to create the tables in the database<br><code>manage.py makemigrations</code> <br><code>manage.py migrate</code><br>First command, will make the migration files (a file that contains the equivalent SQL statements for Database) and second command will execute it.</li>
  <li>Install extension SQLite in visual studio</li>
  <li>Download sqlite.exe from website sqlite.org/download.html (for example: for windows) then drag that into our project. We use that to access our database and load up our csv file.</li>
  <li>Run <code>sqlite.exe</code> file and then select the database <code>db.sqlite3</code> we want to work with<br><code>sqlite.exe db.sqlite3</code></li>
  <li>Load up our csv file into the database<br><code>.mode csv</code><br><code>.import data_cleaning.csv norme_norme</code></li>
</ul>
<br>
<h3>Steps to get data using API:</h3>
<ul>
  <li>Create views: <code>norme/views.py</code></li>
    <ol>
      <li></li>
    </ol>
  <li></li>
  <li></li>
  <li></li>
  <li></li>
  <li></li>
</ul>
