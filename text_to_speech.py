import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 150)    # Speed of speech
engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  
# The text you want to convert to speech
text = "Hello, how can I assist you today?"

# Convert the text to speech
engine.say(text)

# Run the TTS engine
engine.runAndWait()
