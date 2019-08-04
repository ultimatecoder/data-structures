#! /usr/bin/env python
# -*- coding: utf-8 -*-

from node import Node


def test_node_add_child():
    key = "apple"
    node = Node()
    for key_character in key:
        node.add_child(key_character)
        assert key_character in node.children
        assert isinstance(node.children[key_character], Node)
        assert node.children[key_character].children == {}
