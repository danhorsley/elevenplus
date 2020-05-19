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
    second_name_list = ['Smith', 'Jones', 'Patel', 'Davis', 'Horsley', 'Ridley', 'Pressler-Jones', 'Noble', 'Bonky-Clonky',
                       'Luxury-Yacht', 'Gifthorse', 'Smellypants', 'Monobrow']
    second_name = random.choice(second_name_list)
    task_dict = {'losing weight' : ['kg', 'losing weight', 'as fast', 'weight lost', 'lose'],
            'going to the hairdresser' :['dollars', 'spending', 'as much', 'dollars spent', 'spend'],
            'going to the sweetshop':['dollars', 'spending', 'as much', 'dollars spent', 'spend'], 
            'having a laugh':['chortles', 'laughing' , 'as much', 'chortles laughed', 'laugh'],
            'excercising' : ['reps', 'doing push ups', 'as much', 'reps done', 'do']}
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

def make_worksheet(number_questions = 20, my_type = 'random'):
    
    question_bank = []
    answer_bank = []
    for j in range(0,number_questions):
        type_dict = {'rounding' : rounding(), 'percent' : percent_q(), 
                                'ratio' : ratio_q(), 'nth' : nth_term_q(),
                                'percent2' : percent2_q(), 'average' : average_q(),
                                'formula' : form_q(), 'formula2' : formq2()}
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

