from binarytree import tree, bst, Node


class MyNode:
    def __init__(self, value, left=None, right=None, args=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f'{self.value} {self.left} {self.right}'


a = tree(height=4, is_perfect=False)
print(a)
b = bst(height=4, is_perfect=True)
print(b)
root = MyNode(14)
root.left = MyNode(5)
root.right = MyNode(42)
print(root)

print('*' * 50)
bt = bst(height=5, is_perfect=False)
print(bt)
num = int(input('Число для поиска: '))


def search(bin_tree, number, path=''):
    if number == bin_tree.value:
        return f'Число {number} обнаружено по следующему пути:\nКорень{path}'
    if number < bin_tree.value and bin_tree.left is not None:
        return search(bin_tree.left, number, path=f'{path}\nШаг влево')
    if number > bin_tree.value and bin_tree.right is not None:
        return search(bin_tree.right, number, path=f'{path}\nШаг вправо')
    return f'Число {number} отсутсвует'

print(search(bt, num))
