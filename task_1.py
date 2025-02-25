class Node:
    def __init__(self, data: int = None):
        self.data = data
        self.next: 'Node' | None = None

class LinkedList:
    def __init__(self):
        self.head: Node | None = None

    # Insert nodes at the beginning
    def insert_at_beginning(self, data: int) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert nodes at the end
    def insert_at_end(self, data: int) -> None:
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    # Delete a node
    def delete_node(self, key: int) -> None:
        cur, prev = self.head, None
        while cur:
            if cur.data == key:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
                return
            prev, cur = cur, cur.next

    # Search for an element
    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    # Reversing a linked list
    def reverse(self) -> None:
        prev, cur = None, self.head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev, cur = cur, next_node
        self.head = prev

    # Insert sorting
    def insertion_sort(self) -> None:
        if not self.head or not self.head.next:
            return

        sorted_list = None
        cur = self.head
        while cur:
            next_node = cur.next
            sorted_list = self._sorted_insert(sorted_list, cur)
            cur = next_node

        self.head = sorted_list

    #  Insert into a sorted list
    def _sorted_insert(self, sorted_head: Node | None, new_node: Node) -> Node:
        if not sorted_head or new_node.data < sorted_head.data:
            new_node.next = sorted_head
            return new_node

        cur = sorted_head
        while cur.next and cur.next.data < new_node.data:
            cur = cur.next

        new_node.next = cur.next
        cur.next = new_node
        return sorted_head

    # Merging two sorted lists
    def merge_sorted_lists(self, llist2: 'LinkedList') -> None:
        dummy = Node()
        tail = dummy
        l1, l2 = self.head, llist2.head

        while l1 and l2:
            if l1.data < l2.data:
                tail.next, l1 = l1, l1.next
            else:
                tail.next, l2 = l2, l2.next
            tail = tail.next

        tail.next = l1 if l1 else l2
        self.head = dummy.next

    # Print a linked list
    def print_list(self) -> None:
        print(self)

    def __str__(self) -> str:
        result, cur = [], self.head
        while cur:
            result.append(str(cur.data))
            cur = cur.next
        return " -> ".join(result) + " -> None"


llist = LinkedList()

# Insert nodes at the beginning
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

# We insert nodes at the end
llist.insert_at_end(20)
llist.insert_at_end(25)

# Print a linked list
print("Linked list:")
llist.print_list()

# Delete the node
llist.delete_node(10)

print("\nLinked list after removing data node 10:")
llist.print_list()

# Search for an element in a linked list
print("\nWe are looking for element 15:")
element = llist.search_element(15)
if element:
    print(element.data)

#  Reversing a linked list
print("\nReversing linked list:")
llist.reverse()
llist.print_list()

# Insert sorting
print("\nSorting linked list (Linked list 1):")
llist.insertion_sort()
llist.print_list()

# Create a second list for merging
llist2 = LinkedList()
llist2.insert_at_end(3)
llist2.insert_at_end(8)
llist2.insert_at_end(12)
print("\nLinked list 2:")
llist2.print_list()

# Merging two sorted lists
print("\nMerged sorted list:")
llist.merge_sorted_lists(llist2)
llist.print_list()