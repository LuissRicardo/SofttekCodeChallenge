from flask import Flask, jsonify

from database import setup
from database.queries import get_customer_order_status_list, get_detecting_change_list, get_seasons_orders_list

app = Flask(__name__)

# Initializes the DB
setup.setup_database()


# API ROUTES

@app.route("/api/customer_order_status", methods=["GET"])
def customer_order_status():
    try:
        data = get_customer_order_status_list()
        return jsonify(data=data,
                       message=f"{len(data)} status orders retrieved.",
                       status=200, category="success")
    except:
        return jsonify(status=500, category="server error")


@app.route("/api/detecting_change", methods=["GET"])
def detecting_change():
    try:
        data = get_detecting_change_list()
        return jsonify(data=data,
                       message=f"{len(data)} weather changes detected.",
                       status=200, category="success")
    except:
        return jsonify(status=500, category="server error")


@app.route("/api/orders_by_season", methods=["GET"])
def season_orders():
    try:
        data = get_seasons_orders_list()
        return jsonify(data=data,
                       message=f"{len(data)} orders retrieved.",
                       status=200, category="success")
    except:
        return jsonify(status=500, category="server error")


if __name__ == '__main__':
    app.run()
