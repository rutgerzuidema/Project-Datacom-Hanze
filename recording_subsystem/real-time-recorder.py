# Import the necessary libraries
import pyaudio
from digital_filter import process_audio_frame  # Import the filter function

# Set the parameters for the audio recording
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Open an audio stream for recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

# Start recording
print("* recording")

# Stream audio to the digital filter
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    process_audio_frame(data)  # Send the frame to the filter

# Stop recording
print("* done recording")

# Close the stream and terminate PyAudio
stream.stop_stream()
stream.close()
audio.terminate()

#---------
# Filter import link for input streaming

# digital_filter.py
def process_audio_frame(frame):
    # Apply your digital filter to the frame
    # For demonstration, let's just print the frame length
    print(f"Processing frame of length: {len(frame)}")
