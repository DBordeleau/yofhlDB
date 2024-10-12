import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from helpers import apology

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///hockey.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET"])
def index():
        stats = db.execute("SELECT * FROM Stats ORDER BY FPTS DESC LIMIT 100")
        return render_template("index.html", stats=stats)

@app.route("/top100", methods=["GET"])
def top100():
        career_stats = db.execute("SELECT ID, Player, Position, SUM(FPTS) FROM Stats GROUP BY ID ORDER BY SUM(FPTS) DESC LIMIT 100")
        return render_template("top100.html", career_stats=career_stats)

@app.route("/andromeda", methods=["GET"])
def andromeda():
        andromeda_stats = db.execute("SELECT ID, Player, Position, SUM(FPTS) from Stats WHERE YOFHLTeam LIKE '%ASI%' GROUP BY ID ORDER BY SUM(FPTS) DESC LIMIT 10")
        return render_template("andromeda.html", andromeda_stats=andromeda_stats)

@app.route("/carolina", methods=["GET"])
def carolina():
        carolina_stats = db.execute("SELECT ID, Player, Position, SUM(FPTS) from Stats WHERE YOFHLTeam LIKE '%REAPER%' OR YOFHLTeam LIKE '%WTURR%' GROUP BY ID ORDER BY SUM(FPTS) DESC LIMIT 10")
        return render_template("carolina.html", carolina_stats=carolina_stats)

@app.route("/hamhung", methods=["GET"])
def hamhung():
        hamhung_stats = db.execute("SELECT ID, Player, Position, SUM(FPTS) from Stats WHERE YOFHLTeam LIKE '%HUNG%' OR YOFHLTeam LIKE '%MEAT%' OR YOFHLTeam LIKE '%JUBA%' GROUP BY ID ORDER BY SUM(FPTS) DESC LIMIT 10")
        return render_template("hamhung.html", hamhung_stats=hamhung_stats)

@app.route("/hooterville", methods=["GET"])
def hooterville():
        hooterville_stats = db.execute("SELECT ID, Player, Position, SUM(FPTS) from Stats WHERE YOFHLTeam LIKE '%HH%' OR YOFHLTeam LIKE '%STEG%' OR YOFHLTeam LIKE '%STEC%' GROUP BY ID ORDER BY SUM(FPTS) DESC LIMIT 10")
        return render_template("hooterville.html", hooterville_stats=hooterville_stats)

@app.route("/johnny", methods=["GET"])
def johnny():
        johnny_stats = db.execute("SELECT ID, Player, Position, SUM(FPTS) from Stats WHERE YOFHLTeam LIKE '%JTPJ%' GROUP BY ID ORDER BY SUM(FPTS) DESC LIMIT 10")
        return render_template("johnny.html", johnny_stats=johnny_stats)

@app.route("/jagrtown", methods=["GET"])
def jagrtown():
        jagr_stats = db.execute("SELECT ID, Player, Position, SUM(FPTS) from Stats WHERE YOFHLTeam LIKE '%JAGR%' GROUP BY ID ORDER BY SUM(FPTS) DESC LIMIT 10")
        return render_template("jagrtown.html", jagr_stats=jagr_stats)

@app.route("/lalibirdies", methods=["GET"])
def lalibirdies():
        lalibirdies_stats = db.execute("SELECT ID, Player, Position, SUM(FPTS) from Stats WHERE YOFHLTeam LIKE '%LALI%' GROUP BY ID ORDER BY SUM(FPTS) DESC LIMIT 10")
        return render_template("lalibirdies.html", lalibirdies_stats=lalibirdies_stats)

@app.route("/montreal", methods=["GET"])
def montreal():
        montreal_stats = db.execute("SELECT ID, Player, Position, SUM(FPTS) from Stats WHERE YOFHLTeam LIKE '%NFLD%' GROUP BY ID ORDER BY SUM(FPTS) DESC LIMIT 10")
        return render_template("montreal.html", montreal_stats=montreal_stats)

@app.route("/npd", methods=["GET"])
def npd():
        npd_stats = db.execute("SELECT ID, Player, Position, SUM(FPTS) from Stats WHERE YOFHLTeam LIKE '%NPD%' GROUP BY ID ORDER BY SUM(FPTS) DESC LIMIT 10")
        return render_template("npd.html", npd_stats=npd_stats)

@app.route("/nkn", methods=["GET"])
def nkn():
        nkn_stats = db.execute("SELECT ID, Player, Position, SUM(FPTS) from Stats WHERE YOFHLTeam LIKE '%NKN%' OR YOFHLTeam LIKE '%MAC%' OR YOFHLTeam LIKE '%DGWY%' GROUP BY ID ORDER BY SUM(FPTS) DESC LIMIT 10")
        return render_template("nkn.html", nkn_stats=nkn_stats)

@app.route("/paddyville", methods=["GET"])
def paddyville():
        paddyville_stats = db.execute("SELECT ID, Player, Position, SUM(FPTS) from Stats WHERE YOFHLTeam LIKE '%PVLS%' OR YOFHLTeam LIKE '%HCHH%' GROUP BY ID ORDER BY SUM(FPTS) DESC LIMIT 10")
        return render_template("paddyville.html", paddyville_stats=paddyville_stats)

@app.route("/skellige", methods=["GET"])
def skellige():
        skellige_stats = db.execute("SELECT ID, Player, Position, SUM(FPTS) from Stats WHERE YOFHLTeam LIKE '%SKGS%' OR YOFHLTeam LIKE '%SEED%' GROUP BY ID ORDER BY SUM(FPTS) DESC LIMIT 10")
        return render_template("skellige.html", skellige_stats=skellige_stats)

@app.route("/varrock", methods=["GET"])
def varrock():
        varrock_stats = db.execute("SELECT ID, Player, Position, SUM(FPTS) from Stats WHERE YOFHLTeam LIKE '%VWIZ%' GROUP BY ID ORDER BY SUM(FPTS) DESC LIMIT 10")
        return render_template("varrock.html", varrock_stats=varrock_stats)

@app.route("/texas", methods=["GET"])
def texas():
        texas_stats = db.execute("SELECT ID, Player, Position, SUM(FPTS) from Stats WHERE YOFHLTeam LIKE '%TEEHAW%' OR YOFHLTeam LIKE '%ORCA%' OR YOFHLTeam LIKE '%WWE%' GROUP BY ID ORDER BY SUM(FPTS) DESC LIMIT 10")
        return render_template("texas.html", texas_stats=texas_stats)

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("player"):
            return apology("must enter player name", 400)

        else:
            player_name = request.form.get("player")
            player_stats = db.execute("SELECT Player, NHLTeam, Position, SeasonRank, YOFHLTeam, FPTS, FPG, Year FROM stats WHERE Player LIKE ? ORDER BY Year", (f'%{player_name}%'))
            return render_template("searched.html", player_stats=player_stats)
    else:
        return render_template("search.html")