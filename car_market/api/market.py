from fastapi import APIRouter

from car_market.domain.models import Car, Market, Sale, DB

router = APIRouter()


def get_db():
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


DATABASE = get_db()  # TODO: replace by very big enterprise database


@router.post('/market', description='Create market from Car', response_model=Market)
async def resolve_market(car: Car) -> Market:
    return await DATABASE.find_sales(car)
