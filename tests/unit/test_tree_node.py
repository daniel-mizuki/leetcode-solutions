import pytest

from leetcode_solutions.util.tree_node import TreeNode


@pytest.mark.parametrize(
    "val, left, right",
    [
        (1, None, None),
        (1, TreeNode(2), None),
        (1, None, TreeNode(2)),
        (1, TreeNode(2), TreeNode(3)),
    ],
)
def test_tree_node_constructor(val, left, right):
    tree_node = TreeNode(val, left, right)
    assert tree_node.val == val
    assert tree_node.left == left
    assert tree_node.right == right


@pytest.mark.parametrize(
    "tree_node_1, tree_node_2",
    [
        (None, None),
        (TreeNode(1), TreeNode(1)),
        (TreeNode(1, None, TreeNode(2)), TreeNode(1, None, TreeNode(2))),
        (
            TreeNode(1, TreeNode(2), TreeNode(3)),
            TreeNode(1, TreeNode(2), TreeNode(3)),
        ),
        (
            TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(4)),
            TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(4)),
        ),
    ],
)
def test_tree_node_equal(tree_node_1, tree_node_2):
    assert tree_node_1 == tree_node_2


@pytest.mark.parametrize(
    "tree_node_1, tree_node_2",
    [
        (None, TreeNode(1)),
        (TreeNode(1), None),
        (TreeNode(1), TreeNode(2)),
        (TreeNode(1, None, TreeNode(2)), TreeNode(1, None, TreeNode(3))),
        (
            TreeNode(1, None, TreeNode(2)),
            TreeNode(1, None, TreeNode(2, None, TreeNode(3))),
        ),
    ],
)
def test_tree_node_not_equal(tree_node_1, tree_node_2):
    assert tree_node_1 != tree_node_2


@pytest.mark.parametrize(
    "lst, expected",
    [
        ([], None),
        ([1], TreeNode(1)),
        ([1, None, 2], TreeNode(1, None, TreeNode(2))),
        ([1, 2, 3], TreeNode(1, TreeNode(2), TreeNode(3))),
        (
            [1, 2, 3, 4, 5, 6],
            TreeNode(
                1,
                TreeNode(2, TreeNode(4), TreeNode(5)),
                TreeNode(3, TreeNode(6), None),
            ),
        ),
    ],
)
def test_tree_node_from_list(lst, expected):
    assert TreeNode.from_list(lst) == expected


@pytest.mark.parametrize(
    "tree_node, expected",
    [
        (TreeNode.from_list([1]), [1]),
        (TreeNode.from_list([1, 2, 3]), [1, 2, 3]),
        (TreeNode.from_list([1, 2, 3, 4, 5, 6]), [1, 2, 3, 4, 5, 6]),
        (TreeNode.from_list([1, None, 2]), [1, None, 2]),
    ],
)
def test_tree_node_to_list(tree_node, expected):
    assert tree_node.to_list() == expected


@pytest.mark.parametrize(
    "tree_node, expected",
    [
        (TreeNode.from_list([1]), "TreeNode: [1]"),
        (TreeNode.from_list([1, 2, 3]), "TreeNode: [1, 2, 3]"),
        (TreeNode.from_list([1, 2, 3, 4, 5, 6]), "TreeNode: [1, 2, 3, 4, 5, 6]"),
        (TreeNode.from_list([1, None, 2]), "TreeNode: [1, None, 2]"),
    ],
)
def test_tree_node_repr(tree_node, expected):
    assert repr(tree_node) == expected
