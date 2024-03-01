from flask import Flask
from extensions import db,jwt
from auth import authUser_bp,authComp_bp
from job import job_bp
import os
from flask_cors import CORS
from models import init_db
def create_app():

    app=Flask(__name__)
    app.config.from_prefixed_env()
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.environ['DB_USERNAME']}:{os.environ['DB_PASSWORD']}@{os.environ['HOST_NAME']}/{os.environ['DATABASE']}"

    CORS(app)
    #initialize app
    db.init_app(app)
    with app.app_context():
        init_db()

    jwt.init_app(app)

    #register blueprint
    app.register_blueprint(authUser_bp,url_prefix='/auth/user')
    app.register_blueprint(authComp_bp,url_prefix='/auth/company')
    app.register_blueprint(job_bp,url_prefix="/jobs")


    return app

