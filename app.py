# No.1 start
from flask import Flask, jsonify

# No.3 continue here
from flask_cors import CORS
from resources.vocabs import vocab

# No.2 continue
import models


DEBUG = True # print nice helpful error msgs since we are in development
PORT = 8000
#initialize an instance of the Flask class, which starts the website.THIS IS ANALOGOUS TO :const app = express ()
app = Flask(__name__)


# No. 3 continue here
CORS(vocab, origins = ['http://localhost:3000'], supports_credentials=True)
app.register_blueprint(vocab, url_prefix='/api/v1/vocab')

#run the app when the program starts
#this is like app.listen() in express - it goes at the bottom 
#__name__ == '__main__' here means we just ran this file from the command line,as opposed to exporting and importing from somewhere else
if __name__ == '__main__':
    """part of No.2"""
    models.initialize() #has to be above app.run
    app.run(debug=DEBUG, port=PORT)

