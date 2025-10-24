# -*- coding: utf-8 -*-
import base64
import requests
import os
from mistralai import Mistral
from dotenv import load_dotenv
from PIL import Image
import io

load_dotenv()

def encode_image(image_data):
    """Encode une image en base64, accepte soit un chemin soit des bytes"""
    if isinstance(image_data, str):
        # C'est un chemin de fichier
        with open(image_data, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    else:
        # C'est des bytes (depuis Streamlit)
        return base64.b64encode(image_data).decode('utf-8')

def read_text_file(text_file_path):
    with open(text_file_path, "r", encoding='utf-8') as text_file:
        return text_file.read()

def haircut_advice(image_data, context_path="./context.txt", prompt_path="./prompt.txt"):
    """
    Génère des conseils de coupe de cheveux
    image_data: peut être un chemin de fichier ou des bytes
    """
    client = Mistral(api_key=os.environ["MISTRAL_API_KEY"])

    base64_image = encode_image(image_data)

    messages = [
        {
            "role": "system",
            "content": read_text_file(text_file_path=context_path)
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": read_text_file(text_file_path=prompt_path)
                },
                {
                    "type": "image_url",
                    "image_url": f"data:image/jpeg;base64,{base64_image}"
                }
            ]
        }
    ]

    chat_response = client.chat.complete(
        model="pixtral-12b-latest",
        messages=messages
    )
    return chat_response.choices[0].message.content

# Code de test (optionnel)
if __name__ == "__main__":
    image_path = "./image.png"
    advice = haircut_advice(image_path)
    print(advice)