'''
# the simplest generator function
def simple_gen():
    yield 'Oh'
    yield 'hello'
    yield 'there'

for i in simple_gen():
    print(i)
'''

CORRECC_COMBO=(3,6,1)
'''
found_combo=False
for c1 in range(10):
    if found_combo==True:
        break
    for c2 in range(10):
        if found_combo==True:
            break
        for c3 in range(10):
            if found_combo==True:
                break
            if (c1,c2,c3)==CORRECC_COMBO:
                print('Found Correcc_COMBO:{}'.format((c1,c2,c3)))
                found_combo=True
                break
            print(c1,c2,c3)
'''

def combo_gen():
    for c1 in range(10):
        for c2 in range(10):
            for c3 in range(10):
                yield (c1,c2,c3)

for (c1,c2,c3) in combo_gen():
    print(c1,c2,c3)
    if(c1,c2,c3)==CORRECC_COMBO:
        print('found the combo:{}'.format((c1,c2,c3)))
        break
    print(c1,c2,c3)