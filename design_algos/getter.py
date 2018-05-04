from importlib import import_module


def use(model):
    return import_module("."+model, package="design_algos")
