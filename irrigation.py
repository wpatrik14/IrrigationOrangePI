#!/usr/bin/env python
#import the library
from pyA20.gpio import gpio
from pyA20.gpio import port
import schedule
import time
from time import sleep

#initialize the gpio module
gpio.init()
gpio.setcfg(port.PG7, gpio.OUTPUT)
gpio.output(port.PG7, gpio.HIGH)

def job(interval):
	print("Irrigation will go for "+str(interval)+" minutes")
	gpio.output(port.PG7, gpio.LOW)
	print(time.strftime("%H:%M:%S")+" - Irrigation turned ON")
	sleep(60*interval)
	gpio.output(port.PG7, gpio.HIGH)
	print(time.strftime("%H:%M:%S")+" - Irrigation turned OFF")
	sleep(60)

schedule.every().day.at("04:00").do(job,25)
schedule.every().day.at("04:30").do(job,25)
schedule.every().day.at("05:00").do(job,25)
schedule.every().day.at("05:30").do(job,25)

schedule.every().day.at("19:30").do(job,25)
schedule.every().day.at("20:00").do(job,25)
schedule.every().day.at("20:30").do(job,25)
schedule.every().day.at("21:00").do(job,25)


while True:
    schedule.run_pending()
    time.sleep(1)
