import sys
input = lambda : sys.stdin.readline().rstrip()
#sys.setrecursionlimit(10**6)
n = int(input())
card_dic = {}

for i in range(n) :
    card = int(input())
    if card in card_dic :
        card_dic[card] += 1
    else :
        card_dic[card] = 1

result = sorted(card_dic.items(),key = lambda x : (-x[1],x[0]))
print(result[0][0])



