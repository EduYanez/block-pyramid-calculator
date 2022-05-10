blocks = int(input("Enter the number of blocks: "))
next_lvl = 1 #the next level to build is 1 because we haven't started yet
height = 0

while next_lvl <= blocks: #next level to build must be lesser or equal to our current blocks stock
    height += 1 #you add one block at a time (it's a flat pyramid)
    blocks -= next_lvl #this little trick will count towards used blocks ;)
    next_lvl += 1 #time to calculate next level to re-validate condition in WHILE
    if next_lvl > blocks: #when blocks stock is not enough to keep building
        break

print("The height of the pyramid:", height)
