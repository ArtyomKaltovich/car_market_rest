import math

import pytest

from car_market.domain.models import DB, Car, Sale


@pytest.mark.asyncio
class TestFindSales:
    async def test_empty_db(self):
        client = DB()
        car = Car(brand=1, model=1, city=1)
        market = await client.find_sales(car)
        assert market.car == car
        assert math.isnan(market.median_price)
        assert market.sales == []

    @pytest.fixture(scope="class")
    def db(self):
        sales = [Sale(id=1, car=Car(brand=1, model=1, city=1), selling_price=100),
                 Sale(id=2, car=Car(brand=1, model=1, city=1), selling_price=105),
                 Sale(id=3, car=Car(brand=1, model=1, city=1), selling_price=110),

                 Sale(id=4, car=Car(brand=2, model=1, city=1), selling_price=100),
                 Sale(id=5, car=Car(brand=2, model=1, city=1), selling_price=105),

                 Sale(id=1, car=Car(brand=1, model=2, city=1), selling_price=100),
                 Sale(id=1, car=Car(brand=1, model=2, city=1), selling_price=101),
                 Sale(id=1, car=Car(brand=1, model=2, city=1), selling_price=104),

                 Sale(id=6, car=Car(brand=1, model=1, city=2), selling_price=100),
                 Sale(id=6, car=Car(brand=1, model=1, city=3), selling_price=100)]
        return DB(sales)

    async def test_brand(self, db):
        market1 = await db.find_sales(Car(brand=1, model=1, city=1))
        assert market1.median_price == pytest.approx(105.0)
        assert len(market1.sales) == 3
        market2 = await db.find_sales(Car(brand=2, model=1, city=1))
        # pandas returns (m[i - 1] + m[i]) / 2 in case of even number of elements
        assert market2.median_price == pytest.approx(102.5)
        assert len(market2.sales) == 2

    async def test_model(self, db):
        market = await db.find_sales(Car(brand=1, model=2, city=1))
        assert market.median_price == pytest.approx(101.0)
        assert len(market.sales) == 3

    async def test_city(self, db):
        market = await db.find_sales(Car(brand=1, model=1, city=2))
        assert market.median_price == pytest.approx(100.0)
        assert len(market.sales) == 1
        market = await db.find_sales(Car(brand=1, model=1, city=3))
        assert market.median_price == pytest.approx(100.0)
        assert len(market.sales) == 1
