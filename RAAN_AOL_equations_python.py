# RAAN_AOL_equations_python sourced from: DOI: https://doi.org/10.5281/zenodo.4452978 These are from the paper: https://doi.org/10.2514/1.G003739

import numpy as np

def full_man_low(mu, Re, J2, RAAN0, u0, accel, a0, a3, incl, deltaVtotal, ttotal):
    """
    Calculate change in right ascension of ascending node (RAAN) and argument of latitude (AOL) in each phase of manoeuvre
    and at manoeuvre end for orbit lowering 3-phase manoeuvre
    
    --- Inputs ---
    :param mu: standard gravitational parameter of Earth, m^3/s^2
    :param Re: mean Earth radius, m
    :param J2: J2 coefficient, -
    :param RAAN0: initial RAAN, rads
    :param u0: initial AOL, rads  
    :param accel: propulsive acceleration, m/s^2
    :param a0: initial mean semi-major axis, m
    :param a3: final mean semi-major axis, m
    :param incl: initial inclination, rads (assumed constant)
    :param deltaVtotal: deltaV to be used for manoeuvre, m/s
    :param ttotal: total manoeuvre time, seconds 
    
    
    --- Outputs ---
    :return deltaRAAN1_low: change in RAAN during phase 1 of manoeuvre, rads
    :return deltaRAAN2_low: change in RAAN during phase 2 of manoeuvre, rads
    :return deltaRAAN3_low: change in RAAN during phase 3 of manoeuvre, rads
    :return RAANfinal_low: final RAAN at end of manoeuvre, rads
    :return deltau_low: change in AOL during phase 1 of manoeuvre, rads
    :return deltau2_low: change in AOL during phase 2 of manoeuvre, rads
    :return deltau3_low: change in AOL during phase 3 of manoeuvre, rads
    :return ufinal_low: final AOL at end of manoeuvre, rads

    """
    A = -accel             # propulsive acceleration, m/s^2 (negative for lowering case)  

    # ---------------------------
    # Lowering Maneuver Equations
    # ---------------------------
    # RAAN
    # --------------------------
    deltaRAAN1_low = ((3/134217728) * A**(-1) * a0**(-16) * J2 * mu**(-7) * (mu + a0 * (deltaVtotal + (a3**(-1) * mu)**(1/2)) * (deltaVtotal + 2 * (a0**(-1) *
                 mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**8 * Re**2 * np.cos(incl) * (32768 * a0**8 * mu**4 * (mu + a0 * (deltaVtotal + (a3**(-1) * mu)**(1/2)) * 
                 (deltaVtotal  +  2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-4) * (a0**4  +  (-256) * a0**4 * mu**4 * (mu + a0 * (deltaVtotal + (a3**(-1) * 
                 mu)**(1/2)) * (deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-4)) + 1024 * a0**4 * J2 * mu**2 * (mu + a0 * 
                 (deltaVtotal + (a3**(-1) * mu)   **(1/2)) * (deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-2) * (a0**6 + (-4096) * a0**6 * 
                 mu**6 * (mu + a0 * (deltaVtotal + (a3**(-1) * mu)**(1/2)) * (deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-6)) * 
                 Re**2 * (1 + 3 * np.cos(2 * incl)) + 9 * J2**2 * (a0**8 + (-65536) * a0**8 * mu**8 * (mu + a0 * (deltaVtotal + (a3**(-1) * mu)**(1/2)) * 
                 (deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-8)) * Re**4 * (1 + 3 * np.cos(2 * incl))**2))

    deltaRAAN2_low = ((-3/256) * a0**(-2) * J2 * mu**(-2) * (mu + a0 * (deltaVtotal + (a3**(-1) * mu)**(1/2)) * (deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) *
                 mu)**(1/2)))**2 * (a0**(-3) * mu**(-2) * (mu + a0 * (deltaVtotal + (a3**(-1) * mu)**(1/2)) * (deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) *
                 mu)**(1/2)))**3)**(1/2) * Re**2 * np.cos(incl) * (1 + (3/32) * a0**(-2) * J2 * mu**(-2) * (mu + a0 * (deltaVtotal + (a3**(-1) * mu)**(1/2)) *
                 (deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**2 * Re**2 * (1 + (-3/2) * np.sin(incl)**2)) * (ttotal + (-1/640) * A**(-1) * 
                 a3**(-5/2) * mu**(1/2) * (a0 * mu * (mu + a0 * (deltaVtotal + (a3**(-1) * mu)**(1/2)) * (deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) *
                 mu)**(1/2)))**(-1))**(-5/2) * ((-320) * a0**2 * a3**(5/2) * mu**2 * (mu + a0 * (deltaVtotal + (a3**(-1) * mu)**(1/2)) * (deltaVtotal + 2 * 
                 (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-2) + 3 * a3**(5/2) * J2 * Re**2 * ((-2) + 3 * np.sin(incl)**2) + 32 * (a0 * mu * (mu + a0 * 
                 (deltaVtotal + (a3**(-1) * mu)**(1/2)) * (deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-1))**(5/2) * (20 * a3**2 + 3 * 
                 J2 * Re**2 * (2 + (-3) * np.sin(incl)**2))) + (1/640) * A**(-1) * a0**(-5/2) * mu**(1/2) * (a0 * mu * (mu + a0 * (deltaVtotal + (a3**(-1) * 
                 mu)**(1/2)) * (deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-1))**(-5/2) * ((-640) * a0**2 * (a0 * mu * (mu + a0 * 
                 (deltaVtotal + (a3**(-1) * mu)**(1/2)) * (deltaVtotal  +  2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-1))**(5/2) + 96 * J2 * 
                 (a0 * mu * (mu + a0 * (deltaVtotal + (a3**(-1) * mu)**(1/2)) * (deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-1))**(5/2) *
                 Re**2 * ((-2) + 3 * np.sin(incl)**2) + a0**(5/2) * (320 * a0**2 *mu**2 * (mu + a0 * (deltaVtotal + (a3**(-1) * mu)**(1/2)) * (deltaVtotal + 2 * 
                 (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-2) + 3 * J2 * Re**2 * (2 + (-3) * np.sin(incl)**2)))))

    deltaRAAN3_low = ((-3/134217728) * A**(-1) * a0**(-8) * a3**(-8) * J2 * mu**(-7) * (mu + a0 * (deltaVtotal + (a3**(-1) * mu)**(1/2)) * (deltaVtotal + 2 * (a0**(-1) * 
                 mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**8 * Re**2 * np.cos(incl) * (32768 * a0**4 * a3**4 * mu**4 * (mu + a0 * (deltaVtotal + (a3**(-1) * mu)**(1/2)) *  
                 (deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-4) * ((-1) * a3**4 + 256 * a0**4 * mu**4 * (mu + a0 * (deltaVtotal + 
                 (a3**(-1) * mu)**(1/2)) * (deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-4)) + 1024 * a0**2 * a3**2 * J2 * mu**2 * (mu + 
                 a0 * (deltaVtotal + (a3**(-1) * mu)**(1/2)) * (deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-2) * ((-1) * a3**6 + 4096 * 
                 a0**6 *mu**6 * (mu + a0 * (deltaVtotal + (a3**(-1) * mu)**(1/2)) * (deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-6)) * 
                 Re**2 * (1 + 3 * np.cos(2 * incl)) + 9 * J2**2 * ((-1) * a3**8 + 65536 * a0**8 * mu**8 * (mu + a0 * (deltaVtotal + (a3**(-1) * mu)**(1/2)) * 
                 (deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-8)) * Re**4 * (1 + 3 * np.cos(2 * incl))**2))


    RAANfinal_low = RAAN0  +  deltaRAAN1_low  +  deltaRAAN2_low  +  deltaRAAN3_low
    RAANfinal_low = RAANfinal_low % (2*np.pi)

    # ---------------------------
    # AOL
    # ---------------------------

    deltau1_low = ((-1/536870912) * A**(-1) * a0**(-16) * mu**(-7) * (mu + a0 * (deltaVtotal + (a3**(-1) * mu)**(1/2)) * (deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) +
              (a3**(-1) * mu)**(1/2)))**8 * (8388608 * a0**12 * mu**6 * (mu + a0 * (deltaVtotal + (a3**(-1) * mu)**(1/2)) * (deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) +
              (a3**(-1) * mu)**(1/2)))**(-6) * (a0**2 + (-16) * a0**2 * mu**2 * (mu + a0 * (deltaVtotal + (a3**(-1) * mu)**(1/2)) * (deltaVtotal + 2 * (a0**(-1) * 
              mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-2)) + 27 * J2**3 * (a0**8 + (-65536) * a0**8 * mu**8 * (mu + a0 * (deltaVtotal + (a3**(-1) * mu)**(1/2)) * 
              (deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-8)) * Re**6 * (1 + 3 * np.cos(2 * incl))**2 * (3 + 5 * np.cos(2 * incl)) + 98304 * 
              a0**8 * J2 * mu**4 * (mu + a0 * (deltaVtotal + (a3**(-1) * mu)**(1/2)) * (deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-4) * 
              (a0**4 + (-256) * a0**4 * mu**4 * (mu + a0 * (deltaVtotal + (a3**(-1) * mu)**(1/2)) * (deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * 
              mu)**(1/2)))**(-4)) * Re**2 * (5 + 11 * np.cos(2 * incl)) + 768 * a0**4 * J2**2 * mu**2 * (mu + a0 * (deltaVtotal + (a3**(-1) * mu)**(1/2)) * (deltaVtotal + 
              2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-2) * (a0**6 + (-4096) * a0**6 * mu**6 * (mu + a0 * (deltaVtotal + (a3**(-1) * mu)**(1/2)) * 
              (deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-6)) * Re**4 * (53 + 68 * np.cos(2 * incl) + 39 * np.cos(4 * incl))))

    deltau2_low = ((ttotal + (1/2) * A**(-1) * ((-2) * a3**(-1/2) * mu**(1/2) + mu**(1/2) * (a0 * mu * (mu + a0 * (deltaVtotal + (a3**(-1) * mu)**(1/2)) * (deltaVtotal +
              2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-1))**(-1/2) + (-3/5) * a3**(-5/2) * J2 * mu**(1/2) * Re**2 + (3/160) * J2 * mu**(1/2) * (a0 * 
              mu * (mu + a0 * (deltaVtotal + (a3**(-1) * mu)**(1/2)) * (deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-1))**(-5/2) * Re**2 + 
              (9/10) * a3**(-5/2) * J2 * mu**(1/2) * Re**2 * np.sin(incl)**2 + (-9/320) * J2 * mu**(1/2) * (a0 * mu * (mu + a0 * (deltaVtotal + (a3**(-1) * mu)**(1/2)) * 
              (deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-1))**(-5/2) * Re**2 * np.sin(incl)**2) + (-1/2) * A**(-1) * (2 * a0**(-1/2) * mu**(1/2) + 
              (-1) * mu**(1/2) * (a0 * mu * (mu + a0 * (deltaVtotal + (a3**(-1) * mu)**(1/2)) * (deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * 
              mu)**(1/2)))**(-1))**(-1/2) + (3/5) * a0**(-5/2) * J2 * mu**(1/2) * Re**2 + (-3/160) * J2 * mu**(1/2) * (a0 * mu * (mu + a0 * (deltaVtotal + (a3**(-1) * 
              mu)**(1/2)) * (deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-1))**(-5/2) * Re**2 + (-9/10) * a0**(-5/2) * J2 * mu**(1/2) * Re**2 * 
              np.sin(incl)**2 + (9/320) * J2 * mu**(1/2) * (a0 * mu * (mu + a0 * (deltaVtotal + (a3**(-1) * mu)**(1/2)) * (deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + 
              (a3**(-1) * mu)**(1/2)))**(-1))**(-5/2) * Re**2 * np.sin(incl)**2)) * ((1/8) * (a0**(-3) * mu**(-2) * (mu + a0 * (deltaVtotal + (a3**(-1) * mu)**(1/2)) * 
              (deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**3)**(1/2) * (1 + (3/32) * a0**(-2) * J2 * mu**(-2) * (mu + a0 * (deltaVtotal + 
              (a3**(-1) * mu)**(1/2)) * (deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**2 * Re**2 * (1 + (-3/2) * np.sin(incl)**2)) + (3/256) * 
              a0**(-2) * J2 * mu**(-2) * (mu + a0 * (deltaVtotal + (a3**(-1) * mu)**(1/2)) * (deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**2 *
              (a0**(-3) * mu**(-2) * (mu + a0 * (deltaVtotal + (a3**(-1) * mu)**(1/2)) * (deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**3)**(1/2) *
              Re**2 * (2 + (-5/2) * np.sin(incl)**2) * (1 + (3/32) * a0**(-2) * J2 * mu**(-2) * (mu + a0 * (deltaVtotal + (a3**(-1) * mu)**(1/2)) * (deltaVtotal + 2 * 
              (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**2 * Re**2 * (1 + (-3/2) * np.sin(incl)**2)))) 
  

    deltau3_low = ((1/536870912) * A**(-1) * a0**(-8) * a3**(-8) * mu**(-7) * (mu + a0 * (deltaVtotal + (a3**(-1) * mu)**(1/2)) * (deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + 
              (a3**(-1) * mu)**(1/2)))**8 * (8388608 * a0**6 * a3**6 * mu**6 * (mu + a0 * (deltaVtotal + (a3**(-1) * mu)**(1/2)) * (deltaVtotal + 2 * (a0**(-1) * 
              mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-6) * ((-1) * a3**2 + 16 * a0**2 * mu**2 * (mu + a0 * (deltaVtotal + (a3**(-1) * mu)**(1/2)) * (deltaVtotal + 2 * 
              (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-2)) + 27 * J2**3 * ((-1) * a3**8 + 65536 * a0**8 * mu**8 * (mu + a0 * (deltaVtotal + (a3**(-1) * 
              mu)**(1/2)) * (deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-8)) * Re**6 * (1 + 3 * np.cos(2 * incl))**2 * (3 + 5 * np.cos(2 * 
              incl)) + 98304 * a0**4 * a3**4 * J2 * mu**4 * (mu + a0 * (deltaVtotal + (a3**(-1) * mu)**(1/2)) * (deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * 
              mu)**(1/2)))**(-4) * ((-1) * a3**4 + 256 * a0**4 * mu**4 * (mu + a0 * (deltaVtotal + (a3**(-1) * mu)**(1/2)) * (deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + 
              (a3**(-1) * mu)**(1/2)))**(-4)) * Re**2 * (5 + 11 * np.cos(2 * incl)) + 768 * a0**2 * a3**2 * J2**2 * mu**2 * (mu + a0 * (deltaVtotal + (a3**(-1) * 
              mu)**(1/2)) * (deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-2) * ((-1) * a3**6 + 4096 * a0**6 * mu**6 * (mu + a0 * (deltaVtotal + 
              (a3**(-1) * mu)**(1/2)) * (deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-6)) * Re**4 * (53 + 68 * np.cos(2 * incl) + 39 * 
              np.cos(4 * incl))))

    ufinal_low = u0  +  deltau1_low  +  deltau2_low  +  deltau3_low
    ufinal_low = ufinal_low % (2*np.pi) 
    
    #return(deltaRAAN1_low, deltaRAAN2_low, deltaRAAN3_low, RAANfinal_low, deltau1_low, deltau2_low, deltau3_low, ufinal_low)
    return(RAANfinal_low, ufinal_low)

def full_man_raise(mu, Re, J2, RAAN0, u0, accel, a0, a3, incl, deltaVtotal, ttotal):
    """
    Calculate change in right ascension of ascending node (RAAN) and argument of latitude (AOL) in each phase of manoeuvre
    and at manoeuvre end for orbit raising 3-phase manoeuvre
    
    --- Inputs ---
    :param mu: standard gravitational parameter of Earth, m^3/s^2
    :param Re: mean Earth radius, m
    :param J2: J2 coefficient, -
    :param RAAN0: initial RAAN, rads
    :param u0: initial AOL, rads  
    :param accel: propulsive acceleration, m/s^2
    :param a0: initial mean semi-major axis, m
    :param a3: final mean semi-major axis, m
    :param incl: initial inclination, rads (assumed constant)
    :param deltaVtotal: deltaV to be used for manoeuvre, m/s
    :param ttotal: total manoeuvre time, seconds 
    
    
    --- Outputs ---
    :return deltaRAAN1_raise: change in RAAN during phase 1 of manoeuvre, rads
    :return deltaRAAN2_raise: change in RAAN during phase 2 of manoeuvre, rads
    :return deltaRAAN3_raise: change in RAAN during phase 3 of manoeuvre, rads
    :return RAANfinal_raise: final RAAN at end of manoeuvre, rads
    :return deltau_raise: change in AOL during phase 1 of manoeuvre, rads
    :return deltau2_raise: change in AOL during phase 2 of manoeuvre, rads
    :return deltau3_raise: change in AOL during phase 3 of manoeuvre, rads
    :return ufinal_raise: final AOL at end of manoeuvre, rads

    """
    B = accel                # propulsive acceleration, m/s^2 (positive for raising case)

    # ---------------------------
    # Raising Maneuver Equations
    # ---------------------------
    # RAAN
    # ---------------------------
    deltaRAAN1_raise = ((3/134217728) * B**(-1) * a0**(-16) * J2 * mu**(-7) * (mu + a0 * ((-1) * deltaVtotal + (a3**(-1) * mu)**(1/2)) * ((-1) * deltaVtotal + 2 * (a0**(-1) * 
                   mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**8 * Re**2 * np.cos(incl) * (32768 * a0**8 * mu**4 * (mu + a0 * ((-1) * deltaVtotal + (a3**(-1) * mu)**(1/2)) *
                   ((-1) * deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-4) * (a0**4 + (-256) * a0**4 * mu**4 * (mu + a0 * ((-1) *deltaVtotal + 
                   (a3**(-1) * mu)**(1/2)) * ((-1) * deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-4)) + 1024 * a0**4 * J2 * mu**2 * (mu + a0 * 
                   ((-1) * deltaVtotal + (a3**(-1) * mu)**(1/2)) * ((-1) * deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-2) * (a0**6 + (-4096) * 
                   a0**6 * mu**6 * (mu + a0 * ((-1) * deltaVtotal + (a3**(-1) * mu)**(1/2)) * ((-1) * deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * 
                   mu)**(1/2)))**(-6)) * Re**2 * (1 + 3 * np.cos(2 * incl)) + 9 * J2**2 * (a0**8 + (-65536) * a0**8 * mu**8 * (mu + a0 * ((-1) * deltaVtotal + (a3**(-1) * 
                   mu)**(1/2)) * ((-1) * deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-8)) * Re**4 * (1 + 3 * np.cos(2 * incl))**2))

    deltaRAAN2_raise = ((-3/256) * a0**(-2) * J2 * mu**(-2) * (mu + a0 * ((-1) * deltaVtotal + (a3**(-1) * mu)**(1/2)) * ((-1) * deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + 
                   (a3**(-1) * mu)**(1/2)))**2 * (a0**(-3) * mu**(-2) * (mu + a0 * ((-1) * deltaVtotal + (a3**(-1) * mu)**(1/2)) * ((-1) * deltaVtotal + 2 * (a0**(-1) * 
                   mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**3)**(1/2) * Re**2 * np.cos(incl) * (1 + (3/32) * a0**(-2) * J2 * mu**(-2) * (mu + a0 * ((-1) * deltaVtotal + 
                   (a3**(-1) * mu)**(1/2)) * ((-1) * deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**2 * Re**2 * (1 + (-3/2) * np.sin(incl)**2)) * 
                   (ttotal + (-1/640) * B**(-1) * a3**(-5/2) * mu**(1/2) * (a0 * mu * (mu + a0 * ((-1) * deltaVtotal + (a3**(-1) * mu)**(1/2)) * ((-1) * deltaVtotal + 2 * 
                   (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-1))**(-5/2) * ((-320) * a0**2 * a3**(5/2) * mu**2 * (mu + a0 * ((-1) * deltaVtotal + (a3**(-1) * 
                   mu)**(1/2)) * ((-1) * deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-2) + 3 * a3**(5/2) * J2 * Re**2 * ((-2) + 3 * 
                   np.sin(incl)**2) + 32 * (a0 * mu * (mu + a0 * ((-1) * deltaVtotal + (a3**(-1) * mu)**(1/2)) * ((-1) * deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + 
                   (a3**(-1) * mu)**(1/2)))**(-1))**(5/2) * (20 * a3**2 + 3 * J2 * Re**2 * (2 + (-3) * np.sin(incl)**2))) + (1/640) * B**(-1) * a0**(-5/2) * mu**(1/2) *
                   (a0 * mu * (mu + a0 * ((-1) * deltaVtotal + (a3**(-1) * mu)**(1/2)) * ((-1) * deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * 
                   mu)**(1/2)))**(-1))**(-5/2) * ((-640) * a0**2 * (a0 * mu * (mu + a0 * ((-1) * deltaVtotal + (a3**(-1) * mu)**(1/2)) * ((-1) * deltaVtotal + 2 * (a0**(-1) *
                   mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-1))**(5/2) + 96 * J2 * (a0 * mu * (mu + a0 * ((-1) * deltaVtotal + (a3**(-1) * mu)**(1/2)) * ((-1) * deltaVtotal +
                   2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-1))**(5/2) * Re**2 * ((-2) + 3 * np.sin(incl)**2) + a0**(5/2) * (320 * a0**2 * mu**2 * (mu + a0 *
                   ((-1) * deltaVtotal + (a3**(-1) * mu)**(1/2)) * ((-1) * deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-2) + 3 * J2 * Re**2 * (2 + 
                   (-3) * np.sin(incl)**2)))))

    deltaRAAN3_raise = ((-3/134217728) * B**(-1) * a0**(-8) * a3**(-8) * J2 * mu**(-7) * (mu + a0 * ((-1) * deltaVtotal + (a3**(-1) * mu)**(1/2)) * ((-1) * deltaVtotal + 2 * 
                   (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**8 * Re**2 * np.cos(incl) * (32768 * a0**4 * a3**4 * mu**4 * (mu + a0 * ((-1) * deltaVtotal + (a3**(-1) *
                   mu)**(1/2)) * ((-1) * deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-4) * ((-1) * a3**4 + 256 * a0**4 * mu**4 * (mu + a0 * ((-1) * 
                   deltaVtotal + (a3**(-1) * mu)**(1/2)) * ((-1) * deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-4)) + 1024 * a0**2 * a3**2 * J2 * 
                   mu**2 * (mu + a0 * ((-1) * deltaVtotal + (a3**(-1) * mu)**(1/2)) * ((-1) * deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-2) * 
                   ((-1) * a3**6 + 4096 * a0**6 * mu**6 * (mu + a0 * ((-1) * deltaVtotal + (a3**(-1) * mu)**(1/2)) * ((-1) * deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + 
                   (a3**(-1) * mu)**(1/2)))**(-6)) * Re**2 * (1 + 3 * np.cos(2 * incl)) + 9 * J2**2 * ((-1) * a3**8 + 65536 * a0**8 * mu**8 * (mu + a0 * ((-1) * deltaVtotal + 
                   (a3**(-1) * mu)**(1/2)) * ((-1) * deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-8)) * Re**4 * (1 + 3 * np.cos(2 * incl))**2))


    RAANfinal_raise = RAAN0  +  deltaRAAN1_raise  +  deltaRAAN2_raise  +  deltaRAAN3_raise
    RAANfinal_raise = RAANfinal_raise % (2*np.pi)

    # ---------------------------
    # AOL
    # ---------------------------

    deltau1_raise = ((-1/536870912) * B**(-1) * a0**(-16) * mu**(-7) * (mu + a0 * ((-1) * deltaVtotal + (a3**(-1) * mu)**(1/2)) * ((-1) * deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + 
                (a3**(-1) * mu)**(1/2)))**8 * (8388608 * a0**12 * mu**6 * (mu + a0 * ((-1) * deltaVtotal + (a3**(-1) * mu)**(1/2)) * ((-1) * deltaVtotal + 2 * (a0**(-1) * 
                mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-6) * (a0**2 + (-16) * a0**2 * mu**2 * (mu + a0 * ((-1) * deltaVtotal + (a3**(-1) * mu)**(1/2)) * ((-1) * deltaVtotal + 
                2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-2)) + 27 * J2**3 * (a0**8 + (-65536) * a0**8 * mu**8 * (mu + a0 * ((-1) * deltaVtotal + (a3**(-1) *
                mu)**(1/2)) * ((-1) * deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-8)) * Re**6 * (1 + 3 * np.cos(2 * incl))**2 * (3 + 5 * 
                np.cos(2 * incl)) + 98304 * a0**8 * J2 * mu**4 * (mu + a0 * ((-1) * deltaVtotal + (a3**(-1) * mu)**(1/2)) * ((-1) * deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + 
                (a3**(-1) * mu)**(1/2)))**(-4) * (a0**4 + (-256) * a0**4 * mu**4 * (mu + a0 * ((-1) * deltaVtotal + (a3**(-1) * mu)**(1/2)) * ((-1) * deltaVtotal + 2 * 
                (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-4)) * Re**2 * (5 + 11 * np.cos(2 * incl)) + 768 * a0**4 * J2**2 * mu**2 * (mu + a0 * ((-1) * deltaVtotal + 
                (a3**(-1) * mu)**(1/2)) * ((-1) * deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-2) * (a0**6 + (-4096) * a0**6 * mu**6 * (mu + a0 * 
                ((-1) * deltaVtotal + (a3**(-1) * mu)**(1/2)) * ((-1) * deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-6)) * Re**4 * (53 + 68 * 
                np.cos(2 * incl) + 39 * np.cos(4 * incl))))

    deltau2_raise = ((ttotal + (1/2) * B**(-1) * ((-2) * a3**(-1/2) * mu**(1/2) + mu**(1/2) * (a0 * mu * (mu + a0 * ((-1) * deltaVtotal + (a3**(-1) * mu)**(1/2)) * ((-1) * 
                deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-1))**(-1/2) + (-3/5) * a3**(-5/2) * J2 * mu**(1/2) * Re**2 + (3/160) * J2 * mu**(1/2) * 
                (a0 * mu * (mu + a0 * ((-1) * deltaVtotal + (a3**(-1) * mu)**(1/2)) * ((-1) * deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-1))**(-5/2) * 
                Re**2 + (9/10) * a3**(-5/2) * J2 * mu**(1/2) * Re**2 * np.sin(incl)**2 + (-9/320) * J2 * mu**(1/2) * (a0 * mu * (mu + a0 * ((-1) * deltaVtotal + (a3**(-1) * 
                mu)**(1/2)) * ((-1) * deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-1))**(-5/2) * Re**2 * np.sin(incl)**2) + (-1/2) * B**(-1) * 
                (2 * a0**(-1/2) * mu**(1/2) + (-1) * mu**(1/2) * (a0 * mu * (mu + a0 * ((-1) * deltaVtotal + (a3**(-1) * mu)**(1/2)) * ((-1) * deltaVtotal + 2 * (a0**(-1) * 
                mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-1))**(-1/2) + (3/5) * a0**(-5/2) * J2 * mu**(1/2) * Re**2 + (-3/160) * J2 * mu**(1/2) * (a0 * mu * (mu + a0 * ((-1) * 
                deltaVtotal + (a3**(-1) * mu)**(1/2)) * ((-1) * deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-1))**(-5/2) * Re**2 + (-9/10) * 
                a0**(-5/2) * J2 * mu**(1/2) * Re**2 * np.sin(incl)**2 + (9/320) * J2 * mu**(1/2) * (a0 * mu * (mu + a0 * ((-1) * deltaVtotal + (a3**(-1) * mu)**(1/2)) * 
                ((-1) * deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-1))**(-5/2) * Re**2 * np.sin(incl)**2)) * ((1/8) * (a0**(-3) * mu**(-2) * 
                (mu + a0 * ((-1) * deltaVtotal + (a3**(-1) * mu)**(1/2)) * ((-1) * deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**3)**(1/2) * 
                (1 + (3/32) * a0**(-2) * J2 * mu**(-2) * (mu + a0 * ((-1) * deltaVtotal + (a3**(-1) * mu)**(1/2)) * ((-1) * deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + 
                (a3**(-1) * mu)**(1/2)))**2 * Re**2 * (1 + (-3/2) * np.sin(incl)**2)) + (3/256) * a0**(-2) * J2 * mu**(-2) * (mu + a0 * ((-1) * deltaVtotal + 
                (a3**(-1) * mu)**(1/2)) * ((-1) * deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**2 * (a0**(-3) * mu**(-2) * (mu + a0 * ((-1) *
                deltaVtotal + (a3**(-1) * mu)**(1/2)) * ((-1) * deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**3)**(1/2) * Re**2 * (2 + (-5/2) * 
                np.sin(incl)**2) * (1 + (3/32) * a0**(-2) * J2 * mu**(-2) * (mu + a0 * ((-1) * deltaVtotal + (a3**(-1) * mu)**(1/2)) * ((-1) * deltaVtotal + 2 * 
                (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**2 * Re**2 * (1 + (-3/2) * np.sin(incl)**2))))

    deltau3_raise = ((1/536870912) * B**(-1) * a0**(-8) * a3**(-8) * mu**(-7) * (mu + a0 * ((-1) * deltaVtotal + (a3**(-1) * mu)**(1/2)) * ((-1) * deltaVtotal + 2 * (a0**(-1) * 
                mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**8 * (8388608 * a0**6 * a3**6 * mu**6 * (mu + a0 * ((-1) * deltaVtotal + (a3**(-1) * mu)**(1/2)) * ((-1) * deltaVtotal + 
                2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-6) * ((-1) * a3**2 + 16 * a0**2 * mu**2 * (mu + a0 * ((-1) * deltaVtotal + (a3**(-1) * mu)**(1/2)) * 
                ((-1) * deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-2)) + 27 * J2**3 * ((-1) * a3**8 + 65536 * a0**8 * mu**8 * (mu + a0 * ((-1) * 
                deltaVtotal + (a3**(-1) * mu)**(1/2)) * ((-1) * deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-8)) * Re**6 * (1 + 3 * 
                np.cos(2 * incl))**2 * (3 + 5 * np.cos(2 * incl)) + 98304 * a0**4 * a3**4 * J2 * mu**4 * (mu + a0 * ((-1) * deltaVtotal + (a3**(-1) * mu)**(1/2)) * ((-1) * 
                deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-4) * ((-1) * a3**4 + 256 * a0**4 * mu**4 * (mu + a0 * ((-1) * deltaVtotal + 
                (a3**(-1) * mu)**(1/2)) * ((-1) * deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-4)) * Re**2 * (5 + 11 * np.cos(2 * incl)) + 768 * 
                a0**2 * a3**2 * J2**2 * mu**2 * (mu + a0 * ((-1) * deltaVtotal + (a3**(-1) * mu)**(1/2)) * ((-1) * deltaVtotal + 2 * (a0**(-1) * mu)**(1/2) + 
                (a3**(-1) * mu)**(1/2)))**(-2) * ((-1) * a3**6 + 4096 * a0**6 * mu**6 * (mu + a0 * ((-1) * deltaVtotal + (a3**(-1) * mu)**(1/2)) * ((-1) * deltaVtotal + 2 * 
                (a0**(-1) * mu)**(1/2) + (a3**(-1) * mu)**(1/2)))**(-6)) * Re**4 * (53 + 68 * np.cos(2 * incl) + 39 * np.cos(4 * incl))))

    ufinal_raise = u0  +  deltau1_raise  +  deltau2_raise  +  deltau3_raise
    ufinal_raise = ufinal_raise % (2*np.pi) 

    #return(deltaRAAN1_raise, deltaRAAN2_raise, deltaRAAN3_raise, RAANfinal_raise, deltau1_raise, deltau2_raise, deltau3_raise, ufinal_raise)
    return(RAANfinal_raise, ufinal_raise)

def times_man_low(mu, Re, J2, RAAN0, u0, accel, a0, a3, incl, deltaVtotal, ttotal):
    """
    Calculate time for each phase of manoeuvre

    --- Inputs ---
    :param mu: standard gravitational parameter of Earth, m^3/s^2
    :param Re: mean Earth radius, m
    :param J2: J2 coefficient, -
    :param RAAN0: initial RAAN, rads
    :param u0: initial AOL, rads  
    :param accel: propulsive acceleration, m/s^2
    :param a0: initial mean semi-major axis, m
    :param a3: final mean semi-major axis, m
    :param incl: initial inclination, rads (assumed constant)
    :param deltaVtotal: deltaV to be used for manoeuvre, m/s
    :param ttotal: total manoeuvre time, seconds 
    
    
    --- Outputs ---
    :return t1: time for phase 1 of manoeuvre, seconds
    :return t2: time for phase 2 of manoeuvre, seconds
    :return t3: time for phase 1 of manoeuvre, seconds
    """
    A = -accel  # negative for lowering manoeuvre

    t1 = ((-1/640)*A**(-1)*mu**(1/2)*a0**(-5/2)*(mu*a0*(mu+a0*((mu*a3**(-1))**(1/2)+deltaVtotal)*(2*(mu*a0**(-
         1))**(1/2)+(mu*a3**(-1))**(1/2)+deltaVtotal))**(-1))**(-5/2)*((-640)*a0**2*(mu*a0*(mu+a0*((mu*a3**(-1))**(1/2)+
         deltaVtotal)*(2*(mu*a0**(-1))**(1/2)+(mu*a3**(-1))**(1/2)+deltaVtotal))**(-1))**(5/2)+96*((-2)+
         3*np.sin(incl)**2)*J2*Re**2*(mu*a0*(mu+a0*((mu*a3**(-1))**(1/2)+deltaVtotal)*(2*(mu*a0**(-1))**(1/2)+
         (mu*a3**(-1))**(1/2)+deltaVtotal))**(-1))**(5/2)+a0**(5/2)*(3*(2+(-3)*np.sin(incl)**2)*J2*Re**2+
         320*mu**2*a0**2*(mu+a0*((mu*a3**(-1))**(1/2)+deltaVtotal)*(2*(mu*a0**(-1))**(1/2)+(mu*a3**(-1))**(1/2)+
         deltaVtotal))**(-2))))

    t3 = ((1/640)*A**(-1)*mu**(1/2)*a3**(-5/2)*(mu*a0*(mu+a0*((mu*a3**(-1))**(1/2)+deltaVtotal)*(2*(mu*a0**(-1))**(1/2)+
         (mu*a3**(-1))**(1/2)+deltaVtotal))**(-1))**(-5/2)*(3*((-2)+3*np.sin(incl)**2)*a3**(5/2)*J2*Re**2+32*(20*a3**2+3*(2+
         (-3)*np.sin(incl)**2)*J2*Re**2)*(mu*a0*(mu+a0*((mu*a3**(-1))**(1/2)+deltaVtotal)*(2*(mu*a0**(-1))**(1/2)+
         (mu*a3**(-1))**(1/2)+deltaVtotal))**(-1))**(5/2)+(-320)*mu**2*a0**2*a3**(5/2)*(mu+a0*((mu*a3**(-1))**(1/2)+
         deltaVtotal)*(2*(mu*a0**(-1))**(1/2)+(mu*a3**(-1))**(1/2)+deltaVtotal))**(-2)))

    t2 = ttotal - t1 - t3

    return(t1, t2, t3)

def times_man_raise(mu, Re, J2, RAAN0, u0, accel, a0, a3, incl, deltaVtotal, ttotal):
    """
    Calculate time for each phase of manoeuvre

    --- Inputs ---
    :param mu: standard gravitational parameter of Earth, m^3/s^2
    :param Re: mean Earth radius, m
    :param J2: J2 coefficient, -
    :param RAAN0: initial RAAN, rads
    :param u0: initial AOL, rads  
    :param accel: propulsive acceleration, m/s^2
    :param a0: initial mean semi-major axis, m
    :param a3: final mean semi-major axis, m
    :param incl: initial inclination, rads (assumed constant)
    :param deltaVtotal: deltaV to be used for manoeuvre, m/s
    :param ttotal: total manoeuvre time, seconds 
    
    
    --- Outputs ---
    :return t1: time for phase 1 of manoeuvre, seconds
    :return t2: time for phase 2 of manoeuvre, seconds
    :return t3: time for phase 1 of manoeuvre, seconds
    """
    A = accel  # positive for raising manoeuvre

    t1 = -((-1/640)*A**(-1)*mu**(1/2)*a0**(-5/2)*(mu*a0*(mu+a0*((mu*a3**(-1))**(1/2)+deltaVtotal)*(2*(mu*a0**(-
         1))**(1/2)+(mu*a3**(-1))**(1/2)+deltaVtotal))**(-1))**(-5/2)*((-640)*a0**2*(mu*a0*(mu+a0*((mu*a3**(-1))**(1/2)+
         deltaVtotal)*(2*(mu*a0**(-1))**(1/2)+(mu*a3**(-1))**(1/2)+deltaVtotal))**(-1))**(5/2)+96*((-2)+
         3*np.sin(incl)**2)*J2*Re**2*(mu*a0*(mu+a0*((mu*a3**(-1))**(1/2)+deltaVtotal)*(2*(mu*a0**(-1))**(1/2)+
         (mu*a3**(-1))**(1/2)+deltaVtotal))**(-1))**(5/2)+a0**(5/2)*(3*(2+(-3)*np.sin(incl)**2)*J2*Re**2+
         320*mu**2*a0**2*(mu+a0*((mu*a3**(-1))**(1/2)+deltaVtotal)*(2*(mu*a0**(-1))**(1/2)+(mu*a3**(-1))**(1/2)+
         deltaVtotal))**(-2))))

    t3 = -((1/640)*A**(-1)*mu**(1/2)*a3**(-5/2)*(mu*a0*(mu+a0*((mu*a3**(-1))**(1/2)+deltaVtotal)*(2*(mu*a0**(-1))**(1/2)+
         (mu*a3**(-1))**(1/2)+deltaVtotal))**(-1))**(-5/2)*(3*((-2)+3*np.sin(incl)**2)*a3**(5/2)*J2*Re**2+32*(20*a3**2+3*(2+
         (-3)*np.sin(incl)**2)*J2*Re**2)*(mu*a0*(mu+a0*((mu*a3**(-1))**(1/2)+deltaVtotal)*(2*(mu*a0**(-1))**(1/2)+
         (mu*a3**(-1))**(1/2)+deltaVtotal))**(-1))**(5/2)+(-320)*mu**2*a0**2*a3**(5/2)*(mu+a0*((mu*a3**(-1))**(1/2)+
         deltaVtotal)*(2*(mu*a0**(-1))**(1/2)+(mu*a3**(-1))**(1/2)+deltaVtotal))**(-2)))

    t2 = ttotal - t1 - t3

    return(t1, t2, t3)
