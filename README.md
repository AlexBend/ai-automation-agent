# AI Automation Agent

A FastAPI-based AI automation service for classifying incoming user requests and preparing them for further agent-based processing.

## Current stage

Stage 1: Basic FastAPI service with structured request classification.

## Features

- FastAPI REST API
- Pydantic request/response schemas
- Structured classification result
- Health check endpoint
- Basic test coverage

## Run locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload