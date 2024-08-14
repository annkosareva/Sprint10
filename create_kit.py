import configuration
import requests
import data


def create_kit(body):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                         headers=data.headers,
                         json=body)


