# ApacheBench-standalone
ApacheBench standalone - an Apache HTTP Server benchmark tool, known as <b>ab</b> in [apache/httpd](https://github.com/apache/httpd)

---
## Requirement
* gcc / clang
* openssl-devel
* apr-util-devel (apr-devel included)

## Installation
#### Make and install
```bash
make
make install
```
#### Build RPM file on Linux
```bash
rpmbuild -tb ab-<version>.tar.gz
```

## Basic Usage
```bash
ab -c10 -n100 https://g.cn/
```

## Source
Upstream [apache/httpd](https://github.com/apache/httpd) version is from latest tag of [httpd](https://github.com/apache/httpd)
* ap_release.h  - httpd/include/ap_release.h
* ab.c          - httpd/support/ab.c
* docs/man/ab.1 - httpd/docs/man/ab.1

## About Version
ApacheBench seems to have its own version. However it doesn't changes very often.
So we decide to tag this project with the version of httpd that sourced from.
```bash
ab -V   # This is ApacheBench, Version 2.3 <$Revision$>
```

## About Windows
The following lines are commented in ab.c, so Windows is not supported.
```
#if !defined(WIN32) && !defined(NETWARE)
#include "ap_config_auto.h"
#endif
```

## About APR - Apache Portable Runtime
Since [apache/httpd](https://github.com/apache/httpd) is developed based on [apr](https://github.com/apache/apr) / [apr-util](https://github.com/apache/apr-util), ApacheBench should be built with apr-devel and apr-util-devel of official yum packages repository.
You can also build with newer version of apr yourself. (More details in README file of [apr](https://github.com/apache/apr)).
```bash
# Building APR RPM files on Linux
rpmbuild -tb apr-<version>.tar.bz2          # latest version - 1.5.2
rpmbuild -tb apr-util-<version>.tar.bz2     # latest version - 1.5.4
```
