# -*- coding: utf-8 -*-
import os
from flask import Flask, request, url_for, send_from_directory
from werkzeug import secure_filename
import time
import paramiko


ALLOWED_EXTENSIONS = set(['rar','zip', 'tar.gz', 'war'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.getcwd()


html = '''
    <!DOCTYPE html>
    <title>Upload File</title>
    <h1>tomcat单节点部署</h1>
    <form method=post enctype=multipart/form-data>
         <input type=file name=file>
         <br />
         <input type=submit value=上传>
    </form>


    '''


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file_url = url_for('uploaded_file', filename=filename)
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect('192.168.30.102', username='root', password='123456')
            ssh.exec_command('tar -cvf /opt/tomcat/abc.tar.gz /opt/tomcat/webapps/abc.war')
            ftp = ssh.open_sftp()
            ftp.put(filename, '/opt/tomcat/webapps/' + filename)
            ftp.close() 
            ssh.exec_command('rm -rf /opt/tomcat/webapps/abc.war')
            ssh.exec_command('/opt/tomcat/bin/shutdown.sh')
            ssh.exec_command('/opt/tomcat/bin/startup.sh')
            
    return html


if __name__ == '__main__':
    app.run('0.0.0.0')
