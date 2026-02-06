from flask import Flask, render_template, request
import os

app = Flask(__name__)

ALLOWED_BETS = list(range(5, 51, 5))

API_BASE_URL = "https://api.soccerapi.example"  # Placeholder for the Soccer API trial
API_KEY = os.getenv("SOCCER_API_KEY", "")

SAMPLE_MATCHES = [
    {
        "group": "Group A",
        "kickoff": "Sat, Jun 14 - 7:00 PM",
        "home": "Rivergate FC",
        "away": "Northbridge United",
        "odds": {"home": 1.8, "draw": 3.2, "away": 2.4},
    },
    {
        "group": "Group B",
        "kickoff": "Sun, Jun 15 - 4:30 PM",
        "home": "Marina City",
        "away": "Red Coast",
        "odds": {"home": 2.1, "draw": 3.0, "away": 2.9},
    },
    {
        "group": "Group C",
        "kickoff": "Mon, Jun 16 - 1:00 PM",
        "home": "Highland Rovers",
        "away": "Atlas Sporting",
        "odds": {"home": 1.6, "draw": 3.5, "away": 4.1},
    },
]

SAMPLE_BETS = [
    {
        "match": "Rivergate FC vs Northbridge United",
        "pick": "Rivergate FC to win",
        "stake": 25,
        "return": 45.0,
        "status": "Open",
    },
    {
        "match": "Marina City vs Red Coast",
        "pick": "Draw",
        "stake": 15,
        "return": 45.0,
        "status": "Open",
    },
    {
        "match": "Highland Rovers vs Atlas Sporting",
        "pick": "Atlas Sporting to win",
        "stake": 10,
        "return": 41.0,
        "status": "Open",
    },
]


def get_matches():
    """Placeholder for Soccer API integration.

    When the API key is available, swap SAMPLE_MATCHES with a cached
    fetch using API_BASE_URL and SOCCER_API_KEY.
    """

    return SAMPLE_MATCHES


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

    matches = get_matches()
    api_ready = bool(API_KEY)

    return render_template(
        "index.html",
        allowed_bets=ALLOWED_BETS,
        selected=selected,
        message=message,
        matches=matches,
        sample_bets=SAMPLE_BETS,
        api_ready=api_ready,
    )


if __name__ == "__main__":
    app.run(debug=True)
