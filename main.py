import numpy as np

#test inputs
inputs = [1, 2, 3, 2.5]
weights = [[0.2, 0.8, -0.5, 1],
[0.5, -0.91, 0.26, -0.5],
[-0.26, -0.27, 0.17, 0.87]]

biases = [2, 3, 0.5]

def neuron_output(inputs, weights,bias):
    return sum(inputs[i] * weights[i] for i in range(len(inputs)))+ bias

#this can also be done with numpy because its just the dot product of weights and inputs

#np.dot(weights,inputs) + bias


def neuron_layer_output(inputs, weights, biases):
    outputs=[]
    for i in range(len(biases)):
        outputs.append(neuron_output(inputs,weights[i],biases[i]))

    return outputs


print(neuron_layer_output(inputs, weights, biases))


# for input in batches 
# we will have to use matrix operations to calculate outputs

