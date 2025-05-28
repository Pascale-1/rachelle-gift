import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

# --- Custom CSS for a pretty, bubbly look ---
st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #ffe6fa 0%, #e0f7fa 100%);
        }
        .main {
            background-color: #fff0f7;
            border-radius: 18px;
            padding: 2.5rem 2rem;
            box-shadow: 0 6px 36px rgba(255, 192, 203, 0.15);
        }
        h1 {
            color: #e75480;
            font-family: 'Comic Sans MS', cursive, sans-serif;
        }
        .gratitude {
            font-size: 1.18rem;
            color: #ff69b4;
            background: #fff7fa;
            border-radius: 12px;
            padding: 1.2rem;
            margin: 1.5rem 0;
            box-shadow: 0 2px 12px rgba(255,182,193,0.12);
        }
        .gift-note {
            font-size: 1.15rem;
            color: #00897b;
            background: #e0f7fa;
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 2px 10px rgba(0,137,123,0.10);
        }
    </style>
""", unsafe_allow_html=True)

# --- Main content ---
st.markdown('<div class="main">', unsafe_allow_html=True)

st.title("🎁 Hey heeeeeey Rachelle, it's your surprise gift Page Reveal!")

st.markdown("""
<div class="gratitude">
    <span class="balloon-emoji">🎈</span>
    Welcome back to Alma, Rachelle! <br>
    We wanted to find a special way to celebrate your return. <br>
    (Sorry this is a little late—totally on me!)
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="gratitude">
    Thank you for always being a ray of sunshine with your bubbly hellos 🌞,<br>
    and for filling Alma with your heartwarming spirit and contagious energy.<br>
    You truly make every day brighter for everyone around you! 💖<br>
    <b>We’re so grateful for you!</b>
</div>
""", unsafe_allow_html=True)

st.write("Ready for a little surprise? Click the button below to reveal your special gift!")

# --- Reveal button and surprise ---
if st.button("🎉 Reveal My Gift! 🎉"):
    st.balloons()
    st.success("Congratulations, Rachelle! Here is your special gift card:")

    st.markdown("""
    <div class="gift-note">
        🧘‍♀️ <b>This gift card is all about <span style="color:#e75480;">relaxation</span> and <span style="color:#e75480;">treating yourself</span>!</b> <br>
        Take a well-deserved break, enjoy, and let yourself profit from every moment of joy and peace it brings. <br>
        <i>You absolutely deserve it!</i> 🌸✨
    </div>
    """, unsafe_allow_html=True)

    # Display the PDF gift card
    with open("tix.pdf", "rb") as f:
        pdf_bytes = f.read()
        pdf_viewer(input=pdf_bytes, width=700)

    st.info("Enjoy your gift! You deserve all the joy and more! 🥳💝")
else:
    st.markdown('<span style="color:#e75480;font-size:1.1rem;">Your gift is waiting for you, Rachelle... 🎀</span>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
