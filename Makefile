active:
	source venv/bin/activate

dev:
	python api/main.py


deploy:
	docker build -t registry.heroku.com/overwatcher2/web --platform linux/amd64 .
	docker push registry.heroku.com/overwatcher2/web
	heroku container:release web -a overwatcher2