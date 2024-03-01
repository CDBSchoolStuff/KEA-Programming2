from flask import Flask, render_template
import base64
from io import BytesIO
from matplotlib.figure import Figure

app = Flask(__name__)


def stue_temp():
    # Generate the figure **without using pyplot**.
    fig = Figure()
    ax = fig.subplots()
    ax.plot([1, 2])
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return data

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/stue')
def stue():
    stue_temperature = stue_temp()
    return render_template('stue.html', stue_temperature = stue_temperature)

app.run(debug=True)