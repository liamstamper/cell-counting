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
    
    if 'image' not in request.files:
        return 'No file part', 400
    file = request.files['image']
    if file.filename == '':
        return 'No selected file', 400
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join('static', 'uploads', filename)
        file.save(file_path)
        
        results, original_img_path, contours_img_path = process_and_count(file_path)
        
        # Prepare for deletion
        files_to_delete = [file_path, os.path.join('static', contours_img_path)]

        return render_template('result.html', results=results, original_img=original_img_path, contours_img=contours_img_path)
    
def process_and_count(image_path):


    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise and improve thresholding
    blur = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # Adaptive thresholding
    thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY_INV, 11, 2)

    # Find contours
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Filter contours
    filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 50]

    # Draw contours on a copy of the original image
    contours_image = image.copy()
    cv2.drawContours(contours_image, filtered_contours, -1, (0, 255, 0), 3)

    # Save the contours image
    contours_image_path = image_path.replace('.jpg', '_contours.jpg')
    cv2.imwrite(contours_image_path, contours_image)

    # Count the cells
    cell_count = len(filtered_contours)

    return cell_count, image_path, contours_image_path.replace('static/', '')

if __name__ == "__main__":
    image_path = "cells_image.jpg"  # Path to your image
    num_cells = process_and_count(image_path)
    print("Number of cells in the image:", num_cells)






if __name__ == '__main__':
    app.run(debug=True)
