import json

apps = {
    "App1":{"name":"TEste", "Commands":["cd ..", "python teste.py"]},
    "App2": {"name":"TEste", "Commands":["cd ..", "python teste.py"]}
}


with open("x.json", "w") as file:
        json.dump(apps, file, indent=4)