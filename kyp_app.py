import tensorflow as tf
import streamlit as st
import cv2
from PIL import Image, ImageOps
import numpy as np
import sqlite3

connection=sqlite3.connect('Flowers.db')
daisy_cursor = connection.execute("SELECT * FROM Daisy")
dandelion_cursor = connection.execute("SELECT * FROM Dandelion")
rose_cursor = connection.execute("SELECT * FROM Rose")
sunflower_cursor = connection.execute("SELECT * FROM Sunflower")
tulip_cursor = connection.execute("SELECT * FROM Tulip")


model = tf.keras.models.load_model('kyp_model.hdf5')
st.write("""
          Know Your Plants - Plant analysis tool
         """)
st.write("This is a tool used to help identify the plant based off the photo you upload")

file = st.file_uploader("Please Upload your plant Image", type=["jpg","png"])

def upload_image_analysis(image_data, model):
    size = (128,128)
    image =ImageOps.fit(image_data,size,Image.LANCZOS)
    image = np.asarray(image)
    img = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    img_resize = (cv2.resize(img, dsize=(75,75), interpolation=cv2.INTER_CUBIC))/255.
    img_reshape = img_resize[np.newaxis,...]

    analysis = model.predict(img_reshape)

    if analysis.shape[1] == 5:
        analysis = np.insert(analysis,3,0,axis=1)

    return analysis

if file is None:
    st.text("Please Upload Image File of a flower")
else:
    image = Image.open(file)
    st.image(image,use_column_width=True)
    analysis = upload_image_analysis(image,model)
    

    if np.argmax(analysis) == 0:
        st.write("Identified as a Daisy")
        for row in daisy_cursor:
            st.write(f"ID: {row[0]}")
            st.write(f"Orgins: {row[1]}")
            st.write(f"Danger: {row[2]}")
            st.write(f"Feature: {row[3]}")
            st.write(f"WildLife: {row[4]}")
            st.write("----------------------------")

       
    
    elif np.argmax(analysis) == 1:
        st.write("Identified as a Dandelion")
        for row in dandelion_cursor:
            st.write(f"ID: {row[0]}")
            st.write(f"Orgins: {row[1]}")
            st.write(f"Danger: {row[2]}")
            st.write(f"Feature: {row[3]}")
            st.write(f"WildLife: {row[4]}")
            st.write("----------------------------")
    
    elif np.argmax(analysis) == 2:
        st.write("Identified as a Rose")
        for row in rose_cursor:
            st.write(f"ID: {row[0]}")
            st.write(f"Orgins: {row[1]}")
            st.write(f"Danger: {row[2]}")
            st.write(f"Feature: {row[3]}")
            st.write(f"WildLife: {row[4]}")
            st.write("----------------------------")
    
    elif np.argmax(analysis) == 3:
        st.write("Identified as a Sunflower")
        for row in sunflower_cursor:
            st.write(f"ID: {row[0]}")
            st.write(f"Orgins: {row[1]}")
            st.write(f"Danger: {row[2]}")
            st.write(f"Feature: {row[3]}")
            st.write(f"WildLife: {row[4]}")
            st.write("----------------------------")
    
    elif np.argmax(analysis) == 4:
        st.write("Identified as a Tulip")
        for row in tulip_cursor:
            st.write(f"ID: {row[0]}")
            st.write(f"Orgins: {row[1]}")
            st.write(f"Danger: {row[2]}")
            st.write(f"Feature: {row[3]}")
            st.write(f"WildLife: {row[4]}")
            st.write("----------------------------")
    
    else:
        st.write("Unable to identify plant")
    
    st.write(analysis)

connection.close()
