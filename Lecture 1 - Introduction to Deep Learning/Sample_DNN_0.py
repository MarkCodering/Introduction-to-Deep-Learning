weight = 0.5

input_value = int(input())

def nerual_network(input_value, weight):
    prediction = input_value * weight
    return prediction

prediction = nerual_network(input_value, weight)

print(prediction)