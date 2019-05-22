import ctypes

#import functions 
#import util 

api = ctypes.CDLL("../c-lib/build/libapi.so")

def call_num_params():
	int_param = ctypes.c_int(1)
	long_param = ctypes.c_long(2)
	short_param = ctypes.c_short(3)
	float_param = ctypes.c_float(4.0)
	double_param = ctypes.c_double(5.0)

	print("num_params():\n")
	print("int_param: %d" % int_param.value)
	print("long_param: %d" % long_param.value)
	print("short_param: %d" % short_param.value)
	print("float_param: %d" % float_param.value)
	print("double_param: %d" % double_param.value)

	api.num_params(int_param, long_param, short_param,
		float_param, double_param)

	print("\n")

def call_num_params_reference():
	int_param = ctypes.c_int(1)
	long_param = ctypes.c_long(2)
	short_param = ctypes.c_short(3)
	float_param = ctypes.c_float(4.0)
	double_param = ctypes.c_double(5.0)

	print("num_params_reference():\n")
	print("int_param: %d" % int_param.value)
	print("long_param: %d" % long_param.value)
	print("short_param: %d" % short_param.value)
	print("float_param: %d" % float_param.value)
	print("double_param: %d" % double_param.value)

	api.num_params_reference(ctypes.byref(int_param), ctypes.byref(long_param),
		ctypes.byref(short_param), ctypes.byref(float_param), 
		ctypes.byref(double_param))

	print("int_param: %d" % int_param.value)
	print("long_param: %d" % long_param.value)
	print("short_param: %d" % short_param.value)
	print("float_param: %d" % float_param.value)
	print("double_param: %d" % double_param.value)

def call_array_ints():
	pass

def main():
    print("<-- Python")
    print("\tC -->\n")
    
    call_num_params()
    call_num_params_reference()

if __name__ == '__main__':
	main()