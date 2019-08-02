#! /usr/bin/env python
# -*- coding: utf-8 -*-


from typing import Optional, Union, Any

import zope.interface  # type: ignore


Key = Union[int, float, str, bool]


class INode(zope.interface.Interface):

    key = zope.interface.Attribute(
        "Key which will be used to access stored value"
    )
    value = zope.interface.Attribute(
        "Value is accessed via Key attribute."
        " It stores either reference to an object."
    )


@zope.interface.implementer(INode)
class SinglyNode:
    """Represents singly linked list node

    Provides an implementation to store key, value and next element of node. It
    is representing a storage for singly linked list.
    """

    def __init__(self, key: Key, value: Any):
        self.key = key
        self.value = value
        self.next: Optional[SinglyNode] = None
