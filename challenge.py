MString=input('Enter the string')
string1=MString.split('=')
string2=string1[0].split('+')
def grade(ans,comp):
    i,j=0,0
    complement=''
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
listed.append(string2[0])
listed.append(string2[1])
listed.append(string1[1])
for sa in range(0,3):
    for sad in listed[sa]:
        if sad=='w':
            flag=sa
if flag==0:
    li=list(string2[0].split('water'))
    comp=li[0]+li[1]
    ans=str(int(string1[1])-int(string2[1]))
    grade(ans,comp)
elif flag==1:
    li = list(m[1].split('water'))
    comp = li[0] + li[1]
    ans = str(int(string1[1]) - int(string2[0]))
    grade(ans, comp)
elif flag==2:
    li = list(string1[1].split('water'))
    comp = li[0] + li[1]
    ans = str(int(string2[0]) + int(string2[1]))
    grade(ans, comp)
