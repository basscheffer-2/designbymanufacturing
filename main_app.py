import json
from os.path import abspath, splitext
import design_algos


test_vars = json.dumps({
    "foo": "bar"
})


def make_design(model, out_file, **kwargs):
    name, ext = splitext(out_file)

    print "Making new {} design named '{}' with parameters:".format(model, name)
    for param in params:
        print "\t", param, ":", params[param]

    algo = design_algos.use(model)
    m = algo.design(**kwargs)

    with open(out_file, "wb") as fh:
        m.export(fh, ext)

    print "Design saved as:\n\t{}".format(abspath(out_file))


if __name__ == "__main__":
    model = "vase_v1"
    out_file = model+".stl"
    params = json.loads(test_vars)

    make_design(model, out_file, **params)

