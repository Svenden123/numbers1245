def get_float(data):
    try:
        val = float(data)
    except ValueError:
        val = 0.0
    return val


def generate_summ(data):
    summ = 0
    for num in data:
        value = get_float(num)
        summ += value * value
    return summ


data = [1, '5', 'abc', 20, '2']


print(generate_summ(data))
