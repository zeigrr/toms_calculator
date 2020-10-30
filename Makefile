run:
	docker-compose -f docker-compose.yml build
	docker-compose -f docker-compose.yml up -d

stop:
	docker-compose -f docker-compose.yml down

run_tests:
	docker-compose -f docker-compose.pytest.yml up
	docker-compose -f docker-compose.pytest.yml down
