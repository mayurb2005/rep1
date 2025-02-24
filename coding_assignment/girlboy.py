bglist=[]
num_of_iterations=int(input())
for i in range(num_of_iterations):
    llen=int(input())
    bglist.append([sorted(list(map(int,input().split()[:llen]))),sorted(list(map(int,input().split()[:llen])))])



print(bglist)

for i in range(len(bglist)):
    flag=False
    full_list=[]
    if bglist[i][0][0]>bglist[i][1][0]:
        for j in range(len(bglist[i][0])):
            full_list.append(bglist[i][1][j])
            full_list.append(bglist[i][0][j])
    else:
        for j in range(len(bglist[i][0])):
            full_list.append(bglist[i][0][j])
            full_list.append(bglist[i][1][j])

    print(full_list)


    for i in range(1,len(full_list)):
        if full_list[i]>=full_list[i-1]:
            flag=True
        else:
            flag=False
            break
    if flag:
        print('YES')
    else:
        print("NO")
        