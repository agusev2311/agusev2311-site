from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Цветовой фильтр вращающегося фона
BACKGROUND_TINT = "hue-rotate(260deg) saturate(250%) brightness(1.2)"


@app.route("/")
def index():
    return render_template("index.html", tint=BACKGROUND_TINT)

@app.route("/beams.webp")
def index():
    return send_from_directory('beams.webp', "/static")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2311)
