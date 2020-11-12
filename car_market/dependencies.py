from fastapi.requests import Request

from car_market.infrastructure.version_provider import VersionProvider


def get_version_provider(request: Request) -> VersionProvider:
    """
    See: https://fastapi.tiangolo.com/tutorial/dependencies/
    :param request:
    :return:
    """
    return request.app.state.version_provider
