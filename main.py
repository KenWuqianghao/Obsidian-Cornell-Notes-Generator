from flask import Flask, render_template, request, jsonify
from gpt_notes import generate_notes
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_text', methods=['POST'])
def process_text():
    text = request.form['input_text']
    
    processed_text = generate_notes(text)
    
    print(processed_text)
    
    return jsonify({'output_text': processed_text})

if __name__ == '__main__':
    app.run(debug=True)
