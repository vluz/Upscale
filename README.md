# Upscale
### Small streamlit app that uses an ESRGAN to upscale an image

Allows user to upload an image, loads RealESRGAN_x4 model and upscales input image by 4x

<hr>

Open a command prompt and `cd` to a new directory of your choosing:

(optional; recommended) Create a virtual environment with:
```
python -m venv "venv"
venv\Scripts\activate
```

To install do:
```
pip install git+https://github.com/sberbank-ai/Real-ESRGAN.git
git clone https://github.com/vluz/Upscale.git
cd Upscale
pip install -r requirements.txt
```

Go to https://huggingface.co/ai-forever/Real-ESRGAN/blob/a86fc6182b4650b4459cb1ddcb0a0d1ec86bf3b0/RealESRGAN_x4.pth
and download RealESRGAN_x4.pth to the same folder as script

To run do:<br>
`streamlit run up.py` 

App will open on your default browser

<hr>

Click on images to open in new tab

### Example input:
![Input](photo.jpg?raw=true "Input")

### Output:
![Output](20230614-194637.png?raw=true "Output")

