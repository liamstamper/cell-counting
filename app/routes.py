# routes.py
from flask import render_template, request
from . import app
from werkzeug.utils import secure_filename
import os
import cv2




@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    
    # Check if the post request has the file part
    if 'image' not in request.files:
        return 'No file part', 400
    file = request.files['image']
    if file.filename == '':
        return 'No selected file', 400
    if file:        
        # Make the filename safe, remove unsupported characters
        filename=secure_filename(file.filename)
        # Save the file to the uploads folder
        file_path = os.path.join('static', 'uploads', filename)
        file.save(file_path)
        # Process the image and return results
        
        results = process_and_count(file_path)

        return render_template('result.html', results=results)
    
def process_and_count(image_path):


    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise and improve thresholding
    blur = cv2.GaussianBlur(gray_image, (5, 5), 0)

     # Apply adaptive thresholding to get a binary image
    thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

    # Find contours from the binary image
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Filter out very small contours that are likely not cells
    filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 50]

    # Draw contours on the original image (optional)
    # cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

    # Count the number of cells
    cell_count = len(filtered_contours)

    return cell_count

if __name__ == "__main__":
    image_path = "cells_image.jpg"  # Path to your image
    num_cells = process_and_count(image_path)
    print("Number of cells in the image:", num_cells)






if __name__ == '__main__':
    app.run(debug=True)
