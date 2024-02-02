from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Handle the uploaded image and display results
    image = request.files['image']
    # Process the image and get the results
    results = process_image(image)
    return render_template('results.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
