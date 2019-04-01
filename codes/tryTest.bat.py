
import pickle

# all_state = {'first_win': [[]], 'second_win': [[]], 'draw': [[]]}

# with open("efawf.pkl", "wb") as file:
#     pickle.dump(all_state, file, True)

with open("3_3.pkl", "rb") as file:
                list1 = pickle.load(file)

a = list1['first_win'][0:10]
print(a)
m = 0
for i in a:
    for j in i:
        print(j,end=' ')
        m += 1
        if m == 3:
            print()
            m = 0
    m = 0
    print('_'*10)