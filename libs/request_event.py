def snake_to_camel(snake):
    camel = ''
    next_upper = False
    for c in snake:
        if c == '_':
            next_upper = True
        else:
            if next_upper:
                camel += c.upper()
                next_upper = False
            else:
                camel += c
    return camel


def camel_to_snake(camel):
    snake = ''
    for i, c in enumerate(camel):
        if i > 0 and c.isupper():
            snake += '_'
        snake += c.lower()
    return snake


def snake_to_camel_dict(dic):
    new_dict = {}
    for key in list(dic):
        if isinstance(dic[key], dict):
            new_dict[snake_to_camel(key)] = snake_to_camel_dict(dic[key])
        else:
            new_dict[snake_to_camel(key)] = dic[key]
    return new_dict


def camel_to_snake_dict(dic):
    new_dict = {}
    for key in list(dic):
        if isinstance(dic[key], dict):
            new_dict[camel_to_snake(key)] = camel_to_snake_dict(dic[key])
        else:
            new_dict[camel_to_snake(key)] = dic[key]
    return new_dict
