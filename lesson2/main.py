class Transport:

    def __init__(self, title, model, engine):
        self.title = title
        self.model = model
        self.engine = engine

    def start(self):
        print(f"{self.title} {self.model} start engine")


class Car(Transport):

    def __init__(self, title, model, engine, hp, nm):
        super().__init__(title, model, engine)
        self.hp = hp
        self.nm = nm


class Airplane(Car):
    def __init__(self, title, model, engine):
        super().__init__(title, model, engine)


bmw = Car(
    title="BMW",
    model="m5",
    engine="v10",
    hp=510,
    nm=550)
bmw.start()



