class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
        
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        
    def get_level(self):
        
        counter = 0
        curr = self.parent
        while curr:
            counter += 1
            curr = curr.parent
        return counter
    
    def print_tree(self):
        prefix = '' * self.get_level()
        print(prefix + self.data)
        
        if (len(self.children) == 0):
            return
        
        for child in self.children:
            child.print_tree()
        
        

def main():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)
    
    return root
    
    
if __name__ == '__main__':
    root = main()
    root.print_tree()
    pass
        