AM_LDFLAGS = -lm -lssl -pthread -lcrypto -lcrypt -lapr-1 -laprutil-1
AM_CFLAGS = -D_GNU_SOURCE -DHAVE_OPENSSL -I/usr/include/apr-1

bin_PROGRAMS = ab
ab_SOURCES = ab.c
prefix = /usr/bin
bindir = ${prefix}
