#coding=utf8
import openpyxl
import os
import sys
import configparser
base_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(base_path)

class Handconfig:

    def load_ini(self):
        config_path = base_path + '/config.ini'
        rd = configparser.ConfigParser()
        rd.read(config_path, encoding='utf-8-sig')
        return rd

    def get_value(self, key, node=None):
        '''
        获取ini中的value
        '''
        if node == None:
            node = 'server'
        rd = self.load_ini()
        try:
            data = rd.get(node, key)
        except Exception:
            print('未获取到配置文件')
            data = None
        return data

    def write_value(self, key, node=None, value=None):
        config = configparser.ConfigParser()
        config.read(base_path + '/config.ini')
        config.set(key, node, value)
        config.write(open(base_path + '/config.ini', 'w'))

handle_ini = Handconfig()

if __name__ == '__main__':
    get_ini = Handconfig()
    handle_ini.write_value('server', 'token', '1')


