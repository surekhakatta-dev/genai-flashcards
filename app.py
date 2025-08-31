import streamlit as st
from flashcard_generator import generate_flashcards
import json

st.title("🧠 GenAI Flashcards for AWS ML")

topic = st.text_input("Enter an AWS ML topic:")
if st.button("Generate Flashcards") and topic:
    cards = generate_flashcards(topic)
    st.success(f"Generated {len(cards)} flashcards for '{topic}'")

    for card in cards:
        st.markdown(f"**Q:** {card['question']}")
        st.markdown(f"**A:** {card['answer']}")
        st.divider()

    # Save to JSON
    with open("flashcards.json", "w") as f:
        json.dump(cards, f, indent=2)
