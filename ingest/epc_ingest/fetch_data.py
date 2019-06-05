import io
import math
import os
import sys

from dotenv import load_dotenv
import pandas as pd
import requests

load_dotenv()

# https://epc.opendatacommunities.org/docs/api/domestic#domestic-pagination
API_RESULT_LIMIT = 10000
API_PAGE_SIZE_LIMIT = 5000


def get_api_credentials():
    user = os.getenv('EPC_API_USER')
    key = os.getenv('EPC_API_KEY')
    if user is None:
        raise ValueError('EPC_API_USER env var not set')
    if key is None:
        raise ValueError('EPC_API_KEY env var not set')

    return user, key


def count_csv_data_rows(csv_text):
    return csv_text.count('\n')


def fetch_csv(url, params):
    response = requests.get(url, params, auth=get_api_credentials(), headers = {'Accept': 'text/csv'})
    # TODO: add handling of unsuccessful responses
    return response.text


def fetch_page(url, params, page_size, page_from):
    page_params = dict(params)
    page_params['size'] = page_size
    page_params['from'] = page_from

    return fetch_csv(url, page_params)


def fetch_all_pages_as_dataframe(url, params, max_page_size=API_PAGE_SIZE_LIMIT, max_total_results=API_RESULT_LIMIT):
    result = None
    result_rows = 0

    for page_from in range(0, max_total_results, max_page_size):
        page_csv = fetch_page(url, params, max_page_size, page_from)
        page_result = pd.read_csv(io.StringIO(page_csv))
        result = pd.concat([result, page_result])
        result_rows += page_result.shape[0]
        
        if result_rows >= max_total_results:
            sys.stderr.write('Warning: max number of result rows reached ({})'.format(max_total_results))
            break

    return result