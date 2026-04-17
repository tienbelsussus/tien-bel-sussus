from flask import Flask, jsonify

app = Flask(__name__)


# hàm kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):  # chỉ cần tới sqrt(n)
        if n % i == 0:
            return False

    return True


# route API
@app.route("/prime_number/<int:number>")
def check_prime(number):
    result = {
        "Number": number,
        "isPrime": is_prime(number)
    }
    return jsonify(result)


# chạy server
if __name__ == "__main__":
    app.run(debug=True)