from keras.layers import Dense, Dropout
from .shapes import shapes


def hidden_layers(model, params, last_neuron):

    try:
        kernel_initializer = params['kernel_initializer']
    except KeyError:
        kernel_initializer = 'glorot_uniform'

    try:
        kernel_regularizer = params['kernel_regularizer']
    except KeyError:
        kernel_regularizer = None

    try:
        bias_initializer = params['bias_initializer']
    except KeyError:
        bias_initializer = 'zeros'

    try:
        bias_regularizer = params['bias_regularizer']
    except KeyError:
        bias_regularizer = None

    try:
        use_bias = params['use_bias']
    except KeyError:
        use_bias = True

    try:
        activity_regularizer = params['activity_regularizer']
    except KeyError:
        activity_regularizer = None

    try:
        kernel_constraint = params['kernel_constraint']
    except KeyError:
        kernel_constraint = None

    try:
        bias_constraint = params['bias_constraint']
    except KeyError:
        bias_constraint = None

    try:
        params['shapes']
        layer_neurons = shapes(params, last_neuron)
    except KeyError:
        layer_neurons = [params['first_neuron']] * params['hidden_layers']

    for i in range(params['hidden_layers']):

        model.add(Dense(layer_neurons[i],
                        activation=params['activation'],
                        use_bias=use_bias,
                        kernel_initializer=kernel_initializer,
                        kernel_regularizer=kernel_regularizer,
                        bias_initializer=bias_initializer,
                        bias_regularizer=bias_regularizer,
                        activity_regularizer=activity_regularizer,
                        kernel_constraint=kernel_constraint,
                        bias_constraint=bias_constraint))

        model.add(Dropout(params['dropout']))
