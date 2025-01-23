class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next
        
class LinkedList:
    
    def __init__(self):
        self.head = None
    
    #Inserting at beginning of list    
    def insert_at_beginning(self, data):
        self.head = Node(data, self.head)
        
    #Inserting at end of the list
    def insert_at_end(self, data):
        
        if self.head is None:
            self.insert_at_beginning(data)
            return
            
        itr = self.head
        
        while itr.next:
            itr = itr.next
            
        itr.next = Node(data, None)
        
    #Insert values based on a list
    def insert_values(self, lst):
        
        self.head = None
        
        for data in lst:
            self.insert_at_end(data)
            
    #Insert at index
    def insert_at_index(self, index, data):
        
        if index < 0:
            print('index negative')
            return
    
        if index >= self.get_length():
            print('index doesnt exist')
            return
    
        if index ==0:
            self.insert_at_beginning(data)
            return
        
        counter = 0
        itr = self.head
        
        while (itr):
            if counter == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            
            itr = itr.next
            counter += 1

        
        
        
    
    #Remove node at index
    def remove_at_index(self, index):
        if index < 0:
            print('index negative')
            return
        
        if index >= self.get_length():
            print('index doesnt exist')
            return
        
        
        
        if (index == 0):
            self.head = self.head.next
            return
        
        counter = 0
        itr = self.head
        
        while (itr):
            if counter == index - 1:
                itr.next = itr.next.next
                break
            
            itr = itr.next
            counter += 1

        
        
            
            
            
    #Printing the list
    def print(self):
        
        if self.head is None:
            print("List empty")
            return
            
        itr = self.head
        list_printed = ''
        
        while itr:
            list_printed += str(itr.data) + '---->'
            itr = itr.next
        
        print(list_printed)
    
    #Get length of list
    def get_length(self):
        
        counter = 0
        
        itr = self.head
        
        while itr:
            counter += 1
            itr = itr.next
            
        return counter
    
      
        

def main():
    
    linked_list = LinkedList()
    linked_list.insert_values([5, 6,7,8])
    linked_list.print()
    linked_list.insert_at_index(2, 10)
    linked_list.print()
    

if __name__ == '__main__':
    main()
