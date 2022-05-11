# RPi_CharLCD_Clock
This is a python Script for displaying the clock and date with Raspberry Pi and Adafruit_CharLCD.

## Pin Assignment and LCD Configulation
Please edit as needed.
````
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
````

## Usage
Put "clock.py" file on your home directory (or any directory) then run this command in your terminal.
````
$ python3 clock.py
````
Use with crontabs to run repeatedly。
````
$ crontab -e
* * * * * python3 ~/clock.py
````

## A Example of Execution Result
````
 2022/05/11 Wed
     4:21 PM
````
