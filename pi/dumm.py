import RPi.GPIO as GPIO
import time
import wave
pin=4
chans = 1 # 1 channel
samp_rate = 44100 # 44.1kHz sampling rate
chunk = 4096 # 2^12 samples for buffer
record_secs = 6 # seconds to record
dev_index = 2 # device index found by p.get_device_info_by_index(ii)
wav_output_filename = 'test1.wav' # name of .wav file
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
ip = "172.22.5.242"
try:
    while True:
        if(GPIO.input(pin)==GPIO.LOW):
            print("sound detected")
            
except:
    GPIO.cleanup()