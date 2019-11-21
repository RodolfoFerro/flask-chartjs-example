from flask import Flask
from flask import render_template
import numpy as np


app = Flask(__name__)


@app.route('/')
def main():
	"""Main URL to test Chart.js"""

	n, bins = 10000, 20
	normal = np.random.normal(0, 1, n)
	gumbel = np.random.gumbel(0, 1, n)
	weibull = np.random.weibull(5, n)
	nhistogram = np.histogram(normal, bins=bins)
	ghistogram = np.histogram(gumbel, bins=bins)
	whistogram = np.histogram(weibull, bins=bins)

	return render_template('main.html',
							nvalues=nhistogram[0].tolist(),
							nlabels=nhistogram[1].tolist(),
							ncolor='rgba(50, 115, 220, 0.4)',
							gvalues=ghistogram[0].tolist(),
							glabels=ghistogram[1].tolist(),
							gcolor='rgba(0, 205, 175, 0.4)',
							wvalues=whistogram[0].tolist(),
							wlabels=whistogram[1].tolist(),
							wcolor='rgba(255, 56, 96, 0.4)')


if __name__ == "__main__":
	app.run(port=5000, debug=True)