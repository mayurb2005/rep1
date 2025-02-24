import sys

class Node:
    
    def __init__(self,data = 0):
        self.left = None
        self.right = None
        self.data = data
        print(f"Node with data {data} is created")

class Bst:

    def __init__(self, root):
        self.root = root
        print("An  empty Node is created")

    def add_node(self):
        data = int(input("Enter data of the new node: "))
        node = Node(data)
        if self.root is None :
            self.root = node
            return
        temp1 = self.root
        temp2 = None
        while temp1 != None:
            temp2 = temp1
            if data < temp1.data :
                temp1 = temp1.left
            else : 
                temp1 = temp1.right
        if data < temp2.data :
            temp2 = temp2.left
        else : 
            temp2 = temp2.right
    def add_node_recursive(self, root, data):
        if self.root is None: 
            return Node(data)
        
        if data < root.data:
            root.left = self.add_node_recursive(root.left, data) 
        else:
            root.right = self.add_node_recursive(root.right, data)  

        return root  

    def delete_node(self):
        pass

    def inorder(self):
        pass

    def preorder(self):
        pass

    def postorder(self):
        pass

    def search_node(self):
        pass

class Menu:
    def __init__(self): 
        pass
    def get_menu(self, bst):
        menu = {
            1 : bst.add_node,
            2 : bst.delete_node,
            3 : bst.inorder,
            4 : bst.preorder,
            5 : bst.postorder,
            6 : bst.search_node,
            7 : bst.add_node_recursive,
            8 : self.end_of_program
        }
        return menu
    def end_of_program(self):
        sys.exit("Exit")
    def invalid_choice(self):
        print("Invalid choice")
    def run_menu(self):
        bst = Bst(root)
        while(True):
            choice = int(input("1.Add Node, 2.delete node, 3.Inorder,4.Preorder, 5.Postoredr, 6.Search a node, 7.Add node Recursively ,-1.To Exit: "))
            if choice == -1 :
                break
            menu = self.get_menu(bst)
            menu.get(choice, self.invalid_choice)()

def start_app():        
    menu = Menu()
    menu.run_menu()
start_app()