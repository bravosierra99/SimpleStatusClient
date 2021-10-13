from simple_status_client import Client
from simple_status_client import Colors

configs = {
    1: {
        "name": "component one",
        "parent_key": 0,
        "details": "details for one",
        "timeout_min": 120,
        "timeout_color": Colors.red
    },
    2: {
        "name": "component two",
        "details": "details for two",
        "timeout_min": 600,
        "timeout_color": Colors.yellow
    },
    11:{
        "name": "component one one",
        "details": "details for one one",
        "timeout_min": 600,
        "timeout_color": Colors.yellow,
        "parent_name": "component one"
    },
    12: {
        "name": "component one two",
        "details": "details for one two",
        "timeout_min": 600,
        "timeout_color": Colors.yellow,
        "parent_name": "component one"
    },

    121: {
        "name": "component one two one",
        "details": "details for one two one",
        "timeout_min": 600,
        "timeout_color": Colors.yellow,
        "parent_name": "component one two"
    }
}

statuses = {
    "component one": {
        "message": "one is great",
        "color": Colors.green
    },
    "component two": {
        "message": "two is eh",
        "color": Colors.yellow
    },
    "component one one": {
        "message": "one one is great",
        "color": Colors.green
    },
    "component one two": {
        "message": "one two is bleh",
        "color": Colors.red
    },
    "component one two one": {
        "message": "one two one is great",
        "color": Colors.green
    },
}


client = Client("http://127.0.0.1:80/api")

for _, config in configs.items():
    try:
        config.pop("parent_key")
    except:
        pass
    response = client.set_config(**(config))
    print(response.content)

for name, status in statuses.items():
    response = client.set_status(name=name, **status)
    print(response.content)
