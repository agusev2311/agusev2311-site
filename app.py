from flask import Flask, render_template

app = Flask(__name__)

# Цветовой фильтр вращающегося фона
BACKGROUND_TINT = "hue-rotate(260deg) saturate(250%) brightness(1.2)"


@app.route("/")
def index():
    return render_template("index.html", tint=BACKGROUND_TINT)

if __name__ == "__main__":
    app.run(debug=True)