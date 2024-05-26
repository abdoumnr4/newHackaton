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

if __name__ == '__main__':
    app.run(debug=True)
