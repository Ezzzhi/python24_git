from itertools import combinations

def all_variants(text):
    for k in range(1, len(text) + 1):
        txt_lst = []
        b = combinations(text, k)
        txt_lst.extend(b)
        for j in txt_lst:
            j = list(j)
            yield (''.join(j))


a = all_variants("abc")
for i in a:
    print(i)

