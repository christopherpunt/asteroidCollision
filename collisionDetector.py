
def oldcollisionDetector(asteroids):
    for i in range(len(asteroids) -1):
        # if a collision happens
        if asteroids[i] > 0 and asteroids[i+1] < 0:
            if abs(asteroids[i]) > abs(asteroids[i + 1]):
                asteroids.pop(i + 1)
            elif abs(asteroids[i]) < abs(asteroids[i + 1]):
                asteroids.pop(i)
            else:
                asteroids.pop(i)
                asteroids.pop(i + 1)

            
            oldcollisionDetector(asteroids)
            break
    return asteroids
            

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


# oldcollisionDetector(asteroids)
# print(asteroids)

# print(newcollisionDetector(asteroids))