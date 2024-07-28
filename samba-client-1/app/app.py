from flask import Flask, render_template, Response, send_file
import os
import io
from smb.SMBConnection import SMBConnection

app = Flask(__name__)
SAMBA_SERVER = 'samba-server'
SHARE_NAME = 'samba_share'
username = ''
password = ''

conn = SMBConnection(username, password, "client_machine", SAMBA_SERVER, use_ntlm_v2=True)
assert conn.connect(SAMBA_SERVER, 139)

@app.route('/')
def index():
    files = conn.listPath(SHARE_NAME, '/')

    file_name_list = [file.filename for file in files]

    return render_template('index.html', files=file_name_list)

@app.route('/view/<filename>')
def view_file(filename):
    file_obj = io.BytesIO()
    conn.retrieveFile(SHARE_NAME, filename, file_obj)
    file_obj.seek(0)

    # Determine content type based on file extension
    if filename.endswith('.txt'):
        return send_file(file_obj, mimetype='text/plain', as_attachment=False)
    elif filename.endswith(('.png', '.jpg', '.jpeg', '.gif')):
        return send_file(file_obj, mimetype='image/jpeg', as_attachment=False)
    else:
        return Response("Unsupported file type", mimetype='text/plain')
    

@app.teardown_appcontext
def close_connection(exception):
    if conn:
        conn.close()


    # file_path = f'//{SAMBA_SERVER}/{SHARE_NAME}/{filename}'
    # file_content = os.popen(f'smbclient {file_path} -N -c "get {filename} -"').read()
    
    # if '.txt' in filename:
    #     return Response(file_content, mimetype='text/plain')
    
    # elif '.jpg' in filename or '.jpeg' in filename:
    #     return Response(file_content, mimetype='image/jpeg')
    
    # elif '.png' in filename:
    #     return Response(file_content, mimetype='image/png')
    
    # else:
    #     return Response("Unsupported file type", mimetype='text/plain')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
