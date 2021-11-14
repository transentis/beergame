class Module():
    def __init__(self, model, name):
        self.name = name
        self.model = model

    def module_element(self,name):
        return self.name + "." + name
