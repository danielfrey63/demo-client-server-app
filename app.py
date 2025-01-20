from flask import Flask, render_template, request, jsonify, url_for
from datetime import datetime
import qrcode
import io
import base64

app = Flask(__name__)

# In-memory storage for votes
votes = {'yes': 0, 'no': 0}

def generate_qr_code(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Convert the image to base64
    img_buffer = io.BytesIO()
    img.save(img_buffer, format='PNG')
    img_str = base64.b64encode(img_buffer.getvalue()).decode()
    return img_str

@app.route('/survey')
def survey():
    return render_template('survey.html')

@app.route('/')
@app.route('/results')
def results():
    # Generate QR code for the survey URL
    survey_url = request.url_root.rstrip('/') + url_for('survey')
    qr_code = generate_qr_code(survey_url)
    return render_template('results.html', qr_code=qr_code, survey_url=survey_url)

@app.route('/submit_vote', methods=['POST'])
def submit_vote():
    answer = request.json.get('answer')
    if answer in ['yes', 'no']:
        votes[answer] += 1
        return jsonify({'status': 'success'})
    return jsonify({'status': 'error', 'message': 'Invalid vote'}), 400

@app.route('/get_results')
def get_results():
    return jsonify({
        'yes': votes['yes'],
        'no': votes['no']
    })

if __name__ == '__main__':
    app.run(debug=True)
