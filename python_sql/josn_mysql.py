#!/usr/bin/env python
# -*-encoding:utf-8-*-

import json
import os
import MySQLdb
import codecs


dir_path='e:\diff\\show_people.csv'

path_fil = os.path.basename(dir_path)
path_dir = os.path.dirname(dir_path)
str_name = path_fil.split('.')[0]
os.chdir(path_dir)

for lines in open(dir_path):
    str_json = json.loads(lines)
    title = str(str_json.keys())
    print title
    titles = title.replace('[u', '').replace(' u', '').replace(']', '\n').replace("'", '')
    print titles
    j = open("title3.txt", 'a+')
    j.write(titles)
    j.close()
    break

for line in open(dir_path):
#    news = line.replace('\\r', ' ').replace('\\t', ' ').replace('\\n', ' ')
    j = json.loads(line)
    json_valuo=str(j.values())
    jvn = json_valuo.replace('[u', '').replace(', u', ';').replace(']', '\n').replace("'", '')
    new_fil = open("title3.txt", "a+")
    new_fil.write(jvn)
    new_fil.close()



file=codecs.open('title3.txt','r','utf-8')
reader=file.readline()
b=reader.split(',')
colum=''
for a in b:
    colum=colum+a+' varchar(500),'
colum=colum[:-1]
create='create table if not exists '+str_name+' '+'('+colum+')'+' DEFAULT CHARSET=utf8'
data='LOAD DATA LOCAL INFILE \''+'title3.txt'+'\' INTO TABLE '+str_name +' character set utf8 FIELDS TERMINATED BY \';\' ENCLOSED BY \'\"\' LINES TERMINATED BY \''+r'\r\n'+'\' IGNORE 1 LINES;'
e=unicode(data,'utf8')

db_config = {
    'host': '192.168.30.101',
    'user': 'wjn',
    'passwd': '123',
    'port': 3306,
    'db': 'ceshi',
    'charset': 'utf8'
}

conn = MySQLdb.connect(host=db_config['host'],user=db_config['user'],passwd=db_config['passwd'],port=db_config['port'],charset=db_config['charset'])
cursor=conn.cursor()
cursor.execute('SET NAMES utf8;')
cursor.execute('SET character_set_connection=utf8;')
cursor.execute("USE %s" % db_config['db'])
cursor.execute(create)
cursor.execute(e)
#cursor.rowcount

conn.commit()
cursor.close()
#os.remove("title2.txt")
print('OK')