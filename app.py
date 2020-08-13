from flask import Flask, render_template, request
import weather.api as api
import config
import constants

app = Flask(__name__)
config.get_configuration_file()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/search', methods=["POST"])
def search():
    try:
        country = request.form['country']
        region = request.form['region']
        city = request.form['city']
        res = api.daily_forecast(country, region, city).get_data()
        return render_template('result_view.html', **res)
    except Exception:
        return '', 500


if __name__ == '__main__':
    app.run()
