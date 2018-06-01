from urllib.parse import urlencode
from .json_request import json_request
from itertools import count


def pd_gen_url(
        endpoint,
        service_key='%2FfZdR%2Bue1CSxLEnMkZXa9iDYontLTMTIteD5%2BzYCiMYpDKUZNUh2FHGDQ04zazSEmLl34FClDQk8a7flFCIQKA%3D%3D',
        **params):
    return '%s?serviceKey=%s&%s' % (endpoint, service_key, urlencode(params))


def pd_fetch_foreign_visitor(country_code=0, year=0, month=0):
    gen_url = pd_gen_url(endpoint='http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList',
                         YM='{0:04d}{1:02d}'.format(year, month),
                         NAT_CD=country_code,
                         _type='json',
                         ED_CD='E')

    json_response = json_request(gen_url)

    return json_response['response']['body']['items']['item'] \
        if json_response['response']['header']['resultCode'] == '0000' else dict()


def pd_fetch_tourspot_visitor(
        district1='',
        district2='',
        tourspot='',
        year=0,
        month=0):

    results = []
    for pageNo in count(start=1):
        gen_url = pd_gen_url(
            endpoint='http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList',
            YM='{0:04d}{1:02d}'.format(year, month),
            SIDO=district1,
            GUNGU=district2,
            RES_NM=tourspot,
            _type='json',
            pageNo=pageNo,
            numOfRows=100)
        json_response = json_request(gen_url)

        result_code = json_response \
            .get('response') \
            .get('header') \
            .get('resultCode')

        if result_code != '0000':
            return []
        items = json_response.get('response').get('body').get('items')

        if items == '':
            break

        results += items.get('item')
    return results
