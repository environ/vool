
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN)

impuls_count = 0

# Do next lines for i.e. 1000ms:

while True:
  GPIO.wait_for_edge(25, GPIO.FALLING)
  impuls_count = impuls_count + 1
  print impuls_count


