from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

num = random.randint(1, 100)
guesses = [0]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    global num, guesses
    user_guess = int(request.form['guess'])

    if user_guess < 1 or user_guess > 100:
        return jsonify(feedback='Out of Bounds, Try again')

    if user_guess == num:
        feedback = f'Congratulations, You have guessed correctly in only {len(guesses)} guesses'
        num = random.randint(1, 100) 
        guesses = [0]
        return jsonify(feedback=feedback)

    guesses.append(user_guess)

    if guesses[-2]:
        if abs(num - user_guess) < abs(num - guesses[-2]):
            feedback = 'Warmer'
        else:
            feedback = 'Colder'
    else:
        if abs(num - user_guess) <= 10:
            feedback = 'Warm'
        else:
            feedback = 'Cold'

    return jsonify(feedback=feedback)

if __name__ == '__main__':
    app.run(debug=True)
