up:
	docker-compose up -d --build
down:
	docker-compose down

local:
	docker-compose \
		-f docker-compose.local.yml up -d --build
local-down:
	docker-compose \
		-f docker-compose.local.yml down

full:
	docker-compose \
		-f docker-compose.yml \
		-f docker-compose.local.yml \
		-f docker-compose.final.yml --env-file=.env.local up -d --build	
full-down:
	docker-compose \
		-f docker-compose.yml \
		-f docker-compose.local.yml \
		-f docker-compose.final.yml down
