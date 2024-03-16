import streamlit as st
import base64
import anthropic
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API key
api_key = os.getenv("ANTHROPIC_API_KEY")

# Initialize the Anthropic client
client = anthropic.Anthropic(api_key=api_key)

# Set page config with the sidebar initially expanded
st.set_page_config(
    page_title='Play It: A Musical Discovery App',
    initial_sidebar_state='expanded'
)


# Streamlit UI
st.title('🎵 Play It: Discover Musical Instruments')

with st.expander("About 'Play It' - A Musical Discovery App", expanded=False):
    st.markdown("""
    **Project Description:**  
    "Play It" is a application that harmonizes the innovative capabilities of Claude 3's AI with an intuitive and user-friendly interface. This unique platform invites users of all ages to dive into the world of musical instruments, enabling them to explore, learn, and engage in rich, educational conversations driven by visual content.

    **Concept:**  
    At the heart of "Play It" lies the integration of the Claude 3 API, designed to analyze images of musical instruments and generate comprehensive text descriptions and educational content. Users are empowered to interact directly with Claude 3 models, exploring the intricate details, history, and sounds of various instruments through an immersive learning experience.

    **Key Features:**  
    - **Interactive Image Analysis:** With Claude 3's cutting-edge AI, "Play It" interprets uploaded images of musical instruments, identifying key features and providing users with detailed information about the instrument's history, usage, and musical genre.  
    - **Musical Conversations:** Beyond mere analysis, users can engage in dynamic conversations with Claude 3. Whether it's inquiring about playing techniques, the cultural significance of an instrument, or requesting a piece of music associated with it, "Play It" offers a responsive and informative dialogue.

    **Use Cases:**  
    - **Educational Enrichment:** "Play It" serves as a valuable resource for educators and students, offering an engaging way to supplement music education. From classroom discussions to individual exploration, it fosters a deeper appreciation and understanding of musical instruments and their role in various cultures.  
    - **Passionate Hobbyists and Musicians:** Whether you're a seasoned musician or a curious hobbyist, "Play It" opens up a world of exploration. Discover new instruments, delve into their stories, and maybe even find inspiration for your next musical journey.
    """, unsafe_allow_html=True)
st.markdown("---")
uploaded_file = st.file_uploader("Upload an image of a musical instrument", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
    st.write("Analyzing the image...")

    # Convert the file to an image in base64 encoding
    image_data = base64.b64encode(uploaded_file.getvalue()).decode('utf-8')

    # Make the API call
    message = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1000,
        temperature=0.3,
        system="From the image provided, identify the musical instrument and craft a playful and easy-to-understand guide on how to play it. Imagine you're a friendly and animated music teacher who loves making learning fun. Use simple language, humor, and lots of enthusiasm to encourage kids to explore and enjoy music. Begin your message with \"Welcome to Play It, your musical adventure buddy! 🎵✨\", and ensure your instructions are kid-friendly, engaging, and inspire a love for music. Remember, you're not just teaching; you're igniting a passion for musical discovery in the hearts of young learners.",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/jpeg",
                            "data": image_data 
                        }
                    },
                    {
                        "type": "text",
                        "text": "Let's discover how to play this instrument together!"
                    }
                ]
            }
        ]
    )

    # Check if the message has content and display it
    if hasattr(message, 'content') and len(message.content) > 0:
        # Assuming 'message.content' is a list of content blocks
        for content_block in message.content:
            if getattr(content_block, 'type', '') == 'text':
                block_text = getattr(content_block, 'text', '')
                if block_text:
                    st.write(block_text)
    else:
        st.write("An error occurred, or no content was returned. Please try again.")


# Footer & Support Section
st.markdown("---")
st.markdown("✔️ **Project MVV**: This application is part of the MVV initiative, developed with **Team Bilsimaging** for their participation in the **LabLab AI 24-Hour Claude Hackathon**.")
st.markdown("If you find value in what I do and wish to support my efforts, please consider making a donation. Your support enables me to continue creating and sharing valuable projects. **Thank you for being part of this journey! - Bilel Aroua**")
st.markdown("For support, feel free to ☕ [Buy me a Coffee](https://ko-fi.com/bilsimaging).")
st.image('https://storage.ko-fi.com/cdn/brandasset/kofi_button_dark.png', width=150)

# Hide Streamlit branding
st.markdown("<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;}</style>", unsafe_allow_html=True)        
