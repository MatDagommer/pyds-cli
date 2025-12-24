"""Small FastAPI app used as a template in generated projects.

Provides a single health-check endpoint and a uvicorn entrypoint for
local development.
"""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal

app = FastAPI(title="{{ cookiecutter.__repo_name }} API", version="0.1.0")


class HealthResponse(BaseModel):
	status: Literal["ok", "degraded", "down"]
	uptime_seconds: int | None = None


@app.get("/health", response_model=HealthResponse, summary="Health check")
async def health_check() -> HealthResponse:
	"""Return a simple health status for the service.

	This is intentionally minimal so consumers can probe readiness.
	"""
	# In a real app you'd compute uptime, DB connectivity etc.
	return HealthResponse(status="ok", uptime_seconds=None)
