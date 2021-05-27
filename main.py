
from blabel import LabelWriter
import pandas as pd


df = pd.read_excel("input.xlsx")
print("Generating Price Lables")
label_writer = LabelWriter("template.html",items_per_page=24,
                           default_stylesheets=("template.css",))
i=0
records = []
for item in df["Name"]:
    num = df['EAN/Barcode Number'][i]
    name = df['Name'][i]
    price = df['Price'][i]
    records.append(
    dict(sample_id=num, sample_name=name, sample_price="{:.2f}".format(price))
    )
    i = i + 1

label_writer.write_labels(records, target='price_lables.pdf')
print("Completed Generating Price Lables.Check Folder. File Name is 'price_lables.pdf'")