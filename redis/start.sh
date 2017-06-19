#！/bin/bash

redisport=6379
exec=/usr/local/bin/redis-server
cliexec=/usr/local/bin/redis-cli

pidfile=/var/run/redis_${redisport}.pid
conf="/etc/redis/${redisport}.conf"

case "$1" in
	start)
		if [ -f $pidfile ]
		then
			echo "$pidfile exists"
		else
			echo "starting redis server"
			$exec $conf
		fi
		;;
	stop)
		if [ ! -f $pidfile ]
		then
			echo "$pidfile does not exists ,process is not running"
		else 
			pid=$(cat $pidfile)
			echo "stoping..."
			$cliexec -p redisport shutdown
			while [ -x /proc/${pid} ]
			do
				echo "waiting for redis to shutdown.."
				sleep 1
			done
			echo "redis stoppde"
		fi
		;;
	*)
		echo "please use start or stop as first argument"
		;;
esac