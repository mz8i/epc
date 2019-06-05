from epc_ingest.fetch_data import fetch_all_pages_as_dataframe

API_URL = 'https://epc.opendatacommunities.org/api/v1/domestic'
API_SEARCH_URL = API_URL + '/search'


def search(local_authority_code=None, constituency_code=None, property_type=None, energy_band=None):
    url = API_SEARCH_URL

    params = {}
    if local_authority_code is not None:
        params['local-authority'] = local_authority_code
    if constituency_code is not None:
        params['constituency'] = constituency_code
    if property_type is not None:
        params['property-type'] = property_type
    if energy_band is not None:
        params['energy-band'] = energy_band

    return fetch_all_pages_as_dataframe(url, params)
