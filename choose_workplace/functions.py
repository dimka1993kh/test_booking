def find_free_time(choices:list=None, default_choices:list=None):
    result = {'start' : '',
            'end' : '',
            'default' : ''
            }
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
        result['start'] = start_default_choices
        result['end'] = end_default_choices
        result['default'] = default_choices
    else:
        if choices[0] != default_choices[0]:
            part_one = start_default_choices[:start_default_choices.index(choices[0]) + 1]
        else:
            part_one = start_default_choices[:start_default_choices.index(choices[0])]

        if  choices[1] != default_choices[-1]:
            part_two = end_default_choices[end_default_choices.index(choices[1]):]
        else:
            part_two = []

        result['default'] = part_one + part_two
        result['start'] = result['default'][:-1]
        result['end'] = result['default'][1:]
    return result

def analize_time_interval(default_choices:list, now_choices:list, start_time_booking:int, end_time_booking:int, objects_booking_workplaces):
    error = ''
    if int(start_time_booking) > int(end_time_booking):
        error = 'Время начала работы должно быть меньше времени окончания работы'
    if now_choices and objects_booking_workplaces:
        list_now_choices = []
        for el in now_choices:
            list_now_choices.append(el[0])
        list_default_choices = []
        for el in default_choices:
            list_default_choices.append(el[0])
        set_now_choices = set(list_now_choices)
        set_time_interval = set(list(range(start_time_booking, end_time_booking + 1)))
        result = True
        let = []
        st = objects_booking_workplaces.last().start_time
        en = objects_booking_workplaces.last().end_time
        print('objects_booking_workplaces.last()', objects_booking_workplaces.last())
        set1 = set([st, en])
        print('set1', set1)
        print('set_time_interval', set_time_interval)
        dif = set1 & set_time_interval
        print('dif', dif)
        if len(dif) == 1 or len(dif) == 0:
            result = False
        else:
            result = True
        print(result)
        if result:
            min_time = 8
            max_time = 20
            not_free_list = []
            available_time_intervals = []
            for el in objects_booking_workplaces:
                not_free_list.append([el.start_time, el.end_time])
            not_free_list.sort()
            for idx, el in enumerate(not_free_list):
                if idx == 0:
                    available_time_intervals.append(f'{min_time} - {el[0]}')
                elif idx == len(not_free_list) - 1:
                    available_time_intervals.append(f'{not_free_list[idx - 1][-1]} - {el[0]}')
                    available_time_intervals.append(f'{el[1]} - {max_time}')
                else:
                    available_time_intervals.append(f'{not_free_list[idx - 1][-1]} - {el[0]}')
            error = f'Выбрано недопустимое время. Доступные интервалы времени {available_time_intervals}'
    return error


def find_free_workplaces(table, additional_table, start, end):
    result = table
    for el in additional_table:
        set_one = set(range(int(start), int(end) + 1))
        set_two = set(range(el.start_time, el.end_time + 1))
        print('el', el)
        print('set_one', set_one)
        print('set_two', set_two)
        print('set_one & set_two', set_one & set_two)
        if len(set_one & set_two) > 1:
            result = result.exclude(cabinet=el.cabinet, number_wp=el.workplace)
    return result
