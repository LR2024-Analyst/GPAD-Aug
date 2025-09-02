from flask import Flask, render_template
from data.data_processing import load_data
from visualizations.plots import create_visualizations

app = Flask(__name__)

@app.route('/')
def home():
    data = load_data()
    visualizations = create_visualizations(data)
    return render_template('dashboard.html', visualizations=visualizations)

if __name__ == '__main__':
    app.run(debug=True)