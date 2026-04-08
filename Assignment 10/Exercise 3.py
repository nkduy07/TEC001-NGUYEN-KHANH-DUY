from flask import Flask

app = Flask(__name__)

def check_if_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

@app.route('/prime_number/<number>')
def main(number):
    num = int(number)
    status = check_if_prime(num)
    return {"Number": num, "isPrime": status}

app.run(debug=True)