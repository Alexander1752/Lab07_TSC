import pytest
from tree import Tree
import sys
from io import StringIO

@pytest.fixture
def my_tree():
    tree = Tree()
    return tree

def test_tree_add(my_tree):
    """ Test add operation """
    my_tree.add(3)
    my_tree.add(2)
    my_tree.add(5)

    assert my_tree.getRoot().data == 3

def test_tree_structure(my_tree):
    """ Test that tree is a BST """
    my_tree.add(3)
    my_tree.add(2)
    my_tree.add(5)
    my_tree.add(4)

    tmp = sys.stdout
    my_res = StringIO()
    sys.stdout = my_res

    # print to my_res - for testing
    my_tree.printTree()

    sys.stdout = tmp

    assert my_res.getvalue() == '2 \n3 \n4 \n5 \n'

def test_tree_inorder(my_tree):
    """ Test inorder """
    my_tree.add(3)
    my_tree.add(2)
    my_tree.add(5)
    my_tree.add(4)
    my_tree.add(10)
    my_tree.add(15)
    my_tree.add(1)

    tmp = sys.stdout
    my_res = StringIO()
    sys.stdout = my_res

    # print to my_res - for testing
    my_tree.printTree()

    sys.stdout = tmp

    assert my_res.getvalue() == '1 \n2 \n3 \n4 \n5 \n10 \n15 \n'

def test_find1(my_tree):
    """ Test find 1 (find value present in tree) """
    my_tree.add(10)
    res_node = my_tree.find(10)

    assert res_node.data == 10

def test_find2(my_tree):
    """ Test find 2 (find value not present in tree) """
    my_tree.add(10)
    res_node = my_tree.find(22)

    assert res_node is None
