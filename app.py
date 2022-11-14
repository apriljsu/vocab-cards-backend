# No.1 start
from flask import Flask, jsonify

# No.3 continue here
from flask_cors import CORS
from resources.vocabs import vocab

#No.6 continue here
from flask_login import login_manager
from resources.users import user
login_manager = login_manager()



# No.2 continue
import models


DEBUG = True # print nice helpful error msgs since we are in development
PORT = 8000
#initialize an instance of the Flask class, which starts the website.THIS IS ANALOGOUS TO :const app = express ()
app = Flask(__name__)

#no.6 continue here
app.secret_key = 'kdosjfiosdjfd'
login_manager.init_app(app)
@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id ==userid)
    except models.DoesNotExist:
        return None

# No. 3 continue here
CORS(vocab, origins = ['http://localhost:3000'], supports_credentials=True)
app.register_blueprint(vocab, url_prefix= '/api/v1/vocab')

#no.6 continue here
CORS(user, origins = ['http://localhost:3000'], supports_credentials=True)
app.register_blueprint(user, url_prefix = '/api/v1/user')
#run the app when the program starts
#this is like app.listen() in express - it goes at the bottom 
#__name__ == '__main__' here means we just ran this file from the command line,as opposed to exporting and importing from somewhere else
if __name__ == '__main__':
    """part of No.2"""
    models.initialize() #has to be above app.run
    app.run(debug=DEBUG, port=PORT)

