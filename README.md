# Logs Analysis Project
This project to analysis data from news database.we will do three queries:
1. Top three articles.
2. Top three authors.
3. On which days did more than 1% of requests lead to errors.

## What do you need to use in this project?
1. postegrsql
2. python2 or python3 (you need to use DB-API to connect python code with postegr database).
3. virtual box
4. virtual machine (vagrant)

## how run this project? 
1. install [Virtualbox](https://www.virtualbox.org/)
2. install virtual machine [Vagrant](https://www.vagrantup.com/)
3. inside vagrant folder inside virtual machine folder put newsdata.sql file inside vagrant folder.
4. cd into virtual machine folder which vagrant folder inside it.
5. `vagrant up` to start your VM.
6. `vagrant ssh` to login to your VM.
7. `psql -d news -f newsdata.sql` to load data from sql.
8. `python report.py` to run.

## views :
- In this program I used some [VIEWS](https://www.postgresql.org/docs/9.2/sql-createview.html) to store some selects.

> create view all_requist as 
select date(time),count(*) as num from log group by date(time);
---
> create view faild_requist as
select date(time),count(*) as num from log where status='404 NOT FOUND' group by date(time)
---
> create view precentage as
select all_requist.date,all_requist.num as all_req_num,faild_requist.num as faild_req_num,
faild_requist.num/all_requist.num*100 as faild_precentage
from all_requist,faild_requist
where all_requist.date=faild_requist.date;

## Resourses:
> [postgresql Documentation](https://www.postgresql.org/docs/9.2/sql-createview.html)
> [w3resourses](https://w3resource.com/PostgreSQL/rpad-function.php)
> [Writing code with DB-API](https://opensourceforu.com/2009/05/database-programming-in-python/)
> [Vagrant](https://www.vagrantup.com/)
> [Virtualbox](https://www.virtualbox.org/)


