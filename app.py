from flask import Flask, render_template, url_for, request
import requests
import json

app = Flask(__name__)

 

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")



@app.route('/result',methods=['POST', 'GET'])
def result():
    output = request.form.to_dict()
    name = output["name"]
    time_period = output["time"]

    url = "https://graph.facebook.com/v15.0//messages"

    headers = {
        'Authorization': '',
        'Content-Type': 'application/json'
    }

    payload = json.dumps({
      "messaging_product": "whatsapp",
      "to": "918983450203",
      "type": "template",
      "template": {
        "name": "promotional_2",
        "language": {
          "code": "en_US"
        },
        "components": [
            {
                "type": "header",
                "parameters": [
                    {
                        "type": "image",
                        "image": {
                            "id": "565692778524662"
                            }
                        }   
                    ]
                }
            ]
      }
    })
    requests.request("POST", url, headers=headers, data=payload)
    
        
    return render_template('index.html', name = name)
    




if __name__ == "__main__":
    app.run(debug=True)
