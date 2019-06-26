# Brian Leschke
# June 1, 2019
# Version 3.0
# Python Weather Alerts

import feedparser
import os
import time
import sys

weatherAlert = False

feed = feedparser.parse(r'https://alerts.weather.gov/cap/wwaatmget.php?x=LOCATION_KEY_HERE&y=0')

os.system("echo manual > /sys/devices/platform/odroidu2-fan/fan_mode")
os.system("echo 0 > /sys/devices/platform/odroidu2-fan/pwm_duty")
time.sleep(1)
os.system("echo 5 > /sys/devices/platform/odroidu2-fan/pwm_duty")
time.sleep(1)
os.system("echo 0 > /sys/devices/platform/odroidu2-fan/pwm_duty")

if weatherAlert == False:
	for entry in feed.entries:
		if entry.cap_event == "Tornado Warning":
			weatherAlert = True
			os.system("echo 5 > /sys/devices/platform/odroidu2-fan/pwm_duty")
			print("EVENT: " + entry.cap_event)
			os.system("mpg123 -q /home/odroid/WeatherAlerts/tornado-warning.mp3")
			time.sleep(4)
			os.system("mpg123 -q /home/odroid/WeatherAlerts/TornadoAlert.mp3")
			time.sleep(10)
			break

		elif entry.cap_event == "Tornado Watch":
			weatherAlert = True
			os.system("echo 5 > /sys/devices/platform/odroidu2-fan/pwm_duty")
			print("EVENT: " + entry.cap_event)
			os.system("mpg123 -q /home/odroid/WeatherAlerts/tornado-watch.mp3")
			time.sleep(4)
			os.system("mpg123 -q /home/odroid/WeatherAlerts/EAS.mp3")
			time.sleep(10)
			break

		elif entry.cap_event == "Volcanic Activity Statement":
			weatherAlert = True
			os.system("echo 5 > /sys/devices/platform/odroidu2-fan/pwm_duty")
			print("EVENT: " + entry.cap_event)
			os.system("mpg123 -q /home/odroid/WeatherAlerts/WeatherBugNotification.mp3")
			time.sleep(10)
			break

		elif entry.cap_event == "Hurricane Wind Warning":
			weatherAlert = True
			os.system("echo 5 > /sys/devices/platform/odroidu2-fan/pwm_duty")
			print("EVENT: " + entry.cap_event)
			os.system("mpg123 -q /home/odroid/WeatherAlerts/wind.mp3")
			time.sleep(10)
			break

		elif entry.cap_event == "Blizzard Warning":
			weatherAlert = True
			os.system("echo 5 > /sys/devices/platform/odroidu2-fan/pwm_duty")
			print("EVENT: " + entry.cap_event)
			os.system("mpg123 -q /home/odroid/WeatherAlerts/WeatherBugNotification.mp3")
			time.sleep(10)
			break

		elif entry.cap_event == "Winter Storm Warning":
			weatherAlert = True
			os.system("echo 5 > /sys/devices/platform/odroidu2-fan/pwm_duty")
			print("EVENT: " + entry.cap_event)
			os.system("mpg123 -q /home/odroid/WeatherAlerts/WeatherBugNotification.mp3")
			time.sleep(10)
			break

		elif entry.cap_event == "Winter Storm Watch":
			weatherAlert = True
			os.system("echo 5 > /sys/devices/platform/odroidu2-fan/pwm_duty")
			print("EVENT: " + entry.cap_event)
			os.system("mpg123 -q /home/odroid/WeatherAlerts/WeatherBugNotification.mp3")
			time.sleep(10)
			break

		elif entry.cap_event == "Severe Thunderstorm Warning":
			weatherAlert = True
			os.system("echo 5 > /sys/devices/platform/odroidu2-fan/pwm_duty")
			print("EVENT: " + entry.cap_event)
			os.system("mpg123 -q /home/odroid/WeatherAlerts/lightning.mp3")
			time.sleep(10)
			break

		elif entry.cap_event == "Severe Thunderstorm Watch":
			weatherAlert = True
			os.system("echo 5 > /sys/devices/platform/odroidu2-fan/pwm_duty")
			print("EVENT: " + entry.cap_event)
			os.system("mpg123 -q /home/odroid/WeatherAlerts/thunderstorm.mp3")
			time.sleep(10)
			break

		elif entry.cap_event == "Flash Flood Warning":
			weatherAlert = True
			os.system("echo 5 > /sys/devices/platform/odroidu2-fan/pwm_duty")
			print("EVENT: " + entry.cap_event)
			os.system("mpg123 -q /home/odroid/WeatherAlerts/flood.mp3")
			time.sleep(10)
			break

		elif entry.cap_event == "Flood Warning":
			weatherAlert = True
			os.system("echo 5 > /sys/devices/platform/odroidu2-fan/pwm_duty")
			print("EVENT: " + entry.cap_event)
			os.system("mpg123 -q /home/odroid/WeatherAlerts/flood.mp3")
			time.sleep(10)
			break

		elif entry.cap_event == "Flood Watch":
			weatherAlert = True
			os.system("echo 5 > /sys/devices/platform/odroidu2-fan/pwm_duty")
			print("EVENT: " + entry.cap_event)
			os.system("mpg123 -q /home/odroid/WeatherAlerts/rain.mp3")
			time.sleep(10)
			break

		elif entry.cap_event == "High Wind Warning":
			weatherAlert = True
			os.system("echo 5 > /sys/devices/platform/odroidu2-fan/pwm_duty")
			print("EVENT: " + entry.cap_event)
			os.system("mpg123 -q /home/odroid/WeatherAlerts/wind.mp3")
			time.sleep(10)
			break

		elif entry.cap_event == "High Wind Watch":
			weatherAlert = True
			os.system("echo 5 > /sys/devices/platform/odroidu2-fan/pwm_duty")
			print("EVENT: " + entry.cap_event)
			os.system("mpg123 -q /home/odroid/WeatherAlerts/wind.mp3")
			time.sleep(10)
			break

		elif entry.cap_event == "Red Flag Warning":
			weatherAlert = True
			os.system("echo 5 > /sys/devices/platform/odroidu2-fan/pwm_duty")
			print("EVENT: " + entry.cap_event)
			os.system("mpg123 -q /home/odroid/WeatherAlerts/forest-fire.mp3")
			time.sleep(10)
			break

		elif entry.cap_event == "Fire Weather Warning":
			weatherAlert = True
			os.system("echo 5 > /sys/devices/platform/odroidu2-fan/pwm_duty")
			print("EVENT: " + entry.cap_event)
			os.system("mpg123 -q /home/odroid/WeatherAlerts/forest-fire.mp3")
			time.sleep(10)
			break

		elif entry.cap_event == "Fire Weather Watch":
			weatherAlert = True
			os.system("echo 5 > /sys/devices/platform/odroidu2-fan/pwm_duty")
			print("EVENT: " + entry.cap_event)
			os.system("mpg123 -q /home/odroid/WeatherAlerts/forest-fire.mp3")
			time.sleep(10)
			break

		elif entry.cap_event == "Heat Advisory":
			weatherAlert = True
			os.system("echo 5 > /sys/devices/platform/odroidu2-fan/pwm_duty")
			print("EVENT: " + entry.cap_event)
			os.system("mpg123 -q /home/odroid/WeatherAlerts/WeatherBugNotification.mp3")
			time.sleep(10)
			break

		elif entry.cap_event == "Fire Weather Advisory":
			weatherAlert = True
			os.system("echo 5 > /sys/devices/platform/odroidu2-fan/pwm_duty")
			print("EVENT: " + entry.cap_event)
			os.system("mpg123 -q /home/odroid/WeatherAlerts/WeatherBugNotification.mp3")
			time.sleep(10)
			break

		elif entry.cap_event == "Dense Fog Advisory":
			weatherAlert = True
			os.system("echo 5 > /sys/devices/platform/odroidu2-fan/pwm_duty")
			print("EVENT: " + entry.cap_event)
			os.system("mpg123 -q /home/odroid/WeatherAlerts/WeatherBugNotification.mp3")
			time.sleep(10)
			break

		else:
			print ('No Notable Severe Weather Alerts')
			os.system("echo 0 > /sys/devices/platform/odroidu2-fan/pwm_duty")
else:
	print ('Weather Alert is True')
