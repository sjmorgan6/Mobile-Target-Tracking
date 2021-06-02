#---------------------------------------------
# Written by Sarah Morgan (sjmorgan@mit.edu, sjmorgan162@gmail.com)
# This code is a result of my (Sarah Morgan's) SM thesis here: [[3]](#3). Several case studies are shown there with a more in-depth discussion of this procedure of adaptable maneuver planning. 
# © Massachusetts Institute of Technology 2021.
#----------------------------------------------- 
#framework from https://pymoo.org/getting_started.html#Multi-Objective-Optimization
from series_of_maneuvers import series_of_maneuvers
import numpy as np
import pymoo
from pymoo.util.misc import stack
from pymoo.model.problem import Problem
from pymoo.algorithms.so_genetic_algorithm import GA
from pymoo.algorithms.so_brkga import BRKGA

from pymoo.algorithms.nsga2 import NSGA2
from pymoo.factory import get_sampling, get_crossover, get_mutation
from pymoo.util.termination.default import MultiObjectiveDefaultTermination
from pymoo.optimize import minimize
from pymoo.visualization.scatter import Scatter

import matplotlib.pyplot as plt
from pymoo.performance_indicator.hv import Hypervolume
import csv
import time


class MyProblem(Problem):

    #This essentially initializes the problem-- and is the stuff you need to change!
    #n_var = number of variables, number of maneuvers
    #n_obj = number of objectives, 3 given
    #n_constr = number of constraints listed, none in this case
    #xl, xu = lower and upper bounds for the variables given, maximum 5 m/s delta-V
    #(negative signifies lowering maneuvers, positive signifies raising maneuvers)
    def __init__(self):
        super().__init__(n_var=3,
                         n_obj=3,
                         n_constr=0,
                         xl=np.array([-5,-5,-5]),
                         xu=np.array([5,5,5]))

    #this uses our function (series of maneuvers)
    def _evaluate(self, x, out, *args, **kwargs):
        size = (np.shape(x)[0])
        f1 = np.zeros([size,1])
        f2 = np.zeros([size,1])
        f3 = np.zeros([size,1])
        for i in range(size):
            dv1 = x[i,0]
            dv2 = x[i,1]
            dv3 = x[i,2]
            [f1[i],f2[i],f3[i]] = series_of_maneuvers(dv1,dv2,dv3, 0)
            #these f1/f2/f3 vectors store our objectives for given variables dv1, dv2, dv3

        out["F"] = np.column_stack([f1, f2, f3])

tic = time.perf_counter()

problem = MyProblem()

#BRGKA algorithm parameters- can be altered
algorithm = BRKGA(
    n_elites=250,
    n_offsprings=800,
    n_mutants=100,
    bias=0.3,
    eliminate_duplicates=True)

#termination criteria- can be altered
termination = MultiObjectiveDefaultTermination(
    x_tol=1e-8,
    cv_tol=1e-6,
    f_tol=0.0025,
    nth_gen=5,
    n_last=300,
    n_max_gen=300,
    n_max_evals=40000
)

#execute problem
res = minimize(problem,
               algorithm,
               termination,
               seed=1,
               pf=problem.pareto_front(use_cache=False),
               save_history=True,
               verbose=True)

# collect the population in each generation
pop_each_gen = [a.pop for a in res.history]

# receive the population in each generation
obj_and_feasible_each_gen = [pop[pop.get("feasible")[:,0]].get("F") for pop in pop_each_gen]

toc = time.perf_counter()
print(toc-tic)

w = csv.writer(open("output/output_ga_example_designvar.csv", "w"))
for i in res.X:
    w.writerow(i)
    
w = csv.writer(open("output/output_ga_example_objectives.csv", "w"))
for i in res.F:
    w.writerow(i)
