import json
import base64
import PyPDF2
import io
import tempfile
import os
from datetime import datetime

def handler(event, context):
    """Netlify function to handle PDF merging"""
    
    # Handle CORS
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'POST, OPTIONS'
    }
    
    # Handle preflight requests
    if event['httpMethod'] == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': headers,
            'body': ''
        }
    
    try:
        # Parse the request body
        body = json.loads(event['body'])
        
        # Get base64 encoded PDFs
        pdf1_data = base64.b64decode(body['pdf1'])
        pdf2_data = base64.b64decode(body['pdf2'])
        
        # Create PDF merger
        merger = PyPDF2.PdfMerger()
        
        # Add PDFs from memory
        merger.append(io.BytesIO(pdf1_data))
        merger.append(io.BytesIO(pdf2_data))
        
        # Create merged PDF in memory
        output_buffer = io.BytesIO()
        merger.write(output_buffer)
        merger.close()
        
        # Get merged PDF bytes
        merged_pdf_bytes = output_buffer.getvalue()
        
        # Encode to base64 for response
        merged_pdf_b64 = base64.b64encode(merged_pdf_bytes).decode('utf-8')
        
        # Generate filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"merged_pdf_{timestamp}.pdf"
        
        return {
            'statusCode': 200,
            'headers': {
                **headers,
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'success': True,
                'filename': filename,
                'pdf_data': merged_pdf_b64
            })
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                **headers,
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'success': False,
                'error': str(e)
            })
        }
