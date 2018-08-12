from flask import Blueprint, views, render_template, request, session, \
    redirect, url_for, g
from .forms import LoginForm, ResetpwdForm, ResetEmailForm
from .models import CMSUser
from .decorators import login_required
import config
from flask_mail import Message
from exts import db, mail
from utils import restful
import string, random

bp = Blueprint("cms", __name__, url_prefix='/cms')


@bp.route('/')
@login_required
def index():
    return render_template('cms/cms_index.html')

@bp.route('/logout/')
@login_required
def logout():
    del session[config.CMS_USER_ID]
    return redirect(url_for('cms.login'))

@bp.route('/profile/')
@login_required
def profile():
    return render_template('cms/cms_profile.html')

@bp.route('/email_captcha/')
def email_captcha():
    # /email_captcha/?email=xxx@qq.com
    email = request.args.get('email')
    if not email:
        return restful.params_error('请传递邮箱参数')
    source = list(string.ascii_letters)
    source.extend(map(lambda x: str(x), range(0, 10)))
    # source.extend(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
    captcha = "".join(random.sample(source, 6))

    # send captcha to new email
    message = Message('Lazybone captcha', recipients=[email], body='Your captcha is: %s' % captcha)
    try:
        mail.send(message)
    except:
        return restful.server_error()
    return restful.success()
@bp.route('/email/')
def send_email():
    message = Message('Lazybone code', recipients=['425043969@qq.com'], body='ceshi')
    mail.send(message)

class LoginView(views.MethodView):

    def get(self, message=None):

        return render_template('cms/cms_login.html', message=message)

    def post(self):
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            remember = form.remember.data
            print(remember)
            user = CMSUser.query.filter_by(email=email).first()
            if user and user.check_password(password):
                session[config.CMS_USER_ID] = user.id
                if remember:
                    session.permanent = True
                else:
                    session.permanent = False
                return redirect(url_for('cms.index'))
            else:
                return self.get(message='Incorrect email or password')
        else:
            message = form.errors.popitem()[1][0]
            return self.get(message=message)

class ResetPwdView(views.MethodView):
    decorators = [login_required]
    def get(self):
        return render_template('cms/cms_resetpwd.html')

    def post(self):
        form = ResetpwdForm(request.form)
        if form.validate():
            oldpwd = form.oldpwd.data
            newpwd = form.newpwd.data
            user = g.cms_user
            if user.check_password(oldpwd):
                user.password = newpwd
                db.session.commit()
                # {"code":200,message=""}
                # return jsonify({"code":200,"message":""})
                return restful.success()
            else:
                return restful.params_error("旧密码错误！")
        else:
            return restful.params_error(form.get_error())

class ResetEmailView(views.MethodView):
    decorators = [login_required]
    def get(self):
        return render_template('cms/cms_resetemail.html')
    def post(self):
        form = ResetEmailForm(request.form)
        if form.validate():
            email = form.email.data
            g.cms_user.email = email
            db.session.commit()
            return restful.success()
        else:
            return restful.params_error(form.get_error())
bp.add_url_rule('/login/', view_func= LoginView.as_view('login'))
bp.add_url_rule('/resetpwd/', view_func=ResetPwdView.as_view('resetpwd'))
bp.add_url_rule('/resetemail/', view_func=ResetEmailView.as_view('resetemail'))
