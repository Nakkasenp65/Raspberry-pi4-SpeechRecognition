import speech_recognition as sr
import RPi.GPIO as GPIO

recognizer = sr.Recognizer()
LED_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
setLight = 0

while True:
    try:

        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            print('I am listening: ')
            audio = recognizer.listen(mic)
            text = recognizer.recognize_google(audio)
            text = text.lower()
            print(f"Recognized: {text}")

            if text == 'turn on':
                setLight = 1
            if text == 'turn off':
                setLight = 0

            if setLight == 0:
                GPIO.output(LED_PIN, GPIO.LOW)
            if setLight == 1:
                GPIO.output(LED_PIN, GPIO.HIGH)

            if text == 'goodbye':
                GPIO.output(LED_PIN, GPIO.LOW)
                GPIO.cleanup()
                break

    except sr.UnknownValueError:
        print('Restart From Not Understand')
        recognizer = sr.Recognizer()
        continue

