from flask import Flask, render_template_string, \
    session, request, redirect, url_for, send_file, send_from_directory
from hw4_tweepy import tweets_get
from hw4_imageToVideo import image_to_video
import zipfile
import os
import time
app = Flask(__name__)
 
app.secret_key = 'F12Zr47j\3yX R~X@H!jLwf/T'
 

 
@app.route('/')
def login():
    page = '''
    <form action="{{ url_for('do_login') }}" method="post">
        <p>twitter_key: <input type="text" name="user_name" /></p>
        <input type="submit" value="Submit" />
    </form>
    '''
    print(app.root_path)
    return render_template_string(page)

# Download
@app.route('/do_login', methods=['POST'])
def do_login():
    name = request.form.get('user_name')
    session['user_name'] = name



    zipFolder = zipfile.ZipFile('Videozip.zip','w', zipfile.ZIP_DEFLATED)
    #zipFolder.write('abcd.avi')

    try:
        tweets_get(session['user_name'])
        image_to_video(session['user_name'])
        print('convert to videos')
    except Exception as e:
        print(e)
        print('1')




    for file in os.listdir(os.getcwd()):
        if file.endswith('.avi'):
            try:
                zipFolder.write(file)
            except Exception as e:
                print(e)

    zipFolder.close()

    
    # try:
    #     send_file('Videozip.zip', mimetype ='zip', as_attachment=True, attachment_filename = 'Download video')
    # except Exception as e:
    #     print(e)

    #return 'download'
    time.sleep(3)
    return send_file('Videozip.zip', mimetype ='zip', as_attachment=True, attachment_filename = 'Download.zip')
    #return send_from_directory(app.root_path, filename= session['user_name'] + '.avi', as_attachment=True)
 
@app.route('/logout')
def logout():
    session.pop('user_name', None)
    session.clear()
    return redirect(url_for('login'))
 
 
if __name__ == '__main__':
    app.run(debug=True,host = '0.0.0.0', port = 80)












