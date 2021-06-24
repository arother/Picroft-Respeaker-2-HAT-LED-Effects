"""
LED light pattern like Google Home
"""
from mycroft_bus_client import MessageBusClient, Message
from effects import PixelEffects
import threading


timer = None
pixels = PixelEffects()
client =MessageBusClient()

def wakeword_dtected(message):
    pixels.wakeup()
    pixels.listen()

def m_ready(message):
    pixels.off()

def record_end(message):
    pixels.think()
    global timer
    timer = threading.Timer(10.0,pixels.off) 
    timer.start()

def audio_output_start(message):
    global timer
    timer.cancel()
    pixels.speak()

if __name__ == '__main__':
    pixels.wakeup()
    pixels.think()
    client.on('mycroft.ready',m_ready)
    client.on('recognizer_loop:wakeword', wakeword_dtected)
    client.on('recognizer_loop:record_begin', wakeword_dtected)
    client.on('recognizer_loop:record_end',record_end)
    client.on('recognizer_loop:audio_output_start',audio_output_start)
    client.on('recognizer_loop:audio_output_end',m_ready)
    client.on('recognizer_loop:sleep',m_ready)
    client.run_forever()
