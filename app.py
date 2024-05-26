from flask import Flask, request, jsonify, render_template
from model import text_generation
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import librosa
import torch
from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC

app = Flask(_name_)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_text', methods=['GET','POST'])
def generate_text():
    print(request.method)
    if request.method == 'POST':
        print("heeeere")
        # Function to record audio
        print("Recording...")
        audio = sd.rec(int(8 * 16000), samplerate=16000, channels=1, dtype='float32')
        sd.wait()  # Wait until the recording is finished
        print("Recording finished")
        # Record the audio
        audio_data = audio.flatten()  
        # Save the audio to a file (optional, but useful for r  eloading)
        write('recorded_audio.wav', 16000, audio_data)
        # Load the audio data using librosa
        input_audio, sr = librosa.load('recorded_audio.wav', sr=16000)
        # Initialize the processor and model
        processor = Wav2Vec2Processor.from_pretrained('boumehdi/wav2vec2-large-xlsr-moroccan-darija')
        model = Wav2Vec2ForCTC.from_pretrained('boumehdi/wav2vec2-large-xlsr-moroccan-darija')
        # Tokenize the input audio
        input_values = processor(input_audio, return_tensors="pt", padding=True).input_values
        # Retrieve logits
        logits = model(input_values).logits
        # Decode the predicted tokens
        predicted_ids = torch.argmax(logits, axis=-1)
        transcription = processor.batch_decode(predicted_ids)
        print(transcription[0])
        # Call your text generation model with the input_text
        generated_text = text_generation(transcription[0])
        return render_template('index.html',generated_text =generated_text ) 


    input_text = request.args.get('input_text')
    print(input_text)
    # Call your text generation model with the input_text
    generated_text = text_generation(input_text)
    print(generated_text)  # Corrected from print(generate_text)
    return render_template('index.html',generated_text =generated_text ) 


if _name_ == '_main_':
    app.run(debug=True)