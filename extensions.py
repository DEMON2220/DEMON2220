from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_uploads import UploadSet, IMAGES
from flask_caching import Cache
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_restful import Resource
from sqlalchemy import asc, desc, or_
from flask import Flask, render_template, url_for, copy_current_request_context,redirect
import httpie


app = Flask(__name__)
db = SQLAlchemy(app)

jwt = JWTManager()
image_set = UploadSet('images', IMAGES)
cache = Cache()
limiter = Limiter(key_func=get_remote_address)

