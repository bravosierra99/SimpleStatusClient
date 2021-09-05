import SimpleStatusClient as api
from models import Colors
from time import sleep

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
    }
}

statuses_base = {
    1: {
        "message": "one is great",
        "color": Colors.green
    },
    2: {
        "message": "two is eh",
        "color": Colors.yellow
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
    }
}

client = api.APIClient("http://127.0.0.1:80/api")

for key, config in configs.items():
    response = client.set_config_base(key, **config)
    print(response.content)


sleep(1)

for key, status in statuses_base.items():
    response = client.set_status_base(key, **status)
    print(response.content)


sleep(1)

for _, config in configs.items():
    try:
        config.pop("parent_key")
    except:
        pass
    response = client.set_config(**(config))
    print(response.content)


sleep(1)

for name, status in statuses.items():
    response = client.set_status(name=name, **status)
    print(response.content)
