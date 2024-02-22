from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    print("I am inside hello world")
    return 'Hello World! I can make change at route: /change'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)