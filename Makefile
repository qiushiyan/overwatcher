active:
	source venv/bin/activate

dev:
	python api/main.py

build:
	docker build -platorm linux/amd64 .
	heroku container:push web -a overwatcher2

deploy:
	docker build -t overwatcher2 --platform linux/amd64 .
	docker tag overwatcher2 registry.heroku.com/overwatcher2/web
	docker push registry.heroku.com/overwatcher2/web
	heroku container:release web -a overwatcher2