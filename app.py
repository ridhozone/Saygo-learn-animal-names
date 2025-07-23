import json
import streamlit as st
from static.style import style_code
from recognizer import speech_recognizer


st.set_page_config(
    page_title="Saygo - Learn Animal Names", page_icon=":material/cadence:"
)
st.html(style_code)

st.title("Saygo :material/cadence:")
st.subheader("Speak the Animal &mdash; Learn with Fun!")


with open("data/animals.json", "r") as f:
    animals = json.load(f)


if "current_index" not in st.session_state:
    st.session_state.current_index = 0

if "score" not in st.session_state:
    st.session_state.score = 0


def get_current_animal():
    return animals[st.session_state.current_index]


tab1, tab2, tab3 = st.tabs(["Saygo", "How-To", "About"])

with tab1:
    animal = get_current_animal()

    st.write("")
    with st.container(border=True, key="animal-image"):
        st.write("Say the name of this animal!")
        st.image(animal["image"], use_container_width=True)

    st.write("")
    _, center, _ = st.columns([1, 2, 1])
    with center:
        with st.container(border=True, key="mic-container"):
            audio_data = st.audio_input(label="click mic and say animal's name")

    if audio_data is not None:
        guess_word = speech_recognizer(audio_data)
        correct_word = animal["word"].strip().lower()

        if correct_word in guess_word:
            st.success(":material/check_circle: Correct! Moving to the next animal.")
            st.session_state.score += 1
            if st.session_state.current_index < len(animals) - 1:
                st.session_state.current_index += 1
                st.rerun()
            else:
                st.balloons()
                st.markdown("### :material/celebration: You've finished all animals!")
        else:
            st.error(":material/cancel: Not quite. Try again!")
            st.markdown(f"Hint: It starts with **{correct_word[0].upper()}...**")

with tab2:
    st.write("")
    with st.container(border=True, key="howto"):
        st.markdown(
            """
            ### How to Use Saygo

            1. **Look at the animal picture** shown on the screen.  
            2. Tap the microphone button and **say the name of the animal out loud**.  
            3. The app will **listen to your voice** using an AI speech model (Whisper).  
            4. If your answer is **correct**, you'll move on to the next animal.  
            5. If the answer is not correct, **try again** until you get it right.  
            6. Keep going and learn all the animal names!

            ---
            > :material/info: Make sure your microphone is enabled and working.
            ---
            """
        )

with tab3:
    st.write("")
    with st.container(border=True, key="about"):
        st.markdown(
            """
            ### About Saygo

            **Saygo** is a fun and interactive learning app designed to help children **practice speaking and recognize animals** using their voice.

            **Features:**  
            - Real-time speech recognition using Whisper ASR  
            - Interactive picture guessing game  
            - Immediate feedback with encouragement    
            - Simple UI

            ---
            > Developed as part of an educational AI project to support early speaking skills.
            ---
            """
        )
