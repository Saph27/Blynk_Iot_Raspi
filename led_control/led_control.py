import BlynkLib
import RPi.GPIO as GPIO
import BlynkTimer

BLYNK_AUTH_TOKEN = 'TSN7xn-TzqRlVLBJs3D_jfY7wDK01O2A' #Update this with your auth token

led1 = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led1, GPIO.OUT)


x = 20
# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH_TOKEN)

# Led control through V0 virtual pin
@blynk.on("V0")
def v0_write_handler(value):
#    global led_switch
    if int(value[0]) is not 0:
        GPIO.output(led1, GPIO.HIGH)
        print('LED1 HIGH')
    else:
        GPIO.output(led1, GPIO.LOW)
        print('LED1 LOW')

#function to sync the data from virtual pins
@blynk.on("connected")
def blynk_connected():
    print("Raspberry Pi Connected to New Blynk") 

while True:
    blynk.run()

