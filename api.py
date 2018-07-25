from flask import Flask
from flask import request, jsonify,json

app = Flask(__name__)
app.config["DEBUG"] = True

massages = [
    {'Msg_id': 0,'Date': '20/Jan/2018','Title': 'A Fire Upon the Deep','Msg': 'The coldsleep itself was dreamless.With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.'},
    {'Msg_id': 1,'Date': '20/Dec/2018','Title': 'The Ones Who Walk Away From Omelas','Msg': 'You mean the world to me. With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.'}
    ]

@app.route('/api/v1/mydiary/allmassages', methods=['GET'])
def returnAll():
    return jsonify({'massages':massages} )


@app.route('/api/v1/mydiary/allmassages/<int:Msg_id>', methods=['GET'])
def returnOne(Msg_id):
    msg =[massage for massage in massages if massage['Msg_id'] == Msg_id]
    return jsonify({'massage': msg[0]})


@app.route('/api/v1/mydiary/allmassages', methods=['POST'])
def addMassage():
    newMsg ={
    'Msg_id':request.json['Msg_id'],'Date':request.json['Date'],'Title':request.json['Title'],'Msg':request.json['Msg']
    }
    massages.append(newMsg)
    return jsonify({'massages':massages})


@app.route('/api/v1/mydiary/allmassages/<int:Msg_id>', methods=['PUT'])
def modifyOne(Msg_id):
    msg =[massage for massage in massages if massage['Msg_id'] == Msg_id]
    msg[0]['Title'] = request.json['Title']
    msg[0]['Msg'] = request.json['Msg']
    return jsonify({'massage': msg[0]})





if __name__ == '__main__':
    
    app.run()