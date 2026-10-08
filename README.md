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

## OpenClaw integration

This project is prepared to run with an OpenClaw orchestrator that controls the travel agent profile.

The agent profile is located in:

- [openclaw/agents/personal-travel/agent.yaml](openclaw/agents/personal-travel/agent.yaml)
- [openclaw/agents/personal-travel/instructions.md](openclaw/agents/personal-travel/instructions.md)
- [openclaw/tools/travel-api.yaml](openclaw/tools/travel-api.yaml)
- [openclaw/tools/telegram-bot.yaml](openclaw/tools/telegram-bot.yaml)

The agent has explicit permissions to:

- call the travel API for flight searches and ranking
- send replies to Telegram chats authorized by the bot
- answer users with top 3 options, baggage, economy and drawbacks

## Main services

- API: http://localhost:18000
- Web: http://localhost:13000
- Telegram bot: configured via env
- Postgres: localhost:15432
- Redis: localhost:16379

## Goal

The goal of this MVP is to demonstrate the architecture and deployment pattern for a travel intelligence agent that can search and compare flights in money and in miles, returning the best three options with explanations, prices, airline, stops, baggage and savings versus the original dates.
