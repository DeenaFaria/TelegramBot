import openai

# Set your API key
openai.api_key = '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'

# Make an API call
response = openai.Completion.create(
    engine="davinci",  # Choose the GPT-3 model/engine
    prompt="Rapunzel, say something!",  # Provide a prompt
    max_tokens=50,  # Adjust the length of the response
)

# Print the response
print(response)
