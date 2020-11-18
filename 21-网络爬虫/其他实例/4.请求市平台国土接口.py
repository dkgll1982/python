import requests 
# 导入 base64模块
import base64
import json

#请求省平台接口

#查询sign的SQL
sql ='''
          SELECT (lower(utl_raw.cast_to_raw(DBMS_OBFUSCATION_TOOLKIT.MD5(
                        INPUT_STRING => TB.KEY||TD.SERC||td.CREATE_DATE)))) sign,
                        (td.CREATE_DATE) requestTime,
('{\"encryptParam\":\"'||
'PgFimk38kXhdkJmY4dzpUNcpa9KHCL7Avj2Nqxg0B6CTM2orvV0w4G+yARmjcW+6RivhJLFk1dAsKD9t9FV+auHiE05wPqFsSbDotYenPaA9k5lqd3F0CozIaOUuwURQF7YUrW0rxM90v4mb36YCg3zmatnYr+6SPRmXbTsboMipCs+c86vcwRMwGYPId3ZGwlsIDmSHj1AHWiTZowLkv4fk/DqyQ4vphzlhw+Q5NUh9z+5+kELdgnD9btEb+CTj4zwxy7cEfvAmTxB0NRjoQ3CHmWvpzmQGAKiaNiy/RKdKg1yZ5hyqwNsxFIQcarbEpxlPH6f21rwKtlJ0iUDaIAv/4pynJ2yNAE0fhX0pknWtvZP3ZB0mTjXM83kxkC9vmr1fywDhlCCZ7NXRakYSZ7KtVdFiXzSG8yV9Om514vwsTFYLbs8b4o/mbTAeW3xNv4VwKiFlSCfges7iGVMurDi5gLPpo9SmGZ2WsYtdo0w8IMzZBR4QqyOk4VJJqxOvCMed3mIwS8X98DRsfTvcYchWaKhTgO9U6SfkjPoO4HFZT/AJPy0XZoW3ErwuQSvmCVwUiHHgQD7p7x1lGpi72Z4be5nl/82ZDimCwI1OsESFq3mQ3ULmLDvDCmoBBvdvRMWWEwu/wQFw58RCAtH+r0ryDyIV8MszvVU4W4IE8RUv+Gg04km9P/M6JtdkhhDlsE/x2oSaxKkxbOdc+si5MhpHukfdx+mHGW2f9Q4E7AIEIfZnzwUH9/4Mt0VQa3nTQ3EIOPV32uhMeuS1JpJkrJJvcWvBzudV+upTpt8jKYemrLHHccHyBehkFlrYM+bSfT+hddA9vY8d5OuqkpfHHxz8HQqPx2aLeaS0sH46Dthatd0t9fyCnyYORtWI1yJsWN/DTAaV/sJ78tiNJ190kH/wv0hA1lZyyNosJ/rqLG7Lwymj2C2oFxE6T9IadYZ5/pU7Mv/CV8aErR+t3cDWLYI9fvrSJEb08TRtJv5XJoilxFkep1kvIAciyL2YU6A8aWDCaALKU6Hboqbjs2XnTdnU5z8y19dXizGeBUGEUG0LLScCohoZI1nq3d37d3E1PLnsKe5e26RacbDeUtArpEjySJtwv0jB6MSrEP97Vc9F3TklEySmNjfl0Xuhi02y4f4ZRQL6fmv/pQIRT7UUkFMoUzLvhBftiQDEYhdxfv0='
--utl_raw.cast_to_varchar2(utl_encode.base64_encode(utl_raw.cast_to_raw('{"querymanList":"[{\"name\":\"陈青青\",\"zjh\":\"33050119890104880X\"}]","bjsy":"湖州不动产权属查询","jgmc":"公安","cxfw":"湖州市区","cdbh":"cd20180119-0028223","isAllCity":"1","cxbt":"湖州市不动产登记信息查询记录","xzqbm":"330501","isShowXzxx":"1","cdyt":"无房证明","qyca":"1","sm":"查询范围:{0}.","timestamp":"1575538699115"}')))
||'\",\"sign\":\"WH/m4ufovq+sK5JHvj8HrCsXFBYz+hYj5QjLwPIfsgwONCcUGraG4YAcijmakWWY8zGXsOnzGyNPsEE9NfxRAq4d8q0OMu3FHXQ7YZaa/09G6dK0lTjp/JXboRms8LHnS2WPUj88auJNqSmaKK5si9lekuofo+uvgVjo23RxX9g=\",\"userId\":\"27fe2fc3-21eb-4d3d-ad86-e468c17c85ff\"}')              
               example     FROM BASE_SPT_INTERFACE TA
                        JOIN BASE_SPT_SERC TB ON ','||TB.INTERFACE||',' LIKE '%,'||TA.KEY||',%' 
                        JOIN BASE_SPT_QLSX TC ON (','||tC.deptID2||',' like '%,'||tb.deptid||',%' and tC.zxmc is not null and tC.zxbm is not null) 
                        JOIN (select to_char((SYSDATE - TO_DATE('1970-1-1 8', 'YYYY-MM-DD HH24')) * 86400000 + TO_NUMBER(TO_CHAR(SYSTIMESTAMP(3), 'FF'))) create_date,SERC,app_key from (
                            select create_date,row_number() over(partition by app_key order by create_date desc nulls last) rn,requestsecret SERC,app_key from base_spt_keysecret 
                            ) where rn=1 and APP_KEY='ccd1d2a835c246788f54a177395f6ca6') TD ON TD.APP_KEY=TB.KEY
               

'''
url = 'http://59.202.115.11/gateway/api/001008005007017/dataSharing/LQ2aKKb7t6bb90cd.htm'
params = {
	"appKey": "ccd1d2a835c246788f54a177395f6ca6",
	"sign": "46938c7e0f7fd0a4c416e0d785bd0120",
	"requestTime": "1591844081429",
	"additional": "{\"powerMatters\":\"许可-00757-000\",\"subPowerMatters\":\"许可-00757-001\",\"accesscardId\":\"sjgl\",\"materialName\":\"机动车驾驶证初学申领\",\"sponsorName\":\"大数据管理中心\"}",
	"encryptEntity": "{\"encryptParam\":\"bc5upAnW8lZb3qgVh415XBekvEdI4VoFZ05fRsDwBYkW9krL8hXRKs4Yx69Yix/6y3wB/TR9rlqqQ8TnXeNSHe43CJdd/L0ivrVns84ttUY0LF04sf0QdzJGGiUC4s0QDLAUqA73sZSlSFXIfKZdbKCYzo6Qw/WtU8nsFPmAQBo8yC+j40qGhLuBCJ/mG7JTvX1ECqx9EoG5//7ZtGahWgmtYJFHcQcIm32MMn7mZBEXqDQqLgUA3tEWBB+eWMYYC2X0k5k1h03OKMcOa8s3rpDVfJCIQdrPrt9IxYaFNPVVoL2nLh3cBbP/kPK349yTTHB4r9swHG9YBgTkQbOAMoZRcE0YyQi3cvy+4jIwx7Wf3zYHBTfwEoXih1LY5IF23bxqnvaN5arauRI3ZqIz9teHRiXQ/ZEWhJvHG8riaGCcnrhkiTzmza8fQnMaD5a/AJnZsYEXmPxDZL2mMBM8XyR3c5tQcj+jTuUcchqvvkZKYW5Yd05fLBizAFTvTfJYtcQFU6VrB3c1g2NGSAdEWTNN+ZXQTJc8rJramH2Q9lrAwHLGld8N+6H1HhUNoN8qEIPrfETnZCIfwW1TPKCaUXU3PDm+Cl1gxegCv1ToquZTcnNYEiXPheASkrPxHdtGe0rKsF8pmVTR0YACyQknrakpWEaRaqd7aN+Nh4JXmk6Q8MMJsL09dndTjzgppxNLe8ifeRsSeLFw1sxRqj42Fx/ZphKU7XMtb91X7eU/FwqfnXKdCzeXuJPwvOr+/SPL7zxsUXBDaB3YJP4a24+clWSjnvorKOVgN3S888alSyUBjMyoBsUEIZGEfraeeBSMFwyMQfn7l/kJd8NilLDqt1Y1InrwzivGagH8mvm/Xp2+5m8Dy3KDEqlWuxpp/NWPPncdSfsC2IjT4/HnCuiqYj6TuBnB/VKEuGwJs1TH3gKRIsT+4bjveY9USc1xkxU8obxZArb1ud9pNtI5OgyCX8IqHkf2pVngCfdzdtTUDkVUvqAM18NM/aQs3RywVnSqtpt95hKfLVPbOYU71LRukItWa8r3DCH+53CIHWveiC9Pf1jKOCYs9NS3SKTNYOvxldiNUlNrQIMtnoHFSI5ozkXxoJLIcGE8y276yFZS1zSSfdy1yOoHOQ24TQ4ZWocNvd7zURIuNQQZbkpveJyafs3lN0uPNAUoseMol5afcCpju2Ozs3kdXeorQX7wquqcFNdQ51SVDO1CC4hepKVQyTRlzxTAqv5rUYnaNKUpGZRIKD4Syer1Kj/UK5PTwPrfLk+vCRk09whMlR+D+skJLtzPuNb53MTe3p+a2gmeH3V/8XZ6LxzwYyCucm2Ttn5Us3PSqfSuWO390Bo6CuPItA==\",\"sign\":\"C7smDdv74YhMpo7MRg53BUAmjsEiZkx3Zc7hPskFsPQpvzaoLPiMmbU9BvJGaPYmZyje+13J9ZP7R8SdmuFMmooU5s1/f7b6Z1TnteZodvtL3BRDJNdtlFdkt+CYGRAdmxgjt2UpX/csa6OUqj9ZrsDXxrAE5vX8knjSeAUlE0g=\",\"userId\":\"cc0689a0-d286-43f3-ba91-658f1bc1f125\"}"

}
req = requests.get(url,params=params) 
text = req.text 

with open(r'D:\5.txt','w') as f:
    f.write(text)
    
    
json_str = json.loads(text)
datas = json_str['datas'] 
data = json.loads(datas)
with open(r'D:\4.txt','w') as f:
    f.write(data['data'])
    
# SELECT  key,BASEURL||appKey||sign||requestTime||additional||'&'||example as url,APP_KEY  FROM (
#                     SELECT (lower(utl_raw.cast_to_raw(DBMS_OBFUSCATION_TOOLKIT.MD5(
#                         INPUT_STRING => TB.KEY||TD.SERC||td.CREATE_DATE)))) sign,
#                         (td.CREATE_DATE) requestTime,
# ('{\"encryptParam\":\"'||
# 'TyMBKWYg251nau9sNCuAZc3FjX/LyZ0FXclv5BADA3j5cBOjU8IB3O0jqaxQ8wVoGLyNSh1vx+h9AyYS8rhbKcAdjX6kKKyDcGfboa11KMDsuJAA2T0u9qBGzPZWYcu+qqhEjXuBvFlIWqlZG5aMV7tOiEKnzx/8xLxTc9or68SAdb/whfT9TkI+wN9Pc0gmgkjLOyWD56yvLfnx3f1skaRQMs1mGxnUEcxtB6j1YHFGRBhLOu99MI6sf8zOyPkyMXcp/bvoX1A8g6c4+EDH1x2LneQHMHSICX/e7wEhfshplcmZNHBLC981CAYoI8azRKJpRVHF3kHrCNHPwqoalyoTNpFuFOJEKvdow5C89whClx5efCdiHtuuBBVP1fUXowO4PkcVIwD1mzdY1r+bk/0y7ezJ76PvsZHjDGQFn/tPF3s2WAc4MID+2h/eSF+78GaoBjocUXFZzi4BV9kWLHRoI8Gajr098tiRH3FAEcmCe1ZUyCf+quuuXL/RCNKljFnAcw7DP2uksylm9h8CeC78H4eZkNagnSBVLTwgQ/BStyT9+l1b2nZBs9lse6LuG4IHwBFzFQm4Cbr+SJWnf8D9eBshKk4pYH6KsI4PZykMGzJpnVZha2teFIGZt3HLzeGlvGNmdUAjQPIDBkFRrKxHNVNqNJ5kym90Hs/bDq8ZJs1ntcI8kF99TSzdb1JBMBBrwSY9CB3gY3jwc1XzxXZMkgzcX51SXh3VReFdeDWPvlPgJwviJN1+MMpSJFDFqHPu7UyJZgU7p8GoN3ocHYvqdBGYoDH9l6h70L9dNc6BkTBV6Y05iirDlWkvv4foELIpgzOLkgrPSccOnMxO0A=='
# --utl_raw.cast_to_varchar2(utl_encode.base64_encode(utl_raw.cast_to_raw('{"querymanList":"[{\"name\":\"陈青青\",\"zjh\":\"33050119890104880X\"}]","bjsy":"湖州不动产权属查询","jgmc":"公安","cxfw":"湖州市区","cdbh":"cd20180119-0028223","isAllCity":"1","cxbt":"湖州市不动产登记信息查询记录","xzqbm":"330501","isShowXzxx":"1","cdyt":"无房证明","qyca":"1","sm":"查询范围:{0}.","timestamp":"1575538699115"}')))
# ||'\",\"sign\":\"hKuioeEZviZoEoVUgUuS5SuXUN5u6HtZOsFFSv8WhMuD8ncG/gn6apEDAdW7uRWK9SjnBSZ5ystDNPEeBd4ASht8QkH2/BMxTzOdnUVlEgnwqNWAqjLp6E50AX6FufWUxcDvqjYdUadgVIkChNPvgTEt4JlCAD7JdfMSctIWYaA=\",\"userId\":\"27fe2fc3-21eb-4d3d-ad86-e468c17c85ff\"}')              
#                example     FROM BASE_SPT_INTERFACE TA
#                         JOIN BASE_SPT_SERC TB ON ','||TB.INTERFACE||',' LIKE '%,'||TA.KEY||',%' 
#                         JOIN BASE_SPT_QLSX TC ON (','||tC.deptID2||',' like '%,'||tb.deptid||',%' and tC.zxmc is not null and tC.zxbm is not null) 
#                         JOIN (select to_char((SYSDATE - TO_DATE('1970-1-1 8', 'YYYY-MM-DD HH24')) * 86400000 + TO_NUMBER(TO_CHAR(SYSTIMESTAMP(3), 'FF'))) create_date,SERC,app_key from (
#                             select create_date,row_number() over(partition by app_key order by create_date desc nulls last) rn,requestsecret SERC,app_key from base_spt_keysecret 
#                             ) where rn=1 and APP_KEY='ccd1d2a835c246788f54a177395f6ca6') TD ON TD.APP_KEY=TB.KEY
#                 ) TA 
# WHERE RN=1 and APP_KEY='ccd1d2a835c246788f54a177395f6ca6'
