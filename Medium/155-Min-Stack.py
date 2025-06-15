'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
'''


class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stk = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        
        if self.min_stk != [] and self.min_stk[-1] <= val:
            self.min_stk.append(self.min_stk[-1])
        else:
            self.min_stk.append(val)

        

    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            self.min_stk.pop()
            return self.stack.pop()

        

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.min_stk[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()