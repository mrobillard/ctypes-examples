#ifndef FUNCTIONS_H__
#define FUNCTIONS_H__

#include "data_types.h"

/*
 * Basic parameter types 
 */

void num_params(int param, long param_2, short param_3,
                float param_4, double param_5);

void num_params_reference(int *param, long *param_2, short *param_3,
                          float *param_4, double *param_5);

void array_ints(int *arr, int len);

void array_doubles(double *arr, int len);

void int_array(int **arr);

void double_array(double **arr);

/*
 * Structures 
 */

void struct_param(data_type *data);

void nested_structs(nested_type *data);

/*
 * Return type examples
 */

/* 
 * Void pointers
 */

/*
 * Function pointers 
 */


#endif // FUNCTIONS_H__