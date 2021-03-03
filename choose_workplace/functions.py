def find_free_time(choices=None):
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
    start_default_choices = default_choices[:-1]
    end_default_choices = default_choices[1:]
    if choices == None:
        result = {'start' : start_default_choices,
                    'end' : end_default_choices
                    }
    else:
        if choices[0] != (8, 8):
            part_one = start_default_choices[:start_default_choices.index(choices[0]) + 1]
        else:
            part_one = start_default_choices[:start_default_choices.index(choices[0])]

        if  choices[1] != (20, 20):
            part_two = end_default_choices[end_default_choices.index(choices[1]):]
        else:
            part_two = []
        result = part_one + part_two
    return result