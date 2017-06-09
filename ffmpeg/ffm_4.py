#!/usr/bin/env python
# -*-encoding:utf-8-*-
import os

v=["test01.mp4","test-1080-2min.mkv","test-4K-5min.mkv","six.flv"]
num=len(v)
for j in range(0,len(v)):
    ffm_com1 = "ffmpeg -i %s -s 480:272 %s.mp4" % (v[j],j)
    ffm_com2 = "ffmpeg -i %s -i %s -i %s -i %s -filter_complex '[0:v]pad=iw*2:ih*2[a];[a][1:v]overlay=w[b];[b][2:v]overlay=0:h[c];[c][3:v]overlay=w:h' -ar 22050 out.flv" % ("0.mp4","1.mp4","2.mp4","3.mp4")
    test=v[j]
    print len(v)
    os.system(ffm_com1)
    os.system(ffm_com2)



