# No.3 start: set up vocabs.py
import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
#no. 7 start: link user to vocabs
from flask_login import current_user 

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
    # print(type(payload),'payload type') #payload type is class 'dict'
    # print(payload, 'payload')#only shows the vocab card added without ID
    vocab = models.Vocab.create(**payload)
    # print(type(vocab)) # <model:Vocab>
    # print(vocab.__dict__)
    # print(dir(vocab)) #The dir() function returns all properties and methods of the specified object, without the values.
    print(model_to_dict(vocab),'model to dict')
    vocab_dict=model_to_dict(vocab)
    return jsonify(data=vocab_dict, status={'code':201,'message':'Success'} )

@vocab.route('/<id>', methods=['GET'])
def get_one_vocab(id):
    # print(id, 'vocab id')
    vocab = models.Vocab.get_by_id(id)
    # print(vocab) # only shows ID
    print(vocab.__dict__)
    return jsonify(
        data = model_to_dict(vocab),
        status=200,
        message ='Success'
    ), 200

@vocab.route('/<id>', methods=['PUT'])
def update_vocab(id):
    payload = request.get_json()
    query = models.Vocab.update(**payload).where(models.Vocab.id==id)
    query.execute()
    return jsonify(
        data = model_to_dict(models.Vocab.get_by_id(id)),
        status = 200,
        message = 'vocab updated successfully'
    ), 200

@vocab.route('/<id>', methods=['DELETE'])
def delete_vocab(id):
    query = models.Vocab.delete().where(models.Vocab.id==id)
    query.execute()
    return jsonify(
        message = 'vocab deleted succesfully',
        status =200
    ), 200