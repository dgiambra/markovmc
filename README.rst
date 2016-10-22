===============================
markovmc
===============================


.. image:: https://img.shields.io/pypi/v/markovmc.svg
        :target: https://pypi.python.org/pypi/markovmc

.. image:: https://img.shields.io/travis/dgiambra/markovmc.svg
        :target: https://travis-ci.org/dgiambra/markovmc

.. image:: https://readthedocs.org/projects/markovmc/badge/?version=latest
        :target: https://markovmc.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/dgiambra/markovmc/shield.svg
     :target: https://pyup.io/repos/github/dgiambra/markovmc/
     :alt: Updates
     
.. image:: https://coveralls.io/repos/github/dgiambra/markovmc/badge.svg?branch=develop
    :target: https://coveralls.io/github/dgiambra/markovmc?branch=develop


A Markov Chain Monte Carlo Algorithm


* Free software: MIT license
* Documentation: https://markovmc.readthedocs.io.


Features
--------

* Given a distribution of nodes, this algorithm calculates the most likely graphs to be produced from those nodes based on relative probability.
* Uses the Metripolis-Hastings Algorithm
* To use, call markovmc.grapher(x, N, r, T)
* x: list of tuples representing nodes
* N: int, number of iterations
* r & T : int, adjustable Parameters
* Outputs a list of graphs, each one is the more likely graph of its pair

Credits
---------
* Dominic Giambra
This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
