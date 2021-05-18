def raising_maneuver(mu, Re, J2, vel_e, rad, flattening, sat, accel, delta_V, duration):
    
# Sarah Morgan's copy - this code was given to me for use and modification by Dr Ciara McGrath 1/7/2020

#   © Ciara McGrath 20/11/2018
# 
# Equations to calculate change in RAAN and AoL after 3 phase maneuver  
# using low-thrust propulsion.
# From appendix A of PhD Thesis: Analytical Methods for Satellite
# Constellation Reconfiguration and Reconnaissance using Low-Thrust
# Manoeuvres
# 
# Note: The semi-major axis used in these equations is assumed to be the 
#       mean semi-major axis.
# 
# Note: For lowering maneuvers, a negative propulsive acceleration, A, 
#       should be used. For raising maneuvers, a positive acceleration, B, 
#       should be used.
#
# * DISCLAIMER *
#   The S/W remains property of Ciara McGrath and shall not be modified,
#   nor shall it be forwarded to third parties without prior written consent

    import math
#  Variables----------------------------------------------------------
#start_time = seconds since epoch 
#duration   = duration of the maneuver (s) must be sufficiently long to
#allow acceleration to build up
#sat =       contains orbital elements - time since epoch (s), semi-major axis (km), eccentricity, inclination (rad),
#            RAAN (rad), argument of latitude (rad)
    tmaneuver = duration;
    deltaVtotal = delta_V;
    maneuver_capable = True;
    B = accel;
    a0 = sat[1]*1000;
    a3 = sat[1]*1000;
    aref = sat[1]*1000;
    incl = sat[3]*rad;
    RAAN0 = sat[4]*rad;
    RAAN_epoch = sat[7]*rad;
    u0 = sat[6]*rad;
    
    new_sat = sat[:]
    
    tmin = abs(deltaVtotal/B); 
    if tmaneuver < tmin:
         maneuver_capable = False; 
         #print("maneuver not possible - duration too short")
         return 
     
 
    deltaRAAN1_raise = (3/134217728)*B**(-1)*a0**(-16)*J2*mu**(-7)*(mu+a0*((-1)* \
      deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)*deltaVtotal+2*(a0**( \
      -1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**8*Re**2*math.cos(incl)*( \
      32768*a0**8*mu**4*(mu+a0*((-1)*deltaVtotal+(a3**(-1)*mu)**( \
      1/2))*((-1)*deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu) \
      **(1/2)))**(-4)*(a0**4+(-256)*a0**4*mu**4*(mu+a0*((-1)* \
      deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)*deltaVtotal+2*(a0**( \
      -1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-4))+1024*a0**4*J2* \
      mu**2*(mu+a0*((-1)*deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)* \
      deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-2) \
      *(a0**6+(-4096)*a0**6*mu**6*(mu+a0*((-1)*deltaVtotal+(a3**( \
      -1)*mu)**(1/2))*((-1)*deltaVtotal+2*(a0**(-1)*mu)**(1/2)+( \
      a3**(-1)*mu)**(1/2)))**(-6))*Re**2*(1+3*math.cos(2*incl))+9*J2**2*( \
      a0**8+(-65536)*a0**8*mu**8*(mu+a0*((-1)*deltaVtotal+(a3**(-1) \
      *mu)**(1/2))*((-1)*deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**( \
      -1)*mu)**(1/2)))**(-8))*Re**4*(1+3*math.cos(2*incl))**2);
    
    deltaRAAN2_raise = (-3/256)*a0**(-2)*J2*mu**(-2)*(mu+a0*((-1)*deltaVtotal+( \
      a3**(-1)*mu)**(1/2))*((-1)*deltaVtotal+2*(a0**(-1)*mu)**(1/2) \
      +(a3**(-1)*mu)**(1/2)))**2*(a0**(-3)*mu**(-2)*(mu+a0*((-1)* \
      deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)*deltaVtotal+2*(a0**( \
      -1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**3)**(1/2)*Re**2*math.cos(incl) \
      *(1+(3/32)*a0**(-2)*J2*mu**(-2)*(mu+a0*((-1)*deltaVtotal+( \
      a3**(-1)*mu)**(1/2))*((-1)*deltaVtotal+2*(a0**(-1)*mu)**(1/2) \
      +(a3**(-1)*mu)**(1/2)))**2*Re**2*(1+(-3/2)*math.sin(incl)**2))*( \
      tmaneuver+(-1/640)*B**(-1)*a3**(-5/2)*mu**(1/2)*(a0*mu*(mu+a0* \
      ((-1)*deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)*deltaVtotal+2*( \
      a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-1))**(-5/2)*(( \
      -320)*a0**2*a3**(5/2)*mu**2*(mu+a0*((-1)*deltaVtotal+(a3**( \
      -1)*mu)**(1/2))*((-1)*deltaVtotal+2*(a0**(-1)*mu)**(1/2)+( \
      a3**(-1)*mu)**(1/2)))**(-2)+3*a3**(5/2)*J2*Re**2*((-2)+3* \
      math.sin(incl)**2)+32*(a0*mu*(mu+a0*((-1)*deltaVtotal+(a3**(-1)*mu) \
      **(1/2))*((-1)*deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)* \
      mu)**(1/2)))**(-1))**(5/2)*(20*a3**2+3*J2*Re**2*(2+(-3)*math.sin( \
      incl)**2)))+(1/640)*B**(-1)*a0**(-5/2)*mu**(1/2)*(a0*mu*(mu+ \
      a0*((-1)*deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)*deltaVtotal+ \
      2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-1))**(-5/2)*( \
      (-640)*a0**2*(a0*mu*(mu+a0*((-1)*deltaVtotal+(a3**(-1)*mu) \
      **(1/2))*((-1)*deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)* \
      mu)**(1/2)))**(-1))**(5/2)+96*J2*(a0*mu*(mu+a0*((-1)* \
      deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)*deltaVtotal+2*(a0**( \
      -1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-1))**(5/2)*Re**2*(( \
      -2)+3*math.sin(incl)**2)+a0**(5/2)*(320*a0**2*mu**2*(mu+a0*((-1)* \
      deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)*deltaVtotal+2*(a0**( \
      -1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-2)+3*J2*Re**2*(2+( \
      -3)*math.sin(incl)**2))));
    
    deltaRAAN3_raise = (-3/134217728)*B**(-1)*a0**(-8)*a3**(-8)*J2*mu**(-7)*(mu+ \
      a0*((-1)*deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)*deltaVtotal+ \
      2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**8*Re**2*math.cos(incl) \
      *(32768*a0**4*a3**4*mu**4*(mu+a0*((-1)*deltaVtotal+(a3**( \
      -1)*mu)**(1/2))*((-1)*deltaVtotal+2*(a0**(-1)*mu)**(1/2)+( \
      a3**(-1)*mu)**(1/2)))**(-4)*((-1)*a3**4+256*a0**4*mu**4*(mu+ \
      a0*((-1)*deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)*deltaVtotal+ \
      2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-4))+1024* \
      a0**2*a3**2*J2*mu**2*(mu+a0*((-1)*deltaVtotal+(a3**(-1)*mu) \
      **(1/2))*((-1)*deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)* \
      mu)**(1/2)))**(-2)*((-1)*a3**6+4096*a0**6*mu**6*(mu+a0*((-1) \
      *deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)*deltaVtotal+2*(a0**( \
      -1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-6))*Re**2*(1+3*math.cos( \
      2*incl))+9*J2**2*((-1)*a3**8+65536*a0**8*mu**8*(mu+a0*((-1)* \
      deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)*deltaVtotal+2*(a0**( \
      -1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-8))*Re**4*(1+3*math.cos( \
      2*incl))**2);
    
    RAANdif_raise = (3/134217728)*B**(-1)*a0**(-16)*J2*mu**(-7)*(mu+a0*((-1)* \
      deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)*deltaVtotal+2*(a0**( \
      -1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**8*Re**2*math.cos(incl)*( \
      32768*a0**8*mu**4*(mu+a0*((-1)*deltaVtotal+(a3**(-1)*mu)**( \
      1/2))*((-1)*deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu) \
      **(1/2)))**(-4)*(a0**4+(-256)*a0**4*mu**4*(mu+a0*((-1)* \
      deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)*deltaVtotal+2*(a0**( \
      -1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-4))+1024*a0**4*J2* \
      mu**2*(mu+a0*((-1)*deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)* \
      deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-2) \
      *(a0**6+(-4096)*a0**6*mu**6*(mu+a0*((-1)*deltaVtotal+(a3**( \
      -1)*mu)**(1/2))*((-1)*deltaVtotal+2*(a0**(-1)*mu)**(1/2)+( \
      a3**(-1)*mu)**(1/2)))**(-6))*Re**2*(1+3*math.cos(2*incl))+9*J2**2*( \
      a0**8+(-65536)*a0**8*mu**8*(mu+a0*((-1)*deltaVtotal+(a3**(-1) \
      *mu)**(1/2))*((-1)*deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**( \
      -1)*mu)**(1/2)))**(-8))*Re**4*(1+3*math.cos(2*incl))**2)+( \
      -3/134217728)*B**(-1)*a0**(-8)*a3**(-8)*J2*mu**(-7)*(mu+a0* \
      ((-1)*deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)*deltaVtotal+2*( \
      a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**8*Re**2*math.cos(incl)*( \
      32768*a0**4*a3**4*mu**4*(mu+a0*((-1)*deltaVtotal+(a3**(-1)* \
      mu)**(1/2))*((-1)*deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1) \
      *mu)**(1/2)))**(-4)*((-1)*a3**4+256*a0**4*mu**4*(mu+a0*(( \
      -1)*deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)*deltaVtotal+2*( \
      a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-4))+1024*a0**2* \
      a3**2*J2*mu**2*(mu+a0*((-1)*deltaVtotal+(a3**(-1)*mu)**(1/2) \
      )*((-1)*deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**( \
      1/2)))**(-2)*((-1)*a3**6+4096*a0**6*mu**6*(mu+a0*((-1)* \
      deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)*deltaVtotal+2*(a0**( \
      -1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-6))*Re**2*(1+3*math.cos( \
      2*incl))+9*J2**2*((-1)*a3**8+65536*a0**8*mu**8*(mu+a0*((-1)* \
      deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)*deltaVtotal+2*(a0**( \
      -1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-8))*Re**4*(1+3*math.cos( \
      2*incl))**2)+(3/2)*aref**(-2)*J2*(aref**(-3)*mu)**(1/2)*Re**2* \
      tmaneuver*math.cos(incl)*(1+(3/2)*aref**(-2)*J2*Re**2*(1+(-3/2)*math.sin(incl) \
      **2))+(-3/256)*a0**(-2)*J2*mu**(-2)*(mu+a0*((-1)* \
      deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)*deltaVtotal+2*(a0**( \
      -1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**2*(a0**(-3)*mu**(-2)*( \
      mu+a0*((-1)*deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)* \
      deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**3) \
      **(1/2)*Re**2*math.cos(incl)*(1+(3/32)*a0**(-2)*J2*mu**(-2)*(mu+ \
      a0*((-1)*deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)*deltaVtotal+ \
      2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**2*Re**2*(1+( \
      -3/2)*math.sin(incl)**2))*(tmaneuver+(-1/640)*B**(-1)*a3**(-5/2)*mu**( \
      1/2)*(a0*mu*(mu+a0*((-1)*deltaVtotal+(a3**(-1)*mu)**(1/2))* \
      ((-1)*deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)) \
      )**(-1))**(-5/2)*((-320)*a0**2*a3**(5/2)*mu**2*(mu+a0*((-1) \
      *deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)*deltaVtotal+2*(a0**( \
      -1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-2)+3*a3**(5/2)*J2* \
      Re**2*((-2)+3*math.sin(incl)**2)+32*(a0*mu*(mu+a0*((-1)* \
      deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)*deltaVtotal+2*(a0**( \
      -1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-1))**(5/2)*(20*a3**2+ \
      3*J2*Re**2*(2+(-3)*math.sin(incl)**2)))+(1/640)*B**(-1)*a0**(-5/2)* \
      mu**(1/2)*(a0*mu*(mu+a0*((-1)*deltaVtotal+(a3**(-1)*mu)**( \
      1/2))*((-1)*deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu) \
      **(1/2)))**(-1))**(-5/2)*((-640)*a0**2*(a0*mu*(mu+a0*((-1)* \
      deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)*deltaVtotal+2*(a0**( \
      -1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-1))**(5/2)+96*J2*( \
      a0*mu*(mu+a0*((-1)*deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)* \
      deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-1) \
      )**(5/2)*Re**2*((-2)+3*math.sin(incl)**2)+a0**(5/2)*(320*a0**2* \
      mu**2*(mu+a0*((-1)*deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)* \
      deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-2) \
      +3*J2*Re**2*(2+(-3)*math.sin(incl)**2))));
    
    
    RAANtotal_raise = RAAN0 + deltaRAAN1_raise + deltaRAAN2_raise + deltaRAAN3_raise;
    
    
    
    deltau1_raise = (-1/536870912)*B**(-1)*a0**(-16)*mu**(-7)*(mu+a0*((-1)* \
      deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)*deltaVtotal+2*(a0**( \
      -1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**8*(8388608*a0**12* \
      mu**6*(mu+a0*((-1)*deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)* \
      deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-6) \
      *(a0**2+(-16)*a0**2*mu**2*(mu+a0*((-1)*deltaVtotal+(a3**(-1) \
      *mu)**(1/2))*((-1)*deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**( \
      -1)*mu)**(1/2)))**(-2))+27*J2**3*(a0**8+(-65536)*a0**8* \
      mu**8*(mu+a0*((-1)*deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)* \
      deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-8) \
      )*Re**6*(1+3*math.cos(2*incl))**2*(3+5*math.cos(2*incl))+98304*a0**8*J2* \
      mu**4*(mu+a0*((-1)*deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)* \
      deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-4) \
      *(a0**4+(-256)*a0**4*mu**4*(mu+a0*((-1)*deltaVtotal+(a3**( \
      -1)*mu)**(1/2))*((-1)*deltaVtotal+2*(a0**(-1)*mu)**(1/2)+( \
      a3**(-1)*mu)**(1/2)))**(-4))*Re**2*(5+11*math.cos(2*incl))+768* \
      a0**4*J2**2*mu**2*(mu+a0*((-1)*deltaVtotal+(a3**(-1)*mu)**( \
      1/2))*((-1)*deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu) \
      **(1/2)))**(-2)*(a0**6+(-4096)*a0**6*mu**6*(mu+a0*((-1)* \
      deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)*deltaVtotal+2*(a0**( \
      -1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-6))*Re**4*(53+68* \
      math.cos(2*incl)+39*math.cos(4*incl)));
    
    deltau2_raise = (tmaneuver+(1/2)*B**(-1)*((-2)*a3**(-1/2)*mu**(1/2)+mu**(1/2)*( \
      a0*mu*(mu+a0*((-1)*deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)* \
      deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-1) \
      )**(-1/2)+(-3/5)*a3**(-5/2)*J2*mu**(1/2)*Re**2+(3/160)*J2* \
      mu**(1/2)*(a0*mu*(mu+a0*((-1)*deltaVtotal+(a3**(-1)*mu)**( \
      1/2))*((-1)*deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu) \
      **(1/2)))**(-1))**(-5/2)*Re**2+(9/10)*a3**(-5/2)*J2*mu**(1/2) \
      *Re**2*math.sin(incl)**2+(-9/320)*J2*mu**(1/2)*(a0*mu*(mu+a0*((-1) \
      *deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)*deltaVtotal+2*(a0**( \
      -1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-1))**(-5/2)*Re**2* \
      math.sin(incl)**2)+(-1/2)*B**(-1)*(2*a0**(-1/2)*mu**(1/2)+(-1)*mu**( \
      1/2)*(a0*mu*(mu+a0*((-1)*deltaVtotal+(a3**(-1)*mu)**(1/2))* \
      ((-1)*deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)) \
      )**(-1))**(-1/2)+(3/5)*a0**(-5/2)*J2*mu**(1/2)*Re**2+(-3/160) \
      *J2*mu**(1/2)*(a0*mu*(mu+a0*((-1)*deltaVtotal+(a3**(-1)* \
      mu)**(1/2))*((-1)*deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1) \
      *mu)**(1/2)))**(-1))**(-5/2)*Re**2+(-9/10)*a0**(-5/2)*J2* \
      mu**(1/2)*Re**2*math.sin(incl)**2+(9/320)*J2*mu**(1/2)*(a0*mu*(mu+ \
      a0*((-1)*deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)*deltaVtotal+ \
      2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-1))**(-5/2)* \
      Re**2*math.sin(incl)**2))*((1/8)*(a0**(-3)*mu**(-2)*(mu+a0*((-1)* \
      deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)*deltaVtotal+2*(a0**( \
      -1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**3)**(1/2)*(1+(3/32)* \
      a0**(-2)*J2*mu**(-2)*(mu+a0*((-1)*deltaVtotal+(a3**(-1)*mu) \
      **(1/2))*((-1)*deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)* \
      mu)**(1/2)))**2*Re**2*(1+(-3/2)*math.sin(incl)**2))+(3/256)*a0**(-2)* \
      J2*mu**(-2)*(mu+a0*((-1)*deltaVtotal+(a3**(-1)*mu)**(1/2))*( \
      (-1)*deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2))) \
      **2*(a0**(-3)*mu**(-2)*(mu+a0*((-1)*deltaVtotal+(a3**(-1)* \
      mu)**(1/2))*((-1)*deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1) \
      *mu)**(1/2)))**3)**(1/2)*Re**2*(2+(-5/2)*math.sin(incl)**2)*(1+(3/32) \
      *a0**(-2)*J2*mu**(-2)*(mu+a0*((-1)*deltaVtotal+(a3**(-1)* \
      mu)**(1/2))*((-1)*deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1) \
      *mu)**(1/2)))**2*Re**2*(1+(-3/2)*math.sin(incl)**2)));
    
    deltau3_raise = (1/536870912)*B**(-1)*a0**(-8)*a3**(-8)*mu**(-7)*(mu+a0*(( \
      -1)*deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)*deltaVtotal+2*( \
      a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**8*(8388608*a0**6* \
      a3**6*mu**6*(mu+a0*((-1)*deltaVtotal+(a3**(-1)*mu)**(1/2))*( \
      (-1)*deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2))) \
      **(-6)*((-1)*a3**2+16*a0**2*mu**2*(mu+a0*((-1)*deltaVtotal+ \
      (a3**(-1)*mu)**(1/2))*((-1)*deltaVtotal+2*(a0**(-1)*mu)**( \
      1/2)+(a3**(-1)*mu)**(1/2)))**(-2))+27*J2**3*((-1)*a3**8+ \
      65536*a0**8*mu**8*(mu+a0*((-1)*deltaVtotal+(a3**(-1)*mu)**( \
      1/2))*((-1)*deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu) \
      **(1/2)))**(-8))*Re**6*(1+3*math.cos(2*incl))**2*(3+5*math.cos(2*incl))+ \
      98304*a0**4*a3**4*J2*mu**4*(mu+a0*((-1)*deltaVtotal+(a3**( \
      -1)*mu)**(1/2))*((-1)*deltaVtotal+2*(a0**(-1)*mu)**(1/2)+( \
      a3**(-1)*mu)**(1/2)))**(-4)*((-1)*a3**4+256*a0**4*mu**4*(mu+ \
      a0*((-1)*deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)*deltaVtotal+ \
      2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-4))*Re**2*( \
      5+11*math.cos(2*incl))+768*a0**2*a3**2*J2**2*mu**2*(mu+a0*((-1)* \
      deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)*deltaVtotal+2*(a0**( \
      -1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-2)*((-1)*a3**6+4096* \
      a0**6*mu**6*(mu+a0*((-1)*deltaVtotal+(a3**(-1)*mu)**(1/2))*( \
      (-1)*deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2))) \
      **(-6))*Re**4*(53+68*math.cos(2*incl)+39*math.cos(4*incl)));
    
    udif_raise = (-1/536870912)*B**(-1)*a0**(-16)*mu**(-7)*(mu+a0*((-1)* \
      deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)*deltaVtotal+2*(a0**( \
      -1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**8*(8388608*a0**12* \
      mu**6*(mu+a0*((-1)*deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)* \
      deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-6) \
      *(a0**2+(-16)*a0**2*mu**2*(mu+a0*((-1)*deltaVtotal+(a3**(-1) \
      *mu)**(1/2))*((-1)*deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**( \
      -1)*mu)**(1/2)))**(-2))+27*J2**3*(a0**8+(-65536)*a0**8* \
      mu**8*(mu+a0*((-1)*deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)* \
      deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-8) \
      )*Re**6*(1+3*math.cos(2*incl))**2*(3+5*math.cos(2*incl))+98304*a0**8*J2* \
      mu**4*(mu+a0*((-1)*deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)* \
      deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-4) \
      *(a0**4+(-256)*a0**4*mu**4*(mu+a0*((-1)*deltaVtotal+(a3**( \
      -1)*mu)**(1/2))*((-1)*deltaVtotal+2*(a0**(-1)*mu)**(1/2)+( \
      a3**(-1)*mu)**(1/2)))**(-4))*Re**2*(5+11*math.cos(2*incl))+768* \
      a0**4*J2**2*mu**2*(mu+a0*((-1)*deltaVtotal+(a3**(-1)*mu)**( \
      1/2))*((-1)*deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu) \
      **(1/2)))**(-2)*(a0**6+(-4096)*a0**6*mu**6*(mu+a0*((-1)* \
      deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)*deltaVtotal+2*(a0**( \
      -1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-6))*Re**4*(53+68* \
      math.cos(2*incl)+39*math.cos(4*incl)))+(1/536870912)*B**(-1)*a0**(-8)*a3**( \
      -8)*mu**(-7)*(mu+a0*((-1)*deltaVtotal+(a3**(-1)*mu)**(1/2))* \
      ((-1)*deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)) \
      )**8*(8388608*a0**6*a3**6*mu**6*(mu+a0*((-1)*deltaVtotal+( \
      a3**(-1)*mu)**(1/2))*((-1)*deltaVtotal+2*(a0**(-1)*mu)**(1/2) \
      +(a3**(-1)*mu)**(1/2)))**(-6)*((-1)*a3**2+16*a0**2*mu**2*( \
      mu+a0*((-1)*deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)* \
      deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-2) \
      )+27*J2**3*((-1)*a3**8+65536*a0**8*mu**8*(mu+a0*((-1)* \
      deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)*deltaVtotal+2*(a0**( \
      -1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-8))*Re**6*(1+3*math.cos( \
      2*incl))**2*(3+5*math.cos(2*incl))+98304*a0**4*a3**4*J2*mu**4*(mu+ \
      a0*((-1)*deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)*deltaVtotal+ \
      2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-4)*((-1)* \
      a3**4+256*a0**4*mu**4*(mu+a0*((-1)*deltaVtotal+(a3**(-1)*mu) \
      **(1/2))*((-1)*deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)* \
      mu)**(1/2)))**(-4))*Re**2*(5+11*math.cos(2*incl))+768*a0**2*a3**2* \
      J2**2*mu**2*(mu+a0*((-1)*deltaVtotal+(a3**(-1)*mu)**(1/2))*( \
      (-1)*deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2))) \
      **(-2)*((-1)*a3**6+4096*a0**6*mu**6*(mu+a0*((-1)* \
      deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)*deltaVtotal+2*(a0**( \
      -1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-6))*Re**4*(53+68* \
      math.cos(2*incl)+39*math.cos(4*incl)))+tmaneuver*((-1)*(aref**(-3)*mu)**(1/2)* \
      (1+(3/2)*aref**(-2)*J2*Re**2*(1+(-3/2)*math.sin(incl)**2))+(-3/2)* \
      aref**(-2)*J2*(aref**(-3)*mu)**(1/2)*Re**2*(2+(-5/2)*math.sin(incl) \
      **2)*(1+(3/2)*aref**(-2)*J2*Re**2*(1+(-3/2)*math.sin(incl)**2)))+( \
      tmaneuver+(1/2)*B**(-1)*((-2)*a3**(-1/2)*mu**(1/2)+mu**(1/2)*( \
      a0*mu*(mu+a0*((-1)*deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)* \
      deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-1) \
      )**(-1/2)+(-3/5)*a3**(-5/2)*J2*mu**(1/2)*Re**2+(3/160)*J2* \
      mu**(1/2)*(a0*mu*(mu+a0*((-1)*deltaVtotal+(a3**(-1)*mu)**( \
      1/2))*((-1)*deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu) \
      **(1/2)))**(-1))**(-5/2)*Re**2+(9/10)*a3**(-5/2)*J2*mu**(1/2) \
      *Re**2*math.sin(incl)**2+(-9/320)*J2*mu**(1/2)*(a0*mu*(mu+a0*((-1) \
      *deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)*deltaVtotal+2*(a0**( \
      -1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-1))**(-5/2)*Re**2* \
      math.sin(incl)**2)+(-1/2)*B**(-1)*(2*a0**(-1/2)*mu**(1/2)+(-1)*mu**( \
      1/2)*(a0*mu*(mu+a0*((-1)*deltaVtotal+(a3**(-1)*mu)**(1/2))* \
      ((-1)*deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)) \
      )**(-1))**(-1/2)+(3/5)*a0**(-5/2)*J2*mu**(1/2)*Re**2+(-3/160) \
      *J2*mu**(1/2)*(a0*mu*(mu+a0*((-1)*deltaVtotal+(a3**(-1)* \
      mu)**(1/2))*((-1)*deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1) \
      *mu)**(1/2)))**(-1))**(-5/2)*Re**2+(-9/10)*a0**(-5/2)*J2* \
      mu**(1/2)*Re**2*math.sin(incl)**2+(9/320)*J2*mu**(1/2)*(a0*mu*(mu+ \
      a0*((-1)*deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)*deltaVtotal+ \
      2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-1))**(-5/2)* \
      Re**2*math.sin(incl)**2))*((1/8)*(a0**(-3)*mu**(-2)*(mu+a0*((-1)* \
      deltaVtotal+(a3**(-1)*mu)**(1/2))*((-1)*deltaVtotal+2*(a0**( \
      -1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**3)**(1/2)*(1+(3/32)* \
      a0**(-2)*J2*mu**(-2)*(mu+a0*((-1)*deltaVtotal+(a3**(-1)*mu) \
      **(1/2))*((-1)*deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)* \
      mu)**(1/2)))**2*Re**2*(1+(-3/2)*math.sin(incl)**2))+(3/256)*a0**(-2)* \
      J2*mu**(-2)*(mu+a0*((-1)*deltaVtotal+(a3**(-1)*mu)**(1/2))*( \
      (-1)*deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2))) \
      **2*(a0**(-3)*mu**(-2)*(mu+a0*((-1)*deltaVtotal+(a3**(-1)* \
      mu)**(1/2))*((-1)*deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1) \
      *mu)**(1/2)))**3)**(1/2)*Re**2*(2+(-5/2)*math.sin(incl)**2)*(1+(3/32) \
      *a0**(-2)*J2*mu**(-2)*(mu+a0*((-1)*deltaVtotal+(a3**(-1)* \
      mu)**(1/2))*((-1)*deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1) \
      *mu)**(1/2)))**2*Re**2*(1+(-3/2)*math.sin(incl)**2)));

    utotal_raise = u0 + deltau1_raise + deltau2_raise + deltau3_raise;
    
    
    
    new_sat[10] = sat[10]+ tmaneuver;  
    
    lat_SSPc = math.asin(math.sin(incl)*math.sin(utotal_raise)); #this is geocentric
    #lat_SSP
    new_sat[8] = (math.atan(math.tan(lat_SSPc)/(1 - flattening * (2 - flattening))))*180/math.pi;  
    #long_SSP
    new_sat[9] = (math.atan2(math.cos(incl)*math.sin(utotal_raise),math.cos(utotal_raise))\
        -vel_e*(sat[10])+RAANtotal_raise-RAAN_epoch)*180/math.pi;
    
    #RAAN       
    new_sat[4] = RAANtotal_raise*180/math.pi;
    #AoL
    new_sat[6] = utotal_raise*180/math.pi;
     
    new_sat[11] = deltaVtotal
    
    return new_sat