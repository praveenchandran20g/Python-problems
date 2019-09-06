n=input('Enter the string')
l=n.split('=')
m=l[0].split('+')
def fn(k,d):
    le = len(k)
    for i in range(0, le):
        if k[0] == '0':
            k = k[1:]
            li[d] = k
    return li[d]
def grade(ans,comp):
    i,j=0,0
    complement=''
    if comp=='':
        print(ans)
    else:
        length = len(comp)
        length1 = len(ans)
        for z in range(0, length1):
            if comp[i] == ans[j]:
                j += 1
                i += 1
                if i>=length:
                    break
            else:
                complement = complement + ans[j]
                j += 1
        while j < length1:
            complement = complement + ans[j]
            j += 1
    return print(complement)
complement=''
flag=0
listed=[]
listed.append(m[0])
listed.append(m[1])
listed.append(l[1])
for sa in range(0,3):
    for sad in listed[sa]:
        if sad=='w':
            flag=sa
if flag==0:
    li=list(m[0].split('water'))
    k = str(li[0])
    d=0
    fn(k,d)
    comp=li[0]+li[1]
    ans=str(int(l[1])-int(m[1]))
    grade(ans,comp)
elif flag==1:
    li = list(m[1].split('water'))
    k = str(li[0])
    d=0
    fn(k,d)
    comp = li[0] + li[1]
    ans = str(int(l[1]) - int(m[0]))
    grade(ans, comp)
elif flag==2:
    li = list(l[1].split('water'))
    k=str(li[0])
    d = 0
    fn(k, d)
    comp = li[0] + li[1]
    ans = str(int(m[0]) + int(m[1]))
    grade(ans, comp)


