import msvcrt
import pyaudio
import wave
import threading
import time

p = pyaudio.PyAudio()

def get_vbaudiocable_device_info():
    for i in range(p.get_device_count()):
        current_device = p.get_device_info_by_index(i)
        if current_device["name"] == "CABLE Input (VB-Audio Virtual C":
            return current_device

def play_audio(filename):
    with wave.open(filename, 'rb') as wf:
    # Define callback for playback (1)
        def callback(in_data, frame_count, time_info, status):
            data = wf.readframes(frame_count)
            # If len(data) is less than requested frame_count, PyAudio automatically
            # assumes the stream is finished, and the stream stops.
            return (data, pyaudio.paContinue)

        # Instantiate PyAudio and initialize PortAudio system resources (2)
        p = pyaudio.PyAudio()

        vb = get_vbaudiocable_device_info()

        # Open stream using callback (3)
        stream = p.open(format=pyaudio.paInt24,
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True,
                        output_device_index=vb["index"],
                        stream_callback=callback)

        # Wait for stream to finish (4)
        while stream.is_active():
            time.sleep(0.1)

        # Close the stream (5)
        stream.close()

        # Release PortAudio system resources (6)
        p.terminate()


print(get_vbaudiocable_device_info())

User_Input = ""
while True:
    if msvcrt.kbhit():
        key = msvcrt.getch()
        User_Input = key.decode("utf-8")
        print(User_Input)
        if User_Input == "1":
            filename = 'tunamayo.wav'
            play_audio(filename)