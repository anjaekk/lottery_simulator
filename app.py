from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/check')
def check():
    return render_template('check.html')




if __name__ == '__main__':
    # 서버실행
    app.run(host='0.0.0.0', debug=True)
    