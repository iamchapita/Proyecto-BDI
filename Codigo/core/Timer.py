import time
import sys

# Por Ahora esta clase no se utiliza
class Timer:
    def __init__(self):
        self.hours = 0
        self.seconds = 0
        self.minutes = 0

    def start(self):

        while True:

            sys.stdout.write("\r{hours} Hours {minutes} Minutes {seconds} Seconds".format(hours=self.hours, minutes=self.minutes, seconds=self.seconds))
            sys.stdout.flush()
                
            if (self.seconds <= 59):
                time.sleep(1)
                self.seconds += 1

                if (self.minutes <= 59 and self.seconds == 59 + 1):
                    self.minutes += 1

                    if (self.minutes == 60 and self.seconds == 59 + 1 ):
                        self.hours += 1
                        self.minutes = 0
                        self.seconds = 0
            else:
                self.seconds = 0


obj = Timer()
obj.start()