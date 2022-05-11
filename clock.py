#!/usr/bin/python3

import Adafruit_CharLCD as LCD
from datetime import datetime

dt_now = datetime.now()

# GPIO Pin Assignment
lcd_rs = 7
lcd_en = 8
lcd_d4 = 25
lcd_d5 = 24
lcd_d6 = 23
lcd_d7 = 18

# 16 char 2 lines
lcd_columns = 16
lcd_rows = 2

#initize LCD
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)

today = dt_now.strftime(" %Y/%m/%d %a")
thisHour = int(dt_now.strftime("%I"))
thisMin = dt_now.strftime(":%M %p") 

if thisHour < 10:
    padding = "     "
else:
    padding = "    "

message_text = today + "\n" + padding + str(thisHour) + thisMin
lcd.message(message_text)

