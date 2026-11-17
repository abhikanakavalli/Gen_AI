run-docker-compose:
	uv sync --no-install-project
	docker compose up --build -d
# 	docker compose down 
# docker compose ps -a