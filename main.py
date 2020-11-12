from fastapi import FastAPI
from car_market.api.health_check import router as health_check_router
from car_market.infrastructure.version_provider import VersionProvider

app = FastAPI()

app.include_router(health_check_router)


@app.on_event('startup')
def on_startup():
    app.state.version_provider = VersionProvider('0.0.1')
