#!/bin/bash
. /etc/init.d/functions

start() {
        echo -n "Starting Scoreboard: "
        sudo python3 /Scoreboard/nhl_goal_light.py
}

stop() {
        echo -n "Shutting down all python process: "
        sudo pkill python3
}

case "$1" in
    start)
        start
        ;;
    stop)
        stop
        ;;
    status)
    echo "Status unimplemented"
    ;;
    restart)
        stop
        start
        ;;
    *)
        echo "Usage: <servicename> {start|stop|restart}"
        exit 1
        ;;
esac
exit $?