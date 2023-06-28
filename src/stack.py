class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""
    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None

    def __str__(self):
        result = ''
        current_node = self.top
        while current_node is not None:
            result += str(current_node.data) + '\n'
            current_node = current_node.next_node
        else:
            return result[:-1]

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        new_node = Node(data, self.top)
        self.top = new_node

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        last_node = self.top.data
        self.top = self.top.next_node
        return last_node
