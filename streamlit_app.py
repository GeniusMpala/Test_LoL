import streamlit as st
import base64
from pathlib import Path

st.set_page_config(
    page_title="💕 Valentine's Day 💕",
    page_icon="💕",
    layout="centered"
)

# Function to load and encode image as base64
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return None

# Try to load the teddy image
teddy_base64 = get_base64_image("image.png")


# Create the image tag - use base64 if available, otherwise use a sad emoji
if teddy_base64:
    teddy_img = f'<img src="data:image/png;base64,{teddy_base64}" alt="Teddy Bear" style="width: 250px; border-radius: 15px; box-shadow: 0 5px 20px rgba(0,0,0,0.2);">'
else:
    teddy_img = '<div style="font-size: 120px;">😿</div>'

# The complete HTML app
html_content = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            min-height: 100vh;
            background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 50%, #fecfef 100%);
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            overflow: hidden;
        }}

        .container {{
            text-align: center;
            padding: 40px;
            background: rgba(255, 255, 255, 0.9);
            border-radius: 20px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
            max-width: 500px;
            position: relative;
        }}

        h1 {{
            color: #e74c3c;
            font-size: 2.5rem;
            margin-bottom: 20px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
        }}

        .question {{
            font-size: 1.8rem;
            color: #c0392b;
            margin-bottom: 30px;
            font-weight: bold;
        }}

        .cute-image {{
            font-size: 80px;
            margin-bottom: 20px;
        }}

        .buttons {{
            display: flex;
            justify-content: center;
            gap: 20px;
            flex-wrap: wrap;
        }}

        .btn {{
            padding: 15px 40px;
            font-size: 1.2rem;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            transition: all 0.3s ease;
            font-weight: bold;
        }}

        .btn-yes {{
            background: linear-gradient(45deg, #e74c3c, #c0392b);
            color: white;
            position: relative;
        }}

        .btn-yes:hover {{
            transform: scale(1.1);
            box-shadow: 0 5px 20px rgba(231, 76, 60, 0.5);
        }}

        .btn-no {{
            background: linear-gradient(45deg, #95a5a6, #7f8c8d);
            color: white;
        }}

        .btn-no:hover {{
            background: linear-gradient(45deg, #7f8c8d, #6c7a7b);
        }}

        .success-screen, .sad-screen {{
            display: none;
        }}

        .success-screen h1 {{
            color: #27ae60;
            font-size: 2rem;
        }}

        .success-message {{
            font-size: 1.5rem;
            color: #e74c3c;
            margin-top: 20px;
        }}

        .sad-message {{
            font-size: 1.5rem;
            color: #7f8c8d;
            margin-top: 20px;
        }}

        .sad-cat {{
            font-size: 120px;
            margin: 20px 0;
        }}

        .hidden {{
            display: none !important;
        }}
    </style>
</head>
<body>
    <div class="container">
        <!-- Main Question Screen -->
        <div id="question-screen">
            <p class="question">Will you be my Valentine?🌹</p>
            <div class="buttons">
                <button class="btn btn-yes" id="yesBtn" onclick="sayYes()">Yes! 💕</button>
                <button class="btn btn-no" id="noBtn" onmouseenter="dodgeButton()" onclick="handleNoClick()">No 💔</button>
            </div>
        </div>

        <!-- Sad Screen -->
        <div id="sad-screen" class="sad-screen">
            {teddy_img}
            <p class="sad-message">Stop messing with me Lynfruit 😢</p>
            <button class="btn btn-yes" onclick="sayYes()" style="margin-top: 20px;">Okay, okay... Yes! 💕</button>
        </div>
    </div>

    <script>
        let dodgeCount = 0;
        const maxDodges = 2;

        // Dodge the button
        function dodgeButton() {{
            if (dodgeCount >= maxDodges) return;
            
            const noBtn = document.getElementById('noBtn');
            
            // Calculate random position on the screen
            const maxX = window.innerWidth - 150;
            const maxY = window.innerHeight - 80;
            
            const randomX = Math.random() * maxX;
            const randomY = Math.random() * maxY;
            
            noBtn.style.position = 'fixed';
            noBtn.style.left = randomX + 'px';
            noBtn.style.top = randomY + 'px';
            noBtn.style.transition = 'all 0.2s ease';
            noBtn.style.zIndex = '1000';
            
            dodgeCount++;
        }}

        // Handle No button click
        function handleNoClick() {{
            dodgeCount++;
            
            if (dodgeCount >= 3) {{
                showSadCat();
            }}
        }}

        // Show success screen
        function sayYes() {{
            window.open('https://www.instagram.com/reel/DUN9sdvjN89/?igsh=M284Y2xjbmhhYWNi', '_blank');
        }}

        // Show sad cat screen
        function showSadCat() {{
            document.getElementById('question-screen').classList.add('hidden');
            document.getElementById('sad-screen').style.display = 'block';
        }}
    </script>
</body>
</html>
'''

# Hide Streamlit's default elements for a cleaner look
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {
            padding: 0 !important;
            max-width: 100% !important;
        }
        .stApp {
            background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 50%, #fecfef 100%);
        }
        iframe {
            border: none !important;
        }
    </style>
""", unsafe_allow_html=True)

# Render the HTML
st.components.v1.html(html_content, height=700, scrolling=False)
