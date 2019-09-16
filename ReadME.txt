How to make the application work:

step 1 : create DATABASE ::::::::::::::::::::::::::::::::::::

1>Install mysql on you system/server.
2>sql>create database clippy_user; #this will create a data base called clippy_user
3>sql>use clippy_users; #displays the list of DB's, everything we do after executng this command will apply only to this DB.
4>sql>create table clippy_admin_users ( ID int primary key, username varchar(20), password varchar(20)); # creates the table named clippy_admin_users.
5>sql>insert into clippy_admin_users values(1,'sherayas','root'); #insterts the records in the table.
6>sql>select * from clippy_admin_users; # displays all records in table.

step 2: how to clone the project:::::::::::::::::::::::::::::

1> go to your desired path, and perform 
	git init #initilasizes the git repo.
2> git remote add origin https://github.com/STejas91/CRUD.git #connects your local repo to my repo.
3> git clone https://github.com/STejas91/CRUD.git # clones the entire project to your local repo.


step 3 : steps up virtual environment for flask:::::::::::::::

3> $python3 -m venv dbenv # while executing the command make sure you are in "db_project" directory, here we create a virtual environment for our project
4> $ source dbenv/bin/activate #this will activate the Virtual environment for us to work on.
5> $python3 crud.py # runs the .py app
6> the app runs on local machine port 8001.

Note :

please edit the crud.py to change only the below parameters from the code:

app.config['MYSQL_DATABASE_USER'] = 'your username'
app.config['MYSQL_DATABASE_PASSWORD'] = 'your password for database'



