import time

class TrafficLight:
    __color = ""
    __schedule = []

    def __init__(self, schedule = []):
        if len(schedule):
            self.__schedule = schedule
        else:
            self.__schedule = [{"color": "red", "duration": 7}, {"color": "yellow", "duration": 2}, {"color": "green", "duration": 5}]

    def running(self):
        i = -1
        direction = 1
        scheduleLen = len(self.__schedule)
        while True:
            if i == -1 or (self.__schedule[i]['start_time'] + self.__schedule[i]['duration'] <= time.time()):
                if i+direction*1 >= scheduleLen or i+direction*1 < 0:
                    direction *= -1
                i += direction*1
                self.__color = self.__schedule[i]['color']
                self.__schedule[i]['start_time'] = time.time()
                print(self.__color)

if __name__ == '__main__':
    trLight = TrafficLight()
    trLight.running()