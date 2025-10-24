# -*- coding: utf-8 -*-
import base64
import requests
import os
from mistralai import Mistral
from dotenv import load_dotenv

load_dotenv()

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def read_text_file(text_file_path):
    with open(text_file_path, "r") as text_file:
        return text_file.read()


def haircut_advice(image_path):
    client = Mistral(api_key=os.environ["MISTRAL_API_KEY"])

    base64_image = encode_image(image_path)

    messages = [
        {
            "role": "system",
            "content":read_text_file(text_file_path="./context.txt")
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": read_text_file(text_file_path="./prompt.txt")
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


image_path = "./image.png"
advice = haircut_advice(image_path)
print(advice)