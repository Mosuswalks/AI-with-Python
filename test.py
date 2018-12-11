left = [[1, 'A'], [2, 'B'], [3, 'C']]
right = [['A', 2004], ['B', 2008], ['C', 2012], ['B', 2014]]

def merge(left, right, left_on, right_on):
    
    merged = list(filter(lambda x,y: x[left_on] == y[right_on]), right)
    return merged

print(merge(left,right,1,0))