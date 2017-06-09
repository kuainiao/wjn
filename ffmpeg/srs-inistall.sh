git clone https://github.com/ossrs/srs
cd srs/trunk
./configure && make
./objs/srs -c conf/rtmp.conf

service iptables stop
chkconfig iptables off