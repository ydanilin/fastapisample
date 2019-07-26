#! /usr/bin/env bash

export $(grep -v '^#' postgres/database.env | xargs -d '\n')
export POSTGRES_HOST=localhost

if [ "$1" = "" ]; then
	message="Untitled"
else
	message=$1
fi

cd web/backend/machine
PYTHONPATH=. alembic revision --autogenerate -m "$message"
