
def oldcollisionDetector(asteroids):
    for i in range(len(asteroids) -1):
        # if a collision happens
        if asteroids[i] > 0 and asteroids[i+1] < 0:
            if abs(asteroids[i]) > abs(asteroids[i + 1]):
                asteroids.pop(i + 1)
            elif abs(asteroids[i]) < abs(asteroids[i + 1]):
                asteroids.pop(i)
            else:
                asteroids.pop(i + 1)
                asteroids.pop(i)
            oldcollisionDetector(asteroids)
            break

    return asteroids
            

#newcollisionDetector using a stack to get rid of the recursion from the oldcollisionDetector
def newcollisionDetector(asteroids):
    returnArray = []
    for new in asteroids:
        while returnArray and new < 0 < returnArray[-1]:
            if returnArray[-1] < -new:
                returnArray.pop()
                continue
            elif returnArray[-1] == -new:
                returnArray.pop()
            break
        else:
            returnArray.append(new)
    return returnArray