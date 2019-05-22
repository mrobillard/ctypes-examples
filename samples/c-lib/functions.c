#include <stdio.h>

#include "functions.h"

//
// Parameter types 
//

void num_params(int param, long param_2, short param_3,
                float param_4, double param_5) {

	printf("\tint_param: %d\n", param);
	printf("\tlong_param: %d\n", param_2);
	printf("\tshort_param: %d\n", param_3);
	printf("\tfloat_param: %f\n", param_4);
	printf("\tdouble_param: %lf\n", param_5);

}

void num_params_reference(int *param, long *param_2, short *param_3,
                          float *param_4, double *param_5) {

	printf("\tint_param: %d\n", *param);
	printf("\tlong_param: %d\n", *param_2);
	printf("\tshort_param: %d\n", *param_3);
	printf("\tfloat_param: %f\n", *param_4);
	printf("\tdouble_param: %lf\n", *param_5);

	// Increment each value by 1
	*param = 2;
	*param_2 = 3;
	*param_3 = 4;
	*param_4 = 5.0;
	*param_5 = 6.0;

}

void array_ints(int *arr, int len) {

}

void array_doubles(double *arr, int len) {

}

void int_array(int **arr) {

}

void double_array(double **arr) {

}

//
// Structures
//

void struct_param(data_type *data) {

}

void nested_structs(nested_type *data) {

}

//
// Return types 
//

