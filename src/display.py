"""
    This file will be used to display cards on screen

    Note: 
      The code here was written only for experimentation.
      Don't modify it for now!

"""


from rich.console import Console
from rich.table import Table
from rich.layout import Layout
import json

console = Console()
layout = Layout()
layout.split_row(Layout(name="cards"),
                 Layout(name="secret", size=30))


with open("Data/cards.json") as file:
    cards_data = json.load(file)

tables = []
layouts = []
name = "0"
layouts.append(Layout(name=name))
for i, card in enumerate(cards_data):
    table = Table(title=card["name"], title_style="bold")
    table.add_column("Attribute", justify="left", style="cyan")
    table.add_column("Value", justify="center", style="magenta", no_wrap=False)

    for key, val in list(card.items())[1:]:
        if key in ("has", "color"):
            for k, v in card[key].items():
                if v:
                    table.add_row(k.title(), str(v).title())
            continue
        if val:
            table.add_row(key.title(), str(val).title())

    if i % 6 == 0 and i > 0:
        layouts[-1].split_row(*tables)
        
        name = f"{i}"
        tables = []
        layouts.append(Layout(name=name))
        
    tables.append(table)

layouts[-1].split_row(*tables)
layout.get("cards").split_column(*layouts)
layout.get("secret").split_column(table)

console.print(layout)
input()
