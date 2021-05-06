def get_prob(factors):
    for factor, sub_factors in factors.items():
        factor_val = 1/len(factors)
        print('------------------------------')
        print(f'{factor}: 1/{len(factors)}')
        print('------------------------------')
        for sub_factor in sub_factors:
            sub_factor = 1/len(sub_factors)
            print(f'{sub_factor} value: 1/{len(sub_factors)}')

        print('\n')


factors = {'design': ['Load factor', 'Calculator error', 'Wrong use of code'],
'construction': ['Salty sand', 'Sub-standard Reinforcement', 'Alternative structures','Decayed formwork'],
'foundation': ['Lack of soil test', 'Inappropriate foundation type', 'Design error'],
'detailing_and_specification': ['Faulty dimensioning', 'Inconsistent bar marks'], 
'quality_control': ['Poor quality material', 'Wrong manufacturing of construction material', 'Poor installation'],
'engagement_of_quacks': ['Quacks', 'Semi skilled workers', 'Skilled workers'],
'development_control': ['Approval', 'Supervision', 'Certification at each stage'],
'Extra ordinary load cause': ['Working load', 'Natural disaster'],
'procedural': []}

get_prob(factors)