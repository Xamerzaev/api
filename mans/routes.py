from flask import Flask, render_template, jsonify, request
from mans.models import *
from mans import app

@app.route("/")
def index():
    shops = Shop.query.all()
    return render_template("index.html", shops=shops)


@app.route("/text", methods=["POST"])
def text():
    """Отзывы"""
    name = request.form.get("name")
    try:
        shop_id = int(request.form.get("shop_id"))
    except ValueError:
        return render_template("error.html", message="Не существующицй ИД")

    shop = Shop.query.get(shop_id)
    if not shop:
        return render_template("error.html", message="Такого магазина не существует")
    shop.add_text(name)
    return render_template("success.html")


@app.route("/shops")
def shops():
    """Магазины"""
    shops = Shop.query.all()
    return render_template("shops.html", shops=shops)

@app.route("/shops/<int:shop_id>")
def shop(shop_id):
    """Магазины"""

    shop = Shop.query.get(shop_id)
    if shop is None:
        return render_template("error.html", message="Магазин не найден")

    texts = shop.texts
    return render_template("shops.html", shop=shop, texts=texts)


@app.route("/api/shops/<int:shop_id>")
def shop_api(shop_id):
    """Отзывы Магазина"""

    shop = Shop.query.get(shop_id)
    if shop is None:
        return jsonify({"error": "Не правильный ИД"}), 422

    texts = shop.texts
    names = []
    for text in texts:
        names.append(text.name)
    return jsonify({
            "Магазин": shop.name,
            "Отзывы": names
        })