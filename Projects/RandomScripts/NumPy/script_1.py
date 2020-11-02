import numpy as np

cupcakes = [2.0,0.75,2.0,1.0,0.5]

recipes = np.genfromtxt('recipes.csv',delimiter=',')
print(recipes)

eggs = recipes[:,3]
print(eggs)
eggs_need_1 = [(eg == 1.) for eg in eggs]

print(eggs_need_1)
cookis = recipes[2,:]
print(cookis)
double_batch = cookis * 2
grocery_list = cookis + double_batch
