from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to My Flask App!</h1><p>This is a simple Flask web page.</p>"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8060)
    