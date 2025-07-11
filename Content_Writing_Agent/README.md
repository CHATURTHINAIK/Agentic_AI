# 🧠 ContentWritingAgent – A LLM-Based Content Generation Agent

## 📌 Overview

**ContentWritingAgent** is an intelligent content generation agent built using the **Phi framework** and **Groq-hosted LLaMA 3.3-70B** model. It demonstrates the principles of **Agentic AI** by acting as an expert content writer that adapts its output based on the user's intent, tone, format, and constraints.

---

## 🛠 Features

- ✍️ Writes full-length articles based on user prompts  
- 💬 Generates product descriptions, slogans, and bullet points  
- 🎯 Adjusts tone, structure, and format based on instruction  
- 🧩 Offers structured story planning and blog post outlines  
- 🧠 Demonstrates agency in planning, decision-making, and adaptability  

---

## ⚙️ Technologies Used

- [Phi Framework](https://docs.phidata.io/) – for agent orchestration  
- Groq API – to access the LLaMA 3.3 70B Versatile model  
- Python  
- dotenv – for API key management  

---

## 🚀 How It Works

The agent is initialized with:
- A **name** (`ContentWritingAgent`)
- A system **instruction** defining its personality and capabilities
- A **Groq-hosted LLaMA 3.3 70B** model for natural language generation

It then responds to multiple prompts related to content writing, such as article generation, product description, motivational writing, and story planning.

---

## 📂 Project Structure
content-writing-agent/  
│  
├── .env # Contains GROQ_API_KEY  
├── agent_content.py # Main script  
├── README.md # This file

---

## 💡 Sample Prompts

The agent was tested with the following tasks:

1. **Article Writing**  
   _"Write a 500-word article on 'The Impact of Social Media on Teenagers' for a general audience. Use a clear structure with an introduction, 2–3 body paragraphs, and a conclusion."_

2. **Motivational Writing**  
   _"Write a motivational paragraph of 5 sentences for college students who are struggling with time management. Make the tone friendly and slightly humorous."_

3. **Product Description**  
   _"Help me generate content for a product description. The product is a portable blender. Write 3 bullet points for features, 2 use cases, and a catchy slogan."_

4. **Idea Generation**  
   _"Give me 5 creative blog post ideas about personal finance for students. Keep the titles catchy and under 10 words."_

5. **Story Planning**  
   _"Plan a short story about an AI that learns to paint. Include a plot summary, main characters, and 3 key turning points."_

6. **Blog Structuring & Writing**  
   _"I want to write an informative blog post on 'The Future of AI Agents'. First, give me a 5-point outline. Then, write a paragraph for each point."_

---

## 🔐 Environment Setup

1. **Clone the repository**  
   ```bash
   git clone https://github.com/CHATURTHINAIK/Agentic_AI.git
   cd Agentic_AI/Content_Writing_Agent
   
2. **Create a** .env **file**  
   ```bash
   GROQ_API_KEY=your_api_key_here

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

---

## 🧪 Running the Project

```bash
python content_writer.py
