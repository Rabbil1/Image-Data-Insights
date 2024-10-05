from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
import os
from services.image_processing_service import process_image  # Import the image processing function

app = Flask(__name__)

# Configuration
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

# Check if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Home Page
@app.route('/')
def index():
    return render_template('index.html')

# Upload API
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        try:
            file.save(file_path)

            # Process the image for metadata and text extraction
            result = process_image(file_path)

            if "error" in result:
                return jsonify({"error": result["error"]}), 400
            
            # Include extracted text and metadata in the response
            return jsonify({
                "message": "File uploaded successfully!",
                "filename": filename,
                "metadata": result["metadata"],
                "extracted_text": result["extracted_text"],
                "sensitivity_rating": result["sensitivity_rating"]
            }), 200

        except Exception as e:
            return jsonify({"error": f"An error occurred while saving or processing the file: {str(e)}"}), 500

    return jsonify({"error": "File type not allowed"}), 400

if __name__ == '__main__':
    app.run(debug=True)
