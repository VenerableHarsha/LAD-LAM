# Use a pipeline as a high-level helper
from transformers import pipeline

messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe = pipeline("image-text-to-text", model="llava-hf/llava-v1.6-mistral-7b-hf")
pipe(messages)
