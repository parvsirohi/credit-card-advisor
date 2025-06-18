import streamlit as st
from langchain_community.llms import Ollama
from utils import extract_info
from recommender import recommend_cards

# Page config
st.set_page_config(page_title="AI Credit Card Advisor 💳", page_icon="💳")
st.title("💳 AI Credit Card Advisor")
st.write("Answer a few questions to get personalized credit card recommendations.")

llm = Ollama(model="mistral")

# Questions
questions = [
    "What is your approximate monthly income?",
    "How much do you typically spend on fuel, travel, groceries, and dining?",
    "Do you prefer cashback, travel points, or reward points?",
    "Any perks you want? (e.g., lounge, fuel, movie, grocery)",
    "Do you already use any credit cards?",
    "What’s your credit score? (or say 'unknown')"
]

# Session state init
if "step" not in st.session_state:
    st.session_state.step = 0
if "inputs" not in st.session_state:
    st.session_state.inputs = {
        "income": None,
        "rewards": None,
        "perks": [],
        "spend": {},
        "credit_score": None
    }
if "user_response" not in st.session_state:
    st.session_state.user_response = ""
if "recommendations" not in st.session_state:
    st.session_state.recommendations = []

# Display question
if st.session_state.step < len(questions):
    with st.chat_message("assistant"):
        st.write(questions[st.session_state.step])

# Chat input
user_input = st.chat_input("Type your answer here...")

# Process user input
if user_input:
    with st.chat_message("user"):
        st.write(user_input)

    parsed = extract_info(user_input)
    for key in st.session_state.inputs:
        if parsed[key]:
            st.session_state.inputs[key] = parsed[key]

    st.session_state.step += 1
    st.rerun()

# Show recommendations
if st.session_state.step >= len(questions):
    inputs = st.session_state.inputs
    st.subheader("📊 Recommended Credit Cards")

    cards = recommend_cards(
        user_income=inputs["income"],
        preferred_reward_type=inputs["rewards"],
        desired_perks=inputs["perks"],
        spending_habits=inputs["spend"]
    )

    if cards:
        st.session_state.recommendations = cards
        for card, reward, reason in cards:
            st.markdown(f"### 💳 {card[0]} — *{card[1]}*")
            try:
                st.image(card[9], width=220)
            except:
                st.image("https://via.placeholder.com/220x140.png?text=No+Image", width=220)
            st.write(f"**Joining Fee:** ₹{card[2]} | **Annual Fee:** ₹{card[3]}")
            st.write(f"**Reward Type:** {card[4]} ({card[5]})")
            st.write(f"**Perks:** {card[7]}")
            st.info(f"💡 {reason}")
            st.success(f"💰 You could earn ~₹{reward:,}/year")
            st.markdown("---")
    else:
        st.warning("No matching cards found.")

    # Side-by-side comparison
    if st.session_state.recommendations:
        st.subheader("🔍 Compare Top Cards Side-by-Side")
        cols = st.columns(len(st.session_state.recommendations))
        for i, col in enumerate(cols):
            card, reward, reason = st.session_state.recommendations[i]
            with col:
                st.markdown(f"**{card[0]}**")
                try:
                    col.image(card[9], width=160)
                except:
                    col.image("https://via.placeholder.com/160x100.png?text=No+Image", width=160)
                col.caption(f"{card[1]}")
                col.write(f"💰 {card[4]} ({card[5]})")
                col.write(f"Fee: ₹{card[2]}/₹{card[3]}")
                col.write(f"Perks: {card[7]}")
                col.caption(f"💡 {reason}")
                col.success(f"₹{reward:,}/yr")
                col.markdown(f"[Apply]({card[8]})")

# Restart
st.markdown("___")
if st.button("🔄 Restart Advisor"):
    st.session_state.step = 0
    st.session_state.inputs = {
        "income": None,
        "rewards": None,
        "perks": [],
        "spend": {},
        "credit_score": None
    }
    st.session_state.user_response = ""
    st.session_state.recommendations = []
    st.rerun()
