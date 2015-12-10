# Complete the function below.
from collections import namedtuple

def  getSuspiciousList2(transactions):
    DOLLAR_LIMIT = 3000
    TIME_LIMIT = 50
    suspects_set = set()
    ordered_suspects = list()
    last_transaction = dict()
    Transaction = namedtuple('Transaction', 'name dollars location time')
    
    for transaction in transactions:
        name, dollars, location, time = transaction.split('|')
        t = Transaction(name, int(dollars), location, int(time))
        if t.name not in suspects_set:
            if t.dollars >= DOLLAR_LIMIT:
                suspects_set.add(t.name)
                ordered_suspects.append(t.name)
            elif t.name in last_transaction:
                if (t.time-last_transaction[t.name].time<=TIME_LIMIT
                        and t.location != last_transaction[t.name].location):
                    suspects_set.add(t.name)
                    ordered_suspects.append(t.name)

            #clean up hashmap if over time?
            last_transaction[t.name] = t
    return ordered_suspects

from collections import OrderedDict

def  getSuspiciousList(transactions):
    DOLLAR_LIMIT = 3000
    TIME_LIMIT = 50
    suspects_set = set()
    ordered_suspects = OrderedDict()
    Transaction = namedtuple('Transaction', 'name dollars location time')
    
    for transaction in transactions:
        name, dollars, location, time = transaction.split('|')
        t = Transaction(name, int(dollars), location, int(time))

        if t.name not in suspects_set:
            if t.dollars >= DOLLAR_LIMIT:
                suspects_set.add(t.name)
                ordered_suspects[t.name] = (t, True)

            elif t.name in ordered_suspects:
                if (ordered_suspects[t.name][1] == False): 
                    if (t.time-ordered_suspects[t.name][0].time<=TIME_LIMIT
                            and t.location != ordered_suspects[t.name][0].location):
                        suspects_set.add(t.name)
                        ordered_suspects[t.name] = (t, True)
                    else:
                        del ordered_suspects[t.name]
                        ordered_suspects[t.name] = (t, False)


            #last_transaction[t.name] = t
            ordered_suspects[t.name] = (t, False)

    return [name for name in ordered_suspects.keys() if name in suspects_set]


input = ['Shilpa|500|California|63',
'Tom|25|New York|615',
'Krasi|9000|California|1230',
'Tom|25|New York|1235',
'Tom|25|New York|1238',
'Shilpa|50|Michigan|1300',
'Matt|90000|Georgia|1305',
'Jay|100000|Virginia|1310',
'Krasi|49|Florida|1320',
'Krasi|83|California|1325',
'Shilpa|50|California|1350']
print getSuspiciousList(input)

''' EXPECTED
Krasi
Shilpa
Matt
Jay
'''


