# class Car:
#
#     def start(self):
#         print("It's car start engine!")
#
#
# class Airplane:
#
#     def start(self):
#         print("It's Airplane")


class Car:

    _current_speed = 0

    def __init__(self, title, model, max_speed, speed):
        self.title = title
        self.model = model
        self.max_speed = max_speed
        self.speed = speed

    def get_current_speed(self):
        print(self._current_speed)

    def gas(self):
        if self._current_speed + self.speed > self.max_speed:
            print("CHECK")
        else:
            self._current_speed += self.speed
            self.get_current_speed()

    def br(self):
        if self._current_speed - self.speed < 0:
            self._current_speed -= self.speed
            self.get_current_speed()


tico = Car(
    title="Tiko",
    model="t",
    max_speed=150,
    speed=10
)

