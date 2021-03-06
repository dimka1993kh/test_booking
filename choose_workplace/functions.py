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
    return result

def analize_time_interval(default_choices:list, start_time_booking:int, end_time_booking:int, objects_booking_workplaces):
    error = ''
    if default_choices:
        set_default_choices = []
        for el in default_choices:
            set_default_choices.append(el[0])
        set_default_choices = set(set_default_choices)
        set_time_interval = set(list(range(start_time_booking, end_time_booking)))

        result = set_time_interval - set_default_choices
        list_default_choices = list(set_default_choices)
        if result:
            available_time_intervals = []
            new_start = ''
            for idx, el in enumerate(objects_booking_workplaces):
                if idx == 0:
                    start_el = list_default_choices[0]
                    end_el = el.start_time
                    new_start = el.end_time
                    available_time_intervals.append(f'{start_el} - {end_el}')
                elif el == objects_booking_workplaces.last():
                    end_el = el.start_time
                    available_time_intervals.append(f'{new_start} - {end_el}')
                    new_start = el.end_time
                    available_time_intervals.append(f'{new_start} - {list_default_choices[-1]}')
                else:
                    end_el = el.start_time
                    available_time_intervals.append(f'{new_start} - {end_el}')
                    new_start = el.end_time
            error = f'Выбрано недопустимое время. Доступные интервалы времени {available_time_intervals}'
    return error


def find_free_workplaces(table, additional_table, start, end):
    result = table
    for el in additional_table:
        set_one = set(range(int(start), int(end) + 1))
        set_two = set(range(el.start_time, el.end_time + 1))
        if set_one & set_two:
            result = result.exclude(cabinet=el.cabinet, number_wp=el.workplace)
    return result
