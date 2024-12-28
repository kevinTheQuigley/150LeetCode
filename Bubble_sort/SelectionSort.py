class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def selection_sort(self):
        start = self.head
        for i in range(self.length -1):
            print(f"--------Break for {i},starting with {start.value}--------")
            self.print_list()
            current = start 
            minValue = current.value
            for j in range(i,self.length-1):
                nextOne = current.next
                if minValue >nextOne.value:
                    minValue = nextOne.value
                    swapList = [current,nextOne]
                current = current.next

                
            if minValue <start.value:
                swapPrevious = swapList[0]
                swapStart = swapList[1]
                if start == self.head:
                    
                    temp = start.next
                    start.next = swapStart.next
                    swapStart.next = temp
                    
                    self.head = swapStart
                    swapPrevious.next = start
                    start = swapStart

                else:
                    temp = start.next
                    start.next = swapStart.next
                    swapStart.next = temp
                    
                    previous.next = swapStart
                    swapPrevious.next = start
                    start  = swapStart
                    
                    
                
                    
                
                
            previous = start
            start = start.next
            
        
        
        
    # WRITE SELECTION_SORT METHOD HERE #
    #                                  #
    #                                  #
    #                                  #
    #                                  #
    ####################################



my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.selection_sort()

print("\nSorted Linked List:")
my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    Linked List Before Sort:
    4
    2
    6
    5
    1
    3

    Sorted Linked List:
    1
    2
    3
    4
    5
    6

"""

