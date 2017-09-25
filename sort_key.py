# Write a function that sorts the keys in
#a hash by the length of the key as a string.
# For instance, the hash:
# h =  {'abc': 'hello', 'another_key': '123', '4567': 'third'}
def sort_hash(h = {}, sort_dir = False):
    new_arr = []
    for k in sorted(h, key=len, reverse=sort_dir):
        new_arr.append(k)

    print(new_arr)

h =  {'abc': 'hello', 'another_key': '123', '4567': 'third'}
sort_hash(h, True)
