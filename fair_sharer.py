# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 23:05:16 2022

@author: Miriam
"""

def fair_sharer(values, num_iterations, share=0.1):
    """Runs num_iterations.
    In each iteration the highest value in values gives a fraction (share)
    to both the left and right neighbor. The leftmost field is considered
    the neightbor of the rightmost field.
    Examples:
    fair_sharer([0, 1000, 800, 0], 1) --> [100, 800, 900, 0]
    fair_sharer([0, 1000, 800, 0], 2) --> [100, 890, 720, 90]
    Args
    values:
    1D array of values (list or numpy array)
    num_iteration:
    Integer to set the number of iterations
    """
    # code
    

    for num in range(num_iterations):
        
        max_value = max(values)
        
        for i, value in enumerate(values):
            
            if value == max_value:
                max_index = i

        
        if max_value == values[-1]:        
            values[0] = values[0] + max_value*share   
        
        else:           
            values[max_index+1] = values[max_index+1] + max_value*share
            
        values[max_index-1] = values[max_index-1] + max_value*share
        values[max_index] = max_value - 2*max_value*share
        
        values_new = values       
        
    return values_new

print(fair_sharer([1200, 1000, 800, 0],1))