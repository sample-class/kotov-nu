from flask import Flask, render_template
from data import title, subtitle, description, departures, tours

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title=title, subtitle=subtitle, description=description, tours=tours, departures=departures)


@app.route('/direction/<direction>')
def direction(direction):
    suitable_tours = selection_tours_by_dir(direction)
    return render_template('direction.html', title=title, subtitle=subtitle, description=description,
                           tours=tours, direction=direction, departures=departures, suitable_tours=suitable_tours)


@app.route('/tour/<int:id>')
def tour(id):
    return render_template('tour.html', title=title, subtitle=subtitle, tour=tours[id], departures=departures, id=id)


def selection_tours_by_dir(direction):
    suitable_tours = []
    for i, tour in tours.items():
        if tour['departure'] == direction:
            suitable_tours.append(tour)
    return suitable_tours


if __name__ == '__main__':
    app.run()
