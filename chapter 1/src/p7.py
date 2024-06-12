"""
Problem:

Implement a function that receives arguments, x, y, and z and returns a string “{y} is {z} at {x}”, where “{x}”, “{y}”, and “{z}” denote the values of x, y, and z, respectively.
In addition, confirm the return string by giving the arguments x=12, y="temperature", and z=22.4.
"""


def concatenate_string(x, y, z, template: str) -> str:
    template_splitted = template.split()
    for i in range(len(template_splitted)):
        if template_splitted[i] == r"{x}":
            template_splitted[i] = str(x)
        elif template_splitted[i] == r"{y}":
            template_splitted[i] = str(y)
        elif template_splitted[i] == r"{z}":
            template_splitted[i] = str(z)
    return " ".join(template_splitted)
