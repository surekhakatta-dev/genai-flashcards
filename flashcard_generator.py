import openai
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]

def generate_flashcards(topic):
    prompt = f"Generate 3 flashcards for AWS ML topic: {topic}. Format: question and answer."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    content = response.choices[0].message.content

    # Simple parser (assumes numbered Q&A format)
    cards = []
    for line in content.split("\n"):
        if line.startswith("Q:"):
            question = line[2:].strip()
        elif line.startswith("A:"):
            answer = line[2:].strip()
            cards.append({"question": question, "answer": answer})
    return cards
