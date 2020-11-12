from typing import Dict

from fastapi import APIRouter, Depends

from car_market.dependencies import get_version_provider
from car_market.infrastructure.version_provider import VersionProvider

router = APIRouter()


@router.get('/health_check')
async def health_check(version_provider: VersionProvider = Depends(get_version_provider)) -> Dict:
    return {'version': version_provider.get_version()}
