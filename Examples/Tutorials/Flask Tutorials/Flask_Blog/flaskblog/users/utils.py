import os
import secrets
from PIL import Image
from flask import url_for,current_app
from flask_mail import Message
from flaskblog import  mail


def save_picture(form_picture):
    random_name = secrets.token_hex(8)
    fname, fname_extention = os.path.splitext(form_picture.filename)
    new_picture_name = random_name + fname_extention
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', new_picture_name)

    # resize image to reduce big file sizes
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return new_picture_name


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password reset for Flask Blog', sender='mathewjose09@gmail.com', recipients=[user.email])
    msg.body = f'''To Reset your password , visit the link
    {url_for('users.reset_token', token=token, _external=True)}

    Please ignore if you have not made the request .
    '''
    mail.send(msg)
