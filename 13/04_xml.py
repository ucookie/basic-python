#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 本章最后一节将介绍 XML，这是一个较老的结构化数据格式，声称是“纯文本”格式
# 用来表示结构化的数据。尽管 XML 数据是纯文本，但有充分的理由认为 XML 不是人类可读的
# 如果没有解析器的帮助，XML 几乎难以辨认。但 XML 诞生已久，且比 JSON 应用得更广

# CentOS防火墙规则 firewall配置
# jmeter测试文件

import xml.etree.cElementTree as ET

root = ET.Element('mysql')
host = ET.SubElement(root, 'host')
host.text = '127.0.0.1'

port = ET.SubElement(root, 'port')
port.text = '3306'

user = ET.SubElement(root, 'user')
user.text = 'root'

password = ET.SubElement(root, 'password')
password.text = 'admin'


tree = ET.ElementTree(root)
indent(root)
tree.write('db.xml', encoding='utf-8', xml_declaration=True)


# 读取配置
tree = ET.ElementTree(file='db.xml')
root = tree.getroot()
host = root.find('host').text
port = root.find('port').text
user = root.find('user').text
password = root.find('password').text
print('数据库连接信息:', host, port, user, password)
