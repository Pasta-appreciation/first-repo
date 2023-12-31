"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 3.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(!abqi1zl8r7z_uv0h60)aaiw=gyzvstb%3c6v_ezfyd+^9-mm'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#デバッグ用にワイルドカード使ってます！！！！
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts.apps.AccountsConfig',
    'gpt.apps.GptConfig',
    'main_func.apps.MainFuncConfig',
    'corsheaders'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ 
            os.path.join(BASE_DIR, 'templates/'),
            os.path.join(BASE_DIR, 'templates/accounts'),
            os.path.join(BASE_DIR, 'templates/offering'),
            os.path.join(BASE_DIR, 'templates/senior'),
            os.path.join(BASE_DIR, 'templates/test'),
            os.path.join(BASE_DIR, 'templates/gpt'),
        ],
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

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#for login funciton
AUTH_USER_MODEL = 'accounts.CustomUser'

LOGIN_REDIRECT_URL = 'accounts:login_success'
LOGIN_URL = 'accounts:login'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# 許可するオリジン,　脆弱性の極み！！！
CORS_ORIGIN_ALLOW_ALL = True

# レスポンスを公開する
CORS_ALLOW_CREDENTIALS = True

#都道府県のリストを作る(値,ラベル)
PREFECTURES = [
    ("選択なし"  ,"選択なし"  ),  
    ("北海道"  ,"北海道"  ),  
    ("青森県"  ,"青森県"  ),  
    ("岩手県"  ,"岩手県"  ),  
    ("宮城県"  ,"宮城県"  ),  
    ("秋田県"  ,"秋田県"  ),  
    ("山形県"  ,"山形県"  ),  
    ("福島県"  ,"福島県"  ),  
    ("茨城県"  ,"茨城県"  ),  
    ("栃木県"  ,"栃木県"  ),  
    ("群馬県"  ,"群馬県"  ),  
    ("埼玉県"  ,"埼玉県"  ),  
    ("千葉県"  ,"千葉県"  ),  
    ("東京都"  ,"東京都"  ),  
    ("神奈川県","神奈川県"),
    ("新潟県"  ,"新潟県"  ),  
    ("富山県"  ,"富山県"  ),  
    ("石川県"  ,"石川県"  ),  
    ("福井県"  ,"福井県"  ),  
    ("山梨県"  ,"山梨県"  ),  
    ("長野県"  ,"長野県"  ),  
    ("岐阜県"  ,"岐阜県"  ),  
    ("静岡県"  ,"静岡県"  ),  
    ("愛知県"  ,"愛知県"  ),  
    ("三重県"  ,"三重県"  ),  
    ("滋賀県"  ,"滋賀県"  ),  
    ("京都府"  ,"京都府"  ),  
    ("大阪府"  ,"大阪府"  ),  
    ("兵庫県"  ,"兵庫県"  ),  
    ("奈良県"  ,"奈良県"  ),  
    ("和歌山県","和歌山県"),
    ("鳥取県"  ,"鳥取県"  ),  
    ("島根県"  ,"島根県"  ),  
    ("岡山県"  ,"岡山県"  ),  
    ("広島県"  ,"広島県"  ),  
    ("山口県"  ,"山口県"  ),  
    ("徳島県"  ,"徳島県"  ),  
    ("香川県"  ,"香川県"  ),  
    ("愛媛県"  ,"愛媛県"  ),  
    ("高知県"  ,"高知県"  ),  
    ("福岡県"  ,"福岡県"  ),  
    ("佐賀県"  ,"佐賀県"  ),  
    ("長崎県"  ,"長崎県"  ),  
    ("熊本県"  ,"熊本県"  ),  
    ("大分県"  ,"大分県"  ),  
    ("宮崎県"  ,"宮崎県"  ),  
    ("鹿児島県","鹿児島県"),
    ("沖縄県"  ,"沖縄県"  ),  
]

INDUSTRIES = [
    ("選択なし"  ,"選択なし"  ),
    ("IT・通信・インターネット"  ,"IT・通信・インターネット"  ),
    ("商社"  ,"商社"  ),
    ("流通・小売・フード"  ,"流通・小売・フード"  ),
    ("金融・保険"  ,"金融・保険"  ),
    ("不動産・建設・設備"  ,"不動産・建設・設備"  ),
    ("環境・エネルギー"  ,"環境・エネルギー"  ),
    ("メーカー"  ,"メーカー"  ),
    ("サービス・レジャー"  ,"サービス・レジャー"  ),
    ("マスコミ・広告・デザイン"  ,"マスコミ・広告・デザイン"  ),
    ("コンサルティング"  ,"コンサルティング"  ),
    ("運輸・交通・物流・倉庫"  ,"運輸・交通・物流・倉庫"  ),
    ("公的機関"  ,"公的機関"  ),
]

OCCUPATIONS = [
    ("選択なし"  ,"選択なし"  ),
    ("営業"  ,"営業"  ),
    ("医療・福祉"  ,"医療・福祉"  ),
    ("建築・土木"  ,"建築・土木"  ),
    ("電気・電子・機械・半導体"  ,"電気・電子・機械・半導体"  ),
    ("コンサルタント・金融・不動産専門職"  ,"コンサルタント・金融・不動産専門職"  ),
    ("技能工・設備・配送・農林水産"  ,"技能工・設備・配送・農林水産"  ),
    ("管理・事務"  ,"管理・事務"  ),
    ("保育・教育・通訳"  ,"保育・教育・通訳"  ),
    ("販売・フード・アミューズメント"  ,"販売・フード・アミューズメント"  ),
    ("企画・経営"  ,"企画・経営"  ),
    ("ITエンジニア"  ,"ITエンジニア"  ),
    ("医薬・食品・化学・素材"  ,"医薬・食品・化学・素材"  ),
    ("クリエイティブ"  ,"クリエイティブ"  ),
    ("公共サービス"  ,"公共サービス"  ),
    ("美容・ブライダル・ホテル・交通"  ,"美容・ブライダル・ホテル・交通"  ),
    ("WEB・インターネット・ゲーム"  ,"WEB・インターネット・ゲーム"  ),
]

SEX = [
    ("選択なし"  ,"選択なし"  ),
    ("男性"  ,"男性"  ),
    ("女性"  ,"女性"  ),
    ("その他"  ,"その他"  ),
]