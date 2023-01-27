Two Sum
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         numToIndex = {}
#         for i in range(len(nums)):
#             if target - nums[i] in numToIndex:
#                 return [numToIndex[target-nums[i]], i]

#             numToIndex[nums[i]] = i
#         return []
        

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = {}
        for i, j in enumerate(nums):
            #  print(i, j)
            r = target - j
            if r in d: return [d[r], i]
            d[j] = i
		
      
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return[]
        






class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        num = 0
        for i in range(len(s)-1,-1,-1):
            if i==len(s)-1:
                num += dict[s[i]]
            else:
                if dict[s[i]]>=dict[s[i+1]]:
                    num += dict[s[i]]
                else:
                    num -= dict[s[i]]
        return num






class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]
        for i in range(1,len(strs)):
            s = strs[i]
            m = min(len(s), len(ans))
            s1=''
            for j in range(0, m):
                if ans[j]==s[j]:
                    s1 += ans[j]
                else:
                    if s1 == '':
                        return ''
                    break
            ans = s1
                    
        return ans



# class Solution {
#     public String longestCommonPrefix(String[] strs) {
        
#         if(strs.length == 0) return "";
        
#         String str = strs[0];
#         for(int i=1; i<strs.length; i++){
#             while(strs[i].indexOf(str) !=0){
#                 str = str.substring(0,str.length()-1);
#             }
#         }
#         return str;
#     }
# }






class Solution:
    def isValid(self, s: str) -> bool:
        list = []
        for i in range(len(s)):
            print(i)
            if s[i] == '(' or s[i] == '{' or s[i] == '[' :
                list.append(s[i])
            elif s[i] == ')' :
                if len(list)==0 or list[len(list)-1] != '(':
                    return False
                else:
                    list.pop()
            
            elif s[i] == ']':
                print(s[i-1])
                if len(list)==0 or list[len(list)-1] != '[':
                    return False
                else: 
                    list.pop()

            elif s[i] == '}' :
                if len(list)==0 or list[len(list)-1] != '{':
                    return False
                else:
                    list.pop()
        return True if len(list)==0 else False
                    







# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = ListNode()
        curr = l1

        while list1!=None and list2!=None:
            if list1.val > list2.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next
            
            curr = curr.next
        curr.next = list1 if list1 != None else list2
        return l1.next






# class Solution {
#     public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
#         ListNode l1 = new ListNode();
#         ListNode curr = l1;

#         while(list1!=null && list2!=null){
#             if(list1.val>list2.val){
#                 curr.next = list2;
#                 list2=list2.next;
                
#             }else{
#                 curr.next = list1;
#                 list1=list1.next;
                
#             }
#             curr=curr.next;
#         }
#         curr.next = list1==null?list2:list1;
#         // curr.next = list1 != null ? list1 : list2;
#         return l1.next;

        
#     }
# }







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
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        insertIndex = 1
        for i in range(1, size):
            # Found unique element
            if nums[i - 1] != nums[i]:      
                # Updating insertIndex in our main array
                nums[insertIndex] = nums[i] 
                # Incrementing insertIndex count by 1 
                insertIndex = insertIndex + 1       
        return insertIndex

    # def removeDuplicates(self, nums: List[int]) -> int:
	# 	nums[:] = sorted(set(nums))
	# 	return len(nums)