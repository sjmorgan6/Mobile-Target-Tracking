# framework from https://pymoo.org/getting_started.html#Multi-Objective-Optimization
from tree_generation_pred_megi_4_30_targets_accessed import tree_generation5
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

#s= tree_generation5(7.874483612,	-14.89922105,	-10.64985905,	-5.655932462,	4.687130637)
#print(s)

class MyProblem(Problem):

    def __init__(self):
        super().__init__(n_var=2,
                         n_obj=4,
                         n_constr=0,
                         xl=np.array([-15,-15]),
                         xu=np.array([15,15]))

    def _evaluate(self, x, out, *args, **kwargs):
        size = (np.shape(x)[0])
        f1 = np.zeros([size,1])
        f2 = np.zeros([size,1])
        f3 = np.zeros([size,1])
        f4 = np.zeros([size,1])
        f5 = np.zeros([size,1])
        for i in range(size):
            dv1 = x[i,0]
            #print(dv1)
            dv2 = x[i,1]
            [f1[i],f2[i],f3[i],f4[i],f5[i]] = tree_generation5(dv1,dv2, 0)
        #print(f1)

        out["F"] = np.column_stack([f1,f3,f4,f5])


    # --------------------------------------------------
    # Pareto-front - not necessary but used for plotting
    # --------------------------------------------------
#    def _calc_pareto_front(self, flatten=True, **kwargs):
#        f1_a = np.linspace(0.1**2, 0.4**2, 100)
#        f2_a = (np.sqrt(f1_a) - 1)**2
#
#        f1_b = np.linspace(0.6**2, 0.9**2, 100)
#        f2_b = (np.sqrt(f1_b) - 1)**2
#
#        a, b = np.column_stack([f1_a, f2_a]), np.column_stack([f1_b, f2_b])
#        return stack(a, b, flatten=flatten)

    # --------------------------------------------------
    # Pareto-set - not necessary but used for plotting
    # --------------------------------------------------
#    def _calc_pareto_set(self, flatten=True, **kwargs):
#        x1_a = np.linspace(0.1, 0.4, 50)
#        x1_b = np.linspace(0.6, 0.9, 50)
#        x2 = np.zeros(50)
#
#        a, b = np.column_stack([x1_a, x2]), np.column_stack([x1_b, x2])
#        return stack(a,b, flatten=flatten)

problem = MyProblem()
#algorithm = NSGA2(
#    pop_size=50,
#    n_offsprings=50,
#    sampling=get_sampling("real_random"),
#    crossover=get_crossover("real_sbx", prob=0.90, eta=15),
#    mutation=get_mutation("real_pm", eta=20),
#    eliminate_duplicates=True
#)

algorithm = BRKGA(
    n_elites=250,
    n_offsprings=800,
    n_mutants=100,
    bias=0.3,
    eliminate_duplicates=True)

termination = MultiObjectiveDefaultTermination(
    x_tol=1e-9,
    cv_tol=1e-7,
    f_tol=0.0025,
    nth_gen=5,
    n_last=300,
    n_max_gen=10,
    n_max_evals=4000000
)

res = minimize(problem,
               algorithm,
               termination,
               seed=1,
               pf=problem.pareto_front(use_cache=False),
               save_history=True,
               verbose=True)

# create the performance indicator object with reference point (4,4)
metric = Hypervolume(ref_point=np.array([20.0, 100.0, 100.0, 0]))

# collect the population in each generation
pop_each_gen = [a.pop for a in res.history]

# receive the population in each generation
obj_and_feasible_each_gen = [pop[pop.get("feasible")[:,0]].get("F") for pop in pop_each_gen]

# calculate for each generation the HV metric
hv = [metric.calc(f) for f in obj_and_feasible_each_gen]
#
## function evaluations at each snapshot
n_evals = np.array([a.evaluator.n_eval for a in res.history])
#
## visualze the convergence curve
plt.plot(n_evals, hv, '-o')
plt.title("Convergence")
plt.xlabel("Function Evaluations")
plt.ylabel("Hypervolume")
plt.show()


# get the pareto-set and pareto-front for plotting
#ps = problem.pareto_set(use_cache=False, flatten=False)
#pf = problem.pareto_front(use_cache=False, flatten=False)
#
## Design Space
#plot = Scatter(title = "Design Space", axis_labels="x")
#plot.add(res.X, s=30, facecolors='none', edgecolors='r')
#plot.add(ps, plot_type="line", color="black", alpha=0.7)
#plot.do()
#plot.apply(lambda ax: ax.set_xlim(-0.5, 1.5))
#plot.apply(lambda ax: ax.set_ylim(-2, 2))
#plot.show()
#
## Objective Space
#pointsize=10
#plot = Scatter(title = "Objective Space")
#plot.add(res.F)
#plot.do()
#plot.apply(lambda ax: ax.set_zlim(0,100))
#plot.add(pf, plot_type="line", color="black", alpha=0.7)
#plot.show()

w = csv.writer(open("output_ga_4_30_megi_pred_singlesatX_targets.csv", "w"))
for i in res.X:
     w.writerow(i)
     
w = csv.writer(open("output_ga_4_30_megi_pred_singlesatF_targets.csv", "w"))
for i in res.F:
     w.writerow(i)
