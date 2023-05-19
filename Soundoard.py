import msvcrt
import pyaudio
import wave
import threading

def play_audio(filename):
    chunk = 2048  
    wf = wave.open(filename, 'rb')
    p = pyaudio.PyAudio()
    print(p.get_default_output_device_info())
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    data = wf.readframes(chunk)
    while data != '':
        stream.write(data)
        data = wf.readframes(chunk)
    stream.close()

User_Input = ""
while True:
    if msvcrt.kbhit():
        key = msvcrt.getch()
        User_Input = key.decode("utf-8")
        print(User_Input)
        if User_Input == "1":
            filename = 'tunamayo.wav'
            t = threading.Thread(target=play_audio, args=(filename,))
            t.start()