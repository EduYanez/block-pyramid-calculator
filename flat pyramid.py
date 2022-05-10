blocks = int(input("Enter the number of blocks: "))
height = 1
upper_lvl = 1
used_blocks = 1
remain_blocks = blocks - 1
count = 0

while remain_blocks > upper_lvl +1: # <--------------
    height += 1 #1+1 =2
    upper_lvl += 1 #1+1 = 2
    used_blocks += upper_lvl # 1+2 = 3
    remain_blocks = blocks - used_blocks # 6 - 3 = 3 <------- AQUI
    count += 1
    if remain_blocks != upper_lvl +1:
        break

print("The height of the pyramid: ", height)
