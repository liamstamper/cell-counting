# routes.py
from flask import render_template, request
from . import app
import imagej  
from werkzeug.utils import secure_filename
import os

# Initialize ImageJ
ij = imagej.init('sc.fiji:fiji:latest')


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
        
        #results = process_and_count(file_path)
        results = 5

        return render_template('result.html', results=results)
    
def process_and_count(image_path):
    # Open the image.
    image_plus = ij.io().open(image_path)
    

    # Use Gaussian blur to smooth the image.
    blurred = ij.op().run("gauss", image_plus, 5.0)
    
    #Conver the image to greyscale
    gray_image = ij.op().run("convert.toGray8", blurred)


    # # Threshold the image.
    otsu_threshold = ij.op().threshold().otsu(blurred)
    binary_image = ij.op().image().threshold(otsu_threshold)

    # #Perform watershed segmentation
    segmented = ij.op().run("watershed", binary_image)

    # # Feature extraction: get region properties.
    region_props = ij.op().run("regionprops", segmented)
    
    # Analysis and quantification: count cells and measure areas.
    particle_analysis = ij.op().run("analyzeParticles", image_plus)

    return particle_analysis





if __name__ == '__main__':
    app.run(debug=True)
