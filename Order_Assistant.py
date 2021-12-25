# -*- coding: utf-8 -*-
"""
Created on Fri May 21 19:37:14 2021.

Pizza parlor. Verbal communication with a pizza customer

@author: Tindi.Sommers 
"""
from ibm_watson import SpeechToTextV1
from ibm_watson import TextToSpeechV1
import speech_recognition as sr
import pydub  # used to load a WAV file
import pydub.playback  # used to play a WAV file

# initialize the recognizer
r = sr.Recognizer()

def place_order():
    """Verbally assist a customer to make a pizza order"""
    welcome = 'You are welcome to Pizza Parlor. My name is Jane and I am here to help you with your pizza order!'
    
    # Synthesize the English text into English speech
    text_to_speech(text_to_speak=welcome,
        voice_to_use='en-US_AllisonVoice',
        file_name='welcome.wav')
    
    pizza_size_q = 'What size of pizza do you want? Answer Large or Small.'
    
    # Synthesize the English text into English speech
    text_to_speech(text_to_speak=pizza_size_q,
        voice_to_use='en-US_AllisonVoice',
        file_name='pizza_size_q.wav')
    
    # record the customer's response
    pizza_size_ans = record_audio()
    
    # transcribe the user's response to text
    pizza_size = speech_to_text(wav_file=pizza_size_ans, model_id='en-US_BroadbandModel')
    
    # ask the customer if they would like pepperoni
    pepperoni_q = 'Would you like pepperoni? Answer Yes or No.'
    
    # synthesize the english text into english speech
    text_to_speech(text_to_speak=pepperoni_q,
                   voice_to_use='en-US_AllisonVoice',
                   file_name='pepperoni_q.wav')
    
    # get the customer's response
    pepperoni_ans = record_audio()
    
    # transcribe the user's response to text
    pepperoni = speech_to_text(wav_file=pepperoni_ans, model_id='en-US_BroadbandModel')
    
    # ask the customer if he/she wants a mushroom
    mushroom_q = 'Would you like some mushroom with your pizza? Answer Yes or No'
    
    # synthesize the english text into english speech
    text_to_speech(text_to_speak=mushroom_q,
                   voice_to_use='en-US_AllisonVoice',
                   file_name='mushroom_q.wav')
    
    # get the customer's response
    mushroom_ans = record_audio()

    # transcribe the user's response to text
    mushroom = speech_to_text(wav_file=mushroom_ans, model_id='en-US_BroadbandModel')
    
    # A summary of the pizza order
    summary = f'This is a summary of your pizza order. You want your pizza with; Size: {pizza_size} Pepperoni: {pepperoni} Mushroom: {mushroom} Thank you for choosing Pizza Parlor.'
    
    # synthesize the english text into english speech
    text_to_speech(text_to_speak=summary,
                   voice_to_use='en-US_AllisonVoice',
                   file_name='summary.wav')
         
    
    
def speech_to_text(wav_file, model_id):
    """Use the Watson Speech to Text Services to convert an audio file to text"""
    
    # create an object of the speech to text
    stt = SpeechToTextV1()
    
    # pass the wav audio file to recognizer
    result = stt.recognize(audio=wav_file, content_type='audio/wav',
                               model=model_id).get_result()
    
    # Get the 'results' list. This may contain intermediate and final
    # results, depending on method recognize's arguments. We asked 
    # for only final results, so this list contains one element.
    results_list = result['results'] 

    # Get the final speech recognition result--the list's only element.
    speech_recognition_result  = results_list[0]

    # Get the 'alternatives' list. This may contain multiple alternative
    # transcriptions, depending on method recognize's arguments. We did
    # not ask for alternatives, so this list contains one element.
    alternatives_list = speech_recognition_result['alternatives']

    # Get the only alternative transcription from alternatives_list.
    first_alternative = alternatives_list[0]

    # Get the 'transcript' key's value, which contains the audio's 
    # text transcription.
    transcript = first_alternative['transcript']

    return transcript  # return the audio's text transcription

# record the audio from the customer
def record_audio():
    """Record audio input using the microphone"""
    # try to use the microphone
    try:
        with sr.Microphone() as source:
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level 
            r.adjust_for_ambient_noise(source, duration=0.5)
            
            # listen to the user input
            audio = r.listen(source, timeout=2)
            
            # get the wav data from the recorded audio
            wav_file = audio.get_wav_data()
            
            return wav_file # return the recorded audio
    except:
        print('An error occured. Could not record the audio.')


def text_to_speech(text_to_speak, voice_to_use, file_name):
    """Use Watson Text to Speech to convert text to specified voice
       and save to a WAV file."""
    # create Text to Speech client
    tts = TextToSpeechV1()

    # open file and write the synthesized audio content into the file
    with open(file_name, 'wb') as audio_file:
        audio_file.write(tts.synthesize(text_to_speak, 
            accept='audio/wav', voice=voice_to_use).get_result().content)
    
    # play the audio file generated
    play_audio(file_name=file_name)

def play_audio(file_name):
    """Use the pydub module (pip install pydub) to play a WAV file."""
    sound = pydub.AudioSegment.from_wav(file_name)
    pydub.playback.play(sound)

if __name__ == '__main__':
    place_order()  
