#! /usr/bin/env python
# -*- coding: utf-8 -*-


from typing import Any

import zope.interfaces  # type: ignore

from .types import Key


class ILinkedList(zope.interfaces.Interface):

    def insert(key: Key, value: Any) -> None:
        pass

    def delete(value: Any) -> None:
        pass

    def search(key: Key) -> Any:
        pass


@zope.interfaces.implements(ILinkedList)
class SinglyLinkedList:
    pass
