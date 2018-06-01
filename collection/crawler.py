from collection import api

def preprocess_tourspot_visitor(item):
    pass


def preprocess_foreign_visitor(data):
    pass


def crawling_foreign_visitor(country, start_year, end_year):
    pass


def crawling_tourspot_visitor(district, start_year, end_year):
    for year in range(start_year, end_year+1):
        for month in range(1, 13):
            api.pd_fetch_tourspot_visitor(district1=district, year=year, month=month)
