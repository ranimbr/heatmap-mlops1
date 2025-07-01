from flask import Flask, request, render_template, redirect, url_for
import os
from main import generate_heatmap  # Ta fonction de génération

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['RESULT_FOLDER'] = 'static'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['RESULT_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'video' not in request.files:
        return "Pas de fichier vidéo envoyé", 400
    video = request.files['video']
    if video.filename == '':
        return "Aucun fichier sélectionné", 400

    video_path = os.path.join(app.config['UPLOAD_FOLDER'], video.filename)
    video.save(video_path)

    output_filename = 'result.mp4'
    output_path = os.path.join(app.config['RESULT_FOLDER'], output_filename)

    generate_heatmap(video_path, output_path)

    return render_template('index.html', result_video=output_filename)

if __name__ == '__main__':
    app.run(debug=True)
