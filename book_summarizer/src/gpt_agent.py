import os
from openai import OpenAI
import constants


class GPTAgent:

    def __init__(self, version=constants.DEFAULT_MODEL, api_key_file_path=constants.OPENAI_API_KEY_PATH, debug=False, 
                 system_message=constants.DEFAULT_SYSTEM_MESSAGE, temperature=constants.DEFAULT_TEMPERATURE):
        self.client = self._load_client(api_key_file_path)
        self.model_name = self._set_model(version)
        self.debug = debug
        self.system_message = system_message
        self.temperature = temperature

    def _read_api_key(self, api_key_file_path):
        with open(os.path.expanduser(api_key_file_path), 'r') as file:
            for line in file:
                key, value = line.strip().split('=')
                if key == "OPENAI_API_KEY":
                    return value
        raise ValueError("API key not found in the provided file.")

    def _load_client(self, api_key_file_path):
        return OpenAI(api_key=self._read_api_key(api_key_file_path))

    def _set_model(self, version):
        return constants.MODEL_MAP[version]

    def _handle_response(self, response):
        finish_reason = response.choices[0].finish_reason
        warning_msg = f"Warning: Finish reason is '{finish_reason}', not 'stop'. " if finish_reason != "stop" else ""
        debug_info = f"Choices: {len(response.choices)}, Prompt Tokens: {response.usage.prompt_tokens}, Completion \
            Tokens: {response.usage.completion_tokens}, Total Tokens: {response.usage.total_tokens}." if self.debug else ""

        if warning_msg + debug_info:
            print(warning_msg + debug_info)

        return response.choices[0].message.content

    def simple_query(self, user_input):
        messages = [
            {"role": "system", "content": self.system_message},
            {"role": "user", "content": user_input}
        ]
        response = self.client.chat.completions.create(
            model=self.model_name, 
            messages=messages,
            temperature=self.temperature
        )
        return self._handle_response(response)

    def continuous_query(self, user_inputs):
        messages = [{"role": "system", "content": self.system_message}]
        responses = []

        for user_input in user_inputs:
            messages.append({"role": "user", "content": user_input})
            response = self.client.chat.completions.create(
                model=self.model_name, 
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
            response = self.client.chat.completions.create(
                model=self.model_name, 
                messages=messages,
                temperature=self.temperature
            )

            current_response = self._handle_response(response)
            print(f"Assistant: {current_response}")

            messages.append({"role": "assistant", "content": current_response})

if __name__ == "__main__":
    # Initialization
    agent = GPTAgent(
        version=constants.MODEL_VERSION, 
        system_message=constants.DEFAULT_SYSTEM_MESSAGE, 
        temperature=constants.DEFAULT_TEMPERATURE,
        debug=False
    )

    # Start the interactive query session
    agent.interactive_query()

