import SimpleStatusAPI as api
from models import Colors

configs = {
    1:{
      "name":"component one"  ,
      "parent_key":0,
        "details":"details for one",
        "timeout_min":120,
        "timeout_color": Colors.red
    },
    2: {
        "name": "component two",
        "details": "details for two",
        "timeout_min": 600,
        "timeout_color": Colors.yellow
    }
}

statuses = {
    1: {
        "message": "one is great",
        "color": Colors.green
    },
    2: {
        "message": "two is eh",
        "color": Colors.yellow
    }
}

client = api.APIClient("http://127.0.0.1:8001")

for key, config in configs.items():
    response = client.set_config(key,**config)
    print(response.content)

for key, status in statuses.items():
    response = client.set_status(key,**status)
    print(response.content)