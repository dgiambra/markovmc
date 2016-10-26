===============================
markovmc
===============================



.. image:: https://img.shields.io/travis/dgiambra/markovmc.svg
        :target: https://travis-ci.org/dgiambra/markovmc


.. image:: https://pyup.io/repos/github/dgiambra/markovmc/shield.svg
     :target: https://pyup.io/repos/github/dgiambra/markovmc/
     :alt: Updates


A Markov Chain Monte Carlo Algorithm


* Free software: MIT license
* Documentation: https://markovmc.readthedocs.io.


Features
--------
* A software package containing a main grapher function and multiple functions for meaningful statistical analysis

* Grapher: given a distribution of nodes, this algorithm calculates the most likely graphs to be produced from those nodes based on relative probability.
  *   Uses the Metripolis-Hastings Algorithm
  *   To use, call markovmc.grapher(x, N, r, T)
  *    x: list of tuples representing nodes
  *   N: int, number of iterations
  *   r & T : int, adjustable Parameters
  *   Outputs a list of graphs, each one is the more likely graph of its pair

* topOnePercent: given a list of elements, this function returns the 1% of elements most likely to occur
  *   To use, call markovmc.topOnePercent(graphs)
  *   graphs: list of graphs
  *   Outputs a list of graphs, with the last graph being th most likely of the 1%

* expectedDegree: given a list of graphs and a node, this computes the expected degree of the node
  *   To use, call markovmc.expectedDegree(graphs, node):
  *   graphs: list of graphs
  *   node: node of interest
  *   Output a value for expected degree

* expectedNumberofEdges: given a list of graphs, computes the expected number of edges
  *   To use, call markovmc.expectedNumberofEdges(graphs)
  *   graphs: list of graphs
  *   Outputs a value for expected number of edges

* expectedShortestPathLength: given a list of graphs and two nodes, it computes the average shortest path length between the two
  *   To use, call markovmc.expectedShortestPathLength(graphs, nodeA, nodeB)
  *   graphs: list of graphs
  *   nodeA: first node
  *   nodeB: second nodes
  *   Outputs a value for expectedShortestPathLength

Credits
---------
* Dominic Giambra
This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
