from fastapi import APIRouter

from car_market.domain.models import Car

router = APIRouter()


@router.post('/market', description='Create market from Car', response_model=Market)
async def resolve_market(car: Car) -> Market:
    ...
