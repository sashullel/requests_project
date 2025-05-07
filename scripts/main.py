import logging
import random
import requests
from http import HTTPStatus

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def make_request(status_code) -> None:
    """
    Makes an HTTP request to httpstat.us for the status code given

    Args:
        status_code (int): The HTTP status code of the response
    """
    url = f'https://httpstat.us/{status_code}'

    try:
        response = requests.get(url)
        response.raise_for_status()
        logging.info(f'Request to {url} was successful')
        logging.info(f'Response body: {response.text}')

    except requests.exceptions.HTTPError as e:
        logging.error(f'Request to {url} failed')
        raise Exception(f'HTTP error occured: {e}')

    except requests.exceptions.RequestException as e:
        logging.error(f'Request to {url} failed')
        raise Exception(f'An error occured: {e}') 


if __name__ == '__main__':
    status_codes = random.sample([status.value for status in HTTPStatus], 5)
    print(f'The status codes to be tested: {status_codes}')

    for code in status_codes:
        try:
            make_request(code)
        except Exception as e:
            logging.error(e)
