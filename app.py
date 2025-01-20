from flask import Flask, render_template, request, jsonify, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import qrcode
import io
import base64

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///votes.db'
db = SQLAlchemy(app)

class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.String(10), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

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
    new_vote = Vote(answer=answer)
    db.session.add(new_vote)
    db.session.commit()
    return jsonify({'status': 'success'})

@app.route('/get_results')
def get_results():
    yes_votes = Vote.query.filter_by(answer='yes').count()
    no_votes = Vote.query.filter_by(answer='no').count()
    return jsonify({
        'yes': yes_votes,
        'no': no_votes
    })

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # Lösche alle existierenden Einträge beim Start
        Vote.query.delete()
        db.session.commit()
    app.run(debug=True)
else:
    # Für Vercel: Datenbank initialisieren wenn die App als Modul importiert wird
    with app.app_context():
        db.create_all()
