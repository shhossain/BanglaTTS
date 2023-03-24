from typing import Union, List
import torch
from aksharamukha import transliterate
import os
import numpy as np
import scipy.io as sio
from datetime import datetime

MODEL_REPO = 'snakers4/silero-models'
MODEL_NAME = 'silero_tts'
LANGUAGE = 'indic'
SPEAKER = 'v3_indic'


class BanglaTTS:
    def __init__(self, voice='female', save_location=None, device=None, **kw):
        """
        BanglaTTS class to convert text to speech
        
        Methods:
        convert : Converts text to audio and saves it to a file
        convert_numpy : Converts text to audio and returns a numpy array of the audio file

        """
        if save_location is None:
            save_location = os.path.join(os.path.expanduser('~'), 'bangla_tts')
        self.save_location = save_location

        self.voice = self._get_voice(voice)

        torch.hub.set_dir(self.save_location)
        if device is None:
            device = torch.device(
                'cuda' if torch.cuda.is_available() else 'cpu')
        else:
            device = torch.device(device)

        self.model, utils = torch.hub.load(repo_or_dir=MODEL_REPO, model=MODEL_NAME,
                                           language=LANGUAGE, speaker=SPEAKER, device=device, trust_repo=True, **kw)

    def _get_voice(self, voice):
        if voice.lower()[0] == 'f':
            voice = 'bengali_female'
        else:
            voice = 'bengali_male'
        return voice

    def _romanize(self, text) -> str:
        return transliterate.process('Bengali', 'ISO', text)  # type: ignore

    def _save_audio(self, audio: np.ndarray, filename: str, sample_rate=44100) -> str:
        sio.wavfile.write(filename, sample_rate, audio)
        return filename

    def convert_numpy(self, text) -> np.ndarray:
        """
        Converts text to audio and returns a numpy array of the audio file
        
        Parameters:
        ----------
        text : str
            Text to convert to audio
        """
        text = str(text.strip())
        roman_text = self._romanize(text)
        audio = self.model.apply_tts(roman_text, speaker=self.voice)
        npaudio = np.array(audio)
        return npaudio

    def convert(self, text, filename: str = None, sample_rate=44100) -> str:  # type: ignore
        """
        Converts text to audio and saves it to a file
        
        Parameters:
        ----------
        text : str
            Text to convert to audio
        filename : str, optional
            Filename or path to save the audio file, by default time of the day
        sample_rate : int, optional
            Sample rate of the audio file, by default 44100

        """
        if filename is None:
            filename = datetime.now().strftime('%d_%m_%Y_%H_%M_%S') + '.wav' # type: ignore
        
        
        npaudio = self.convert_numpy(text)
        return self._save_audio(npaudio, filename, sample_rate)


    def __call__(self, text: Union[List[str], str], filename: str = None, sample_rate: int = 44100, voice: str = None, convert_type: str="file") -> Union[str, np.ndarray, List[str]]: # type: ignore
        """ 
        Converts text to audio and saves it to a file or returns a numpy array of the audio file
       
        Parameters:
        ----------
        text : str, list
            Text to convert to audio
        filename : str, optional
            Filename or path to save the audio file, by default time of the day
        sample_rate : int, optional
            Sample rate of the audio file, by default 44100
        voice : str, optional
            voice of the text to speech, either 'male' or 'female', by default 'female'
        convert_type : str, optional
            Type of output, either 'file' or 'numpy', by default 'file'

        Returns
        -------
        str
            Path to the audio file
        np.ndarray
            Numpy array of the audio file
        """
        if voice:
            self.voice = self._get_voice(voice)
        
        if isinstance(text, list):
            return [self(text, filename, sample_rate, voice, convert_type) for text in text] # type: ignore

        if convert_type.lower() == 'file':
            return self.convert(text, filename, sample_rate)
        elif convert_type.lower() == 'numpy':
            return self.convert_numpy(text)
        else:
            raise ValueError("convert should be either 'file' or 'numpy'")


if __name__ == '__main__':
    bangla_tts = BanglaTTS(save_location='test')
    bangla_tts('তোর নাম কি ।', 'test3.wav', voice='female')
