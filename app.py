from flask import Flask, request, render_template
from dotenv import load_dotenv
import os
import google.generativeai as genai

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])

    generation_config = {
        "temperature": 1.75,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash-exp",
        generation_config=generation_config,
    )

    theme = request.form.get('theme')
    name = request.form.get('name')
    age = request.form.get('age')
    gender = request.form.get('gender')
    height = request.form.get('height')
    weight = request.form.get('weight')
    build = request.form.get('build')
    hair = request.form.get('hair')
    eye = request.form.get('eye')
    clothing = request.form.get('clothing')
    accessories = request.form.get('accessories')
    personality = request.form.get('personality')
    skills = request.form.get('skills')
    character_background = request.form.get('character_background')

    prompt = ["Write a character design in a pirate-themed game set in the Joseon era.",
  "input: Main Character (Female)",
  "output: **Name:** Haenyeo\n\n**Appearance:**\n\n* **Age:** Mid-twenties\n* **Height:** 5'7\"\n* **Weight:** 130 lbs\n* **Build:** Athletic and agile\n* **Hair:** Long, black hair worn in a practical braid\n* **Eyes:** Piercing hazel eyes that reflect the sea's depths\n* **Clothing:**\n    * Loose, dark-colored pants tucked into sturdy leather boots\n    * A lightweight cotton shirt with a low neckline, trimmed with intricate embroidery\n    * A leather vest with multiple pockets for tools and supplies\n* **Accessories:**\n    * A broad-brimmed hat to shield her face from the sun\n    * A pair of silver earrings in the shape of anchors\n    * A leather belt with a small pouch for valuables\n\n**Personality:**\n\n* **Determined:** Haenyeo is a fearless and tenacious pirate, driven by a strong sense of justice and a desire for adventure.\n* **Resourceful:** Her time spent as a haenyeo (Korean female diver) has honed her survival instincts and adaptability.\n* **Empathetic:** Despite her pirate lifestyle, Haenyeo has a compassionate heart and a soft spot for those in need.\n* **Intelligent:** She is quick-witted and observant, able to assess situations and make decisions swiftly.\n* **Independent:** Haenyeo values her freedom and relies on her own abilities rather than seeking help from others.\n\n**Skills:**\n\n* **Diving:** Haenyeo is an expert diver, capable of holding her breath for extended periods and navigating underwater with ease.\n* **Swimming:** Her exceptional swimming abilities allow her to navigate the treacherous ocean currents and avoid danger.\n* **Spearfishing:** She is a skilled spearfisher, using her knowledge of marine life to locate and catch prey underwater.\n* **Seamanship:** As a pirate, Haenyeo is familiar with the basics of sailing and ship navigation.\n* **Hand-to-Hand Combat:** While not an expert fighter, she is proficient in basic self-defense techniques, using her agility and knowledge of pressure points to subdue opponents.\n\n**Background:**\n\nHaenyeo was raised on a coastal village and learned the ways of the haenyeo from a young age. However, when her village was attacked by bandits, she witnessed firsthand the brutality of war and decided to fight back.\n\nJoining a pirate crew, Haenyeo has proven herself as a valuable member, using her diving skills to scout for enemy ships and gather underwater resources. Her determination and compassion have also earned her the respect of her crewmates.",
  "input: Main Character (Male)",
  "output: ",]

    # prompt = [
    #     f"""Write a character design with this theme: {theme}.{(f"Consider this Image as background: ", file) if file.filename else ""}
    #     input: Main Character ({gender})""",
    #     f"""output: **Name:** {name}\n\n**Appearance:**\n\n* **Age:** {age}\n{f'* **Height:** {height}' if height else ''}\n{f'* **Weight:** {weight}' if weight else ''}\n* **Build:** {build}\n* **Hair:** {hair}\n* **Eyes:** {eye}\n* **Clothing:**\n{'\n'.join([f'* {text}' for text in clothing.split('.')])}\n* **Accessories:**\n{'\n'.join([f'* {text}' for text in accessories.split('.')])}\n\n**Personality:**\n\n{'\n'.join([f'* {text}' for text in personality.split('.')])}\n\n**Skills:**\n\n{'\n'.join([f'* {text}' for text in skills.split(',')])}\n\n**Background:**\n\n{character_background}""",
    # f"input: Villain ({gender})",
    # "output: ",
    # ]
    response = model.generate_content(prompt, stream=True)

    
    return render_template('result.html', recipe=response)

if __name__ == '__main__':
    app.run(debug=True)
