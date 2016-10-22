#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_markovmc
----------------------------------

Tests for `markovmc` module.
"""


import sys
import unittest
from contextlib import contextmanager
from click.testing import CliRunner

from markovmc import markovmc




class TestMarkovmc(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_something(self):
        pass

    # def test_command_line_interface(self):
    #    runner = CliRunner()
    #    result = runner.invoke(cli.main)
    #    assert result.exit_code == 0
    #    assert 'markovmc.cli.main' in result.output
    #    help_result = runner.invoke(cli.main, ['--help'])
    #    assert help_result.exit_code == 0
    #    assert '--help  Show this message and exit.' in help_result.output

    def test_theta_out(self):
        import networkx as nx
        G = nx.Graph()
        G.add_edges_from([(0,1),(1,2),(2,3),(3,4),(4,5)], weight = 3)
        theta = markovmc.theta(G,1)
        self.assertIsInstance(theta, int)

    def test_theta_one_node(self):
        import networkx as nx
        G = nx.Graph()
        G.add_node(1)
        theta = markovmc.theta(G,1)
        self.assertTrue(theta == 0)

    def test_theta_disconnect(self):
        import networkx as nx
        G = nx.Graph()
        G.add_node(1)
        G.add_node(2)
        self.assertRaises(RuntimeError, lambda: markovmc.theta(G,1))

    def test_grapher_out(self):
        self.assertIsInstance(markovmc.grapher([(0,0),(1,2),(2,2),(3,3),(4,4),(5,5),(6,6)],20,1,1),list)
