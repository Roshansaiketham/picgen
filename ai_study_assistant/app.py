import streamlit as st
from diffusers import StableDiffusionPipeline
import torch
import os
from utils import sanitize_prompt, save_image

st.title(" AI Study Assistant - Educational Image Generator")
st.markdown("Enter a topic below to generate a study diagram or illustration.")

# Input prompt
prompt = st.text_input("Enter your study topic", "photosynthesis diagram for 6th grade")

if st.button("Generate Image"):
    with st.spinner("Generating Image..."):
        # Load model (cache it on first run)
        @st.cache_resource
        def load_model():
            pipe = StableDiffusionPipeline.from_pretrained(
                "CompVis/stable-diffusion-v1-4",
                torch_dtype=torch.float16,
                revision="fp16",
                use_auth_token=True  # Add your Hugging Face token here
            ).to("cuda")
            return pipe

        pipe = load_model()

        # Sanitize prompt for filename
        safe_prompt = sanitize_prompt(prompt)

        # Generate image
        image = pipe(prompt).images[0]

        # Save image locally
        save_dir = "/content/drive/MyDrive/ml/ai_study_assistant/saved_images"

        os.makedirs(save_dir, exist_ok=True)
        image_path = os.path.join(save_dir, f"{safe_prompt}.png")
        image.save(image_path)

        st.image(image, caption="Generated Study Image", use_column_width=True)
        st.success(f"Image saved at: {image_path}")
