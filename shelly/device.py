
import requests
from pprint import pprint
from typing import Dict


class Device:

    def __init__(self, **kwds) -> None:
        self._ip = kwds['ip']
        self._api_state = {}

    @property
    def ip(self) -> str:
        return self._ip

    @property
    def api_state(self) -> Dict[str, str]:
        return self._api_state

    def api_get(self, query: str) -> Dict[str, str]:
        url = f'http://{self.ip}/{query}'
        
        print(f'GET: {url}')
        response = requests.get(url)
        print(f'STATUS: {response.status_code}')
        pprint(response.json(), indent=4)

        return response.json()

    def api_post(self, query: str, data: Dict[str, str]) -> Dict[str, str]:
        url = f'http://{self.ip}/{query}'
        
        print(f'POST: {url}')
        pprint(data, indent=4)
        response = requests.post(url, params=data)
        print(f'STATUS: {response.status_code}')
        pprint(response.json(), indent=4)

        return response.json()

    def reload(self) -> None:
        self._api_state = {}
        self.api_state['shelly'] = self.api_get('shelly')
