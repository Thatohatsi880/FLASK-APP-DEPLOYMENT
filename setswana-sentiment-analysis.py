from flask import Flask

app = Flask("SetswanaSentimentAnalysisApp")

@app.route('/', methods=['GET'])
def welcome():
    return "<h1>Hello world</h1>"

if __name__ == '__main__':
    app.run()
