#! /usr/bin/env bash

export $(grep -v '^#' postgres/database.env | xargs -d '\n')
export POSTGRES_HOST=localhost

export FIRST_SUPERUSER=putin@sntozero.com
export FIRST_SUPERUSER_PASSWORD=shalom

cd web/backend/machine
python initial_data.py
