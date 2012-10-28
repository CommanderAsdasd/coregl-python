Overview
========

This is a simple example of using the OpenGL Core Profile (aka "modern" OpenGL) with PyQt, numpy, and PyOpenGL.

Build Instructions for Mac
==========================

Install Qt for Mac
----

    brew install qt

Hack, Build, and Install PyQt for Mac
----

Needs some hackery to get core profile to work on mac!

1. wget http://downloads.sf.net/project/pyqt/sip/sip-4.13.3/sip-4.13.3.tar.gz
2. build & install sip in the usual way
3. wget http://downloads.sf.net/project/pyqt/PyQt4/PyQt-4.9.4/PyQt-mac-gpl-4.9.4.tar.gz
4. build PyQt with some hacks:

    tar xvf PyQt-mac-gpl-4.9.4.tar.gz
    mv PyQt-mac-gpl-4.9.4 PyQt4
    cp -r pyqt-hacks/ PyQt4 ; # trailing slash required to overlay files
    cd PyQt4
    python ./configure.py --confirm-license --bindir=/usr/local/Cellar/pyqt/4.9.4/bin --destdir=/usr/local/Cellar/pyqt/4.9.4/lib/python2.7/site-p
    make
    sudo make install

QED