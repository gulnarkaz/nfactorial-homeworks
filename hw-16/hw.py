from typing import List, Any, Dict, Set, Generator

class StaticArray:
    def __init__(self, capacity: int):
        """
        Initialize a static array of a given capacity.
        """
        self.capacity = capacity
        self.array = [None] * capacity 

    def set(self, index: int, value: int) -> None:
        """
        Set the value at a particular index.
        """
        if 0 <= index < self.capacity:
            self.array[index] = value 
        else:
            raise IndexError("Index out of bounds") 

    def get(self, index: int) -> int:
        """
        Retrieve the value at a particular index.
        """
        if 0 <= index < self.capacity:
            return self.array[index]
        else:
            raise IndexError("Index out of bounds")
        

class DynamicArray:
    def __init__(self):
        """
        Initialize an empty dynamic array.
        """
        self.array = []

    def append(self, value: int) -> None:
        """
        Add a value to the end of the dynamic array.
        """
        self.array.append(value)

    def insert(self, index: int, value: int) -> None:
        """
        Insert a value at a particular index.
        """
        if index < 0 or index > len(self.array):
            raise IndexError("Index out of boundary")
        self.array.insert(index, value)

    def delete(self, index: int) -> None:
        """
        Delete the value at a particular index.
        """
        if index < 0 or index >= len(self.array):
            raise IndexError("Index out of boundary")
        self.array.pop(index)
        
    def get(self, index: int) -> int:
        """
        Retrieve the value at a particular index.
        """
        if index < 0 or index >= len(self.array):
            raise IndexError("Index out of boundary")
        return self.array[index]
     
     
     
class Node:
    def __init__(self, value: int):
        """
        Initialize a node.
        """
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        """
        Initialize an empty singly linked list.
        """
        self.head = None
        self.tail = None 
        
    def append(self, value: int) -> None:
        """
        Add a node with a value to the end of the linked list.
        """
        node = Node(value)
        
        if not self.head:     # if list empty
            self.head = node
            return
        
        current = self.head    # if list not empty
        while current.next:
            current = current.next 
        current.next = node
        
    def insert(self, position: int, value: int) -> None:
        """
        Insert a node with a value at a particular position.
        """
        node = Node(value)
        
        if position == 0:   # insert on head position for O(1)
            node.next = self.head 
            self.head = node
            return
         
        current = self.head # insert on any index if position > 0 for O(n) time compl
        index = 0  # counter for index
            
        while current and index < position - 1:
            current = current.next
            index += 1
            
        if current:
            node.next = current.next
            current.next = node
        else:
            print("Position out of range")    
                     

    def delete(self, value: int) -> None:
        """
        Delete the first node with a specific value.
        """
        current = self.head
        
        if not current:
            print("List is empty")
        if current.value == value:
            self.head = current.next
            return
        while current.next and current.next.value != value:
            current = current.next
            
        if current.next:
            current.next = current.next.next
        else:
            print(f"{value} not found in list")
            
            
    def find(self, value: int) -> Node:
        """
        Find a node with a specific value.
        """
        current = self.head
        
        while current:
            if current.value == value:
                return current 
            current = current.next
        return None

    def size(self) -> int:
        """
        Returns the number of elements in the linked list.
        """
        current = self.head
        size = 0
        while current:
            current = current.next
            size += 1
        return size
    def is_empty(self) -> bool:
        """
        Checks if the linked list is empty.
        """
        return self.head is None
    def print_list(self) -> None:
        """
        Prints all elements in the linked list.
        """
        current = self.head
        while current:
            print(current.value)
            current = current.next
            
    def reverse(self) -> None:
        """
        Reverse the linked list in-place.
        """
        prev = None
        current = self.head
        while current:
            node = current.next
            current.next = prev
            prev = current
            current = node
        self.head = prev
        
    def get_head(self) -> Node:
        """
        Returns the head node of the linked list.
        """
        return self.head # O(1)
    
    def get_tail(self) -> Node:
        """
        Returns the tail node of the linked list.
        """
        current = self.head
        while current and current.next:
            current = current.next
        return current

class DoubleNode:
    def __init__(self, value: int, next_node = None, prev_node = None):
        """
        Initialize a double node with value, next, and previous.
        """
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

class DoublyLinkedList:
    def __init__(self):
        """
        Initialize an empty doubly linked list.
        """
        self.head = None
        self.tail = None
        self.size = 0
        
    def append(self, value: int) -> None:
        """
        Add a node with a value to the end of the linked list.
        """
        node = DoubleNode(value)
        if self.tail:
            self.tail.next_node = node
            node.prev_node = self.tail
            self.tail = node
        else:
            self.head = self.tail = node
        self.size += 1

    def insert(self, position: int, value: int) -> None:
        """
        Insert a node with a value at a particular position.
        """
        if position < 0 or position > self.size:
            raise IndexError("Invalid position")
        
        node = DoubleNode(value) 
        
        if position == 0:
            if self.head:
                node.next_node = self.head
                self.head.prev_node = node
                self.head = node 
            else:
                self.head = self.tail = node 
        elif position == self.size:
            self.append(value)
        else: 
            current = self.head
            for _ in range(position):
                current = current.next_node
            node.prev_node = current.prev_node
            node.next_node = current
            if current.prev_node:
                current.prev_node.next_node = node
            current.prev_node = node
        self.size += 1
    def delete(self, value: int) -> None:
        """
        Delete the first node with a specific value.
        """
        
        current = self.head  # Начинаем с головы списка
        while current:  # Идем по списку, пока не дойдем до конца
            if current.value == value:  # Нашли узел с нужным значением
                if current.prev_node:  # Если узел не первый
                    current.prev_node.next_node = current.next_node  # Пропускаем удаляемый узел
                if current.next_node:  # Если узел не последний
                    current.next_node.prev_node = current.prev_node  # Пропускаем удаляемый узел
                if current == self.head:  # Если это был первый узел
                    self.head = current.next_node  # Голова списка сдвигается на следующий узел
                if current == self.tail:  # Если это был последний узел
                    self.tail = current.prev_node  # Хвост списка сдвигается на предыдущий узел
                self.size -= 1  # Уменьшаем размер списка
                return  # Выход из функции, так как мы нашли и удалили элемент
            current = current.next_node  # Переходим к следующему узлу
    
        raise ValueError("Value not found")  # Если не нашли элемент с таким значением

    def find(self, value: int) -> DoubleNode:
        """
        Find a node with a specific value.
        """
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next_node
        raise ValueError("Value nott found")
    

    def size(self) -> int:
        """
        Returns the number of elements in the linked list.
        """
        return self.size
    def is_empty(self) -> bool:
        """
        Checks if the linked list is empty.
        """
        return self.size == 0 
    def print_list(self) -> None:
        """
        Prints all elements in the linked list.
        """
        current = self.head
        while current:
            print(current.value)
            current = current.next_node
        print()
    def reverse(self) -> None:
        """
        Reverse the linked list in-place.
        """
        current = self.head
        while current:
            current.prev_node, current.next_node = current.next_node, current.prev_node
            current = current.prev_node  # Переходим к следующему узлу
        self.head, self.tail = self.tail, self.head  # Меняем голову и хвост местами
        
    def get_head(self) -> DoubleNode:
        """
        Returns the head node of the linked list.
        """
        return self.head
    def get_tail(self) -> DoubleNode:
        """
        Returns the tail node of the linked list.
        """
        return self.tail


class Queue:
    def __init__(self):
        """
        Initialize an empty queue.
        """
        self.queue = []
    def enqueue(self, value: int) -> None:
        """
        Add a value to the end of the queue.
        """
        self.queue.append(value)
    def dequeue(self) -> int:
        """
        Remove a value from the front of the queue and return it.
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.queue.pop(0)
    
    def peek(self) -> int:
        """
        Peek at the value at the front of the queue without removing it.
        """
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.queue[0]
    def is_empty(self) -> bool:
        """
        Check if the queue is empty.
        """
        return len(self.queue) == 0
    
class TreeNode:
    def __init__(self, value: int):
        """
        Initialize a tree node with value.
        """

class BinarySearchTree:
    def __init__(self):
        """
        Initialize an empty binary search tree.
        """

    def insert(self, value: int) -> None:
        """
        Insert a node with a specific value into the binary search tree.
        """

    def delete(self, value: int) -> None:
        """
        Remove a node with a specific value from the binary search tree.
        """

    def search(self, value: int) -> TreeNode:
        """
        Search for a node with a specific value in the binary search tree.
        """

    def inorder_traversal(self) -> List[int]:
        """
        Perform an in-order traversal of the binary search tree.
        """
    
    def size(self) -> int:
        """
        Returns the number of nodes in the tree.
        """

    def is_empty(self) -> bool:
        """
        Checks if the tree is empty.
        """

    def height(self) -> int:
        """
        Returns the height of the tree.
        """

    def preorder_traversal(self) -> List[int]:
        """
        Perform a pre-order traversal of the tree.
        """

    def postorder_traversal(self) -> List[int]:
        """
        Perform a post-order traversal of the tree.
        """

    def level_order_traversal(self) -> List[int]:
        """
        Perform a level order (breadth-first) traversal of the tree.
        """

    def minimum(self) -> TreeNode:
        """
        Returns the node with the minimum value in the tree.
        """

    def maximum(self) -> TreeNode:
        """
        Returns the node with the maximum value in the tree.
        """
    
    def is_valid_bst(self) -> bool:
        """
        Check if the tree is a valid binary search tree.
        """

def insertion_sort(lst: List[int]) -> List[int]:
    pass

def selection_sort(lst: List[int]) -> List[int]:
    pass

def bubble_sort(lst: List[int]) -> List[int]:
    pass

def shell_sort(lst: List[int]) -> List[int]:
    pass

def merge_sort(lst: List[int]) -> List[int]:
    pass

def quick_sort(lst: List[int]) -> List[int]:
    pass
