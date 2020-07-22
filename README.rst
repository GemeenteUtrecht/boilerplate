==========================
Boilerplate Django project
==========================

:Version: 0.1.0
:Source: https://github.com/GemeenteUtrecht/boilerplate
:Keywords: django, boilerplate
:PythonVersion: 3.8

|build-status| |black|

Boilerplate Django project for prototyping.

Developed by `Maykin Media B.V.`_ for Gemeente Utrecht.

Introduction
============

Gemeente Utrecht embraces Open Source development and combining components from
different software development parties into end products serving their staff.

A number of these projects are based on Django applications started from a
`default-project`_ template. The boilerplate follows the same setup, with a couple of
additions:

- ADFS based Single Sign On
- Frontend toolchain with Utrecht styling

This project serves as a starting point for anyone developing (npm) packages/components
to be used in projects based on Django. It allows you to test your own developments on
a platform that's realistic *and* de-cluttered from project-specific code.

Documentation
=============

See ``INSTALL.rst`` for installation instructions, available settings and
commands.

References
==========

* `Issues <https://github.com/GemeenteUtrecht/boilerplate/issues>`_
* `Code <https://github.com/GemeenteUtrecht/boilerplate>`_


.. |build-status| image:: https://travis-ci.org/GemeenteUtrecht/boilerplate.svg?branch=master
    :alt: Build status
    :target: https://travis-ci.org/GemeenteUtrecht/boilerplate

.. |docs| image:: https://readthedocs.org/projects/gu-django-boilerplate/badge/?version=latest
    :target: https://gu-django-boilerplate.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black


.. _Maykin Media B.V.: https://www.maykinmedia.nl
.. _default-project: https://bitbucket.org/maykinmedia/default-project
