#test cases

from collisionDetector import oldcollisionDetector, newcollisionDetector

asteroids0 = []
asteroids1 = [1, -1]
asteroids2 = [-1, 1]
asteroids3 = [4, 5, -6]
asteroids4 = [10, -9, -1, 2]
asteroids5 = [-2, 5, -30]
asteroids6 = [-4, -2, 5, -1]
asteroids7 = [10, -4, 3, 8, 6, -7]

#run Tests
# assert oldcollisionDetector(asteroids0) == []
# assert newcollisionDetector(asteroids0) == []

assert oldcollisionDetector(asteroids1) == []
assert newcollisionDetector(asteroids1) == []

assert oldcollisionDetector(asteroids2) == [-1, 1]
assert newcollisionDetector(asteroids2) == [-1, 1]

assert oldcollisionDetector(asteroids3) == [-6]
assert newcollisionDetector(asteroids3) == [-6]

assert oldcollisionDetector(asteroids4) == [10, 2]
assert newcollisionDetector(asteroids4) == [10, 2]

assert oldcollisionDetector(asteroids5) == [-2, -30]
assert newcollisionDetector(asteroids5) == [-2, -30]

assert oldcollisionDetector(asteroids6) == [-4, -2, 5]
assert newcollisionDetector(asteroids6) == [-4, -2, 5]

assert oldcollisionDetector(asteroids7) == [10, 3, 8]
assert newcollisionDetector(asteroids7) == [10, 3, 8]
