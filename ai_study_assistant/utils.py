import re
import os

def sanitize_prompt(prompt: str) -> str:
    """
    Sanitize prompt string to create a safe filename.
    """
    return re.sub(r'[^a-zA-Z0-9_-]', '_', prompt.strip().lower())

def save_image(image, path: str):
    """
    Save PIL Image object to the given path.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    image.save(path)
