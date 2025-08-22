from draw import Draw
from datetime import datetime
import calendar
import requestAPI
import google_calendar
import secret

class CalendarDraw():
    def __init__(self):
        self.draw = Draw()
        self.now = datetime.now()
        self.y = self.now.year
        self.m = self.now.month
        self.d = self.now.day
        calendar.setfirstweekday(calendar.SUNDAY)
        self.calendar = calendar.monthcalendar(self.y, self.m)
        self.holidaysdic, self.holidays = self.__get_holidays()
        self.WEEK = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"]
        self.WEEKDAY = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    def draw_days(self):
        y = 120
        for index, weekstr in enumerate(self.WEEK):
            if index == 0:
                self.draw.text(weekstr, 32, y, 3, self.draw.RED)
                #epd.imagered.large_text(weekstr, 32, y, 3, 0xff)
            else:
                self.draw.text(weekstr, 32+(index*64), y, 3, self.draw.BLACK)
                #epd.imageblack.large_text(weekstr, 32+(index*64), y, 3, 0x00)

        dy = 56
        weeklen = len(self.calendar)
        if weeklen == 6:
            dy = 48
        if weeklen == 4:
            dy = 64
            
        y += dy
        for i in self.calendar:
            x = 32
            for index, day in enumerate(i):
                if day == 0:
                    pass
                else:
                    if day == self.d:
                        fill = True
                    else:
                        fill = False
                        
                    if index == 0 or day in self.holidays[self.m]:
                        c = self.draw.RED
                    else:
                        c = self.draw.BLACK
                        
                    self.draw.text(f"{day:>2}", x, y, 3, c, fill, 4, 8)

                x += 64
            y += dy

    def draw_today(self):
        self.draw.text(f"{self.y}", 32, 48, 2)
        self.draw.text(f"{self.m:02}/{self.d:02}", 116, 28, 5)
        self.draw.text(f"{self.WEEKDAY[datetime.isoweekday(self.now)%7]}", 336, 28, 5)

    def get_event(self):
        google_calendar.get_calendar_events()

    def __get_holidays(self):
        url = f"https://holidays-jp.github.io/api/v1/{self.y}/datetime.json"
        tmp = requestAPI.request_API(url)
        result = [[] for _ in range(12)]
        for date in tmp.keys():
            d = datetime.fromtimestamp(int(date))
            result[d.month].append(d.day)

        return tmp, result


c = CalendarDraw()
c.draw_days()
c.draw_today()
c.draw.line(500, 0, 500, 480, 3)
c.draw.line(0, 88, 500, 88, 3)

c.draw._save("image.png")