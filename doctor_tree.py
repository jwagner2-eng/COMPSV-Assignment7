class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    def __init__(self):
        self.root = None

    def insert(self, parent_name, doctor_name, side, current_node=None):
        if self.root is None:
            print("Error: Add a head doctor first.")
            return False

        if current_node is None:
            current_node = self.root

        if current_node.name == parent_name:
            if side == "left":
                if current_node.left is None:
                    current_node.left = DoctorNode(doctor_name)
                    print(f"{doctor_name} added to the LEFT of {parent_name}")
                else:
                    print("Error: Left side is already taken.")

            elif side == "right":
                if current_node.right is None:
                    current_node.right = DoctorNode(doctor_name)
                    print(f"{doctor_name} added to the RIGHT of {parent_name}")
                else:
                    print("Error: Right side is already taken.")

            else:
                print("Error: Choose left or right.")

            return True

        if current_node.left is not None:
            if self.insert(parent_name, doctor_name, side, current_node.left):
                return True

        if current_node.right is not None:
            if self.insert(parent_name, doctor_name, side, current_node.right):
                return True

        return False


    def preorder(self, node):
        if node is None:
            return []

        return (
            [node.name]
            + self.preorder(node.left)
            + self.preorder(node.right)
        )


    def inorder(self, node):
        if node is None:
            return []

        return (
            self.inorder(node.left)
            + [node.name]
            + self.inorder(node.right)
        )

    def postorder(self, node):
        if node is None:
            return []

        return (
            self.postorder(node.left)
            + self.postorder(node.right)
            + [node.name]
        )




# Test your DoctorTree and DoctorNode classes here


tree = DoctorTree()
tree.root = DoctorNode("Dr. Croft")

tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
tree.insert("Dr. Croft", "Dr. Phan", "left")
tree.insert("Dr. Phan", "Dr. Carson", "right")
tree.insert("Dr. Phan", "Dr. Morgan", "left")

print("\nPreorder:")
print(tree.preorder(tree.root))

print("\nInorder:")
print(tree.inorder(tree.root))

print("\nPostorder:")
print(tree.postorder(tree.root))

# Test edge cases
print("\nTesting missing manager:")
print(tree.insert("Dr. Smith", "Dr. Lee", "left"))

print("\nTesting invalid side:")
tree.insert("Dr. Croft", "Dr. Lee", "middle")

print("\nTesting empty tree:")
empty_tree = DoctorTree()
print(empty_tree.preorder(empty_tree.root))
print(empty_tree.inorder(empty_tree.root))
print(empty_tree.postorder(empty_tree.root))
