import json
from datetime import datetime

import requests
import yarl

from models import Colors, ConfigIn, StatusIn


class APIClient():

    def __init__(self, url):
        self.url = yarl.URL(url)
        response = requests.get(url=self.url / "ping")
        assert b"pong" in response.content

    def set_config(self,
                   component_key: int,
                   name: str,
                   details: str,
                   timeout_min: int,
                   timeout_color: Colors,
                   parent_key: int = 0,
                   ):
        """
        This method will set a config for a given a component using it's component_key to identify it.  The
        component_key must be unique, an easy way to do this is to pick a unqiue name and hash it
        :param component_key: a unique identifier for your component, non unique values will result in overwriting
        the config
        :param name: The name of your component
        :param parent_key: a key for your parent component, results in your
        :param details: Any further information about your component you wish to convey
        :param timeout_min: the number of minutes your status should remain valid for
        :param timeout_color: the color your status should change to once it times out, will never "improve" the
        color of your status
        :return:
        """
        config = ConfigIn(name=name, parent_key=parent_key, details=details, timeout_min=timeout_min,
                             timeout_color=timeout_color)
        url = self.url / "components" / str(component_key) / "config"
        response = self.send_it(config, url)
        return response

    def set_status(self,
                   component_key: int,
                   color: Colors,
                   message: str,
                    date: datetime = datetime.now(),
                   ):
        status = StatusIn(color=color, date=date, message=message)
        url = self.url / "components" / str(component_key) / "status"
        response = self.send_it(status, url)
        return response

    def send_it(self, post_content, url):
        response = requests.post(url, json=json.loads(post_content.json()))
        if response.status_code != 200:
            raise Exception(response.content)
        return response
