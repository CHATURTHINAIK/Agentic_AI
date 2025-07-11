from phi.agent import Agent, RunResponse
from phi.model.groq import Groq

import openai, os
from dotenv import load_dotenv
load_dotenv()
openai.api_key=os.getenv("GROQ_API_KEY")

agent = Agent(
    name="ContentWritingAgent",
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=(
        "You are an expert content writer who creates clear, engaging, and well-structured content. "
        "You can write articles, product descriptions, story ideas, outlines, and creative content for any given topic. "
        "Always tailor your content based on the user's goal, tone, audience, and constraints if specified. "
        "If the user asks for structure or formatting (like bullet points or sections), follow it strictly. "
        "Keep your answers professional unless told to use humor or casual tone."
    ),
    markdown=True
)

# Print the response in the terminal
'''Prompt 1'''
agent.print_response(
    "Write a 500-word article on 'The Impact of Social Media on Teenagers' for a general audience. Use a clear structure with an introduction, 2–3 body paragraphs, and a conclusion."
)

'''Prompt 2'''
agent.print_response(
    "Write a motivational paragraph of 5 sentences for college students who are struggling with time management. Make the tone friendly and slightly humorous."
)

'''Prompt 3'''
agent.print_response(
    "Help me generate content for a product description. The product is a portable blender. Write 3 bullet points for features, 2 use cases, and a catchy slogan."
)

'''Prompt 4'''
agent.print_response(
    "Give me 5 creative blog post ideas about personal finance for students. Keep the titles catchy and under 10 words."
)

'''Prompt 5'''
agent.print_response(
    "Plan a short story about an AI that learns to paint. Include a plot summary, main characters, and 3 key turning points."
)

'''Prompt 6'''
agent.print_response(
    "I want to write an informative blog post on 'The Future of AI Agents'. First, give me a 5-point outline. Then, write a paragraph for each point."
)