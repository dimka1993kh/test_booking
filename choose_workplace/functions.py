def find_free_time(choices:list=None, default_choices:list=None):
    if default_choices == None:
        default_choices = [
                            (8, 8),
                            (9, 9),
                            (10, 10),
                            (11, 11),
                            (12, 12),
                            (13, 13),
                            (14, 14),
                            (15, 15),
                            (16, 16),
                            (17, 17),
                            (18, 18), 
                            (19, 19),
                            (20, 20),
                        ]
    if choices:
        choices = ((choices[0], choices[0]), (choices[1], choices[1]))
    start_default_choices = default_choices[:-1]
    end_default_choices = default_choices[1:]
    if choices == None:
        result = {'start' : start_default_choices,
                    'end' : end_default_choices,
                    'default' : default_choices
                    }
    else:
        if choices[0] != default_choices[0]:
            part_one = start_default_choices[:start_default_choices.index(choices[0]) + 1]
        else:
            part_one = start_default_choices[:start_default_choices.index(choices[0])]

        if  choices[1] != default_choices[-1]:
            part_two = end_default_choices[end_default_choices.index(choices[1]):]
        else:
            part_two = []
        choices = part_one + part_two
        start_choices = choices[:-1]
        end_choices = choices[1:]

        result = {'start' : start_choices,
                    'end' : end_choices,
                    'default' : choices
                    }
        # result = part_one + part_two
        print(result)
    return result

def analize_time_interval(default_choices:list, start_time_booking:int, end_time_booking:int):
    error = ''
    if default_choices:
        print('default_choices', default_choices)
        set_default_choices = []
        for el in default_choices:
            set_default_choices.append(el[0])
        set_default_choices = set(set_default_choices)
        set_time_interval = set(list(range(start_time_booking, end_time_booking)))

        print('set_default_choices',set_default_choices)
        print('set_time_interval',set_time_interval)

        result = set_time_interval - set_default_choices
        if len(result) != 0:
            available_time_intervals = []
            last_el = list(set_default_choices)[0]
            for el in list(result):
                available_time_intervals.append(f'{last_el} - {el - 1}')
                print('result', result)
                print('set_default_choices', set_default_choices)
                # print('set_start_choices.index(el)', list(set_start_choices).index(el))
                
                list_default_choices = list(set_default_choices)
                # if list_start_choices.index(el) != len(list_start_choices) - 1:
                last_el = list_default_choices[list_default_choices.index(el + 1)]
                if el == list(result)[-1]:
                    available_time_intervals.append(f'{last_el} - {list(set_default_choices)[-1]}')
            error = f'Выбрано недопустимое время. Доступные интервалы времени {available_time_intervals}'
        print(result)
        return error

# uuu = analize_time_interval([(8, 8),(9, 9),(10, 10),(12, 12),(13, 13),(14, 14),(16, 16),(17, 17),(18, 18),(19, 19),(20, 20),], 8, 21)
# print(uuu)