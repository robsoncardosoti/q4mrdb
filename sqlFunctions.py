def Aggregate():
    max = {'higher':'max', 'highest':'max', 'maximum':'max', 'maximal':'max', 'larger':'max', 'largest':'max', 'greater':'max', 'greatest':'max', 'most':'max', 'max':'max'}
    min = {'lower':'min', 'lowest':'min', 'minimal':'min', 'minimum':'min', 'smaller':'min', 'smallest':'min', 'least':'min', 'shorter':'min', 'shortest':'min', 'min':'min'}
    avg = {'average':'avg', 'mean':'avg', 'avg':'avg'}
    sum ={'total':'sum', 'sum':'sum'}
    count = {'quantity':'count', 'how_many':'count', 'amount':'count', 'number':'count', 'count':'count'}
    aggregate = dict(avg, **sum, **max, **count, **min)
    return aggregate

def Group():
    group = {'for_each': 'group by', 'of_each': 'group by', 'aggregate_by': 'group by', 'for_all': 'group by',
             'group': 'group by', 'grouped_by': 'group by'}
    return dict(group)

def Order():
    order = {'order_by': 'order by', 'ordered_by': 'order by', 'sorted_by': 'order by', 'ranked_by': 'order by',
             'classified_by': 'order by', 'organized_by': 'order by'}
    return dict(order)

def Compound():
    compound = [("order", "by"),("ordered", "by"), ("ranked", "by"),("sorted", "by"), ("classified", "by"), ("organized", "by"),
                ("for", "each"),("of","each"),("aggregate","by"),("for","all"),("grouped","by"),("how","many")]
    return compound