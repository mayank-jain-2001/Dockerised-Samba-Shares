from flask import Flask, render_template, Response, send_file
import os
import io
from smb.SMBConnection import SMBConnection

app = Flask(__name__)
SAMBA_SERVER = 'samba-server'
SHARE_NAME = 'samba_share'
username = ''
password = ''


@app.route('/')
def index():
    conn = SMBConnection(username, password, "client_machine", SAMBA_SERVER, use_ntlm_v2=True)
    assert conn.connect(SAMBA_SERVER, 139)

    files = conn.listPath(SHARE_NAME, '/')
    files = [file for file in files if not file.isDirectory]

    file_name_list = [file.filename for file in files]

    conn.close()

    return render_template('index.html', files=file_name_list)

@app.route('/view/<filename>')
def view_file(filename):
    conn = SMBConnection(username, password, "client_machine", SAMBA_SERVER, use_ntlm_v2=True)
    assert conn.connect(SAMBA_SERVER, 139)

    file_obj = io.BytesIO()
    conn.retrieveFile(SHARE_NAME, filename, file_obj)
    file_obj.seek(0)

    conn.close()

    if filename.endswith('.txt'):
        return send_file(file_obj, mimetype='text/plain', as_attachment=False)
    elif filename.endswith(('.png', '.jpg', '.jpeg', '.gif')):
        return send_file(file_obj, mimetype='image/jpeg', as_attachment=False)
    else:
        return Response("Unsupported file type", mimetype='text/plain')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
