#!/bin/bash
function assign(){  export $1=$2;}
function start(){
    assign PORT $1 $PORT 4321 ; shift
    echo PORT $PORT
    cd $DIR; echo $PORT > g/port
    pr3 .<jobs.txt >> g/pgid;}
function stop(){ cd $DIR; kill -INT -`cat g/pgid`;}
case $0 in
    *.sh) echo "Don't run me, only source me."; exit 2;;
esac
export DIR=$(realpath $(dirname $BASH_SOURCE)); cd $DIR
case $1 in
    start) shift ; action=start;;
    stop)  shift ; action=stop;;
esac
source defaults.sh
source local.sh
case $action in
    start) start $* ;;
    stop)  stop  ;;
esac
