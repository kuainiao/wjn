#!/usr/bin/env python
# -*-encoding:utf-8-*-

import sys
import io
import json
import code
reload(sys)
sys.setdefaultencoding('utf8')
import MySQLdb

db_config = {
    'host': '192.168.30.101',
    'user': 'wjn',
    'passwd': '123',
    'port': 3306,
    'db': 'python',
    'charset': 'utf8'
}


conn = MySQLdb.connect(host=db_config['host'],user=db_config['user'],passwd=db_config['passwd'],port=db_config['port'],charset=db_config['charset'])
conn.autocommit(True)
curr = conn.cursor()
curr.execute("SET NAMES utf8");
curr.execute("USE %s" % db_config['db']);
dir="e:\diff\\bout.csv"
for line in open(dir):

    j=json.loads(line)
    strdata = j["division"], int(j["show_id"]), j["bout_round"], j["last_round_time"], j["comments"], j["bout_url"], j["bout_id"], j["num"], j["bout_result"], j["winner_boxer_id"], j["bout_result_by"], j["rounds"]
#    strdata = j["division"], int(j["show_id"]), int(j["bout_round"]), j["last_round_time"], j["comments"], j["bout_url"], int(j["bout_id"]), int(j["num"]), j["bout_result"], int(j["winner_boxer_id"]), j["bout_result_by"], int(j["rounds"])
    curr.execute('insert into bout2 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', strdata)


conn.commit()
curr.close()
conn.close()