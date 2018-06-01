import sys
from urllib.request import Request, urlopen
from datetime import *
import json


def json_request(
        url='',
        encoding='utf-8',
        success=None,
        error=lambda e: print('%s : %s' % (e, datetime.now()), file=sys.stderr)):
    try:
        request = Request(url)
        resp = urlopen(request)

        resp_body = resp.read().decode(encoding)
        # resp_body = '{"response":{"header":{"resultCode":"0000","resultMsg":"OK"},"body":{"items":{"item":[{"addrCd":2635,"csForCnt":286,"csNatCnt":9110,"gungu":"해운대구","resNm":"부산시립미술관","rnum":1,"sido":"부산광역시","ym":201201},{"addrCd":2635,"csForCnt":80,"csNatCnt":937,"gungu":"해운대구","resNm":"M.Do 관광호텔","rnum":2,"sido":"부산광역시","ym":201201},{"addrCd":2635,"csForCnt":7004,"csNatCnt":16473,"gungu":"해운대구","resNm":"파라다이스호텔부산","rnum":3,"sido":"부산광역시","ym":201201},{"addrCd":2635,"csForCnt":59,"csNatCnt":1436,"gungu":"해운대구","resNm":"호텔일루아","rnum":4,"sido":"부산광역시","ym":201201},{"addrCd":2635,"csForCnt":2063,"csNatCnt":4830,"gungu":"해운대구","resNm":"해운대그랜드호텔","rnum":5,"sido":"부산광역시","ym":201201},{"addrCd":2635,"csForCnt":1403,"csNatCnt":6012,"gungu":"해운대구","resNm":"부산웨스턴조선호텔","rnum":6,"sido":"부산광역시","ym":201201},{"addrCd":2635,"csForCnt":712,"csNatCnt":17025,"gungu":"해운대구","resNm":"해운대 글로리콘도","rnum":7,"sido":"부산광역시","ym":201201},{"addrCd":2635,"csForCnt":1113,"csNatCnt":5736,"gungu":"해운대구","resNm":"노보텔부산","rnum":8,"sido":"부산광역시","ym":201201},{"addrCd":2635,"csForCnt":9610,"csNatCnt":37223,"gungu":"해운대구","resNm":"해운대 한화리조트 부산","rnum":9,"sido":"부산광역시","ym":201201},{"addrCd":2635,"csForCnt":73,"csNatCnt":1188,"gungu":"해운대구","resNm":"송정관광호텔","rnum":10,"sido":"부산광역시","ym":201201}]},"numOfRows":10,"pageNo":1,"totalCount":10}}}'
        # resp_body = '{"response":{"header":{"resultCode":"0000","resultMsg":"OK"},"body":{"items":{"item":{"ed":"방한외래관광객","edCd":"E","natCd":112,"natKorNm":"중  국","num":565243,"rnum":1,"ym":201701}},"numOfRows":10,"pageNo":1,"totalCount":1}}}'
        json_result = json.loads(resp_body)

        print('%s : success for request [%s]' % (datetime.now(), url))

        if callable(success) is False:
            return json_result

        success(json_result)

    except Exception as e:
        callable(error) and error(e)
