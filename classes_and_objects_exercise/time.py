class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):

        result = ''

        if self.seconds > Time.max_seconds:
            self.seconds = 0
            self.minutes += 1

            if self.minutes > Time.max_minutes:
                self.minutes = 0
                self.hours += 1

                if self.hours > Time.max_hours:
                    self.hours = 0

        if self.hours > 9:
            result += f'{self.hours}:'
        else:
            result += f'0{self.hours}:'

        if self.minutes > 9:
            result += f'{self.minutes}:'
        else:
            result += f'0{self.minutes}:'

        if self.seconds > 9:
            result += f'{self.seconds}'
        else:
            result += f'0{self.seconds}'

        return result

    def next_second(self):
        self.seconds += 1
        return self.get_time()


time = Time(23, 55, 9)
print(time.next_second())

time = Time(10, 59, 58)
print(time.next_second())

