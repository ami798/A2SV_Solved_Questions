from collections import defaultdict

class Solution:
    def findDuplicate(self, paths):
        content_map = defaultdict(list)
        
        for path in paths:
            parts = path.split(" ")
            directory = parts[0]
            
            for file_info in parts[1:]:
                name, content = file_info.split("(")
                content = content[:-1]   
                
                full_path = directory + "/" + name
                content_map[content].append(full_path)
        
        
        return [files for files in content_map.values() if len(files) > 1]