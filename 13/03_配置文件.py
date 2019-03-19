#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 使用mysql的配置文件举例

'''
[mysql]
host = 127.0.0.1
port = 3306
user = root
password = admin
'''
import time
import configparser

# 写入这样一个配置到配置文件
with open('db.conf', 'w') as fconf:
    config = configparser.ConfigParser()
    config['mysql'] = {'host': '127.0.0.1',
                       'port': 3306,
                       'user': 'root',
                       'password': 'admin'}
    config.write(fconf)

# 程序中读取配置
def connect_mysql(path):
    '''连接数据库'''
    print('模拟连接数据库')
    time.sleep(1)
    # config = configparser.RawConfigParser()
    config = configparser.ConfigParser()
    with open(path, 'r') as fconf:
        config.readfp(fconf)
        print('连接到数据库',
              config['mysql'].get('host'),
              config['mysql'].get('port'))
        time.sleep(1)
        print('用户(%s:***)登陆' % config['mysql'].get('user'))

# connect_mysql('db.conf')


# 修改配置文件
print(config['mysql']['host'])
config['mysql']['host'] = '192.168.0.1'
config['mysql']['port'] = '3333'
# 写回原配置
with open('db.conf', 'w') as fconf:
    fconf.write(config)

