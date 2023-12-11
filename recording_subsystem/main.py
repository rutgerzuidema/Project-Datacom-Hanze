
"Record audio signals from device microphone using Pyaudio Microphone class"
# Import the necessary libraries
import pyaudio
import wave

# Set the parameters for the audio recording
FORMAT = pyaudio.paInt16  # Audio format (16-bit PCM)
CHANNELS = 1              # Mono channel
RATE = 44100              # Sampling rate (44.1kHz)
CHUNK = 1024              # Number of frames per buffer
RECORD_SECONDS = 5        # Duration of recording in seconds
WAVE_OUTPUT_FILENAME = "output.wav"  # Output file name

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Open an audio stream for recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

# Start recording
print("* recording")
frames = []

# Record audio in chunks and append to the frames list
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

# Stop recording
print("* done recording")

# Close the stream and terminate PyAudio
stream.stop_stream()
stream.close()
audio.terminate()

# Save the recorded audio to a WAV file
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(audio.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()