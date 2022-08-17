from lesson4.car.models import Bmw, Mers, Audi

cars = {
    "bmw": Bmw,
    "mers": Mers,
    "audi": Audi
}


def create(title, model, engine, which_car):
    return cars[which_car](title=title, model=model, engine=engine)

