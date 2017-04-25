dev:
	pip install -r dev-requirements.txt

requirements:
	pip install -r requirements.txt

test:
	nosetests -s tests/

benchmark:
	nosetests -s benchmarks/ > benchmark.log 2> benchmark.err

data-server-10:
	docker run --name osier-data -d -p 80:80 earthquakesan/osier-data:server-10

data-server-30:
	docker run --name osier-data -d -p 80:80 earthquakesan/osier-data:server-30

data-server-50:
	docker run --name osier-data -d -p 80:80 earthquakesan/osier-data:server-50
