from flask import Flask, request,jsonify
from model import TextGenerator
from flask_cors import CORS
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

try:
    gen = TextGenerator('../model/result')
    if(gen):
        print(gen)
        print('Loaded the model successfully')
except KeyError as e:
    print(f'Error from loading the model : {e}')

app = Flask(__name__)
CORS(app, origins=["*"])


    

@app.route('/question', methods=['POST'])
def ask_question():
    try:
        data = request.json
        instruction = data.get('instruction')
        prompt_input = data.get('promptInput')

        sample = {
                    'instruction': instruction,
                    'input': prompt_input
                }

        # Generate text based on the instruction and input text
        generated_text = gen.generate_text(sample)
        response = generated_text
        
        print(f'asnwer : {response}')

       
        # Return the answer along with serialized source documents
        return jsonify({
            'answer': response
            })
    except KeyError as e:
        return jsonify({'error': f"KeyError: {str(e)}"}), 404
    except Exception as e:
        return jsonify({'error': f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)