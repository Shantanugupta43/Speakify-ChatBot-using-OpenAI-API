<h1>VoiceAudio GPT ChatBot using OpenAI API</h1>

Created a chatbot using OpenAI API where a user can ask different questions or have casual conversations with the bot using speech.

<b> NOTE: No Neural Networks or Artificial Intelligence is used while coding the bot. It communicates all the responses from OpenAI Library.</b>

<h3> Instructions to use the Bot</h3>

- Import the code using ``git clone <repo-link>`` and navigate to the directory
- Install all the dependencies using ``pip install <dependency-name>``  The dependencies used here are openai, speech_recognition, gtts and pygame.
- Run the command ``python textbot.py`` to start the application


<b>OR</b>

- Click the <b>textbot.exe</b> file in the dist folder.

<h3> Packaging the bot into .exe file</h3>

To package the bot into executable file-

Install PyInstaller using pip: ``pip install pyinstaller``
Navigate to the directory where your Python file is located using the command prompt.
Run the following command: pyinstaller --onefile textbot.py
This will create a standalone executable file in the dist folder within the directory where your Python file is located.
