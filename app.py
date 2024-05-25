from flask import Flask, request, jsonify, render_template
from model import text_generation

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_text', methods=['GET'])
def generate_text():
    input_text = request.args.get('input_text')
    print(input_text)
    # Call your text generation model with the input_text
    generated_text = text_generation(input_text)
    print(generated_text)  # Corrected from print(generate_text)
    return jsonify({'generated_text': generated_text})

@app.route('/audio_text', methods=['GET'])
def audio_text():

    import sounddevice as sd
    import numpy as np
    from scipy.io.wavfile import write
    import librosa
    import torch
    from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC

    # Function to record audio
    def record_audio(duration, sample_rate):
        print("Recording...")
        audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float32')
        sd.wait()  # Wait until the recording is finished
        print("Recording finished")
        return audio.flatten()

    # Set the duration and sample rate
    duration = 8  # seconds
    sample_rate = 16000  # Hz


    # Record the audio
    audio_data = record_audio(duration, sample_rate)
        
    # Save the audio to a file (optional, but useful for reloading)
    write('recorded_audio.wav', sample_rate, audio_data)
    
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

    # Call your text generation model with the input_text
    generated_text = text_generation(transcription[0])
    print(generated_text)  # Corrected from print(generate_text)
    return jsonify({'generated_text': generated_text})

if __name__ == '__main__':
    app.run(debug=True)
