from shutil import copyfile
import shutil
import os,sys,re
if 0:
    #shutil.copy2('sai_help.py','abcd/efh/sai_help.py')
    #os.makedirs('abcd/efh/sai_help.py',exist_ok=True)
    path = '/nfs/site/disks/lnl_soc_disk_001/ashish/soc_package/ptl/ptl_0p5_drop/snapshot_model/ptl_ww7p4_Media_SOC_0p5_snapshot_ankit/bld/sm/MEDIA_LPM_SD.o3c.vpi.sipdfx.gtsynth.goldenrpt.default64/export_ip/debug_u2c/ip_package/smedia_top/source/upf/sai_help.py'

    rtl_folder = 'smedia_top/source'
    print(path.index(rtl_folder))

    full_path= 'abcd/'+path[217:]
    print(full_path)
    os.makedirs(os.path.dirname(full_path))
    copyfile('sai_help.py',full_path)
if 0:
    print(len(sys.argv))
    print(sys.argv[0])
    print(type(sys.argv[0]))
    print(sys.argv[1])
    print(type(sys.argv[1]))
    a = int(sys.argv[1])
    print(type(a))
    sys.exit("closed the execution")
if 0:
    s1 = {1,2,3,4,5}
    s2 = {1,2,3,6}
    print(s1-s2)
    print(s2-s1)


if 0:
    from abc import ABC, abstractmethod
    
    class AbstractClassExample(ABC):

        @abstractmethod
        def do_something(self):
            print("Some implementation!")


    class AnotherSubclass(AbstractClassExample):

        def do_something(self):
            super().do_something()  # still we can use the abstract method before overriding. But finally we have to override the method

    
    x = AnotherSubclass()
    x.do_something()


if 0:
    # import the threading module
    import threading
    
    class thread(threading.Thread):
    	def __init__(self, thread_name, thread_ID):
    		threading.Thread.__init__(self)
    		self.thread_name = thread_name
    		self.thread_ID = thread_ID
    
    		# helper function to execute the threads
    	def run(self):
            # print(self.thread_name,self.thread_ID)
            print(self.thread_name +" "+ str(self.thread_ID));
    
    thread1 = thread("GFG", 1000)
    thread2 = thread("GeeksforGeeks", 2000);
    
    thread1.start()
    thread2.start()
    
    print("Exit")

if 0:
    
    # insert operation in binary search tree
    # A utility class that represents an individual node in a BST
    
    class Node:
    	def __init__(self, key):
    		self.left = None
    		self.right = None
    		self.val = key
    
    # A utility function to insert
    # a new node with the given key
    
    
    def insert(root, key):
    	if root is None:
    		return Node(key)
    	else:
    		if root.val == key:
    			return root
    		elif root.val < key:
    			root.right = insert(root.right, key)
    		else:
    			root.left = insert(root.left, key)
    	return root
    
    # A utility function to search a given key in BST
    def search(root,key):
    	
    	# Base Cases: root is null or key is present at root
    	if root is None or root.val == key:
    		return root
    
    	# Key is greater than root's key
    	if root.val < key:
    		return search(root.right,key)
    
    	# Key is smaller than root's key
    	return search(root.left,key)
    
    # A utility function to do inorder tree traversal    
    def inorder(root):
    	if root:
    		inorder(root.left)
    		print(root.val)
    		inorder(root.right)
    def preorder(root):
        if root:
            print(root.val)
            preorder(root.left)
            preorder(root.right)
            
    def postorder(root):
        if root:
            postorder(root.left)
            postorder(root.right)
            print(root.val)
    
    r = Node(50)
    r = insert(r, 30)
    r = insert(r, 20)
    r = insert(r, 40)
    r = insert(r, 70)
    r = insert(r, 60)
    r = insert(r, 80)
    a = search(r,40)
    print(a.val)
    # Print inoder traversal of the BST
    inorder(r)
str1 = '/*apples are @red & green'
#print(re.split('[/\*@&]',str1))
if 0:
    a = b'1000'
    print(bin(int(a,2)+int(b'0011',2)))
    print(type(a))


if 0:
    import dummy2
    dummy2.tiny(1,2)
if 0:
    n  = 5
    for i in range(n):
        print(((chr(65+i)+" ")*n).strip())

if 0:
    n = 5
    for i in range(1,n+1):
        print("* "*i)
if 0:#nmot completed
    n = 3
    for i in range(1,(n*2)):
        if i < n:
            print(" "*(n-1)+"* "*i)
