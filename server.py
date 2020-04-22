from flask import Flask, request, jsonify
import requests
app=Flask(__name__)

@app.route('/', methods=['GET'])
def respond():
    name = request.args.get('name')
    print(name)
    if(name):
        res={'name':name}
        return jsonify(res)
    else:
        return "enter query"


@app.route('/webhook', methods=['POST'])
def query():
    req = request.get_json(silent=True , force = True)
    intent=req.get('queryResult').get('intent').get('displayName')
    if intent == 'Default Welcome Intent':
        qtext=req.get('queryResult').get('queryText')
        res={'fulfillmentText':'kaam bol bc '}
        return jsonify(res)
    elif intent == 'numbers':
        qtype=req.get('queryResult').get('parameters').get('type')
        num=req.get('queryResult').get('parameters').get('number')
        num=int(num)
        print(qtype,num)
        url = 'http://numbersapi.com/'
        final_url = url + str(num) + '/' + qtype + '?json'
        reqs= requests.get(final_url)
        text = reqs.json()['text']
        print(text)
        return jsonify({'fulfillmentText':text})
        
    return jsonify({'fulfillmentText':'Dhangg se Likh be'})    




if __name__=='_main_':
    app.run()
