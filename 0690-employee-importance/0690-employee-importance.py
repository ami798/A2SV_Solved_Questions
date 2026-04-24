from collections import deque
from typing import List

# Employee definition (given by LeetCode)
# class Employee:
#     def __init__(self, id, importance, subordinates):
#         self.id = id
#         self.importance = importance
#         self.subordinates = subordinates

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        
        emp_map = {emp.id: emp for emp in employees}
        
        
        queue = deque([id])
        
        total_importance = 0
        
        
        while queue:
            current_id = queue.popleft()
            employee = emp_map[current_id]
            
            
            total_importance += employee.importance
            
            
            for sub_id in employee.subordinates:
                queue.append(sub_id)
        
        return total_importance