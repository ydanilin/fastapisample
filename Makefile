run:
	bash run_develop.sh
depend:
	pip freeze | grep "fastapi\|uvicorn\|SQLAlchemy\|alembic\|psycopg2\|python-multipart\|pyjwt\|passlib\|bcrypt\|emails" > ./web/backend/requirements.txt
buildweb:
	docker build -t fapi ./web
dockback:
	docker run -d --rm --name fapi \
		--env-file postgres/database.env \
		-v $(CURDIR)/web/backend/machine:/app \
		-v uvicorn_sockdir:/var/uvicorn_sockdir \
		fapi \
		uvicorn app.main:app --uds /var/uvicorn_sockdir/backend.sock
docknginx:
	docker run -d --rm --name nginx \
		-v $(CURDIR)/nginx/fapi.conf:/etc/nginx/conf.d/fapi.conf \
		-v $(CURDIR)/nginx/logs:/etc/nginx/logs \
		-v uvicorn_sockdir:/var/uvicorn_sockdir \
		-p 80:80 \
		nginx
dockpostgr:
	docker run -d --rm --name postgres \
		--env-file postgres/database.env \
		-v uvicorn_sockdir:/var/run/postgresql \
		-v app-db-data:/var/lib/postgresql/data/pgdata \
		-p 5432:5432 \
		postgres:11
dockerit: dockback docknginx
dbadm:
	docker run --name admi --link postgres:example -p 8080:8080 -d --rm adminer
