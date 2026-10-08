#!/usr/bin/env bash
set -euo pipefail

cd /docker/personal-travel || {
  echo "Diretório /docker/personal-travel não existe. Crie o diretório e rode novamente."
  exit 1
}

if [ -d .git ]; then
  git pull origin main
else
  git clone https://github.com/ederqueirozdf/personal-travel.git .
fi

cp -n .env.example .env || true

if [ -n "${TRAEFIK_HOST:-}" ]; then
  echo "Usando Traefik Hostinger"
  docker compose -f docker-compose.yml -f docker-compose.traefik.yml up -d --build
else
  echo "Usando stack local"
  docker compose up -d --build
fi

docker compose ps
