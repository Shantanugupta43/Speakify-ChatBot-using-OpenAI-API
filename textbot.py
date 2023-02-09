import openai   # importing openAI Library
import speech_recognition as sr  # Importing Speech Recognition Library

from gtts import gTTS  # importing Google Text To Speech Library
import pygame  # importing pygame



# A function to speak a message using the gTTS engine
def speak(message):
    tts = gTTS(text=message, lang='en-gb', slow=False)  # text will load the message when the speak(message) function is used in English UK language and in normal speed
    tts.save("C:/Users/gupta/Downloads/textbot/file.mp3") # saves that audio as file.mp3
    pygame.init()  #pygame used to load and play the sound
    pygame.mixer.music.load("C:/Users/gupta/Downloads/textbot/file.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(2)
    pygame.quit()
    

# Set the API key for OpenAI
openai.api_key = "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" 

# Initialize the text-to-speech engine

# Starting Message
speak("Hello Shaan! I am now activated. Talk to me or ask me questions. I am happy to assist")

# Creating a function for generating a response from the OpenAI API
def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.9,
    )

    return response.choices[0].text





# Define a function to recognise speech using the speech_recognition library
def recognize_speech():
    r = sr.Recognizer()  
    with sr.Microphone() as source:  # when microphone on
        speak("Speak Now!") # says this message
        audio = r.listen(source, timeout=3)   # setting microphone timeout till 3 seconds after getting the message
    
    try:
        return r.recognize_google(audio)  
    except sr.UnknownValueError:                #setting exception errors
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print("")
        return None



# Using a loop such that a user can infinitely talk with the bot
while True:
    user_input = recognize_speech()  #uses recognise speach function which turns on the mic and starts listening
    if user_input == "exit":
        break
    response = generate_response(user_input)  # the user response is stored in the variable user_input and we use generate_response function to communicate bot response via the api
    print(f"Bot: {response}")  #printing the response
    speak(response)  # saying the response 
    


