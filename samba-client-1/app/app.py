from flask import Flask, render_template
import os

app = Flask(__name__)
SAMBA_SERVER = 'samba-server'
SHARE_NAME = 'samba_share'

@app.route('/')
def index():
    files = os.popen(f'smbclient //{SAMBA_SERVER}/{SHARE_NAME} -N -c "ls"').read()
    files_list = files.split('\n')
    return render_template('index.html', files=files_list)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
