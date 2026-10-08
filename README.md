# Travel Agent MVP

This project contains a minimal but realistic architecture for a travel search system with:

- travel search by cash
- search by miles/points
- Telegram bot integration
- web frontend
- background workers
- Docker Compose deployment for a VPS / Hostinger environment
- optional Traefik integration for automatic HTTPS routing

## Quick start

1. Copy `.env.example` to `.env`
2. Update the required environment values
3. Run the stack locally:

```bash
docker compose up --build -d
```

4. Verify services:

```bash
docker compose ps
```

## Hostinger + Traefik

For Hostinger VPS environments with Traefik already running in host mode, use the override file:

```bash
docker compose -f docker-compose.yml -f docker-compose.traefik.yml up -d --build
```

Expected variables:

```bash
export COMPOSE_PROJECT_NAME=travelagent
export TRAEFIK_HOST=yourdomain.com
```

Then the app becomes available through:

- https://${COMPOSE_PROJECT_NAME}.${TRAEFIK_HOST}
- https://api.${COMPOSE_PROJECT_NAME}.${TRAEFIK_HOST}

## Main services

- API: http://localhost:8000
- Web: http://localhost:3000
- Telegram bot: configured via env
- Postgres: localhost:5432
- Redis: localhost:6379

## Goal

The goal of this MVP is to demonstrate the architecture and deployment pattern for a travel intelligence agent that can search and compare flights in money and in miles, returning the best three options with explanations, prices, airline, stops, baggage and savings versus the original dates.
