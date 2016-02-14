from flask import Flask, render_template, send_file
import os
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/image/jpeg.cgi')
def image():
    if not os.path.isdir('cam'):
        os.mkdir('cam')
    result = subprocess.Popen('raspistill -o cam/cam.jpg', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read()
    if result:
        return render_template('cam_err.html', result=str(result, 'ascii'))
    return send_file('cam/cam.jpg', mimetype='image/jpeg')

if __name__ == '__main__':
    import os
    if os.getuid() == 0:
        port = 80
    else:
        port = 5000
    app.run(debug=True, host='0.0.0.0', port=port)
