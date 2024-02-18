import random


def sort_weight_value(weights, values):
    # weights = []
    # values = []

    # for i in range(0,len(weights_values)):
    #     if i%2==0:
    #         weights.append(weights_values[i])

    #     else:
    #         values.append(weights_values[i])

    n = len(weights)

    values_weights_ratios = []

    for i in range(0, n):
        values_weights_ratios.append(values[i]/weights[i])

    for i in range(0, n):
        for j in range(0, n):
            if values_weights_ratios[i] > values_weights_ratios[j]:
                values_weights_ratios[i], values_weights_ratios[j] = values_weights_ratios[j], values_weights_ratios[i]
                weights[i], weights[j] = weights[j], weights[i]
                values[i], values[j] = values[j], values[i]

    return weights, values


def max_weight_value(capacity, weights, values):

    weights, values = sort_weight_value(weights, values)

    i = 0
    total = 0

    while capacity >= 0:

        w_i = weights[i]

        v_i = values[i]

        if w_i < capacity:

            total += v_i
            capacity -= w_i

        else:
            total += (v_i/w_i)*capacity
            capacity -= w_i

        i += 1

    return total


capacity = 1000000
weights = random.sample(range(200000), 1000)
values = random.sample(range(200000, 4000000), 1000)

print(max_weight_value(capacity, weights, values))


