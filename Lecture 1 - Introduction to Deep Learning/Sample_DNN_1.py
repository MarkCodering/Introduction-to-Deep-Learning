weight = 0.5
sum = 0

input_value = [5]

#Data Input (Array)
for i in range(0,5):
    input_value[i] = input()

#Summation
for s in range(0, 5):
    sum =+ input_value[s]

def nerual_network(input_value, weight):
    prediction = input_value * sum
    return prediction

prediction = nerual_network(input_value, weight)

print(prediction)