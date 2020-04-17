# Simple demo of the TCS34725 color sensor.
# Will detect the color from the sensor and print it out every second.
import time
import board
import busio
import adafruit_tcs34725
import RPi.GPIO as GPIO
# Initialize I2C bus and sensor.
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_tcs34725.TCS34725(i2c)
GPIO.setmode(GPIO.BCM)
red = 18
green = 23
yellow = 24
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
# Main loop reading color and printing it every second.

def flash(num,col):
    print("blink ",col)
    GPIO.output(num,GPIO.LOW)
    time.sleep(1)
    GPIO.output(num,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(num,GPIO.LOW)
    time.sleep(1)
    
while True:
    # Read the color temperature and lux of the sensor too.
    r, g, b= 0, 0, 0
    GPIO.output(red,GPIO.HIGH)
    GPIO.output(yellow,GPIO.HIGH)
    GPIO.output(green,GPIO.HIGH)
    for i in range(8):
        temp = sensor.color_temperature
        lux = sensor.lux
        r += sensor.color_rgb_bytes[0]
        g += sensor.color_rgb_bytes[1]
        b += sensor.color_rgb_bytes[2]
       
        # print("Temperature: {0}K Lux: {1}".format(temp, lux))
        # Delay for a second and repeat.
        time.sleep(0.25)
    print('Average Color: ({0}, {1}, {2})'.format(r/8,g/8,b/8))
    print('Now flash LEDs')
    if r > max(g,b):
        flash(red,'red')
    elif g > max(r,b):
        flash(green,'green')
    elif b > max(r,g):
        flash(blue,'blue')
    else:
        print('same value, not flashing')
        
            
    
    