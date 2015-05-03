=========
cmtoolkit
=========

This software is a Python library for building and manipulating `conformal maps
<http://en.wikipedia.org/wiki/Conformal_map>`_. Conformal mapping is an
important tool in solving Laplace's equation - which occur in heat and
diffusion transport problems.

This package is an unofficial port of the (MATLAB) `Conformal Mapping Toolkit
(CMToolkit) <https://github.com/tobydriscoll/conformalmapping>`_, written by
Toby Driscoll.

|build_status|

Installation
============

The latest version of this package can be installed from github

.. code-block:: console

    $ pip install git+git://github.com/AndrewWalker/cmtoolkit

Examples
========

- `Mobius transformation notebook <http://nbviewer.ipython.org/github/AndrewWalker/cmtoolkit/blob/master/notebooks/mobius_grids.ipynb>`_

License
=======

This Python package has been derived from Conformal Mapping Toolkit, but this
port is not associated with the author of that package, or the University of
Delaware in any way. 

Users of this software must comply with the `license <LICENSE>`_ for this package, and the
`CMToolkit's license <LICENSE.conformalmappingtoolbox>`_

.. |build_status| image:: https://api.travis-ci.org/AndrewWalker/cmtoolkit.png
   :target: https://travis-ci.org/AndrewWalker/cmtoolkit
   :alt: Current build status
