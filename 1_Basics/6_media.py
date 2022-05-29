import streamlit as st 

# Working Media files( videos/images/audio)
# Displayy image
from PIL import Image
img = Image.open("data/image_03.jpg")
st.image(img,use_column_width=True)

# from url
st.image("https://www.independent.ie/entertainment/movies/81e44/35936907.ece/AUTOCROP/w1240/ipanews_7c125421-077c-42ce-bb36-631f75a560cc_1")

# Display videos
video_file = open("data/secret_of_success.mp4","rb")
st.video(video_file)

# Display Audio/Working with Audio
audio_file = open("data/song.mp3","rb")
st.audio(audio_file)

