from urllib.parse import urlencode
from .json_request import json_request


def pd_gen_url(
        endpoint,
        service_key='xndt9aE0vWNU2zQcWp8iBPms%2BTgWggyBYGwQkxs47RHcSdy12U%2FpUDZ7dS4TT33OLafiai%2By6fiCNqdkEwnkWA%3D%3D',
        # service_key='%2FfZdR%2Bue1CSxLEnMkZXa9iDYontLTMTIteD5%2BzYCiMYpDKUZNUh2FHGDQ04zazSEmLl34FClDQk8a7flFCIQKA%3D%3D',
        **params):
    return '%s?serviceKey=%s&%s' % (endpoint, service_key, urlencode(params))


def pd_fetch_foreign_visitor(country_code=0, year=0, month=0, service_key=''):
    pass


def pd_fetch_tourspot_visitor(
        district1='',
        district2='',
        tourspot='',
        year=0,
        month=0):
    gen_url = pd_gen_url(
        endpoint='http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList',
        YM='{0:04d}{1:02d}'.format(year, month),
        SIDO=district1,
        GUNGU=district2,
        RES_NM=tourspot,
        _type='json')
    json_response = json_request(gen_url)
    result_msg = json_response\
        .get('response')\
        .get('header')\
        .get('resultMsg')

    return json_response\
        .get('response')\
        .get('body')\
        .get('items')\
        .get('item') if result_msg == 'OK' else []
