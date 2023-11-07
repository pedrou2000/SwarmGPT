import os
import openai

class GPTAgent:
    
    MODEL_MAP = {
        3: {
            "small": "gpt-3.5-turbo",
            "big": "gpt-3.5-turbo-16k"
        },
        4: {
            "small": "gpt-4-1106-preview",
            "big": "gpt-4-1106-preview"
        }
    }

    def __init__(self, version=3, size="small", api_key_file_path="~/.openai", debug=False, system_message="You are a helpful assistant.", temperature=1.0):
        self.api_key = self._load_api_key(api_key_file_path)
        openai.api_key = self.api_key
        self.debug = debug
        self.system_message = system_message
        self.temperature = temperature
        self._set_model(version, size)

    def _load_api_key(self, api_key_file_path):
        with open(os.path.expanduser(api_key_file_path), 'r') as file:
            for line in file:
                key, value = line.strip().split('=')
                if key == "OPENAI_API_KEY":
                    return value
        raise ValueError("API key not found in the provided file.")

    def _set_model(self, version, size):
        if not version in self.MODEL_MAP or not size in self.MODEL_MAP[version]:
            print("Invalid model version or size provided. Available options are:")
            for ver, sizes in self.MODEL_MAP.items():
                print(f"Version {ver}: {', '.join(sizes.keys())}")
            raise ValueError("Invalid model configuration.")
        self.model = self.MODEL_MAP[version][size]

    def _handle_response(self, response):
        finish_reason = response.get('choices', [{}])[0].get('finish_reason')
        warning_msg = f"Warning: Finish reason is '{finish_reason}', not 'stop'. " if finish_reason != "stop" else ""
        debug_info = f"Choices: {len(response.get('choices', []))}, Prompt Tokens: {response.get('usage', {}).get('prompt_tokens')}, Completion Tokens: {response.get('usage', {}).get('completion_tokens')}, Total Tokens: {response.get('usage', {}).get('total_tokens')}." if self.debug else ""

        if warning_msg + debug_info:
            print(warning_msg + debug_info)

        responses = [choice["message"]["content"] for choice in response.get('choices', [])]
        return responses[0] if len(responses) == 1 else responses

    def simple_query(self, user_input):
        messages = [
            {"role": "system", "content": self.system_message},
            {"role": "user", "content": user_input}
        ]
        response = openai.ChatCompletion.create(
            model=self.model, 
            messages=messages,
            temperature=self.temperature
        )
        return self._handle_response(response)

    def continuous_query(self, user_inputs):
        messages = [{"role": "system", "content": self.system_message}]
        responses = []

        for user_input in user_inputs:
            messages.append({"role": "user", "content": user_input})
            response = openai.ChatCompletion.create(
                model=self.model, 
                messages=messages,
                temperature=self.temperature
            )
            current_response = self._handle_response(response)
            responses.append(current_response)
            messages.append({"role": "assistant", "content": current_response})

        return responses

    def interactive_query(self):
        messages = [{"role": "system", "content": self.system_message}]
        
        while True:
            # Get input from the user
            user_input = input("You: ")
            if user_input.lower() == 'quit' or user_input.lower() == 'exit' or user_input.lower() == 'q':
                break
            
            messages.append({"role": "user", "content": user_input})
            
            response = openai.ChatCompletion.create(
                model=self.model, 
                messages=messages,
                temperature=self.temperature
            )
            
            current_response = self._handle_response(response)
            print(f"Assistant: {current_response}")
            
            messages.append({"role": "assistant", "content": current_response})

if __name__ == "__main__":
    # Configuration
    model_version = 4
    model_size = "small"
    system_msg = "You are a helpful assistant."
    temperature_setting = 1.0
    debug_mode = False

    # Initialization
    agent = GPTAgent(
        version=model_version, 
        size=model_size, 
        system_message=system_msg, 
        temperature=temperature_setting,
        debug=debug_mode
    )
    
    # Start the interactive query session
    agent.interactive_query()

