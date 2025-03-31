import os
import anthropic
from anthropic import Anthropic

# Set up API key - ideally from environment variables
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "your-api-key-here")

# Initialize the client
client = Anthropic(api_key=ANTHROPIC_API_KEY)

my_model_name = "claude-3-5-sonnet-20241022"

def get_claude_response(prompt, max_tokens=1000, temperature=0.7):
    """
    Get a response from Claude 3.5 Sonnet
    
    Args:
        prompt: The prompt to send to Claude
        max_tokens: Maximum tokens in the response
        temperature: Controls randomness (0.0-1.0)
    
    Returns:
        The model's response text
    """
    try:
        message = client.messages.create(
            model=my_model_name,
            max_tokens=max_tokens,
            temperature=temperature,
            system="You are a helpful AI assistant.",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return message.content[0].text
    except Exception as e:
        print(f"Error calling Claude API: {e}")
        return None

# Example usage
if __name__ == "__main__":
    prompt = "Explain quantum computing in simple terms."
    response = get_claude_response(prompt)
    print(response)
