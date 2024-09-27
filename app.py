from flask import Flask, request, jsonify
import pyttsx3

app = Flask(__name__)

# Initialize the TTS engine globally
engine = pyttsx3.init()

# Set up some default properties for the engine
engine.setProperty('rate', 150)    # Speed of speech
engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # You can change the voice index here

# Define an API endpoint to accept text input and trigger TTS
@app.route('/speak', methods=['POST'])
def speak():
    data = request.json
    text = data.get('text', '')
    
    if text:
        # Speak the text
        engine.say(text)
        engine.runAndWait()
        return jsonify({"message": "Speech completed"}), 200
    else:
        return jsonify({"error": "No text provided"}), 400

# Serve the HTML page on the root URL
@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Text to Speech</title>
    </head>
    <body>
        <h1>Text to Speech</h1>
        <textarea id="text" rows="5" cols="40" placeholder="Enter text here..."></textarea><br><br>
        <button onclick="convertToSpeech()">Speak</button>

        <script>
            function convertToSpeech() {
                const text = document.getElementById("text").value;
                fetch('/speak', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ text: text })
                })
                .then(response => response.json())
                .then(data => {
                    console.log(data);
                })
                .catch(error => {
                    console.error('Error:', error);
                });
            }
        </script>
    </body>
    </html>
    '''

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
