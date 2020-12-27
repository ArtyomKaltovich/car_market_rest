import nest_asyncio

from car_market.domain.models import Car

nest_asyncio.apply()  # https://github.com/encode/starlette/issues/440#issuecomment-524613908

import pytest
from fastapi.testclient import TestClient
from main import app
from fastapi.encoders import jsonable_encoder

client = TestClient(app)


@pytest.mark.asyncio
async def test_market_resolver_WhenSalesEvenThenMiddleMean():
    response = client.post("/market",
                           json=jsonable_encoder(Car(brand=2, model=1, city=1)),
                           )
    assert response.status_code == 200
    assert response.text == '{"car":{"brand":2,"model":1,"city":1},' \
                            '"median_price":102.5,' \
                            '"sales":[{"id":4,"car":{"brand":2,"model":1,"city":1},"selling_price":100},' \
                            '{"id":5,"car":{"brand":2,"model":1,"city":1},"selling_price":105}]}'


@pytest.mark.asyncio
async def test_market_resolver_WhenSalesOddThenMiddle():
    response = client.post("/market",
                           json=jsonable_encoder(Car(brand=1, model=1, city=1)),
                           )
    assert response.status_code == 200
    assert response.text == '{"car":{"brand":1,"model":1,"city":1},' \
                            '"median_price":105.0,' \
                            '"sales":[{"id":1,"car":{"brand":1,"model":2,"city":1},"selling_price":104},' \
                            '{"id":2,"car":{"brand":1,"model":1,"city":1},"selling_price":105},' \
                            '{"id":3,"car":{"brand":1,"model":1,"city":1},"selling_price":110}]}'
