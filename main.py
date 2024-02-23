from flask import Flask
app = Flask(__name__)
@app.route('/', methods=['GET'])
def hello():
    print("I am inside hello world")
    return 'Hello World! I can make change at route: /change'

if __name__ == '__main__':
    app.run( host='0.0.0.0', port=5000, debug=True)