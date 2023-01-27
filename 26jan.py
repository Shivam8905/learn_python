class Solution:
    def plusOne(self, digit: List[int]) -> List[int]:
        for i in range(len(digit)-1, -1, -1):
            if digit[i] != 9 :
                digit[i] = digit[i] + 1
                break
            else:
                digit[i] = 0
        
        if digit[0] == 0:
            digit.insert(0, 1)
        return digit







class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while right>=left:
            mid = (left + right)//2

            if mid*mid<=x:
                left = mid+1
            else:
                right = mid-1       
        return right




class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0: return 0
        if n==1: return 1
        if n==2: return 2

        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]




        # def climb(n):
        #     if n==1:
        #         return 1
        #     if n==2:
        #         return 2
            
        #     return climb(n-1) + climb(n-2)
        # return climb(n)




class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1,p2,i=m-1,n-1, m+n-1
        while p2>=0:
            if p1>=0 and nums1[p1]>nums2[p2]:
                nums1[i]=nums1[p1]
                i=i-1
                p1=p1-1
            else:
                nums1[i]=nums2[p2]
                i=i-1
                p2=p2-1





#         class Solution {
#     public void merge(int[] nums1, int m, int[] nums2, int n) {
#         int p1=m-1, p2=n-1, i=m+n-1;
        
#         while(p2>=0){
#             if(p1>=0 && nums1[p1]>nums2[p2]){
#                 nums1[i] = nums1[p1];
#                 i--;
#                 p1--;
#             }else{
#                 nums1[i] = nums2[p2];
#                 i--;
#                 p2--;
#             }
#         }
       
        
#     }
# }





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # list = []
    # def inHelper(root):
    #     if root==None:
    #         return
    #     list.append(root.val)
    #     inHelper(root.left)
    #     inHelper(root.right)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # inHelper(root)
        # return list
        res = []
        self.helper(root, res)
        return res
        
    def helper(self, root, res):
        if root:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root.left, root.right)

    def helper(self, r1, r2):
        if r1==None and r2==None:
            return True
        if r1==None or r2==None:
            return False

        return r1.val==r2.val and self.helper(r1.left,r2.right) and self.helper(r1.right, r2.left)









# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.helper(root)

    def helper(self, root):
        if root==None:
            return 0
        return max(self.helper(root.left), self.helper(root.right))+1





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        mid = len(nums)//2
        root = nums[mid]
        left = nums[:mid]
        right = nums[mid+1:]
        return TreeNode(root, self.sortedArrayToBST(left), self.sortedArrayToBST(right))







    #     lenght = len(nums)
    #     m = int(lenght/2)
    #     return self.helper(nums, 0, lenght-1)

    # def helper(self, nums, l, r):
    #     if l>r:
    #         return None
    #     mid = (l+r)/2
    #     root = TreeNode(nums[mid])
    #     root.left = self.helper(nums, l, mid-1)
    #     root.right = self.helper(nums, mid+1, r)
    #     return root







class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        list = []
        for i in range(numRows):
            curr = []
            for j in range(0, i+1):
                if j==0 or j==i:
                    curr.append(1)
                else:
                    curr.append(list[i-1][j-1] + list[i-1][j])

            list.append(curr)
        return list



# class Solution {
#     public List<List<Integer>> generate(int numRows) {
#         List<List<Integer>> ans = new ArrayList<List<Integer>>();
#         if(numRows <= 0) return ans;

#         for(int i=0; i<numRows; i++){
#             ArrayList<Integer> sub = new ArrayList<>();
#             for(int j=0; j<i+1; j++){
#                 if(j==0 || j==i){
#                     sub.add(1);
#                 }else{
#                     sub.add(ans.get(i-1).get(j-1) + ans.get(i-1).get(j));
#                 }
#             }
#             ans.add(sub);
#         }
#         return ans;
#     }
# }








class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        m = 0
        for i in prices:
            m = max(m, i-low)
            low = min(low, i)
        return m
            






class Solution(object):
    def isPalindrome(self, s):
        import re
        s = re.sub(r'[^0-9a-zA-Z]', '', s).lower()
        #ADjusting string to the final form without space or comma
        left = 0
        right =  len(s) -1
        #Initializing two pointer P1 and P2 point to the left-most side and the right-most 
        while left <right:
        #Moving two pointers in and compare two pointers if one case does not match then know that string is not a palindrom
            if s[left] != s[right]:
                return False
            left +=1
            right -=1
        return True






class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            ans = ans ^ i
        return ans






# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head==None:
            return False
        slow = head
        fast = head.next

        while slow != fast:
            if fast==None or fast.next==None:
                return False
            slow = slow.next
            fast = fast.next.next
         
        return True
            

        
        





# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1, l2, diff = 0,0,0
        temp = headA
        while temp!=None:
            l1 = l1+1
            temp = temp.next

        temp = headB
        while temp!=None:
            l2=l2+1
            temp=temp.next

        first, second = None, None
        if l1>l2 :
            diff = l1-l2
            first = headB
            temp = headA
        else:
            diff = l2-l1
            first = headA
            temp = headB

        k=0
        while k<diff:
            temp = temp.next
            k=k+1
        second = temp

        while first!=None:
            if first==second:
                return first
            first = first.next
            second = second.next

        return None









class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[int(len(nums)/2)]



class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res=0
        # for i in columnTitle:
        #     res = res*26 + ord(i)-ord('A')+1
        # return res
        val = [i for i in range(1, 27)]
        letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

        d= dict(zip(letters, val))
        for i in columnTitle:
            res = res*26 + d[i]
        return res





class Solution:
    def reverseBits(self, n: int) -> int:
        if n==0:
            return 0
        res=0
        for i in range(31):
            bit = n&1
            res = res|bit
            res<<=1
            n>>=1
        
        res |=n
        return res
        

'''
    int res = 0;
    for(int i= 1; i<=32; i++){
        //check last digit 0 or !
        int lsb = n & 1;
        // 1101 -> 110
        n = n >> 1;
        //1 = 10000...0
        lsb = lsb << (32-i);
        //1000 | 100 = 1100
        res = res | lsb;
    }
    return res;
'''




class Solution:
    def hammingWeight(self, n: int) -> int: 
        c=0
        for i in range(32):
            curr = 1&n
            if curr==1:
                c=c+1
            n >>=1
        return c




class Solution:
    def isHappy(self, n: int) -> bool:

        def getNext(n):
            sum=0
            while n!=0:
                n, digit = divmod(n, 10)
                sum += digit**2
            return sum

        seen = set()
        while n!=1 and n not in seen:
            seen.add(n)
            n = getNext(n)
        return n==1
        





# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        curr = head
        while curr != None:
            temp = curr.next
            curr.next=pre
            pre = curr
            curr = temp
        return pre






class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        con = set()
        for i in nums:
            if i in con:
                return True
            else:
                con.add(i)
        return False




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast, prev = head, head, None
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        prev, slow, prev.next = slow, slow.next, None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next
        fast, slow = head, prev
        while slow:
            if fast.val != slow.val: return False
            fast, slow = fast.next, slow.next
        return True







# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast, prev = head, head, None
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        prev, slow, prev.next = slow, slow.next, None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next
        fast, slow = head, prev
        while slow:
            if fast.val != slow.val: return False
            fast, slow = fast.next, slow.next
        return True






class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict={}
        for i in s:
            if i in dict:
                val = dict[i]
                dict[i] = val+1
            else:
                dict[i] = 1
        for i in t:
            if i in dict:
                val = dict[i]
                if val==1:
                    del dict[i]
                else:
                    dict[i] = val-1
            else:
                return False
        return True if len(dict)==0 else False






class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(0, len(nums)):
            if i not in nums:
                return i
        return len(nums)




class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a,b=0,0
        for i in range(len(nums)):
            if nums[a]==0 and nums[b]==0:
                b=b+1
            elif nums[a]==0 and nums[b]!=0:
                nums[a]=nums[b]
                nums[b]=0
                a=a+1
                b=b+1
            else:
                a=a+1
                b=b+1
        





class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==0:
            return False
        while n!=1:
            n,a = divmod(n,3)
            if a!=0:
                return False
        return True





class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()




class Solution(object):
    def intersect(self, nums1, nums2):
        sortedArr1 = sorted(nums1)
        sortedArr2 = sorted(nums2)
        i = 0
        j = 0
        output = []
        while i < len(sortedArr1) and j < len(sortedArr2):
            if sortedArr1[i] < sortedArr2[j]:
                i += 1
            elif sortedArr2[j] < sortedArr1[i]:
                j += 1
            else:
                output.append(sortedArr1[i])
                i += 1
                j += 1
        return output      





class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = {}
        for i in range(len(s)):
            if s[i] in dict:
                val = dict[s[i]]
                dict[s[i]] = val+1
            else:
                dict[s[i]] = 1
        
        for i in range(len(s)):
            if dict[s[i]] == 1:
                return i
        return -1







class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        list = []
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                list.append('FizzBuzz')
            elif i%3==0:
                list.append('Fizz')
            elif i%5==0:
                list.append('Buzz')
            else:
                list.append(str(i))
        return list


