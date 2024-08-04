import pyaudio
import wave

FRAMERATE_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000

p = pyaudio.PyAudio()

stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=FRAMERATE_PER_BUFFER
)

print('Started streaming')

seconds = 5
frames = []

for i in range(0, int(RATE / FRAMERATE_PER_BUFFER * seconds)):
    data = stream.read(FRAMERATE_PER_BUFFER)
    frames.append(data)

stream.stop_stream()
stream.close()
p.terminate()

print('Finished streaming')

obj = wave.open('./wav/intro.wav', 'wb')
obj.setnchannels(CHANNELS)
obj.setsampwidth(p.get_sample_size(FORMAT))
obj.setframerate(RATE)
obj.writeframes(b''.join(frames))
obj.close()

