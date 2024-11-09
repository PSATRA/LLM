# ------------------------------------------api info-----------------------------------------
import os
from openai import OpenAI

os.environ["OPENAI_API_KEY"] = "sk-dGm0cNd8ApWOFxyhA3A96c76572e478f9c9b133f634eEe34"
os.environ["OPENAI_BASE_URL"] = "https://api.xiaoai.plus/v1"
client = OpenAI()
# ------------------------------------------api info-----------------------------------------

# After an image has been processed by the model, it is deleted from OpenAI servers and not retained.

response = client.chat.completions.create(
    model="gpt-4o-mini",
    temperature=0.1,
    # top_p=0.5,
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Describe the image."},
                {"type": "image_url", "image_url":
                    {"url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the"
                            "-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
                     "detail": "low"}, },
            ],
        }
    ],
    max_tokens=10,
)

print(response.choices[0])
# print(response.choices[0].message.content)
# print(response.id)
# print(response.model)
