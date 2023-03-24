# BanglaTTS
BanglaTTS is a text-to-speech (TTS) system for Bangla language that works in offline mode. You can convert text to speech in male or female voice.

## Features
* Convert any bangla text to speech.
* Save the converted speech as an audio file.

## Requirements
* Python 3.6 or higher

## Installation
```bash
pip install BanglaTTS
```

## Usage
```python
from banglatts import BanglaTTS


tts = BanglaTTS(save_location="save_model_location")
path = tts("আমি বাংলায় কথা বলতে পারি।", voice='female', filename='1.wav') # voice can be male or female
```


