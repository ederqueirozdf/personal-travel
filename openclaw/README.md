# OpenClaw agent profile: personal-travel

This directory contains the OpenClaw profile for the travel agent.

The agent is designed to operate as the orchestrator layer between the Telegram user, the travel search API and the trip optimizer logic.

## Responsibilities

- understand travel requests from Telegram or web
- normalize origin, destination, dates and search window
- trigger the flight search API
- compare cash and miles offers
- sort the top 3 options with explanations
- answer the user in natural language

## Required permissions

- call the internal search API
- read the travel search schema
- write messages to Telegram chats authorized by the bot
- consult the ranking and recommendation engine

## Files

- agents/personal-travel/agent.yaml — agent definition and permissions
- agents/personal-travel/instructions.md — role and behavior instructions
- tools/travel-api.yaml — HTTP tool definition for search and ranking actions
- tools/telegram-bot.yaml — Telegram permissions for outbound messages
