import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Capture the audio from the default microphone
with sr.Microphone() as source:
    print("Listening... Speak something!")
    recognizer.adjust_for_ambient_noise(source)  # Adjust for noise
    audio_data = recognizer.listen(source)  # Record the audio input

# Convert speech to text
try:
    print("Recognizing...")
    text = recognizer.recognize_google(audio_data)
    print("You said:", text)
except sr.UnknownValueError:
    print("Sorry, I couldn't understand the audio.")
except sr.RequestError as e:
    print("Sorry, I couldn't request results from Google Speech Recognition service; {0}".format(e))
