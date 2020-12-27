from typing import Any

import orjson
import uvicorn
from fastapi import FastAPI
from starlette.responses import JSONResponse

from car_market.api.health_check import router as health_check_router
from car_market.api.market import router as market_router
from car_market.infrastructure.version_provider import VersionProvider


class ORJSONResponse(JSONResponse):
    media_type = "application/json"

    def render(self, content: Any) -> bytes:
        return orjson.dumps(content)


app = FastAPI(default_response_class=ORJSONResponse)  # change default json to process nan

app.include_router(health_check_router)
app.include_router(market_router)


@app.on_event('startup')
def on_startup():
    app.state.version_provider = VersionProvider('0.0.1')


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
