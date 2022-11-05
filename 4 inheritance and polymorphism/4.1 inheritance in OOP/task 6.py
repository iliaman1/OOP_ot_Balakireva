class Layer:
    def __init__(self, name='Layer'):
        self.next_layer = None
        self.name = name

    def __call__(self, layer, *args, **kwargs):
        self.next_layer = layer
        return layer


class Input(Layer):
    def __init__(self, inputs: int):
        super().__init__('Input')
        self.inputs = inputs


class Dense(Layer):
    def __init__(self, inputs: int, outputs: int, activation: str):
        super().__init__('Dense')
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation


class NetworkIterator:
    def __init__(self, network):
        self.network = network

    def __iter__(self):
        self.current_layer = self.network
        return self

    def __next__(self) -> object:
        if self.current_layer is None:
            raise StopIteration

        res = self.current_layer
        self.current_layer = self.current_layer.next_layer

        return res
