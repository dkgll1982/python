import json
dicts = {
    "pp": '''    INSERT INTO ZZ_ADD_PERSON_HISTORY(ID,NAME,CARD_NUM,GENDER,DEPARTMENT_ID,ADD_DATE,FOCUS_TYPE,ADD_AUDIT_STATUS,PERSON_TYPE,CREATE_USERID,
        CREATE_USER,CREATE_DATE,DATA_SOURCES,ADD_OBJECT) 
    select CREATEGUID() id,tb.name,tb.card_num,gender,g_id DEPARTMENT_ID,sysdate add_date,'易肇精患' FOCUS_TYPE,0 ADD_AUDIT_STATUS,'203' PERSON_TYPE,
             'ADMIN' CREATE_USERID,'ODPS'||TO_CHAR(SYSDATE,'YYYYMMDD') CREATE_USER,SYSDATE CREATE_DATE,'2' DATA_SOURCES,          
              '{'||
    '"cardNum": "'||tb.card_num||'",'||
    '"name": "'||tb.name||'",'||
    '"personType": "'||tb.person_type||'",'||
    '"gId": "'||tb.g_id||'",'||
    '"gridName": "'||tc.displayname||'",'||
    '"dType": "",'||
    '"rAddr": "'||tb.r_addr||'",'||
    '"illName": "",'||
    '"mType": "02",'||
    '"guardian": "",'||
    '"gCardNum": "",'||
    '"gUsedName": "",'||
    '"gPhone": "",'||
    '"treat": "02",'||
    '"eFamily": "",'||
    '"hosReason": "",'||
    '"inLow": "",'||
    '"hosName": "",'||
    '"rehabName": "",'||
    '"isSeriousIll": "",'||
    '"supCase": ['||
    'null'||
    '],'||
    '"supCase[]": [],'||
    '"focusType": "203",'||
    '"focusTypeName": "精神病人",'||
    '"dangerLevel": "",'||
    '"createDate": "'||to_char(sysdate,'yyyy-mm-dd hh24:mi:ss')||'"'||
    '}' ADD_OBJECT 
            from ODPS_PRSN_SEVERE_PSYCHOPATH ta
            join zz_person tb on ta.p_id=tb.id 
            join a4_sys_department tc on tb.g_id=tc.departmentid
            where not exists(
                select * from ZZ_ADD_PERSON_HISTORY td where tb.card_num=td.card_num and person_type='203' 
            ) and tb.id not in(
                select p_id from ZZ_PERSON_PSYCHIATRIC where p_id is not null
            ) 
'''
}
# json.dumps 进行序列化时，默认使用ascii编码， print json.dumps(dic)输出unicode编码的结果： {"a": "\u4e2d\u56fd"}
# json.dumps(dic,ensure_ascii=False)，不使用ascii编码，输出结果为：{"a": "中国"}
# 参考链接：https://www.cnblogs.com/shiju/p/9511916.html
json_dicts = json.dumps(dicts, indent=4, ensure_ascii=False)
print(json_dicts)
