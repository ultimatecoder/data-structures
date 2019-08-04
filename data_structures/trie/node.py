#! /usr/bin/env python
# -*- coding: utf-8 -*-

import zope.interface


class INode(zope.interface.Interface):

    children = zope.interface.Attribute(
        """A collection of child nodes"""
    )

    def add_child(character_of_key: str) -> None:
        pass

    def is_leaf() -> bool:
        pass


@zope.interface.Implement(INode)
class Node:
    pass


class NodeFactory:
    pass
