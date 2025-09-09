from flask import Flask, request, render_template, send_file, flash, redirect, url_for
from werkzeug.utils import secure_filename
import PyPDF2
import io
import os
import tempfile
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}
MAX_FILE_SIZE = 16 * 1024 * 1024  # 16MB max file size

# Create uploads directory if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """Check if the uploaded file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def merge_pdfs(pdf1_path, pdf2_path):
    """Merge two PDF files and return the merged PDF as data."""
    try:
        # Create a PDF merger object
        merger = PyPDF2.PdfMerger()
        
        # Add the first PDF
        with open(pdf1_path, 'rb') as file1:
            merger.append(file1)
        
        # Add the second PDF
        with open(pdf2_path, 'rb') as file2:
            merger.append(file2)
        
        # Create a bytes buffer to hold the merged PDF
        output_buffer = io.BytesIO()
        merger.write(output_buffer)
        merger.close()
        
        # Get the merged PDF bytes
        output_buffer.seek(0)
        return output_buffer.getvalue()
    
    except Exception as e:
        raise Exception(f"Error merging PDFs: {str(e)}")

@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')

@app.route('/merge', methods=['POST'])
def merge_files():
    """Handle PDF file upload and merging."""
    try:
        # Check if files were uploaded
        if 'pdf1' not in request.files or 'pdf2' not in request.files:
            flash('Please upload both PDF files.')
            return redirect(url_for('index'))
        
        pdf1 = request.files['pdf1']
        pdf2 = request.files['pdf2']
        
        # Check if files were selected
        if pdf1.filename == '' or pdf2.filename == '':
            flash('Please select both PDF files.')
            return redirect(url_for('index'))
        
        # Check if files are allowed
        if not (allowed_file(pdf1.filename) and allowed_file(pdf2.filename)):
            flash('Only PDF files are allowed.')
            return redirect(url_for('index'))
        
        # Check file sizes
        pdf1.seek(0, 2)  # Seek to end
        pdf1_size = pdf1.tell()
        pdf1.seek(0)  # Reset to beginning
        
        pdf2.seek(0, 2)  # Seek to end
        pdf2_size = pdf2.tell()
        pdf2.seek(0)  # Reset to beginning
        
        if pdf1_size > MAX_FILE_SIZE or pdf2_size > MAX_FILE_SIZE:
            flash('File size too large. Maximum size is 16MB per file.')
            return redirect(url_for('index'))
        
        # Save uploaded files temporarily
        pdf1_filename = secure_filename(pdf1.filename)
        pdf2_filename = secure_filename(pdf2.filename)
        
        pdf1_path = os.path.join(UPLOAD_FOLDER, f"temp1_{pdf1_filename}")
        pdf2_path = os.path.join(UPLOAD_FOLDER, f"temp2_{pdf2_filename}")
        
        pdf1.save(pdf1_path)
        pdf2.save(pdf2_path)
        
        # Merge the PDFs
        merged_pdf_bytes = merge_pdfs(pdf1_path, pdf2_path)
        
        # Clean up temporary files
        os.remove(pdf1_path)
        os.remove(pdf2_path)
        
        # Create a temporary file for the merged PDF
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_file:
            temp_file.write(merged_pdf_bytes)
            temp_file_path = temp_file.name
        
        # Generate a filename for download
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        download_filename = f"merged_pdf_{timestamp}.pdf"
        
        return send_file(
            temp_file_path,
            as_attachment=True,
            download_name=download_filename,
            mimetype='application/pdf'
        )
    
    except Exception as e:
        flash(f'Error processing files: {str(e)}')
        return redirect(url_for('index'))

@app.route('/health')
def health_check():
    """Health check endpoint."""
    return {'status': 'healthy', 'message': 'PDF Merger App is running'}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(debug=debug, host='0.0.0.0', port=port)
