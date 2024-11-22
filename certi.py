from flask import Flask, request, send_file, render_template
from PIL import Image, ImageDraw, ImageFont
import os

app = Flask(__name__)

# Configuration
TEMPLATE_PATH = "certificate_template.png"  # Path to your certificate template
OUTPUT_FOLDER = "certificates/"  # Folder to save generated certificates
FONT_PATH = "arialbd.ttf"  # Path to your font file
FONT_SIZE = 60
TEXT_COLOR = (255, 255, 255)

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_certificate():
    name = request.form['name'].strip().upper()
    if not name:
        return "Name is required", 400

    # Open the certificate template
    img = Image.open(TEMPLATE_PATH)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)

    # Calculate text position
    text_bbox = draw.textbbox((0, 0), name, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    image_width, image_height = img.size
    x = (image_width - text_width) / 2
    y = (image_height - text_height) / 2 + 100  # Adjust Y position based on your design

    # Add name to the certificate
    draw.text((x, y), name, fill=TEXT_COLOR, font=font)

    # Save the certificate
    output_path = os.path.join(OUTPUT_FOLDER, f"{name}_certificate.png")
    img.save(output_path)

    # Return the generated certificate
    return send_file(output_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
