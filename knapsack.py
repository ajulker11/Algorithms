#Solving the Knapsack problem using an implicit DFS tree 

''' 
problem statement: 

"Given a set of items, each with a weight and a value, determine the combination of items to include in a knapsack so 
that the total weight is less than or equal to a given limit and the total value is maximized.

'''

class Knapsack: 
      def __init__(self,value,weight):
            self.value=value 
            self.weight=weight 


def is_viable(ss,max_weight): 
      total_weight=0
      for item in ss: 
            total_weight+=item.weight 
      return total_weight<=max_weight 

def cost(ss):
      return sum(item.value for item in ss)

def DFS(i,items,sol,max_weight):
      if i==len(items):
            if is_viable(sol,max_weight):
                  return cost(sol) 
            else: 
                  return -float('inf') 
            
      return max(DFS(i+1,items,sol,max_weight),DFS(i+1,items,sol+[items[i]],max_weight))


items=[Knapsack(60,10),Knapsack(100,20),Knapsack(120,30)]
max_weight=50 
print(DFS(0,items,[],max_weight))
