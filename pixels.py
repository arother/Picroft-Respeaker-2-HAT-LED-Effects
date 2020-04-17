"""
LED light pattern like Google Home
"""
from mycroft_bus_client import MessageBusClient, Message
from effects import PixelEffects

pixels = PixelEffects()
client =MessageBusClient()

def wakeword_dtected(message):
    pixels.wakeup()
    pixels.listen()

def audio_output_start(message):
    pixels.speak()

def m_ready(message):
    pixels.off()

def record_end(message):
    pixels.think()

if __name__ == '__main__':
    pixels.wakeup()
    pixels.think()
    client.on('mycroft.ready',m_ready)
    client.on('recognizer_loop:wakeword', wakeword_dtected)
    client.on('recognizer_loop:record_end',record_end)
    client.on('recognizer_loop:audio_output_start',audio_output_start)
    client.on('recognizer_loop:audio_output_end',m_ready)
    client.run_forever()