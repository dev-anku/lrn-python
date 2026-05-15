class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert_at_beg(head, val):
    new_node = Node(val)
    new_node.next = head
    return new_node


def insert_at_end(head, val):
    new_node = Node(val)

    if head is None:
        return new_node

    temp = head
    while temp.next:
        temp = temp.next
    temp.next = new_node

    return head


def delete_node_by_value(head, val):
    if head is None:
        return None

    if head.data == val:
        return head.next

    temp = head
    while temp.next:
        if temp.next.data == val:
            temp.next = temp.next.next
            return head
        temp = temp.next

    print("Value not found")
    return head


def print_list(head):
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("NULL")


head = None

nodes = int(input("Number of Nodes: "))
for _ in range(nodes):
    val = int(input("Enter values: "))
    head = insert_at_end(head, val)

print_list(head)

to_delete = int(input("Enter value to delete: "))
head = delete_node_by_value(head, to_delete)
print_list(head)
