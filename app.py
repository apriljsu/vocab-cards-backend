# No.1 start
from flask import Flask, jsonify, after_this_request

# No.3 continue here
from flask_cors import CORS
from resources.vocabs import vocab

#No.6 continue here
from flask_login import LoginManager
from resources.users import user
login_manager = LoginManager()

#No. 8 set up env.
import os
from dotenv import load_dotenv
load_dotenv()

# No.2 continue
import models


DEBUG = True # print nice helpful error msgs since we are in development
PORT = os.environ.get("PORT") # part of No.8
#initialize an instance of the Flask class, which starts the website.THIS IS ANALOGOUS TO :const app = express ()
app = Flask(__name__)


#no.6 continue here
app.secret_key = os.environ.get('APP_SECRET')

app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='None',
)

login_manager.init_app(app)
@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id ==userid)
    except models.DoesNotExist:
        return None

# No. 3 continue here
# CORS(vocab, origins = ['*'], supports_credentials=True)
# CORS(vocab, origins = ['http://localhost:3000'])
CORS(vocab, origins = ['http://localhost:3000', 'https://vocab-cards-frontend.herokuapp.com'], supports_credentials=True)

app.register_blueprint(vocab, url_prefix = '/api/v1/vocab')

#no.6 continue here
CORS(user, origins = ['http://localhost:3000', 'https://vocab-cards-frontend.herokuapp.com'], supports_credentials=True)
app.register_blueprint(user, url_prefix = '/api/v1/user')

# we don't want to hog up the SQL connection pool
# so we should connect to the DB before every request
# and close the db connection after every request

@app.before_request # use this decorator to cause a function to run before reqs
def before_request():

    """Connect to the db before each request"""
    print("you should see this before each request") # optional -- to illustrate that this code runs before each request -- similar to custom middleware in express.  you could also set it up for specific blueprints only.
    models.DATABASE.connect()

    @after_this_request # use this decorator to Executes a function after this request
    def after_request(response):
        """Close the db connetion after each request"""
        print("you should see this after each request") # optional -- to illustrate that this code runs after each request
        models.DATABASE.close()
        return response # go ahead and send response back to client
                      # (in our case this will be some JSON)

# ADD THESE THREE LINES -- because we need to initialize the
# tables in production too!
if os.environ.get('FLASK_ENV') != 'development':
  print('\non heroku!')
  models.initialize()


#run the app when the program starts
#this is like app.listen() in express - it goes at the bottom 
#__name__ == '__main__' here means we just ran this file from the command line,as opposed to exporting and importing from somewhere else
if __name__ == '__main__':
    """part of No.2"""
    models.initialize() #has to be above app.run
    app.run(debug=DEBUG, port=PORT)

