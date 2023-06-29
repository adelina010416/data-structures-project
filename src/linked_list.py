class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        if type(data) != dict or 'id' not in data.keys():
            raise Exception("Incorrect data type")
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        new_node = Node(data, self.head)
        if self.head:
            new_node.next_node = self.head
        else:
            self.tail = new_node
        self.head = new_node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        new_node = Node(data)
        if self.tail:
            self.tail.next_node = new_node
        else:
            self.head = new_node
        self.tail = new_node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string[1:]

    def to_list(self):
        """
        Возвращает список с данными, содержащимися в односвязном списке LinkedList.
        """
        node = self.head
        if node is None:
            return str(None)
        ll_string = []
        while node:
            ll_string.append(node.data)
            node = node.next_node
        return ll_string

    def get_data_by_id(self, node_id):
        """
        Возвращает первый найденный в LinkedList словарь с ключом 'id',
        значение которого равно переданному в метод значению.
        """
        try:
            node_id = int(node_id)
        except ValueError:
            print("Incorrect data type")
        for i in self.to_list():
            if int(i["id"]) == node_id:
                return i
        return 'DataNotFound'
