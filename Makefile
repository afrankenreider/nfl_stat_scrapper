DOCKERFILE := Dockerfile
APP_NAME := nfl_stats

## up                  | Build and run
up:
	docker-compose up -d --build

## down                | Stop the app
down:
	docker-compose down