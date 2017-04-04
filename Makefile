dev:
	pip install -r dev-requirements.txt

test:
	nosetests -s tests/

data-server:
	docker run -p 80:80 osier
