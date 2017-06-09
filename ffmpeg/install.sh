
tar -xf ffmpeg-3.3.1.tar.bz2 
cd ffmpeg-3.3.1/
./configure --prefix=/usr/local/ffmpeg
yum -y install yasm
./configure --prefix=/usr/local/ffmpeg
make
make install
ln -s /usr/local/ffmpeg/bin/ffmpeg /usr/bin/










#！/bin/bash
git clone git://git.videolan.org/x264
cd x264
./configure --host=arm-unknown-linux-gnueabi --enable-static --disable-opencl
make
make install
cd ..
rm -rf x264

git clone git://source.ffmpeg.org/ffmpeg.git
cd ffmpeg
./configure --arch=armel --target-os=linux --enable-gpl --enable-libx264 --enable-nonfree
make
make install
cd ..
rm -rf ffmpeg


1. ffmpeg安装
安装环境：
ubuntu 12.04
（1）删除已安装的文件，避免冲突
sudo apt-get remove ffmpeg x264
sudo apt-get autoremove
（2）安装需要的支持
sudo apt-get install make automake g++ bzip2 python unzip patch subversion ruby build-essential git-core checkinstall yasm texi2html libfaac-dev libmp3lame-dev libopencore-amrnb-dev libopencore-amrwb-dev libsdl1.2-dev libtheora-dev libvdpau-dev libvorbis-dev libvpx-dev libx11-dev libxfixes-dev libxvidcore-dev zlib1g-dev
（3）安装 x264 （自己选择是否安装）
x264 依赖于yasm，而且版本较高。
sudo git clone git://git.videolan.org/x264.git
cd x264
sudo ./configure --enable-shared --prefix=/usr/local
sudo make
sudo make install
cd ..
（4）安装libvpx （自己选择是否安装）
libvp是开源的VP8解码器，属于webM的项目。
sudo wget http://webm.googlecode.com/files/libvpx-v0.9.7-p1.tar.bz2
sudo tar xvjf libvpx-v0.9.7-p1.tar.bz2
cd libvpx-v0.9.7-p1
sudo ./configure --enable-shared --prefix=/usr/local
sudo make
sudo make install
cd ..
（5）安装FFMPEG
sudo wget http://ffmpeg.org/releases/ffmpeg-0.8.10.tar.bz2
sudo tar xvjf ffmpeg-0.8.10.tar.bz2
cd ffmpeg-0.8.10
./configure --enable-gpl --enable-version3 --enable-nonfree --enable-postproc --enable-libfaac --enable-libmp3lame --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libtheora --enable-libvorbis --enable-libvpx --enable-libx264 --enable-libxvid --enable-shared --prefix=/usr/local
sudo make
sudo make install
cd ..
configure过程根据自己的情况开启某部分功能。