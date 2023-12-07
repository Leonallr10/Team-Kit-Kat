from machine import Pin, Timer, UART
import utime
from machine import PWM
from time import sleep
from machine import time_pulse_us
import time

timer = Timer()
trigger = Pin(14, Pin.OUT)
echo = Pin(15, Pin.IN)
distance = 0
pir = Pin(17, Pin.IN)
uart0 = UART(0, 9600)
led1 = Pin(16, Pin.OUT)
led1.value(0)
uart0.write("welcome to void \n")
buzz = Pin(4, Pin.OUT)

trigger1 = Pin(2, Pin.OUT)
echo1 = Pin(3, Pin.IN)
distance1 = 0


def get_distance():
    global distance
    trigger.high()
    utime.sleep(0.00001)
    trigger.low()
    while echo.value() == 0:
        start = utime.ticks_us()

    while echo.value() == 1:
        stop = utime.ticks_us()
    duration = stop - start
    distance = (duration * 0.0343) / 2
    print(distance, "cm")

    return distance


def ultra1():
    global distance1
    trigger1.low()
    utime.sleep_us(2)
    trigger1.high()
    utime.sleep_us(5)
    trigger1.low()
    while echo1.value() == 0:
        signaloff = utime.ticks_us()
    while echo1.value() == 1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    distance1 = (timepassed * 0.0343) / 2
    distance1 = (18.5 - distance1) * 100 / 18.5
    if distance1 < 1:
        distance1 = 0
    print(distance1, "percentage full")
    return distance1


while True:
    if uart0.any() > 0:
        data = uart0.read(1)
        if "a" in data:
            uart0.write("dustbin turned on ")
            uart0.write("\n")
            led1.value(1)
            while True:
                get_distance()
                sleep(0.2)
                if distance < 20:
                    servo = PWM(Pin(10))  # the Pico PWM pin
                    servo.freq(50)

                    # Move to 150 degrees
                    servo.duty_u16(7500)

                    sleep(0.9)

                    # Wait for 6 seconds
                    servo.deinit()
                    sleep(3)
                    # Return to normal position
                    servo.duty_u16(3500)

                    sleep(0.8)

                    servo.deinit()
                    uart0.write(str(distance1))
                    uart0.write("  percent full")
                    uart0.write("\n")

                ultra1()
        elif "b" in data:
            uart0.write("alarm system turned on")
            uart0.write("\n")
            while True:
                if pir.value() == 1:
                    print(f"PIR value: {pir.value()}     Status: Motion detected!")
                    uart0.write("someone in the house")
                    uart0.write("\n")
                    led1.value(1)
                    buzz.value(1)
                    sleep(5)
                    buzz.value(0)

                else:
                    print(f"PIR value: {pir.value()}     Status: Waiting for movement...")
                    led1.value(0)

                # PIR sensor would check for movement every second
                sleep(1)
