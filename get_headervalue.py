#coding=utf8
from Base.base_requests import request
from practice import md5
from Read_main.read_config import handle_ini
import requests

class get_headervalue:
    url = 'https://console-rd.pxxclass.com/class_in/admin/user/login'
    data = {
        "account": handle_ini.get_value('username', 'adminuser'),
        "password": md5.getmd5(handle_ini.get_value('password', 'adminuser')),
        "isVaildCode": 'false'
    }
    cookie = {
        'beegosessionID': 'a89d6154725a2d00c26a4d648cd85'
    }
    # 获取token并写入config
    def get_token(self):
        res = request.run_main('POST', self.url, self.data, self.cookie)
        token = res['user']['token']
        handle_ini.write_value('server', 'token', token)
        return token

    # 获取cookie
    def get_cookie(self):
        session = requests.session()
        session.request("POST", self.url, data=self.data, cookies=self.cookie)
        cookie = session.cookies['beegosessionID']
        return cookie

get_value = get_headervalue()

if __name__ == '__main__':
    get_headervalue().get_token()

