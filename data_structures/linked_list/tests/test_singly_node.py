#! /usr/bin/env python
# -*- coding: utf-8 -*-

from zope.interface.verify import verifyClass, verifyObject  # type: ignore

from data_structures.linked_list.node import INode, SinglyNode


def test_that_singly_node_follows_node_interface():
    verifyClass(INode, SinglyNode)


def test_that_singly_node_instance_follows_node_insterface():
    node = SinglyNode(key="test", value="test-value")
    verifyObject(INode, node)


def test_it_is_possible_to_initialize_node():
    data = {
        "key": "test",
        "value": "test-value"
    }
    node = SinglyNode(key=data["key"], value=data["value"])
    assert node.key == data["key"]
    assert node.value == data["value"]
    assert hasattr(node, "next") is True
    assert node.next is None
