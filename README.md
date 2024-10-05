# Image Processing Tool

## Overview

The **Image Processing Tool** is a web application that allows users to upload images and extract valuable information, including metadata and text from images using Optical Character Recognition (OCR). This project utilizes Flask, a lightweight web framework, along with the Python Imaging Library (PIL) and Tesseract for text extraction.

## Features

- **Image Upload**: Users can upload images in PNG, JPG, or JPEG formats.
- **Metadata Extraction**: Automatically extracts metadata including filename, format, size, and mode.
- **Text Extraction**: Uses OCR to extract text from uploaded images.
- **Sensitivity Analysis**: Analyzes extracted text for sensitive information.

## Installation

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- Pip (Python package installer)

### Clone the Repository

bash
git clone https://github.com/Rabbil1/Image-Data-Insights.git
cd Image-Data-Insights
Install Required Packages
bash
Copy code
pip install -r requirements.txt

Add the Tesseract executable to your system's PATH.
Usage
Start the Flask application:
bash
Copy code
python app.py
Open your web browser and go to http://127.0.0.1:5000/.

Upload an image file, and the application will process it to display the extracted metadata, text, and sensitivity rating.

File Structure
php
Copy code
Image-Data-Insights/
│
├── static/
│   └── uploads/          # Uploaded images are stored here
│
├── services/
│   └── image_processing_service.py  # Contains the image processing logic
│
├── app.py                # Main Flask application
│
├── requirements.txt      # Required Python packages
│
└── README.md             # Project documentation
Contributing
Contributions are welcome! Please open an issue or submit a pull request if you'd like to contribute to this project.

License
This project is licensed under the MIT License. See the LICENSE file for details.

