import requests

from philips_hue_hooks.action.action import Action


class WebHookAction(Action):
    def __init__(self, post_url):
        self.post_url = post_url

    def __str__(self):
        return f'WebHook at {self.post_url}'

    def invoke(self, device_class, device_id, device_name, device_type, new_state):
        requests.post(self.post_url, json={
            'class': device_class,
            'id': device_id,
            'name': device_name,
            'type': device_type,
            'state': new_state
        })
