import math
import sys
import inspect

def displayInfoClass(instance):
    class_name = instance.__class__.__name__

    curframe = inspect.currentframe()
    calframe = inspect.getouterframes(curframe, 2)
    method_name = calframe[1][3]

    code_context = calframe[2][4][1]

    print("# {0}::{1} ({2}) #".format(class_name, method_name, code_context[:-1]))

