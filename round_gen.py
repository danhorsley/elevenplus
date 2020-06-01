import random

def rounding(with_answer = True):
    round_amounts = {'thousand' : [1000,0], 'hundred': [100,0],
                     'unit' : [1,0], 'tenth' : [0.1,1], 'hundreth' : [0.01,2],
                     'thousandth' : [0.001,3]}
    random_size = 10 ** random.randint(1,8)
    
    random_number = round(random.random()*random_size,5)
    
    my_rounding = random.choice(list(round_amounts.keys()))
    
    question = f'Round {random_number} to the nearest { my_rounding}.'
    
    round_num = round_amounts[my_rounding][0]
    
    correct_answer = round(round(random_number / round_num, 0) * round_num, round_amounts[my_rounding][1])
    
    if round_num >=1:
        correct_answer = int(correct_answer)
    
    return [question, correct_answer]

def percent_q():
    number_items = random.choice([4,5,6,8,10,12,15])
    disc = random.choice([10,20,30,40,50,60, 70])

    items = ['Bears', 'Unicorns', 'Fribgidgets', 'BangPops', 'Frobdoobelizers', 'Coins', 'Flowers', 'Stars',
            'Wizards', 'Surprises', 'Rascals', 'FreezyMcBreezies', 'Pyramids']
    adj = ['Chocloate', 'Strawberry', 'Jammy', 'Sugar', 'Honey', 'Orange', 'Cola', 'Disgusting', 'Mint', 'Apple']
    my_item = random.choice(adj) + ' ' + random.choice(items)
    number_items_to_price = 1 #random.choice(range(5,20))
    
    answer = round(round(random.random()*10,2) * ((100-disc)/100),2)
    price = round((answer / (1-(disc/100))) * number_items,2)
    question = f'''A packet of {number_items} {my_item} costs ${price}.  
        They are on special offer with {disc}% off. What is the cost of {number_items_to_price} {my_item[:-1]}'''
    return [question.replace('\n                    ',''), answer]

def ratio_q():
    number_ratios = random.choice([2,3,4])
    ratios = [random.randint(5,21) for j in range(0,number_ratios)]
    ratio1 = random.randint(5,21)
    ratio2 = random.randint(1,ratio1)
    #my_integer = (ratio1 + ratio2) * random.randint(10,200)
    my_integer = sum(ratios) * random.randint(10,200)
    #ratio_string = f'{ratio1} : {ratio2}'
    ratio_string = str(ratios[0])
    for i in ratios[1:]:
        ratio_string = ratio_string + ' : ' + str(i)
    my_q = f'split {my_integer} in the ratio {ratio_string}'
    #answer = [int(ratio1 * my_integer / (ratio1 + ratio2)), int(ratio2 * my_integer / (ratio1 + ratio2))]
    answer = [(r * my_integer/ sum(ratios)) for r in ratios]
    return [my_q, answer]

def nth_term_q():
    seq_mult = random.choice([-1,1]) * random.randint(1,10)
    seq_const = random.choice([-1,1]) * random.randint(1,10)
    if seq_mult == 1:
        my_mult = ''
    elif seq_mult == -1:
        my_mult = '-'
    else:
        my_mult = seq_mult
    if seq_const == 0:
        const_str = ''
    elif seq_const < 0:
        const_str = f'{seq_const}'
    else:
        const_str = f'+ {seq_const}'
    def my_form(n):
        return (seq_mult * n) + seq_const
    formula_string = f'{my_mult}n {const_str}'
    my_seq = f'{my_form(1)}   {my_form(2)}   {my_form(3)}   {my_form(4)}   {my_form(5)}'
    my_q = f'what is the nth term of this sequence   -   {my_seq}'
    return [my_q, formula_string]

def percent2_q():
    name_dict = {'Steve' : 'he', 'Barry' : 'he', 'Hilda' : 'she', 'Deirdre' : 'she', 'Agatha': 'she', 'Norman': 'he', 'Doreen': 'she'}
    my_name = random.choice(['Steve', 'Barry', 'Hilda', 'Deirdre', 'Agatha', 'Norman', 'Doreen'])
    spend = random.choice([90, 80, 75, 60, 50, 40, 30, 25, 10, 15])
    final_amount = round(random.random()*100,2)
    start_amount = round(final_amount/(1-(spend/100)),2)
    question = f'{my_name} has some money.  After spending {spend}% of it {name_dict[my_name]} is left with ${final_amount}.  How much money did {name_dict[my_name]} start with?'
    return question, start_amount

def average_q():
    number1 = random.randint(1,10)
    number2 = random.randint(1,10)
    missing1 = random.randint(1,10)
    missing2 = 4 - (number1 + number2 + missing1)%4
    
    if missing2 ==0:
        missing2 =4
    
    mean = int((number1 + number2 + missing1 + missing2 )/4)
    
    i = 0
    poss_answers = [(missing1, missing2)]
    while i<4:
        w1 = random.randint(1,10)
        w2 = random.randint(1,10)
        if (w1 != missing1 and w2 != missing2) and (w1 != missing2 and w1 != missing1) and (((w1+w2+number1+number2)/4)!=mean):
            poss_answers.append((w1,w2))
            i = i + 1
        else:
            pass
    poss_answers = random.sample(poss_answers,5)
    poss_answer_string =''
    counter = 0
    for my_pair in poss_answers:
        counter += 1
        poss_answer_string = poss_answer_string + str(my_pair[0]) + ' and ' + str(my_pair[1]) 
        if counter < 5:
            poss_answer_string = poss_answer_string +  ', '
        else:
            poss_answer_string = poss_answer_string +  '.'
    question = f'''you are given two numbers : {number1} and {number2}.  there are also two missing numbers.
                    The mean of the numbers is {mean}.  Which of the following pairs could be the missing numbers?
                    {poss_answer_string}'''    
    return [question.replace('\n                    ', ' '), (missing1, missing2)]

def form_q():
    job_list =['An electrician', 'A mechanic', 'A repairman', 'A plumber', 'A plasterer', 'A builder']
    time_period_list = ['day', 'week', 'month']
    job = random.choice(job_list)
    tp = random.choice(time_period_list)
    job_cost = random.randint(1,10) * 10
    hourly = random.randint(1,10) * 5
    q = f'''{job} charges a customer ${job_cost} for every job and ${hourly} for every {tp} he works.
            Write a formula for how much he charges (C) for t {tp}s of work'''
    answer = f'C = {job_cost} + {hourly}t'
    return [q.replace('\n                    ', ' '), answer]

def formq2():
    second_name_list = ['Smith', 'Davis', 'Jones'] 
    #'Smith', 'Jones', 'Patel', 'Davis', 'Gifthorse', 'Noble','Monobrow','Wobbly-Bum','Bonky-Clonky',
                     #  'Luxury-Yacht',  'Smellypants',  ]
    second_name = random.choice(second_name_list)
    task_dict = {'losing weight' : ['kg', 'losing weight', 'as fast', 'weight lost', 'lose'],
            'going to the hairdresser' :['dollars', 'spending', 'as much', 'dollars spent', 'spend'],
            'going to the sweetshop':['dollars', 'spending', 'as much', 'dollars spent', 'spend'], 
            'having a laugh':['chortles', 'laughing' , 'as much', 'chortles laughed', 'laugh'],
            'excercising' : ['reps', 'doing push ups', 'as much', 'reps done', 'do'],
            'eating pies' : ['pies', 'eating pies', 'as many', 'pies eaten', 'eat']}
    task = random.choice(list(task_dict.keys()))    
    
    small_int = random.randint(2, 5)
    second_int = random.randint(3,7)
    
    family_member_list = {f'Mrs {second_name}' : small_int, f'Mr {second_name}': second_int, f'the children' : 1}
    family_member = random.choice(list(family_member_list.keys()))
    seed = random.randint(50,100)
    final_number = (small_int*second_int + second_int + 1) * seed
    answer = seed * family_member_list[family_member]
    q = f'''Mr and Mrs {second_name} and their children are all {task}.
            Mrs {second_name} is {task_dict[task][1]} {small_int} times {task_dict[task][2]}  
            as Mr {second_name} and Mr {second_name} is {task_dict[task][1]} {second_int} times {task_dict[task][2]} 
            as the children.  If the total amount of 
            {task_dict[task][3]} is {final_number} {task_dict[task][0]} how many {task_dict[task][0]} did 
            {family_member} {task_dict[task][4]}?'''
                                    
    return [q.replace('\n            ', ''), answer]

def form_q3():
    name_list = ['Barry', 'Norman', 'Algernon']
    prod_list =['flower', 'balloon', 'comic', 'sweet']
    
    name = random.choice(name_list)
    prod = random.choice(prod_list)
    individual_cost = random.randint(1,10) 
    box_size = random.randint(5,10) 
    total_bot = box_size * random.randint(2,10)
    
    q = f'''{name} is opening up a {prod} stall at the market.
    He buys a stall for $S and the boxes of {prod} for $B.
    Each box contains {box_size} {prod}s and {name} buys {total_bot} {prod}s.
    Write an expression in terms of S & B that shows the total cost in dollars?'''
    answer = f'S + {int(total_bot/box_size)}B'
    return [q.replace('\n ', ''), answer]
def form_q4():
    #part1
    name_list1 = ['Barry', 'Norman', 'Algernon']
    name_list2 = ['Steve', 'Dave', 'Jack']
    name_list3 = ['Billy', 'George', 'Neil']
    prod_list = ['flower', 'balloon', 'comic', 'sweet']
    name1 = random.choice(name_list1)
    name2 = random.choice(name_list2)
    name3 = random.choice(name_list3)
    prod = random.choice(prod_list)
    my_int1 = random.randint(2,10)
    my_int2 = random.randint(2,10)
    my_int3 = random.randint(2,10)
    answer_int = random.randint(3,15)
    total_int = (my_int2 + 1 + my_int3)*answer_int + my_int1
    exp1 = f'{my_int3}P + {my_int1}'
    exp2 = f'{my_int2}P'
    #part2
    name_list4 = ['Victor', 'Larry', 'Albert']
    name4 = random.choice(name_list4)
    my_int4 = random.randint(2,9)
    const = my_int4*my_int1
    grad = my_int4*my_int3
    answer1 = f'{my_int4}({exp1})'
    answer2 = f'{grad}P + {const}'
    q = f'''{name1} has P {prod}s, {name2} has {exp1} {prod}s and {name3} has {exp2} {prod}s.
    Altogether {name1}, {name2} and {name3} have {total_int} {prod}s.  How many {prod}s does {name1} have?
    {name4} has {my_int4} times as many {prod}s as {name2}.  Write an expression in terms of P that shows the number
    of {prod}s that {name4} has in non-simplified and simplified form.'''
    return [q.replace('\n ', ''), [answer_int, answer1, answer2]]

def alg_sub():
    second_name_list = ['Smith', 'Jones', 'Patel', 'Davis', 'Bonky-Clonky',
                       'Luxury-Yacht', 'Gifthorse', 'Smellypants', 'Monobrow']
    object_list = {'plank of wood' : 'length', 'pile of bricks' : 'weight', 'bucket' : 'a volume of'}
    my_obj = random.choice(list(object_list.keys()))
    second_name = random.choice(second_name_list)
    dimension = {'length' : ['cm long', 'is','makes','new plank', 'of', ' is no wood'],
                 'weight' : ['kg', 'weighs','makes','new pile', 'of', 'are no bricks'],
                 'a volume of' : ['litres of water', 'contains','fills', 'new bucket', 'with', 'is no water']}
    
    measure1 = random.randint(25,100)
    measure2 = random.randint(25,100)
    measure3 = random.randint(25,100)
    scalar1 = random.randint(1,5)
    scalar2 = random.randint(1,5)
    scalar3 = random.randint(1,5)
    def balancer(var1, var2):
        if var1>var2:
            return f' + {var1 - var2}'
        elif var2>var1:
            return f' - {var2 - var1}'
        else:
            return ''
    measure_total = scalar1 * measure1 + scalar2 * measure2 + scalar3 * measure3
    def pluralizer(my_scalar):
        if my_scalar == 1:
            return ''
        else:
            return 's'
    my_q = f'''Mr {second_name} has a {my_obj} that {dimension[object_list[my_obj]][1]} 
            {measure_total} {dimension[object_list[my_obj]][0]}. He {dimension[object_list[my_obj]][2]} {scalar1} 
            {dimension[object_list[my_obj]][3]}{pluralizer(scalar1)} {dimension[object_list[my_obj]][4]} 
            {object_list[my_obj]} x {dimension[object_list[my_obj]][0]}, 
            {scalar2} 
            {dimension[object_list[my_obj]][3]}{pluralizer(scalar2)} {dimension[object_list[my_obj]][4]} 
            {object_list[my_obj]} y {dimension[object_list[my_obj]][0]}, 
            {scalar3} 
            {dimension[object_list[my_obj]][3]}{pluralizer(scalar2)} {dimension[object_list[my_obj]][4]} 
            {object_list[my_obj]} z {dimension[object_list[my_obj]][0]}. 
            There {dimension[object_list[my_obj]][5]} left over.  Write an equation that gives the 
            {object_list[my_obj]} of the {my_obj} in terms of x, y and z. 
            Calculate x and z if y = {measure2} and z = x{balancer(measure3, measure1)}
            '''
    return [my_q.replace('\n            ', ''), f'x = {measure1}, z = {measure3}']

def ooo1():
    scalar1 = random.choice([-1,1]) * random.randint(1,9)
    scalar2 = random.choice([-1,1]) * random.randint(1,9)
    scalar3 = random.choice([-1,1]) * random.randint(1,9)
    
    def oner(my_scalar):
        if my_scalar==1:
            return ''
        elif my_scalar==-1:
            return '-'
        else:
            return f'{my_scalar}'
    def signer(my_int) :
        if my_int < 0:
            return ''
        else:
            return '+'
    my_q = f'Simplify the following expression : {oner(scalar1)}({oner(scalar2)}x {signer(scalar3)} {scalar3})'
    answer = f'{scalar1*scalar2}x {signer(scalar1*scalar3)} {scalar1*scalar3}'
    return [my_q, answer] 

def quick_way():
    adj = random.randint(2,4)
    large_int = random.randint(1000//adj,10000//adj) * adj
    my_iters = random.randint(2,4) 
    last_iters = my_iters * adj
    
    def my_form(my_int,iters):
        ret = str(my_int)
        for i in range(1,iters):
            ret = ret + ' + ' + str(my_int)
        ret = ret + f' = X * {last_iters}'
        return ret
    f = my_form(large_int, my_iters)
    q = f"""Find X in the following equation : 
    {f}
    """
    return [q.replace('\n    ', ''), large_int//adj]

def slow_grow():
    slow_animal = ['sloth', 'snail', 'slug', 'tortoise']
    slow = random.choice(slow_animal)
    inc = random.choice([0,0.005])
    speed = random.randint(1,9) * 5 /1000 #+ inc
    minutes = random.choice([15,30,45])
    answer = random.randint(2,19)
    distance = round(answer * speed * 60/minutes,2)
    q = f"""A {slow} moves at {speed} metres every {minutes} minutes.  How many hours will it take to move
     {int(distance * 100)} cm?"""
    object_list = []
    return [q.replace('\n    ', ''),answer]

def simple_ratio():
    name_list = ['Susan', 'Grace', 'Ruby']
    int1 = 1 # random.randint(1,3)
    int2 = random.randint(1,3)
    mult = random.randint(2,5)
    obj1 = random.choice(['A', 'X', '?', '$'])
    obj2 = random.choice(['B', 'Y', '#', '%'])
    list1 = [obj1 for i in range(int1*mult)]
    list2 = [obj2 for j in range(int2*mult)]
    
    name = random.choice(name_list)
    ret_list = random.sample(list1 + list2, len(list1 + list2))
    str_ret = ''
    for i in range(len(ret_list)):
        str_ret = str_ret + ret_list[i] + '  '
    answer = f'{int1} : {int2}'
    q = f"""{str_ret}
         What is the ratio of {obj1} to {obj2} in its simplest form"""
    return [q.replace('\n    ', ''), answer]

def make_worksheet(number_questions = 30, my_type = 'random'):
    
    question_bank = []
    answer_bank = []
    for j in range(0,number_questions):
        type_dict = {'rounding' : rounding(), 'percent' : percent_q(), 
                                'ratio' : ratio_q(), 'simple_ratio' : simple_ratio(),
                                'nth' : nth_term_q(),
                                'percent2' : percent2_q(), 'average' : average_q(),
                                'formula' : form_q(), 'formula2' : formq2(),
                                'formula' : form_q3(), 'formula2' : form_q4(),
                                'ooo1' : ooo1(), 'alg_sub' : alg_sub(),
                                'quick_way' : quick_way(), 'slow_grow' : slow_grow()}
        if my_type == 'random':
            look_up = random.choice(list(type_dict.keys()))
        else:
            look_up = my_type
        my_q = type_dict[look_up]
        question_bank.append(my_q[0])
        answer_bank.append(my_q[1])
        
    return question_bank, answer_bank

def create_text_file(worksheet):
    with open('worksheet.txt', 'w') as f:
        i = 0
        for item in worksheet[0]:
            i = i + 1
            item = f'{i}. ' + str(item)
            f.write("%s\n" % item)
    with open('answersheet.txt', 'w') as f:
        i = 0
        for item in worksheet[1]:
            i = i + 1
            item = f'{i}. ' + str(item)
            f.write("%s\n" % item)

