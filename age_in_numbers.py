import time
import datetime

class YourAgeInNumber:
    def __init__(self, b_day, b_month, b_year):
        self.b_day = b_day
        self.b_month = b_month
        self.b_year = b_year
        self.current_day = datetime.date.today().strftime("%d")
        self.current_month = datetime.date.today().strftime("%m")
        self.current_year = datetime.date.today().strftime("%Y")

    def cal_day(self):
        return abs(int(self.current_day) - self.b_day)

    def cal_month(self):
        return  (int(self.current_month) - self.b_month) + 12 if int(self.current_month) < self.b_month else  abs(int(self.current_month) - self.b_month)

    def cal_year(self):
        return abs(int(self.current_year) - self.b_year) - 1 if self.current_month > self.b_month or (self.current_month == self.b_month and int(self.current_day) > self.b_day) else abs(int(self.current_year) - self.b_year)

    def __str__(self):
        return 'You\'re {} Years {} month and {} days old'.format(str(self.cal_year()),str(self.cal_month()),str(self.cal_day()))


a = YourAgeInNumber(b_day=19,b_month=9,b_year=1980)
print a
