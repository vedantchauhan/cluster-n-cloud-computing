import couchdb

server = couchdb.Server("http://127.0.0.1:5984")
db = server["tweets"]


max_value = 0
first_item = second_item = third_item = 0
first = second = third = 0
for item in db.view('group49/ade_sports', group = True):
    #print(item.key, item.value)
    if item.value > first:
        third_item = second_item
        third = second
        second_item = first_item
        second = first
        first_item = item.key
        first = item.value
    elif item.value > second:
        third_item = second_item
        third = second
        second_item = item.key
        second = item.value
    elif item.value > third:
        third_item = item.key
        third = item.value

print(first)
print(first_item)
print(second)
print(second_item)
print(third)
print(third_item)


