#! /usr/bin/env python
# -*- coding: utf-8 -*-

class Node:
    """A LinkedList Node

    This implementation of Node is for storing information of Singley Linked
    List.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class SinglyLinkedList:

    def __init__(self):
        self.head = None
