weight = 0.5

#Input Data
input_value = int(input())

#Nerual Network (Single Neural)
def nerual_network(input_value, weight):
    prediction = input_value * weight
    return prediction

prediction = nerual_network(input_value, weight)

print(prediction)