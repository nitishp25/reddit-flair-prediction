from flask import Flask, render_template, request
import prediction
app = Flask(__name__)

# homepage
@app.route('/')
def index():
    return render_template('index.html')

# result page
@app.route('/',methods = ['POST'])
def pred():
    if request.method == 'POST':
        url = request.form['url']
        data = prediction.predict(url)
        return render_template('index2.html', data=data)  
    else:
        return 

# analysis page
@app.route('/analysis', methods=['POST'])
def analysis():
    return render_template('analysis.html')
        
if __name__ == '__main__':
    app.run(debug = False)
