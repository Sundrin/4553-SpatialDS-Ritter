import random

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.p = None

    def __repr__(self):
        return "< %s %s >" % (self.key,self.p)

    def __str__(self):
        return "< %s %s >" % (self.key,self.p)

class BinaryTree:
    def __init__(self):
        self.root = None

    def length(self):
        return self.size

    def inorder(self, node):
        if node == None:
            return None
        else:
            self.inorder(node.left)
            print node.key
            self.inorder(node.right)

    def search(self, k):
        node = self.root
        while node != None:
            if node.key == k:
                return node
            if node.key > k:
                node = node.left
            else:
                node = node.right
        return None

    def minimum(self, node):
        x = None
        while node.left != None:
            x = node.left
            node = node.left
        return x

    def maximum(self, node):
        x = None
        while node.right != None:
            x = node.right
            node = node.right
        return x

    def successor(self, node):
        parent = None
        if node.right != None:
            return self.minimum(node.right)
        parent = node.p
        while parent != None and node == parent.right:
            node = parent
            parent = parent.p
        return parent

    def predecessor(self, node):
        parent = None
        if node.left != None:
            return self.maximum(node.left)
        parent = node.p
        while parent != None and node == parent.left:
            node = parent
            parent = parent.p
        return parent

    def insert(self, k):
        t = TreeNode(k) #T is the node we're trying to insert
        parent = None
        node = self.root
        while node != None:
            parent = node
            if node.key > t.key:
                node = node.left
            else:
                node = node.right
        t.p = parent
        if parent == None:
            self.root = t
        elif t.key < parent.key:
            parent.left = t
        else:
            parent.right = t
        return t

    def nextdisc(self, node):
        node = self.root
        discriminator = 0
        if node != None:
            nextdisc = (discriminator + 1) % 2 #mod 2 because it's a 2D tree
        return nextdisc

    def delete(self, node):
        if node.left == None:
            self.transplant(node, node.right)
        elif node.right == None:
            self.transplant(node, node.left)
        else:
            succ = self.minimum(node.right)
            if succ.p != node:
                self.transplant(succ, succ.right)
                succ.right = node.right
                succ.right.p = succ
            self.transplant(node, succ)
            succ.left = node.left
            succ.left.p = succ

    def transplant(self, node, newnode):
        if node.p == None:
            self.root = newnode
        elif node == node.p.left:
            node.p.left = newnode
        else:
            node.p.right = newnode
        if newnode != None:
            newnode.p = node.p

if __name__ == "__main__":

    print "========================"
    print "Devin Ritter\nTerry Griffin\n4553 Spatial Data Structures\nFinal Exam Thing"
    print "========================\n\n\n"
    B = BinaryTree()
    num = 11
    extranums = 9

    for i in range(100):
        r1 = random.randint(1,100)
        r2 = random.randint(1,100)
        B.insert([r1,r2])

    while extranums != 0:
        B.insert([num,num])
        num = num + 11
        extranums = extranums - 1
    B.insert([100,100])

    """If I wanted to insert pairs of numbers"""

'''for i in range(10):
        for j in range(10):
            r1 = random.randint(1,100)
            r2 = random.randint(1,100)
            B.insert([r1,r2])
            print (r1,r2)'''
