# Text-To-Speech

This is a simple Text-to-Speech (TTS) web application built using Python, Flask, and pyttsx3. The application allows users to type text into a web interface, submit it, and hear the text spoken aloud through the Python pyttsx3 engine. The web app is hosted locally and can be accessed via a browser.

## Table of Contents
  1. [ Features ](#Features)
  2. [ Prerequisites ](#Prerequisites)
  3. [ How to Run the Project ](#How-to-Run-the-Project)
  4. [ Usage ](#Usage)
  5. [ Customization ](#Customization)

## Features

- Text Input: Type any text into a text box on the web page.
- Text-to-Speech: The typed text is converted into speech using the pyttsx3 TTS engine.
- Cross-Platform Support: Works on all platforms (Windows, macOS, Linux) because pyttsx3 is an offline text-to-speech 
  engine.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.7 or higher
- pip package manager

## How to Run the Project

 1. Clone the repository (or download the files):
    ```
    
    git clone <repository-url>
    cd <repository-folder>
    
    ```
 2. Install dependencies:
    ```

    pip install -r requirements.txt

    ```
 3. Run the Flask app:
    ```

    python app.py

    ```
 4. Open your browser and go to http://127.0.0.1:5000/ or http://localhost:5000/. You should see a webpage with a text box 
    and a button.
    
##Usage:
- Enter the text you want to convert to speech in the text box.
- Click the "Speak" button to hear the typed text.
- The application will use the pyttsx3 engine to convert text to speech.
    
## Customization
  ### Changing the Speech Rate
  If you want to change the rate at which the speech is spoken, you can modify the rate property in the app.py file:
  ```
    
  engine.setProperty('rate', 150) # Adjust 150 to a higher or lower value

  ```
  ### Changing the Volume
  You can adjust the volume of the speech in the app.py file:
  ```

   engine.setProperty('volume', 0.9)  # Value between 0.0 and 1.0

   ```
   ### Changing the Voice
   To change the voice (e.g., male or female), modify the following line in the app.py file:
   ```
   voices = engine.getProperty('voices')
   engine.setProperty('voice', voices[0].id)  # Change index for different voices (0: male, 1: female)
   ```
  
    

    






























