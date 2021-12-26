# Pizza_Order_Assistant

<img src="https://images.pexels.com/photos/1653877/pexels-photo-1653877.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940">

## Introduction
An automated program that helps customers of Pizza Palour place their pizza orders. The program uses voice commands. In the background, the program uses IBM Watson's Deep Learning API.

## Installations
To use the program, the user needs to [register](https://cloud.ibm.com/registration?target=%2Fdeveloper%2Fwatson%2Fdashboard) on IBM Watson cloud services; and thereafter install ***ibm_watson*** which is a Python Library for accessing the API. You can read more about IBM watson services [here](https://cloud.ibm.com/docs). To use this program, activate TextToSpeechV1 and SpeechToTextV1. Both services require IAM API keys which you need to generate when you register for the services. Kindly follow the instructions on the IBM website on how to generate the API keys.
You will also need to install speech_recognition library. it's a library for performing speech recognition, with support for several engines and APIs, online and offline. To install speech_recognition, run the following command on your commmand line: ***pip install SpeechRecognition***
Pydub is required for processing the audio files. Install pydub by running the following command: ***pip install pydub***

## Description
The function ***place_order*** handles the sequence flow for the program, from welcoming the customer to making a summary of the pizza order. It welcomes the user by first sythetizing a welcome text into English speech which is played for the customer. The customer then chooses the size of the pizza by answering either Large or Small to a voice prompt. The customer's response is converted to text and saved. The customer is further asked to answer yes or no questions about other finishings for the pizza. At the end, a summary of the order is played for the customer. 

The function ***text_to_speech*** uses the TextToSpeechV1 to synthesize a given text to speech. The function requires the text to synthesize, the voice to use and a file_name to save the synthesized speech as. The format is .wav file. After synthesizing, the saved audio file is played using the playdub module.
The function ***speech_to_text*** uses SpeechToTextV1 to transcribe an audio file to text. The function requires an audio file, and the language to transcribe the text in. The transcription is returned by the function.

