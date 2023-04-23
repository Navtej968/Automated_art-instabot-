from get_prompt import get_prompt ,style_list
from instagrapi import Client
from PIL import Image
import requests
import random
import base64
import time
import io
import os

bot = Client()
def login():
  bot.login('Username','password',relogin=True)

def getimage():
  engine_id = "stable-diffusion-v1-5"
  response = requests.post(f"https://api.stability.ai/v1/generation/{engine_id}/text-to-image",
  headers={
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": "API KEY Goes here "
  },
    json={
        "text_prompts": [
            {
                "text": get_prompt()
            }
        ],
        "cfg_scale": 7,
        "clip_guidance_preset": "FAST_BLUE",
        "height": 512,
        "width": 512,
        "style_preser": style_list[random.randrange(0,17)],
        "samples": 1,
        "steps": 30,})
  data=response.json()
  byte = (data['artifacts'][0]['base64'])
  decoded= base64.b64decode(byte)
  img = Image.open(io.BytesIO(decoded))
  img.save('pic.jpg')

def upload_img():
  bot.photo_upload(r'pic.jpg','You are cool. :)')
  os.remove(r'pic.jpg')

def main():
  login()
  while(True):
    getimage()
    upload_img()
    print(get_prompt())
    time.sleep(21600)
main()
