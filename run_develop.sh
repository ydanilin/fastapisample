#! /usr/bin/env bash

export $(grep -v '^#' postgres/database.env | xargs -d '\n')
export POSTGRES_HOST=localhost
cd web/backend/machine
uvicorn app.main:app --reload
