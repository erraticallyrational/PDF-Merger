# 📄 PDF Merger Web App

A simple and elegant web application for merging PDF files built with Python Flask and PyPDF2. Upload two PDF files and merge them into one document instantly with a beautiful, modern interface.

![PDF Merger](https://img.shields.io/badge/PDF-Merger-blue)
![Python](https://img.shields.io/badge/Python-3.7+-green)
![Flask](https://img.shields.io/badge/Flask-2.3.3-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ Features

- 🚀 **Easy to use**: Upload two PDF files and merge them with a single click
- 🎨 **Modern UI**: Beautiful, responsive design that works on all devices
- 🔒 **Secure**: Files are processed locally and deleted after merging
- 📱 **Mobile-friendly**: Responsive design that works on phones and tablets
- ⚡ **Fast**: Quick processing with minimal server load
- 🛡️ **Safe**: File size limits and type validation
- 🎯 **Drag & Drop**: Intuitive file upload with drag-and-drop support
- 🔄 **Real-time feedback**: Loading states and progress indicators

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/pdf-merger-app.git
   cd pdf-merger-app
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:5000`

### 🐳 Docker Support (Optional)
```bash
# Build the image
docker build -t pdf-merger .

# Run the container
docker run -p 5000:5000 pdf-merger
```

## Usage

1. **Upload Files**: Click the "Choose First PDF" and "Choose Second PDF" buttons to select your files
2. **Merge**: Click the "Merge PDFs" button to combine your files
3. **Download**: The merged PDF will automatically download to your device

## Technical Details

- **Backend**: Python Flask
- **PDF Processing**: PyPDF2 library
- **Frontend**: HTML5, CSS3, JavaScript
- **File Handling**: Secure file upload with validation
- **Maximum file size**: 16MB per file
- **Supported formats**: PDF only

## File Structure

```
pdf_merger_app/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html     # Main web interface
├── uploads/           # Temporary file storage (auto-created)
└── README.md          # This file
```

## API Endpoints

- `GET /` - Main application page
- `POST /merge` - Merge PDF files
- `GET /health` - Health check endpoint

## Security Features

- File type validation (PDF only)
- File size limits (16MB max)
- Secure filename handling
- Temporary file cleanup
- No persistent file storage

## Browser Compatibility

- Chrome (recommended)
- Firefox
- Safari
- Edge
- Mobile browsers

## Troubleshooting

**"Only PDF files are allowed"**
- Make sure you're uploading actual PDF files, not images or other formats

**"File size too large"**
- Reduce the size of your PDF files (maximum 16MB each)

**"Error processing files"**
- Check that your PDF files are not corrupted or password-protected

## Development

To run in development mode:
```bash
export FLASK_ENV=development
python app.py
```

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to submit issues and enhancement requests!
