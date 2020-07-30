from flask import Flask
app = Flask(__name__)

def sum(a,b):
	return a+b

@app.route("/")
def hello():
	res = sum(3,2)
	return "Hello world %s" % (res)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)
