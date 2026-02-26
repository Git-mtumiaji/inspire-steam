# Name : Ronnie Muturi
# Date : 26/02/2026
# Program to make a password in Wokwi

from machine import Pin, I2C, PWM
import time
from i2c_lcd import I2cLcd  # make sure lcd_api.py & i2c_lcd.py are added

# ---------------- LCD SETUP ----------------
I2C_ADDR = 0x27
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

# ---------------- BUZZER ----------------
buzzer = PWM(Pin(15))

# ---------------- KEYPAD SETUP ----------------
rows = [Pin(6, Pin.OUT), Pin(7, Pin.OUT), Pin(8, Pin.OUT), Pin(9, Pin.OUT)]
cols = [Pin(10, Pin.IN, Pin.PULL_DOWN), Pin(11, Pin.IN, Pin.PULL_DOWN),
        Pin(12, Pin.IN, Pin.PULL_DOWN), Pin(13, Pin.IN, Pin.PULL_DOWN)]

keys = [
    ['1','2','3','A'],
    ['4','5','6','B'],
    ['7','8','9','C'],
    ['*','0','#','D']
]

# ---------------- FUNCTIONS ----------------
def read_key():
    for r in range(4):
        rows[r].high()
        for c in range(4):
            if cols[c].value():
                time.sleep(0.25)  # debounce
                rows[r].low()
                return keys[r][c]
        rows[r].low()
    return None

def beep(times):
    """Simple single-tone beep"""
    for _ in range(times):
        buzzer.freq(1000)
        buzzer.duty_u16(30000)
        time.sleep(0.2)
        buzzer.duty_u16(0)
        time.sleep(0.2)

def alarm():
    """Stronger sweeping alarm siren"""
    for _ in range(10):  # repeat 10 times
        # sweep up
        for freq in range(600, 1500, 50):
            buzzer.freq(freq)
            buzzer.duty_u16(30000)
            time.sleep(0.01)
        # sweep down
        for freq in range(1500, 600, -50):
            buzzer.freq(freq)
            buzzer.duty_u16(30000)
            time.sleep(0.01)
    buzzer.duty_u16(0)

def get_password(message):
    lcd.clear()
    lcd.putstr(message)
    lcd.move_to(0, 1)
    entered = ""
    while True:
        key = read_key()
        if not key:
            continue
        # CLEAR
        if key == '*':
            entered = ""
            lcd.move_to(0, 1)
            lcd.putstr(" " * 16)
            lcd.move_to(0, 1)
        # ENTER
        elif key == '#':
            if len(entered) == 6:
                return entered
            else:
                lcd.move_to(0, 1)
                lcd.putstr("Need 6 digits")
                time.sleep(1)
                lcd.move_to(0, 1)
                lcd.putstr(" " * 16)
                lcd.move_to(0, 1)
                entered = ""
        # DIGITS
        elif key.isdigit() and len(entered) < 6:
            entered += key
            lcd.putstr("*")

# ---------------- SET PASSWORD ----------------
lcd.clear()
lcd.putstr("Set Password")
time.sleep(1)
password = get_password("Set Password")
lcd.clear()
lcd.putstr("Password Saved")
beep(1)
time.sleep(1)

# ---------------- MAIN LOOP ----------------
while True:
    entered = get_password("Enter Password")
    if entered == password:
        lcd.clear()
        lcd.putstr("Access Granted")
        beep(1)
    else:
        lcd.clear()
        lcd.putstr("Wrong Password")
        alarm()  # intense siren alarm
    time.sleep(2)