from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask on AWS EC2!"

@app.route('/second')
def second():
    return "This is the second route!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
p r i n t ( ' G i t H u b   A c t i o n s   D e p l o y m e n t   T e s t ' )  
 