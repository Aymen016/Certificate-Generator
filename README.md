# Certificate Generator 🚀🎓

This project is a **Certificate Generator** web application built using **HTML**, **CSS**, and **Python (Flask)**. Users can enter their name, generate a personalized certificate 🖼️, and download it as an image.

---

## Features ✨

- **Responsive Design** 📱: Modern and visually appealing user interface with gradient backgrounds and interactive elements.
- **Dynamic Certificate Generation** 🖊️: Users can input their name, and the app dynamically adds the name to a certificate template.
- **Animated Background** 🎇: Includes animated elements (e.g., floating spaceship or rocket) for a visually engaging experience.
- **Downloadable Certificates** 📥: Users can download their generated certificate as a PNG file.
- **Customizable Template** 🎨: You can replace the default template with your own design!

---

## Technologies Used 🛠️

### Frontend
- **HTML**: For the basic structure of the web app.
- **CSS**: For styling and animations.

### Backend
- **Python (Flask)**: For handling certificate generation and file downloads.
- **Pillow (PIL)**: For dynamically adding text to the certificate template.

---

## File Structure 📂

```
project-folder/
├── static/
│   ├── images/
│   │   ├── rocket.png       # Rocket image for background
│   │   ├── certificate_template.png # Certificate template
├── templates/
│   ├── index.html           # Main HTML file
├── app.py                   # Flask backend
├── requirements.txt         # Python dependencies
```

---

## Setup Instructions 🛠️

### Prerequisites

- Python 3.x installed on your system.
- A code editor (e.g., VS Code).

### Installation 🚀

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/certificate-generator.git
   cd certificate-generator
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Place Certificate Template and Assets**:
   - Ensure the `certificate_template.png` file is in the `static/images/` folder.
   - Add any required images (e.g., rocket) to the same folder.

5. **Run the Application**:
   ```bash
   python app.py
   ```
   - The app will run at `http://127.0.0.1:5000`.

---

## Usage 💡

1. Open the app in your browser by visiting `http://127.0.0.1:5000`.
2. Enter your name in the input field.
3. Click the **"Generate Certificate"** button.
4. The app generates a certificate preview.
5. Download the certificate by clicking the **Download Certificate** button.

---

## Customization 🎨

1. **Change the Certificate Template**:
   - Replace `certificate_template.png` with your custom design.
   - Ensure the template has a blank area where the name will be added.

2. **Update Animations**:
   - Modify the CSS `@keyframes` rules in `index.html` to adjust the floating effect or add new animated elements.

3. **Change Fonts**:
   - Update the `FONT_PATH` variable in `app.py` to point to your preferred font file.

---

## Dependencies 📦

- **Flask**: Web framework for Python.
- **Pillow**: Python Imaging Library for image manipulation.

To install all dependencies:
```bash
pip install -r requirements.txt
```

---

Template Example 🎨

The default certificate template looks like this:

![certificate_template](https://github.com/user-attachments/assets/c2d3f265-e60e-497b-a926-d30c538afbc2)



You can replace this template with your own design by updating the certificate_template.png file in the static/images/ folder. Ensure the new template has a blank area where the name can be dynamically added!

## Example 🎉

Here’s how the app looks in action:

![Screenshot 2024-11-22 214542](https://github.com/user-attachments/assets/fc7eb14d-6791-41b8-b3d7-f973b7cd24a6)


---

## Credits 👏

- **Background Icons**: [Flaticon](https://www.flaticon.com/)
- **Template Design**: Customizable based on user requirements.


---

Enjoy building your certificates! 🎓✨ Feel free to customize and enhance this project as per your needs.

