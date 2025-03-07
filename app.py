import tkinter as tk
import customtkinter as ctk
from PIL import Image
import os
import requests

# Hugging Face API credentials
API_KEY = "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"  # Replace with your actual API key
MODEL_URL = "https://api-inference.huggingface.co/models/prompthero/openjourney"

def generate_image_from_prompt(prompt):
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    data = {"inputs": prompt}
    
    response = requests.post(MODEL_URL, headers=headers, json=data)
    if response.status_code != 200:
        print("Error: Failed to generate image")
        return None
    
    image_path = "generated_image.png"
    with open(image_path, "wb") as f:
        f.write(response.content)
    
    return image_path

# Create the main app
app = tk.Tk()
app.geometry("532x632")
app.title("Stable Bud")
ctk.set_appearance_mode("dark")

# Input field for the prompt
prompt_entry = ctk.CTkEntry(app, height=40, width=512, font=("Arial", 20), text_color="black", fg_color="white")
prompt_entry.place(x=10, y=10)

# Label to display the image
lmain = ctk.CTkLabel(app, height=512, width=512)
lmain.place(x=10, y=110)

def generate():
    prompt = prompt_entry.get()
    if not prompt:
        return
    
    image_path = generate_image_from_prompt(prompt)
    if image_path and os.path.exists(image_path):
        display_image(image_path)
    else:
        print("Error: Image not found or not generated.")

def display_image(image_path):
    img = Image.open(image_path)
    img = img.resize((512, 512))
    img_tk = ctk.CTkImage(light_image=img, size=(512, 512))
    lmain.configure(image=img_tk)
    lmain.image = img_tk  # Keep a reference to prevent garbage collection
    lmain.update()  # Force UI update

# Generate button
trigger = ctk.CTkButton(app, height=40, width=120, font=("Arial", 20), text_color="white", fg_color="blue", command=generate, text="Generate")
trigger.place(x=206, y=60)

# Run the app
app.mainloop()