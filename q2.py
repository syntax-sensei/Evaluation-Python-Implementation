import json


def analyze():
    try:
        with open("sales.json", "r") as sale:
            item = json.load(sale)

        with open("report.txt", "w") as sale:
            for i in item:
                tot = i["price"] * i["qty"]
                sale.write(f"{i['item']} -> {tot}\n")  # Pen → ₹100

    except Exception as e:
        print(e)


analyze()
