
from wtforms import Form, StringField, IntegerField
from wtforms.validators import Email, Length, InputRequired, EqualTo

class LoginForm(Form):
    email = StringField(validators=[Email(message='Wrong Email Format'),InputRequired(message='Please input your email')])
    password = StringField(validators=[Length(6, 20, message='Wrong Password Format')])
    remember = IntegerField()

class ResetpwdForm(Form):
    oldpwd = StringField(validators=[Length(6,20,message='请输入正确格式的旧密码')])
    newpwd = StringField(validators=[Length(6,20,message='请输入正确格式的新密码')])
    newpwd2 = StringField(validators=[EqualTo("newpwd",message='确认密码必须和新密码保持一致')])

class ResetEmailForm(Form):
    email = StringField(validators=[Email(message='请输入正确格式的邮箱！')])
    captcha = StringField(validators=[Length(min=6,max=6,message='请输入正确长度的验证码！')])
