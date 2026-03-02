#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE DATABASE auth_db;
    CREATE DATABASE userdb;
    CREATE DATABASE companydb;
    CREATE DATABASE jobdb;
    CREATE DATABASE applicationdb;
EOSQL
