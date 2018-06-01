import json
from collection import api

RESULT_DIRECTORY = '__results__/crawling'


def preprocess_tourspot_visitor(item):
    result = dict()
    result['disticnt'] = item.get('sido')
    result['tourist_spot'] = item.get('resNm')
    result['date'] = item.get('ym')
    result['count_foreigner'] = item.get('csForCnt')
    result['count_locals'] = item.get('csNatCnt')
    return result


def preprocess_foreign_visitor(data):
    result = dict()
    result['country_code'] = data['natCd']
    result['country_name'] = str(data['natKorNm']) # 공백제거
    result['data'] = data['ym']
    result['visit_count'] = data['num']

    return result


def crawling_foreign_visitor(country, start_year, end_year):
    results = []
    filename = '%s/%s_foreignvisitor_%s_%s.json' % (RESULT_DIRECTORY, country[0], start_year, end_year)
    for year in range(start_year, end_year+1):
        for month in range(1, 13):
            results.append(
                preprocess_foreign_visitor(
                    api.pd_fetch_foreign_visitor(country_code=country[1],
                                                 year=year,
                                                 month=month)))

    with open(filename, 'wt', encoding='UTF-8') as file:
        json_string = json.dumps(results, indent=4, sort_keys=True, ensure_ascii=False)
        file.write(json_string)

    return filename


def crawling_tourspot_visitor(district, start_year, end_year):
    results = []
    filename = '%s/%s_tourspot_%s_%s.json' % (RESULT_DIRECTORY, district, start_year, end_year)
    for year in range(start_year, end_year+1):
        for month in range(1, 13):
            for item in api.pd_fetch_tourspot_visitor(district1=district, year=year, month=month):
                results.append(preprocess_tourspot_visitor(item))

    with open(filename, 'wt', encoding='UTF-8') as file:
        json_string = json.dumps(results, indent=4, sort_keys=True, ensure_ascii=False)
        file.write(json_string)

    return filename
