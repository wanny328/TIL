L1 = []
L2 = []
L3 = []
L4 = []
L5 = []

l1 = input().split()
l2 = input().split()
l3 = input().split()
l4 = input().split()
l5 = input().split()

for i in l1:
    L1.append(i)
for i in l2:
    L2.append(i)  
for i in l3:
    L3.append(i)   
for i in l4:
    L4.append(i) 
for i in l5:
    L5.append(i)

R1 = [L1[0], L2[0], L3[0], L4[0], L5[0]]
R2 = [L1[1], L2[1], L3[1], L4[1], L5[1]]
R3 = [L1[2], L2[2], L3[2], L4[2], L5[2]]
R4 = [L1[3], L2[3], L3[3], L4[3], L5[3]]
R5 = [L1[4], L2[4], L3[4], L4[4], L5[4]]

C1 = [L1[0], L2[1], L3[2], L4[3], L5[4]]
C2 = [L1[4], L2[3], L3[2], L4[1], L5[0]]

Board = L1, L2, L3, L4, L5, R1, R2, R3, R4, R5, C1, C2
Ans = []

for i in range(5):
    x = input().split()
    for j in x:
        Ans.append(j)

cnt = 0

for i in Ans:
    for j in Board:
        if i in j:
            j.remove(i)
            if j == []:
                cnt += 1
                if cnt == 3:
                    print(Ans.index(i) + 1)
                    break