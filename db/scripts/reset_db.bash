#!/usr/bin/env bash

#
# Load a SQL file into db using user:pass
#
function loadSqlIntoDB
{
   echo ">>> $2 ($1)"
    if [[ "$OSTYPE" == "msys" ]]; then
        winpty mysql --table --host=127.0.0.1 -u$3 -p -e "source sql/$1"
    else
        mysql --table --host=127.0.0.1 -u$3 -p < sql/$1 > /dev/null
    fi
}

#
# Recreate and reset the database to be as after part II.
#
echo ">>> Reset recipe database"
echo ">>> Recreate the database (as root)"
loadSqlIntoDB "setup.sql"       "Create database"   "root"
loadSqlIntoDB "ddl.sql"     "Create tables"     "dev"
loadSqlIntoDB "insert_generated.sql"  "Insert all recipes" "dev"
