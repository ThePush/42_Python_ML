from NumPyCreator import NumPyCreator
import numpy as np

npc = NumPyCreator()
print(npc.from_list([[1,2,3],[6,3,4]]))
print()
# Output :
#array([[1, 2, 3],
#[6, 3, 4]])
print(npc.from_list([[1,2,3],[6,4]]))
print()
# Output :
#None
print(npc.from_list([[1,2,3],['a','b','c'],[6,4,7]]))
print()
# Output :
#array([['1','2','3'],
#['a','b','c'],
#['6','4','7'], dtype='<U21'])
print(npc.from_list(((1,2),(3,4))))
print()
# Output :
#None
print(npc.from_tuple(("a", "b", "c")))
print()
# Output :
#array(['a', 'b', 'c'])
print(npc.from_tuple(["a", "b", "c"]))
print()
# Output :
#None
print(npc.from_iterable(range(5)))
print()
# Output :
#array([0, 1, 2, 3, 4])
shape=(3,5)
print(npc.from_shape(shape))
print()
# Output :
#array([[0, 0, 0, 0, 0],
#[0, 0, 0, 0, 0],
#[0, 0, 0, 0, 0]])
print(npc.random(shape))
print()
# Output :
#array([[0.57055863, 0.23519999, 0.56209311, 0.79231567, 0.213768 ],
#[0.39608366, 0.18632147, 0.80054602, 0.44905766, 0.81313615],
#[0.79585328, 0.00660962, 0.92910958, 0.9905421 , 0.05244791]])
print(npc.identity(4))
print()
# Output :
#array([[1., 0., 0., 0.],
#[0., 1., 0., 0.],
#[0., 0., 1., 0.],
#[0., 0., 0., 1.]])