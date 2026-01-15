from flask import Flask, render_template, request

app = Flask(__name__)

ALLOWED_BETS = list(range(5, 51, 5))


@app.route("/", methods=["GET", "POST"])
def index():
    selected = None
    message = None

    if request.method == "POST":
        try:
            selected = int(request.form.get("bet", "0"))
        except ValueError:
            selected = 0

        if selected in ALLOWED_BETS:
            message = f"Bet placed: ${selected}"
        else:
            message = "Invalid bet amount."
            selected = None

    return render_template(
        "index.html",
        allowed_bets=ALLOWED_BETS,
        selected=selected,
        message=message,
    )


if __name__ == "__main__":
    app.run(debug=True)