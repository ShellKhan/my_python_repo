class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(self.name + ' is started')

    def stop(self):
        print(self.name + ' is stopped')

    def turn(self, direction):
        print(self.name + ' turns ' + direction)

    def show_speed(self):
        print('My speed is ' + str(self.speed) + 'mph')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('My speed is exceeded. Police catch me.')
        else:
            print('My speed is ' + str(self.speed) + 'mph')


class SportCar(Car):
    def flash_lights(self):
        print(self.name + ' flashes lights')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('My speed is exceeded. Police catch me.')
        else:
            print('My speed is ' + str(self.speed) + 'mph')


class PoliceCar(Car):
    siren = False

    def call_siren(self):
        self.siren = not self.siren
        if self.siren:
            print('Siren is on!')
        else:
            print('Siren is off...')


lincoln = TownCar(150, 'black', 'Lincoln', False)
taz = TownCar(50, 'blue', 'VAZ', False)
mustdie = SportCar(250, 'red', 'Bugatti', False)
bmv = SportCar(200, 'black', 'BMW', False)
truck = WorkCar(30, 'orange', 'ZIL', False)
foorah = WorkCar(90, 'gray', 'MAZ', False)
police = PoliceCar(100, 'yellow', 'uaz', True)

lincoln.go()
lincoln.stop()
lincoln.show_speed()

taz.turn('left')
taz.turn('right')
taz.show_speed()

print(mustdie.color)
mustdie.show_speed()

print(bmv.name)
bmv.show_speed()

truck.show_speed()
foorah.show_speed()

police.call_siren()
police.call_siren()
police.call_siren()
police.call_siren()
police.show_speed()
