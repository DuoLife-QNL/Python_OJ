n = int(input())

book_list = []
for x in range(0, n):
    book = {}
    book["name"], rest = input().split(' ', 1) 
    book["sale_num"], book["year"], book["month"], book["day"], book["price"], book["rate"] = map(int, rest.split())
    book_list.append(book)

book_list.sort(key = lambda x: (x["price"], -x["year"], -x["month"], -x["day"], -x["sale_num"], -x["rate"]))

for x in book_list:
    print("{} {} {} {} {} {} {}".format(x["name"], x["sale_num"], x["year"], x["month"], x["day"], x["price"], x["rate"]))