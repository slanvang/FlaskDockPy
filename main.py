from flask import Flask
#Flask Main assign
app = Flask(__name__)
#any root web access
@app.route('/')
def hello():
    return 'Hello, World! From Flask to Docker'

#main function
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
