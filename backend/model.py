import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline


class TextGenerator:
    def __init__(self, model_path, max_new_tokens=100, temperature=1.0):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.save_path = model_path
        self.model = AutoModelForCausalLM.from_pretrained(self.save_path, device_map='auto')
        self.tokenizer = AutoTokenizer.from_pretrained(self.save_path)
        self.text_generator = pipeline("text-generation", model=self.model, tokenizer=self.tokenizer,
                                       device_map='auto', pad_token_id=self.tokenizer.eos_token_id,
                                       max_new_tokens=max_new_tokens, temperature=temperature)

    def generate_text(self, sample):
        try:
            instruction = sample.get('instruction', '')
            input_text = sample.get('input', '')

            prompt = self._construct_prompt(instruction, input_text)

            output = self.text_generator(prompt)
            generated_text = output[0]['generated_text'].split("### Response:\n")[-1].strip()
            
        except KeyError as e:
            return f'Error from generate_text : {e}'

        return generated_text

    def _construct_prompt(self,instruction, prompt_input=None):
	
        if prompt_input:
            return f"""
    Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

    ### Instruction:
    {instruction}

    ### Input:
    {prompt_input}

    ### Response:
    """.strip()
                
        else:
            return f"""
    Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

    ### Instruction:
    {instruction}

    ### Response:
    """.strip()