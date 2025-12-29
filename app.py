from flask import Flask, render_template, request, session, redirect, url_for
from game import create_game
import random

app = Flask(__name__)
app.secret_key = "dev-secret"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        players = int(request.form["players"])
        difficulty = int(request.form["difficulty"])
        mode = request.form.get("mode", "classic")

        game = create_game(players, difficulty, mode)
        game["current_player"] = 0
        game["state"] = "blank"
        session["game"] = game

        return redirect(url_for("player_turn"))

    return render_template("index.html")

@app.route("/player_turn", methods=["GET", "POST"])
def player_turn():
    game = session.get("game")
    if not game:
        return redirect(url_for("index"))

    current = game["current_player"]
    if current >= game["players"]:
        return redirect(url_for("final"))

    if request.method == "POST":
        game["state"] = "reveal"
        session["game"] = game
        return redirect(url_for("player_turn"))

    show_word = game["state"] == "reveal"
    role = game["roles"][current] if show_word else None
    is_imposter = current in game["imposters"]

    message = None
    if show_word:
        if game["mode"] == "imposter_no_word" and role is None:
            message = "You are the imposter!"
        elif game["mode"] == "question":
            message = f"Your question: {role}"
        else:
            message = f"Your word: {role}"

    return render_template(
        "reveal.html",
        player_num=current + 1,
        show_word=show_word,
        message=message
    )

@app.route("/next_player")
def next_player():
    game = session.get("game")
    if not game:
        return redirect(url_for("index"))

    game["current_player"] += 1
    game["state"] = "blank"

    # After last player, pick a random final player
    if game["current_player"] >= game["players"]:
        game["final_random_player"] = random.randint(1, game["players"])
        game["imposters_revealed"] = False
        session["game"] = game
        return redirect(url_for("final"))

    session["game"] = game
    return redirect(url_for("player_turn"))

@app.route("/reveal_imposters")
def reveal_imposters():
    game = session.get("game")
    if not game:
        return redirect(url_for("index"))

    game["imposters_revealed"] = True
    session["game"] = game
    return redirect(url_for("final"))

@app.route("/final")
def final():
    game = session.get("game")
    if not game:
        return redirect(url_for("index"))

    return render_template("final.html", game=game)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)








