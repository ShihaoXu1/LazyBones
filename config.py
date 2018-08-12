import os
# Setting of debug
DEBUG = True

# SECRET_KEY = os.urandom(24)
SECRET_KEY = "dsfasfsdgdfhgsdfsdft"

# Setting of database
DIALECT = 'mysql'
DRIVER = 'pymysql'
DB_USERNAME = 'root'
DB_PASSWORD = 'Xushihao527'
DB_HOST = '127.0.0.1'
DB_PORT = '3306'
DB_NAME = 'LazyBone'
DB_URI = "{}+{}://{}:{}@{}:{}/{}".format(DIALECT, DRIVER, DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False


CMS_USER_ID = 'ABSJDI'

# MAIL_USE_TLS：端口号587
# MAIL_USE_SSL：端口号465
# QQ邮箱不支持非加密方式发送邮件
# 发送者邮箱的服务器地址
MAIL_SERVER = "smtp.qq.com"
MAIL_PORT = '587'
MAIL_USE_TLS = True
# MAIL_USE_SSL
MAIL_USERNAME = "26652283@qq.com"
MAIL_PASSWORD = "ypwwxnpofezibije"
MAIL_DEFAULT_SENDER = "26652283@qq.com"
