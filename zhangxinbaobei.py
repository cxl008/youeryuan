# coding: utf-8

import requests
import re
import os
import json



parent_list[] = []
parent['parents_username'] = os.getenv('parents_username1')
parent['parents_password'] = os.getenv('parents_password1')
parent['Identity'] = os.getenv('Identity1')
parent_list.add(parent)

parent['parents_username'] = os.getenv('parents_username2')
parent['parents_password'] = os.getenv('parents_password2')
parent['Identity'] = os.getenv('Identity2')
parent_list.add(parent)

session = requests.Session()

def parent_login():



    headers = {
                'Mobile-Agent': 'iPhone/iPhone10,2,3.9.3',
                'User-Agent': 'æå¿å®è´ 3.9.3 rv:5 (iPhone; iOS 12.0; zh_CN)',
                'Accept': 'application/json',
                'Host':'120.27.83.33',
                'User-Identity':parent['Identity'],
                'Mobile-Name': '%E2%80%9CChengxianlong%E2%80%9D%E7%9A%84%20iPhone',
                'Accept-Encoding': 'gzip',
              }
    

    session.headers.update(headers)

    
    lgoin_url = "https://120.27.83.33/openuser/userlogin?type=parent&username=%s&userpassword=%s" %(parents_username,parents_password)
    login_post = {"type":"parent","username":parent['parents_username'],"userpassword":['parents_password']}
    resp = session.post(lgoin_url, login_post,verify=False)
    print(resp.text)

    login_item = json.loads(resp.text)

    sessionid = login_item['data'][0]['sessionid']
    headers['Session'] = sessionid
    session.headers.update(headers)


    changestudentv4_item = {"newtime_babyinfo":"1537260894","newtime_schoolinfo":"1537146548","newtime_schoolconfig":"1537146548","studentid":"1616116"}


    changestudentv4_url = "https://120.27.83.33/openparent/changestudentv4"
    resp = session.post(changestudentv4_url,changestudentv4_item,verify=False)
    print(resp.text) 

    getuserloginbaseinfo_url = "https://120.27.83.33/openuser/getuserloginbaseinfo"
    resp = session.post(getuserloginbaseinfo_url,verify=False)
    print(resp.text) 


    # studentinfo_url = "https://120.27.83.33//openuser/studentinfo"
    # resp = session.get(studentinfo_url,verify=False)
    # print(resp.text) 


    # devicetoken_url = "https://120.27.83.33/opensetdevicetoken/setdevicetoken?devicetoken=18171adc035615faf7f"
    # resp = session.get(devicetoken_url,verify=False)
    # print(resp.text) 

    # homestudent_url = "https://120.27.83.33/openpoints/homestudent"
    # resp = session.get(homestudent_url,verify=False)
    # print(resp.text) 

    

def parent_sign():
    sign_url = "https://120.27.83.33/openpoints/set?commend=sign"
    resp = session.get(sign_url,verify=False)
    print(resp.text) 

def parent_share():
    sign_url = "https://120.27.83.33/openpoints/set?commend=share"
    resp = session.get(sign_url,verify=False)
    print(resp.text) 


def add_flower(parent)
    parent_login(parent)
    parent_sign()
    for i in [0,1,2]:
        parent_share()


if __name__ == '__main__':
    add_flower(parent_list[0])
    add_flower(parent_list[1])
