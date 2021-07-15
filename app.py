from flask import Flask, flash, url_for, render_template, request, abort, redirect
from models import User

app = Flask(__name__)
app.secret_key = '123'

from wtforms import Form, TextField, PasswordField, validators


class LoginForm(Form):
    username = TextField("username", [validators.Required()])
    password = PasswordField("password", [validators.Required()])


@app.route("/user", methods=['GET', 'POST'])
def login():
    myForm = LoginForm(request.form)
    if request.method == 'POST':
        if myForm.username.data == "jikexueyuan" and myForm.password.data == "123456" and myForm.validate():
            return redirect("http://www.jikexueyuan.com")
        else:
            message = "Login Failed"
            return render_template('index2.html', message=message, form=myForm)
    return render_template('index2.html', form=myForm)


if __name__ == '__main__':
    app.run()
