import random
num=int(input('enter number of candidate:'))
candidate=input(f"enter{num} candidate now \n").split()
print("candidate are:",candidate)
print("voting is live")
print("finished")
votes=[]
for x in range(0,num):
    c=random.randrange(1,100,3)
    votes.append(c)
for i in range(num):
    print(candidate[i],":",votes[i])
print("you win")
maximum=max(votes)
count=0
for r in range(num):
    if votes[r]==maximum:
        count=r
print(candidate[count],":",maximum)
