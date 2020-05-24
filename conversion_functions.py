import ctypes 

import numpy as np

def _convert_pylist_strings_to_cstring_array(py_list):
    if py_list is None:
        raise ValueError("Parameter 'py_list' must be a Python list, not %s"\
         % type(py_list))

    c_array = (ctypes.c_char_p * len(py_list))()
    c_array[:] = py_list

    return c_array

def convert_pylist_to_carray_long(py_list):
    if py_list is None:
        raise ValueError("Parameter 'py_list' must be a Python list (not 'None')")

    return (ctypes.c_long * len(py_list))(*py_list)

# def convert_pylist_to_carraydouble(py_list):
#   if py_list is None:
#       raise ValueError("Parameter 'py_list' must be a Python list (not 'None')")

#   return (ctypes.c_float * len(py_list))(*py_list)

def convert_cstring_to_pylist(cstring, len):
    return [cstring[i] for i in xrange(len)]

def convert_nparray_to_carraydouble(np_arr):
    if np_arr is None:
        raise ValueError("Parameter 'np_arr' must be a NumPy array (not 'None')")

    np_arr.flatten('C')

    return np_arr.ctypes.data_as(ctypes.POINTER(ctypes.c_double))

def convert_nparray_to_carraylong(np_arr):
    if np_arr is None:
        raise ValueError("Parameter 'np_arr' must be a NumPy array (not 'None')")

    np_arr.flatten('C')

    return np_arr.ctypes.data_as(ctypes.POINTER(ctypes.c_long))

def convert_carray_to_pylist(c_arr, len):
    if c_arr is None:
        raise ValueError("Parameter 'c_arr' must be a NumPy array (not 'None')")

    if len is None:
        raise ValueError("Parameter 'len' must be an integer (not 'None')")

    return [c_arr[i] for i in xrange(len)]

def convert_cstringarr_to_pylist(c_string_arr, len):
    py_list = []
    for c_str in range(0, len):
        py_list.append(c_string_arr[c_str])

    return py_list