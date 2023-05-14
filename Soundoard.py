# import msvcrt
# import pyaudio
# import wave
# import threading


# def play_audio(filename):
   
#     chunk = 2048  

#     wf = wave.open(filename, 'rb')

#     p = pyaudio.PyAudio()

#     stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
#                     channels = wf.getnchannels(),
#                     rate = wf.getframerate(),
#                     output = True)
    
#     micstream = p.open(format = pyaudio.paInt16,
#                     channels = 1,
#                     rate = 44100,
#                     input = True,
#                     input_device_index=1)

#     data = wf.readframes(chunk)
    
#     while data != '':
#         stream.write(data)
#         micstream.read(data)
#         data = wf.readframes(chunk)

#     stream.close()


# User_Input = ""

# while True:
    
#     if msvcrt.kbhit():
#         key = msvcrt.getch()
#         User_Input = key.decode("utf-8")
#         print(User_Input)
#         if User_Input == "1":
#             filname = 'tunamayo.wav'

#             # start playing audio in separate thread
#             t = threading.Thread(target=play_audio, args=(filname,))
#             t.start()


import msvcrt
import pyaudio
import wave
import threading

def play_audio(filename):
    chunk = 2048  
    wf = wave.open(filename, 'rb')
    p = pyaudio.PyAudio()
    # micstream = p.open(format=pyaudio.paInt16,
    #                    channels=1,
    #                    rate=44100,
    #                    input=True,
    #                    frames_per_buffer=chunk,
    #                    input_device_index=1)
    print(p.get_default_output_device_info())
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    data = wf.readframes(chunk)
    while data != '':
        stream.write(data)
        # micstream.read(chunk)
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