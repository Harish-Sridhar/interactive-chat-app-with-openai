# interactive-chat-app-with-openai
interactive chat app with openai whisper and chat gpt 3 model.

# Pre-requisties

* python `3.9`.
* Create an account in openai and create a API Key.

# setting up local environment

* create venv.
    
    # check if python version is 3.9
    python --version 
    # create venv
    python3 venv .venv

* install requirements

    source .venv/bin/activate
    pip install -r requirements.txt

* install ffmpeg. This is needed for openai-whisper

    # on Ubuntu or Debian
    sudo apt update && sudo apt install ffmpeg

    # on Arch Linux
    sudo pacman -S ffmpeg

    # on MacOS using Homebrew (https://brew.sh/)
    brew install ffmpeg

    # on Windows using Chocolatey (https://chocolatey.org/)
    choco install ffmpeg

    # on Windows using Scoop (https://scoop.sh/)
    scoop install ffmpeg


# Running the application

## setup openai api key env variable

* go to [openai website](https://platform.openai.com/overview) and create an account if you don't have one.  
* Once account is created. create API Keys. 
* Set up api key as env variable 

    export OPENAI_API_KEY=<Your API Key>

## starting the application

    ./.venv/bin/python frontend/app.py

then go to the url `http://127.0.0.1:5000/`

# Resources

* https://github.com/openai/whisper
* https://platform.openai.com/docs/introduction
* https://flask.palletsprojects.com/en/2.2.x/
* https://huggingface.co/blog/sentiment-analysis-python
* https://developer.mozilla.org/en-US/docs/Web/API/MediaStream_Recording_API/Using_the_MediaStream_Recording_API
* https://getbootstrap.com/

