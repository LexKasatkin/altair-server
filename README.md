#altair 
##Project setup
###Database
sudo -su postgres
psql

SELECT 
    pg_terminate_backend(pid) 
FROM 
    pg_stat_activity 
WHERE 
    -- don't kill my own connection!
    pid <> pg_backend_pid()
    -- don't kill the connections to other databases
    AND datname = 'realty';
DROP DATABASE realty;
CREATE DATABASE realty;

###Migrate
python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
