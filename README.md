Overview
========

This is a simple example of using the OpenGL Core Profile (aka "modern" OpenGL) with PyQt, numpy, and PyOpenGL.

The [DemoCanvas](https://github.com/prideout/coregl-python/blob/master/demoCanvas.py) class is a good starting point to explore the demo code.  It derives from [Canvas](https://github.com/prideout/coregl-python/blob/master/canvas.py) which derives from `QGLWidget`.

I've provided `translation`, `look_at`, and `projection` functions in [utility.py](https://github.com/prideout/coregl-python/blob/master/utility.py).  For a more thorough set of affine transformations wih numpy, take a look at some code from Christoph Gohlke:

<http://www.lfd.uci.edu/~gohlke/code/transformations.py.html>

Build Instructions for Mac
==========================

Install Qt for Mac
----

    brew install qt

Hack, Build, and Install PyQt for Mac
----

Here's some hackery to get core profile to work on mac.

1. wget http://downloads.sf.net/project/pyqt/sip/sip-4.13.3/sip-4.13.3.tar.gz
2. build & install sip in the usual way
3. wget http://downloads.sf.net/project/pyqt/PyQt4/PyQt-4.9.4/PyQt-mac-gpl-4.9.4.tar.gz

Next you'll build PyQt using some hacks I've provided to get core profile working on Lion.  Qt doesn't support core profile for Lion at the time of this writing.

    tar xvf PyQt-mac-gpl-4.9.4.tar.gz
    mv PyQt-mac-gpl-4.9.4 PyQt4
    cp -r pyqt-hacks/ PyQt4 ; # trailing slash required to overlay files
    cd PyQt4
    python ./configure.py --confirm-license \
           --bindir=/usr/local/Cellar/pyqt/4.9.4/bin \
           --destdir=/usr/local/Cellar/pyqt/4.9.4/lib/python2.7/site-p
    make -j2
    sudo make install
    cd ..; mv PyQt4 PyQt4.done

After the `make`, you might see an error about `virtual` being outside a class.  Sometimes `%TypeCode` doesn't work as expected and sip places the `chooseMacVisual` method outside the class declaration, in which case you'll need to hand-edit the generated file (`./QtOpenGL/sipQtOpenGLQGLContext.cpp`) and copy-paste it into the class declaration.
