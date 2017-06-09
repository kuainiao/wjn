#!/usr/bin/env python
# coding=utf-8
# filename : backup_svn.py

import os
import time
import paramiko



source = 'data/'
target_dir = '/home/tc_backup/svn/'
#target = target_dir + "svn.data_" + time.strftime('%Y%m%d%H%M%S') + '.tar.gz'
target = target_dir + 'svn_data.tar.gz'
tar_command = "tar -zcvf '%s' %s" % (target, ''.join(source))
if os.system(tar_command) == 0:
    print 'Successful backup to', target
else:
    print 'Backup Failed!'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.1.10', username='root', password='zjtachao')
ftp = ssh.open_sftp()
ftp.put('/home/tc_backup/svn/svn_data.tar.gz', '/home/tc_backup/svn/' + time.strftime('%Y%m%d') + '_svn_data.tar.gz')
ftp.close()


os.remove('/home/tc_backup/svn/svn_data.tar.gz')












