#!/bin/bash

function clean(){
    make distclean
    rm -rf stamp-h1 config.log Makefile compile config.h* config.status aclocal.m4 configure depcomp missing autom4te.cache config.h.in install-sh
    find ./ -name Makefile.in -exec rm {} \;
}

function build(){
    make distclean
    autoreconf -fiv
    ./configure
    make
}

function test(){
    src/ab -c2 -n100 https://g.cn/
}

case "${1}" in
    'build')
        build ;;
    'clean')
        clean ;;
    'test')
        test ;;
          *)
        echo "Usage: $0 { build | clean | test }"
        ;;
esac
