class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        new_node = Node(data)
        try:
            self.tail.next_node = new_node
        except AttributeError:
            self.head = new_node
        self.tail = new_node

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        try:
            deleted_node = self.head.data
            self.head = self.head.next_node
        except AttributeError:
            return None
        return deleted_node

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        result = ''
        current_node = self.head
        while current_node is not None:
            result += str(current_node.data) + '\n'
            current_node = current_node.next_node
        else:
            return result[:-1]
