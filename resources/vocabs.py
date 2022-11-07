# No.3 start
import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict

vocab = Blueprint('vocabs', 'vocab')

@vocab.route('/', methods=['GET'])
def get_all_vocabs():
    try: 
        vocabs = [model_to_dict(vocab) for vocab in models.Vocab.select()]
        print(vocabs)
        return jsonify(data=vocabs, status={'code':200, 'message':'Success'})
    except models.DoesNotExist:
        return jsonify(data={}, status={'code':401, 'message':'Error'})

@vocab.route('/', methods=['POST'])
def create_vocab():
    payload = request.get_json()
    print(type(payload),'payload')
    vocab = models.Vocab.create(**payload)
    print(vocab.__dict__)
    print(dir(vocab))
    print(model_to_dict(vocab),'model to dict')
    vocab_dict=model_to_dict(vocab)
    return jsonify(data=vocab_dict, status={'code':201,'message':'Success'} )