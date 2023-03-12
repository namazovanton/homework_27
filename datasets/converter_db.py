import csv
import json


def csv_to_json(csv_file, json_file, model):
    result = []
    with open(csv_file, encoding='utf-8') as csv_f:
        for row in csv.DictReader(csv_f):
            del row["id"]
            if "price" in row:
                row["price"] = int(row["price"])
            if "is_published" in row:
                if "is_published" == "TRUE":
                    row["is_published"] = True
                else:
                    row["is_published"] = False
            result.append({"model": model, "fields": row})

    with open(json_file, 'w', encoding='utf-8') as json_f:
        json_f.write(json.dumps(result, ensure_ascii=False))


csv_to_json("categories.csv", "categories.json", "ads.category")
csv_to_json("ads.csv", "ads.json", "ads.ad")
