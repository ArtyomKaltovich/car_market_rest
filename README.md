### Настройка
Install:
```
python -m pip install -r requirements.txt
```

Run service:
```bash
uvicorn main:app --reload --port 8000
```

UI: http://127.0.0.1:8000/docs

### Задача
С использованием FastAPI необходимо разработать http-сервис по расчету рынка проданных автомобилей. Т.е. на вход сервиса мы отдаем автомобиль, на выходе хотим получить рынок. 
Автомобиль представляет собой комбинацию марки, модели и города. Эти поля —целочисленные значения.
Рынок представляет собой сущность из автомобиля, количества авто на рынке и медианной цены среди продаж подобных авто.
Продажами управляет другой http-сервис. Предполагается, что клиент для сервиса продаж будет реализован в другой задаче. Примерный интерфейс клиента:

```python
@dataclass
class Car:
   brand: int
   model: int
   city: int

@dataclass
class Sale:
   id: int
   car: Car
   selling_price: int

class SalesClient(ABC):
   @abstractmethod
   async def find_sales(self, car: Car) -> List[Sale]:
        pass
```

Интерфейс сервиса должен быть REST. 

Бонус. Предполагаем, что в некоторых случаях рынок не может быть рассчитан быстро, поэтому мы не можем долго держать пользовательское http-соединение.