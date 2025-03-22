import os
from openai import OpenAI
from dotenv import load_dotenv

# Load OpenAI API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Global conversation history
conversation_history = [
    {
        "role": "system",
        "content": (
            "You are a prompt optimization engine. Your role is to Generate Optimal Prompts using user input. The user is a software or AI agent                  developer with minimal coding skills. User sometime vaguely pastes error messages which means he/she is looking for a fix"
            "Your job is to take their vague or simple request and rewrite it into a professional, technically sound, "
            "implementation-ready prompt designed for ChatGPT to return complete working Python code. "
            "You should NOT generate any responses or code yourself. ONLY return a rewritten prompt."
            "For now the expectation is to generate prompts for Python code only."
            "Structure your prompt in Technical requirement format under many headers like Overall purpose, Where Am i? Ask from you."
        )
    }
]

def generate_optimal_prompt(user_message: str, model="gpt-4o", max_turns=5) -> str:
    conversation_history.append({"role": "user", "content": user_message})

    try:
        response = client.chat.completions.create(
            model=model,
            messages=conversation_history[-(2 * max_turns + 1):],
            temperature=0.3,
            max_tokens=200
        )
        optimized_prompt = response.choices[0].message.content.strip()
        conversation_history.append({"role": "assistant", "content": optimized_prompt})
        return optimized_prompt

    except Exception as e:
        raise RuntimeError(f"Failed to generate optimal prompt: {e}")