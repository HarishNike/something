from detecto import core
dataset=core.Dataset('images/')
dataset=core.Dataset('labels/','images/')
image,target=dataset[0]
print(image,target)