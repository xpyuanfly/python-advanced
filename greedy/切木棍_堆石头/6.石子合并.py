# 7
# 45 13 12 16 9 5 22

def merge():
    n = int(input())
    s = list(map(int, input().split()))
    c=0
    while len(s)>1:
        sum=[]
        # 两两求和放到列表中
        for i in range(len(s)-1):
            m=s[i] + s[i+1]
            sum.append(m)
        a = min(sum) # 取和最小值
        k = sum.index(a) # 获取最小和位置，方便对列表进行合并更新
        s[k]=a
        # if k+1<len(s):
        s.pop(k+1)
        c=c+a # 计算每一步的花费
    print(c)


merge()

