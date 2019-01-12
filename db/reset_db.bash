#!/usr/bin/env bash

#
# Load a SQL file into skolan using user:pass
#
function loadSqlIntoSkolan
{
    echo ">>> $2 ($1)"
    mysql --table --host=127.0.0.1 -udev < scripts/$1 > /dev/null
}

#
# Recreate and reset the database to be as after part II.
#
echo ">>> Reset recipe database"
echo ">>> Recreate the database (as root)"
mysql --table --host=127.0.0.1 -uroot -p < scripts/setup.sql > /dev/null

loadSqlIntoSkolan "ddl.sql"     "Create tables"
loadSqlIntoSkolan "insert.sql"  "Insert into larare"
