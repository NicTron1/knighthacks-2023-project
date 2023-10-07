import openai

# Set your OpenAI API key here
openai.api_key = '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'

def generate_response(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # You can change the engine if needed
            prompt=prompt,
            max_tokens=150,  # Adjust the maximum number of tokens in the response
            n=1,  # Number of completions to generate
            stop=None,  # You can specify a stopping condition if necessary
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error: {e}")
        return None

# Example usage
prompt = "Translate the following English text to French: 'Hello, how are you?'"
response = generate_response(prompt)

if response:
    print("Response from GPT-3.5:", response)
else:
    print("Failed to generate a response.")
