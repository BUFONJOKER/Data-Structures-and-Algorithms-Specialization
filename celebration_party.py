def celebration_party(child_ages):
    
    sorted_child = sort_child_ages(child_ages)
    
    groups = 1
    
    age = sorted_child[0]
    
    for i in sort_child_ages[1:]:
        if i - age > 1:
            groups+=1
        age = i
        
    return groups
    
    
def sort_child_ages(child_ages):
    minimum = child_ages[0]
    
    sorted = []
    
    n = len(child_ages)
    
    for i in range(0,n):
        minimum = child_ages[0]
        n = len(child_ages)
        for j in range(0, n):
            
            if child_ages[j] < minimum:
                minimum = child_ages[j]
                
        sorted.append(minimum)
        child_ages.remove(minimum)
    return sorted
        
        
        
    
child_ages = [10, 8, 12, 9, 11, 7]

print(celebration_party(child_ages))