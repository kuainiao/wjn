@echo off
set "Ymd=%date:~,4%%date:~5,2%%date:~8,2%"
C:\soft\mysql-5.6.25-winx64\bin\mysqldump  -uzjtachao -p123456 hd > D:\mysql_bak\hd_%Ymd%.sql
C:\soft\mysql-5.6.25-winx64\bin\mysqldump  -uzjtachao -p123456 hd-data > D:\mysql_bak\hd-data_%Ymd%.sql
C:\soft\mysql-5.6.25-winx64\bin\mysqldump  -uzjtachao -p123456 qtang > D:\mysql_bak\qtang_%Ymd%.sql
C:\soft\mysql-5.6.25-winx64\bin\mysqldump  -uzjtachao -p123456 ttc_test > D:\mysql_bak\ttc_test_%Ymd%.sql
C:\soft\mysql-5.6.25-winx64\bin\mysqldump  -uzjtachao -p123456 wcad > D:\mysql_bak\wcad_%Ymd%.sql
C:\soft\mysql-5.6.25-winx64\bin\mysqldump  -uzjtachao -p123456 wcad_bak > D:\mysql_bak\wcad_bak_%Ymd%.sql
C:\soft\mysql-5.6.25-winx64\bin\mysqldump  -uzjtachao -p123456 wcuser > D:\mysql_bak\wcuser_%Ymd%.sql
C:\soft\mysql-5.6.25-winx64\bin\mysqldump  -uzjtachao -p123456 xchao > D:\mysql_bak\xchao_%Ymd%.sql
C:\soft\mysql-5.6.25-winx64\bin\mysqldump  -uzjtachao -p123456 zjtachao > D:\mysql_bak\zjtachao_%Ymd%.sql

@echo on