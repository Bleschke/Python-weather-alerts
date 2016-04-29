from urllib2 import urlopen
import json
import time
import os
import sys
import RPi.GPIO as GPIO
import pyvona


v = pyvona.create_voice('Access Key', 'Secret Key')
v.region = 'us-east'
v.voice_name = 'Salli'

global WeatherLED
WeatherLED = 18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(WeatherLED, GPIO.OUT)

GPIO.output(WeatherLED,False)

req = urlopen('http://api.wunderground.com/api/API KEY/alerts/q/STATE/CITY.json')
parsed_json = json.load(req)

type = str(parsed_json['alerts'][0]['type'])
description = str(parsed_json['alerts'][0]['description'])
date = str(parsed_json['alerts'][0]['date']) 
expires = str(parsed_json['alerts'][0]['expires'])
significance = str(parsed_json['alerts'][0]['significance'])


# The following is a debugging value.
# Edit out the hash and change
# The Voice alert response.

# The default setting is to play a voice over the speakers
# for any active alerts.


if type == 'TOR':
	print ('Tornado Warning')
	GPIO.output(WeatherLED,True)
	cmd_string = 'mpg123 -q /home/pi/WeatherAlerts/TornadoAlert.mp3'
	os.system(cmd_string)
	v.speak('ATTENTION! A')
	v.speak(description)
	v.speak('is in effect from')
	v.speak(date)
	v.speak('until')
	v.speak(expires)
	v.speak('SEEK SHELTER IMMEDIATELY!')
	

elif type == 'TOW':
	print ('Tornado Watch')
	GPIO.output(WeatherLED,True)
	cmd_string = 'mpg123 -q /home/pi/WeatherAlerts/EAS.mp3'
	os.system(cmd_string)
	v.speak('ATTENTION! A')
	v.speak(description)
	v.speak('is in effect from')
	v.speak(date)
	v.speak('until')
	v.speak(expires)

elif type == 'VOL':
	print ('Volcanic Activity Statement')
	GPIO.output(WeatherLED,True)
	cmd_string = '/home/pi/WeatherAlerts/speech.sh ATTENTION! A'
	os.system(cmd_string)
	v.speak('ATTENTION! A')
	v.speak(description)
	v.speak('is in effect from')
	v.speak(date)
	v.speak('until')
	v.speak(expires)
		
elif type == 'HWW':
	print ('Hurricane Wind Warning')
	GPIO.output(WeatherLED,True)
	cmd_string = '/home/pi/WeatherAlerts/speech.sh ATTENTION! A'
	os.system(cmd_string)
	v.speak('ATTENTION! A')
	v.speak(description)
	v.speak('is in effect from')
	v.speak(date)
	v.speak('until')
	v.speak(expires)

elif type == 'WRN':
	print ('Severe Thunderstorm Warning')
	GPIO.output(WeatherLED,True)
	cmd_string = 'mpg123 -q /home/pi/WeatherAlerts/WeatherBugNotification.mp3'
	os.system(cmd_string)

elif type == 'SEW':
	print ('Severe Thunderstorm Watch')
	GPIO.output(WeatherLED,True)
	cmd_string = 'mpg123 -q /home/pi/WeatherAlerts/WeatherBugNotification.mp3'
	os.system(cmd_string)	

elif type == 'WIN':
	print ('Winter Weather')
	GPIO.output(WeatherLED,True)
		

elif type == 'FLO':
	print ('Flood Warning')
	GPIO.output(WeatherLED,True)
		

elif type == 'WAT':
	print ('Flood Watch')
	GPIO.output(WeatherLED,True)
		

elif type == 'WND':
	print ('High Wind Advisory')
	GPIO.output(WeatherLED,True)
	cmd_string = 'mpg123 -q /home/pi/WeatherAlerts/WeatherBugNotification.mp3'
	os.system(cmd_string)	

elif type == 'HEA':
	print ('Heat Advisory')
	GPIO.output(WeatherLED,True)	

elif type == 'FIR':
	print ('Fire Weather Advisory')
	GPIO.output(WeatherLED,True)
	cmd_string = 'mpg123 -q /home/pi/WeatherAlerts/WeatherBugNotification.mp3'
	os.system(cmd_string)	

elif type == 'FOG':
	print ('Dense Fog Advisory')
	GPIO.output(WeatherLED,True)
		


else:

	print ('No Active Severe Weather Alerts')
	GPIO.output(WeatherLED,False)
	

