import os

valid_accuracy_params = (0, 1, True)
valid_interval_or_approximation_params = (float('-inf'), float('inf'), True)


def valid_file(path):
    return os.path.isfile(path) and os.path.getsize(path) > 0


def valid_value(value, min_value, max_value, is_strict):
    if value == 'exit':
        raise KeyboardInterrupt
    try:
        return (min_value < float(value) < max_value) if is_strict else (min_value <= float(value) <= max_value)
    except ValueError:
        return False


def valid_accuracy(accuracy):
    return valid_value(accuracy, *valid_accuracy_params)


def valid_interval_or_approximation(interval_or_approximations):
    valid_left_bound_or_x = valid_value(interval_or_approximations[0], *valid_interval_or_approximation_params)
    valid_right_bound_or_y = valid_value(interval_or_approximations[1], *valid_interval_or_approximation_params)
    return valid_left_bound_or_x and valid_right_bound_or_y
