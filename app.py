from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>مرحباً سالم</h1><p>موقع إدارة المصروفات يعمل بنجاح!</p>"

app.run()
