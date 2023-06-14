import streamlit as st
import warnings
import time
import torch
from PIL import Image
import numpy as np
from RealESRGAN import RealESRGAN


@st.cache_resource
def loadmodel():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = RealESRGAN(device, scale=4)
    model.load_weights('RealESRGAN_x4.pth', download=False)
    return model


warnings.filterwarnings("ignore")
st.title("AI Upscale 4x")
st.divider()
uploaded_file = st.file_uploader("Upload a file to upscale", type=["png", "jpg"])

if uploaded_file:
    st.image(uploaded_file, caption='Original')
    if st.button("Upscale"):
        with st.spinner("Upscale..."):
            input = Image.open(uploaded_file).convert('RGB')
            model = loadmodel()
            output = model.predict(input)
            now = str(time.strftime("%Y%m%d-%H%M%S"))
            filename = now + ".png"
            output.save(filename)
            st.image(output, caption='Result')

