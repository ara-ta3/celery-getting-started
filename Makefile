DOCKER_COMPOSE=$(shell which docker-compose)
PYTHON=python

run: bin/activate count.txt
	source $< && python ./main.py

celery/worker: bin/activate
	source $< && celery worker -A tasks

redis:
	$(DOCKER_COMPOSE) up

install: bin/activate
	source bin/activate && pip install -r requirements.txt

bin/activate:
	$(MAKE) virtualenv

virtualenv:
	virtualenv -p $(PYTHON) .

count.txt:
	echo 0 > $@

