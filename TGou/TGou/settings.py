import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static').replace('\\', '/'),
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+u4#266&7&n*-ovzr7c3nv!63&64zpmk^89sqkouoxg-to+hib'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

ALLOWED_HOSTS = []

# Application definition
# 注册app
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'TGous.apps.TgousConfig',
    'Login.apps.LoginConfig',
    'captcha',

]


#验证码配置
CAPTCHA_LENGTH = 4 #字符个数
CAPTCHA_TIMEOUT = 1 #超时时间
CAPTCHA_IMAGE_SIZE=(100,30) #图像大小
CAPTCHA_BACKGROUND_COLOR ='#f3f3f3'





MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'TGou.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'TGou.wsgi.application'

from TGous.static import email_pwd

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': email_pwd.mysql_db_name,
        'USER': email_pwd.mysql_name,
        'PASSWORD': email_pwd.mysql_pwd,
        'HOST': '127.0.0.1',
        'PORT': '3306',
    },
}
# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/
# 英文变中文
LANGUAGE_CODE = 'zh-hans'
# LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
# 时区
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

# USE_TZ = True
USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/


# 邮箱配置
EMAIL_USE_SSL = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = email_pwd.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = email_pwd.EMAIL_HOST_PASSWORD
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
CONFIRM_DAYS = 7

# LOG_DIR = os.path.join(BASE_DIR, 'TGous/log')
# if not os.path.exists(LOG_DIR):
#     os.makedirs(LOG_DIR)
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': True,
#     'formatters': {  # 日志格式
#         'standard': {
#             'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(pathname)s:%(funcName)s:%(lineno)d] [%(levelname)s]- %(message)s'},
#         'Access_statistics': {
#             'format': '%(message)s'
#         }
#     },
#
#     'filters': {  # 过滤器
#         'test': {
#             '()': 'TGous.ops.TestFilter'
#         }
#     },
#     # 处理器
#     'handlers': {
#         'null': {
#             'level': 'DEBUG',
#             'class': 'logging.NullHandler',
#         },
#         # 文件处理器
#         'file_handler': {  # 记录到日志文件(需要创建对应的目录，否则会出错)
#             'level': 'DEBUG',
#             'class': 'logging.handlers.RotatingFileHandler',  # 循环文件处理,当文件到达一定大小时,自动将文件切为两份
#             'filename': os.path.join(LOG_DIR, 'service.log'),  # 日志输出文件
#             'maxBytes': 1024 * 1024 * 10,  # 文件大小
#             'backupCount': 5,  # 备份份数
#             'formatter': 'standard',  # 使用哪种formatters日志格式
#             'encoding': 'utf8',
#         },
#         # 访问统计
#         'Access_statistics_handler': {  # 记录到日志文件(需要创建对应的目录，否则会出错)
#             'level': 'DEBUG',
#             'class': 'logging.handlers.RotatingFileHandler',  # 循环文件处理,当文件到达一定大小时,自动将文件切为两份
#             'filename': os.path.join(LOG_DIR, 'Access_statistics.log'),  # 日志输出文件
#             'maxBytes': 1024 * 1024 * 5,  # 文件大小
#             'backupCount': 5,  # 备份份数
#             'formatter': 'Access_statistics',  # 使用哪种formatters日志格式
#             'encoding': 'utf-8',
#         },
#         # 终端处理器
#         'console_handler': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'formatter': 'standard',
#         },
#     },
#     'loggers': {  # logging管理器
#         'django': {
#             'handlers': ['console_handler', 'file_handler'],
#             'filters': ['test'],
#             'level': 'DEBUG'
#         },
#         'statistics': {
#                         'handlers': ['Access_statistics_handler'],
#                         'level': 'DEBUG'
#                     }
#         }
#     }
