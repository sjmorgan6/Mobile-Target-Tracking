# Mobile Target Tracking

## Motivation
This code (primarily in Python) can be used to plan sequential low thrust maneuvers for satellites tracking a mobile target- particularly, this has been used for tracking hurricanes as in [[1]](#1) and [[2]](#2).  This is enabled by an analytical solution for low-thrust three-phase maneuvers [[4]](#4).  
This code compilation is a result of my Master's thesis here: [[3]](#3). Several case studies are shown there with a more in-depth discussion of this procedure of adaptable maneuver planning. 

## Summary of Approaches
Several methods for maneuver planning are included in this Github. Each of these show possible sequential maneuver solutions to achieve accesses of the mobile target at defined target locations with associated target times. Each essentially follow the following process:
* targets are defined along the hurricane track, each with some _viewing window_ (i.e. the satellite should view the storm at 10/10/2010 12:00 UTC +/- 20 hours)
    * the hurricane track will be interpolated between available points to approximate its location at each point in time in the model
* satellite(s) initialized at epoch with given initial conditions
* the satellite maneuvers with some delta-V (according to the approach used) over a fixed maneuver duration
* the satellite is then propagated (no delta-V applied) over the fixed _viewing window_
* storm accesses are recorded
* several delta-V options are attempted, according to the approach used
    * if there are no accesses recorded for a given target, the satellite will propagate through this maneuver duration (no delta-V applied)

All of the resulting delta-V solutions and associated storm accesses are recorded and presented according to the methods described below (i.e. displayed in a tree as the output of the graph theory approach or shown as a non-dominated set as the output from optimization). 

### Inputs
Each of these methods require the following inputs:
* initial satellite(s) state (can include multiple satellites)
    * orbit altitude
    * orbit inclination
    * initial right ascension of ascending node (_RAAN_)
    * initial argument of latitude (_u_)
    * epoch
    * right ascension of Greenwich at epoch

* satellite mass
* satellite maximum thrust capability
* target track to be used

The following assumptions are made:
* J2 effects only are included
* only circular orbits are used
* the general perturbation analytical solution is used for both propagation and raising/lowering maneuvers (an approximation as opposed to something like a numerical solution)
* initial and ending altitude of the three-phase maneuvers are the same
* model parameters:
   * mean Earth radius: 6371000 m
   * Earth flattening parameter: 0.00335281
   * angular velocity of the Earth: 7.29212*10^(-5) rad/s
   * standard gravitational parameter: 3.98600*10^(14) m^3/s^2
   * coefficient of the Earth's gravitational zonal harmonic of the 2nd degree (J2): 1082.7*10^(-6)

## __Graph theory approach__:
### Description:
(Python) this is similar to the approach used by McGrath et al. [[1]](#1). Possible maneuvers are displayed in a tree- this involves discretizing the maneuver space. For example, the satellite will maneuver from epoch with some delta-V (i.e. 0.5m/s, 1 m/s, 1.5 m/s). This delta-V step size can be adjusted. In this graph theory approach, each satellite state is a node, maneuvered to the next state by an edge of some delta-V. So, for example, a satellite will begin at node 0, maneuver with 0.5m/s, 1m/s and 1.5m/s, attempting to view Target 1. Each of these maneuver options are shown as edges branching from node 0, creating nodes 1, 2, and 3. Then, the satellite will maneuver from each of these states attempting to view Target 2, and so on. This will create a graph of possible maneuvers, with each branch representing a possible set of sequential maneuvers.  


There are a number of ways to analyze the resulting graph. Currently, the shortest path (lowest delta-V) is recorded, found through Dijkstra’s method as in <a id="1">[1]</a>. 


For a 3 target optimization with delta-V options of (-5:0.5:5 m/s) per manuever, this approach takes around x mins to produce results on a PC with 16 GB RAM (CPU: Intel Core i7 @ 1.9GHz). Note this will take an exponentially greater amount of time with more targets (increasing tree depth) 

### Process
The process as described above is shown in the flowchart below. 
Note in the code a negative delta-V corresponds to a lowering maneuver (delta-V applied opposite the satellite velocity vector) and a positive delta-V (delta-V applied in the direction of the satellite velocity vector) corresponds to a raising maneuver. 

<img src="./Images/tree_gen_loop.jpg" alt="Graph theory process flowchart." width="500"/>

### Output
The result of this is a graph of possible manuever options with the lowest delta-V solution. The 

## __Optimization (GA) approach__ - (Python) this approach utilizes continuous exploration of possible delta-V space. Rather than 

<img src="./Images/optimizer_loop.JPG" alt="Optimization process flowchart." width="700"/>

## __GUI__ - (Matlab and Python) this interface allows a user to define external inputs, which will display the output of the optimization approach

<img src="./Images/gui_mockup.JPG" alt="GUI mock-up." width="500"/>

## 
<img src="./Images/gui_mockup.JPG" alt="GUI mock-up." width="500"/>

## Sources:
Raising and lowering equations sourced from: DOI: https://doi.org/10.5281/zenodo.4452978
These are from the paper: https://doi.org/10.2514/1.G003739 

<a id="1">[1]</a> 
McGrath, Ciara N., Ruaridh A. Clark, Astrid Werkmeister, and Malcolm Macdonald. “Small Satellite Operations Planning for Agile Disaster Response Using Graph Theoretical Techniques.” Washington, D.C., 2019. https://www.iac2019.org.

<a id="2">[2]</a> 
Morgan, Sarah J., Ciara McGrath, and Olivier L. De Weck. “Mobile Target Tracking Using a Reconfigurable Low Earth Orbit Constellation.” In ASCEND 2020. Virtual Event: American Institute of Aeronautics and Astronautics, 2020. https://doi.org/10.2514/6.2020-4247.

<a id="3">[3]</a> 
Thesis will be posted in MIT DSpace: https://dspace.mit.edu/ 
It is not yet posted (5/24/2021) but once it is posted, it can be found under the title: "Reconfigurable Satellite Constellations for Mobile Target Tracking" by Sarah J. Morgan

<a id="4">[4]</a> 
Mcgrath, Ciara, and Malcolm Macdonald. “General Perturbation Method for Satellite Constellation Reconfiguration Using Low-Thrust Maneuvers.” Journal of Guidance, Control, and Dynamics 42 (July 2019): 1–17. https://doi.org/10.2514/1.G003739.


Hagberg, Aric, Dan Schult, and Pieter Swart. “NetworkX — NetworkX Documentation.” NetworkX Network Analysis in Python, 2021. https://networkx.org/.


Blank, J., and K. Deb. “Pymoo: Multi-Objective Optimization in Python.” IEEE Access 8 (2020): 89497–509.
https://pymoo.org/algorithms/brkga.html
