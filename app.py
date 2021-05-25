from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route("/eda")
def eda():
    return render_template('eda.html')

if __name__ == '__main__':
    app.run(debug=True)