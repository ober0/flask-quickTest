from flask import Flask, redirect, render_template, request, url_for, jsonify

app = Flask(__name__)

count = 0
correctAnswer = {
    '1': '81',
    '2': '12',
    '3': '12',
    '4': '6',
    '5': '6',
    '6': '56',
    '7': '7',
    '8': '25',
    '9': '8',
    '10': '90',
    '11': '11',
    '12': '25',
    '13': '12',
    '14': '180',
    '15': '36',
    '16': '9',
    '17': '16',
    '18': '25',
    '19': '8',
    '20': '81'
}

@app.route('/')
def index():
    global count
    count = 0

    return render_template('index.html')


@app.route('/checkAnswer', methods=['POST'])
def checkAnswer():
    if request.method == 'POST':
        global count
        questNum = request.json['questNum']
        questValue = request.json['questValue']

        try:
            if int(questValue) == int(correctAnswer[str(questNum)]):
                count += 1
                return jsonify({
                    'result': True,
                    'correctAnswer': True
                })
            else:
                return jsonify({
                    'result': True,
                    'correctAnswer': False
                })
        except Exception as e:
            return jsonify({
                'result': False,
                'correctAnswer': False,
                'message': e
            })
    return jsonify({
        'result': False,
        'correctAnswer': False,
        'message': 'Ошибка доступа'
    })


@app.route('/result')
def result():
    global count
    _all = 20
    procent = f'{int(count / _all * 100)}%'
    return render_template('result.html', correct=count, procent=procent, all=_all)



if __name__ == '__main__':
    app.run(debug=True)
