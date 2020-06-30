class TrafficLight:
    __color = None
    COLORS = ('red', 'yellow', 'green')
    time_order = (7, 2, 6)

    def running(self, count=6):
        from itertools import cycle
        from time import sleep
        print('Program started')
        for index in cycle([0, 1, 2]):
            self.__color = self.COLORS[index]
            print('Color goes ' + self.__color)
            count -= 1
            if not count:
                print('Program stopped')
                break
            else:
                sleep(self.time_order[index])


testing_object = TrafficLight()
testing_object.running()
