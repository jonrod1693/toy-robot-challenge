build:
	docker build -t toy-robot .

run:
	docker run --name toy-robot-container --rm -it toy-robot

stop:
	docker stop toy-robot-container

pytest:
	docker run --name toy-robot-container --rm -it toy-robot sh -c pytest

start: build run

test: build pytest
