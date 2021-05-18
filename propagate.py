def propagate(mu, Re, J2, vel_e, rad, flattening, sat, duration):
    
    import math
    import numpy as np
#  Variables----------------------------------------------------------
#start_time = seconds since epoch 
#duration   = duration of the maneuver (s) must be sufficiently long to
#allow acceleration to build up
#sat =       contains orbital elements - time since epoch (s), semi-major axis (km), eccentricity, inclination (rad),
#            RAAN (rad), argument of latitude (rad)
    deltaVtotal = 0;
    maneuver_capable = True;
    A = 1;
    a0 = sat[1]*1000;
    a3 = sat[1]*1000;
    aref = sat[1]*1000;
    incl = sat[3]*rad;
    RAAN0 = sat[4]*rad;
    RAAN_epoch = sat[7]*rad;
    u0 = sat[6]*rad;
    
    new_sat = sat[:]
    
    tmin = abs(deltaVtotal/A); 
    
    filter_arr = []
    
    # go through each element in arr
    if isinstance(duration, float) or isinstance(duration, int):
        tmaneuver = duration
    else:     
        for element in duration:
            if element < tmin:
                filter_arr.append(False)
                
            else:
                filter_arr.append(True)
        
        tmaneuver = duration[filter_arr]
#    % ---------------------------
#    % Lowering Maneuver Equations
#    % ---------------------------
#    % RAAN
#    % ---------------------------
    deltaRAAN1_low = (3/134217728)*A**(-1)*a0**(-16)*J2*mu**(-7)*(mu+a0*( \
      deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+2*(a0**(-1)*mu) \
      **(1/2)+(a3**(-1)*mu)**(1/2)))**8*Re**2*math.cos(incl)*(32768*a0**8* \
      mu**4*(mu+a0*(deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+ \
      2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-4)*(a0**4+( \
      -256)*a0**4*mu**4*(mu+a0*(deltaVtotal+(a3**(-1)*mu)**(1/2))* \
      (deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**( \
      -4))+1024*a0**4*J2*mu**2*(mu+a0*(deltaVtotal+(a3**(-1)*mu) \
      **(1/2))*(deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**( \
      1/2)))**(-2)*(a0**6+(-4096)*a0**6*mu**6*(mu+a0*(deltaVtotal+( \
      a3**(-1)*mu)**(1/2))*(deltaVtotal+2*(a0**(-1)*mu)**(1/2)+( \
      a3**(-1)*mu)**(1/2)))**(-6))*Re**2*(1+3*math.cos(2*incl))+9*J2**2*( \
      a0**8+(-65536)*a0**8*mu**8*(mu+a0*(deltaVtotal+(a3**(-1)*mu) \
      **(1/2))*(deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**( \
      1/2)))**(-8))*Re**4*(1+3*math.cos(2*incl))**2);
    
    deltaRAAN2_low = (-3/256)*a0**(-2)*J2*mu**(-2)*(mu+a0*(deltaVtotal+(a3**(-1)* \
      mu)**(1/2))*(deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu) \
      **(1/2)))**2*(a0**(-3)*mu**(-2)*(mu+a0*(deltaVtotal+(a3**(-1) \
      *mu)**(1/2))*(deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)* \
      mu)**(1/2)))**3)**(1/2)*Re**2*math.cos(incl)*(1+(3/32)*a0**(-2)*J2* \
      mu**(-2)*(mu+a0*(deltaVtotal+(a3**(-1)*mu)**(1/2))*( \
      deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**2* \
      Re**2*(1+(-3/2)*math.sin(incl)**2))*(tmaneuver+(-1/640)*A**(-1)*a3**( \
      -5/2)*mu**(1/2)*(a0*mu*(mu+a0*(deltaVtotal+(a3**(-1)*mu)**( \
      1/2))*(deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2) \
      ))**(-1))**(-5/2)*((-320)*a0**2*a3**(5/2)*mu**2*(mu+a0*( \
      deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+2*(a0**(-1)*mu) \
      **(1/2)+(a3**(-1)*mu)**(1/2)))**(-2)+3*a3**(5/2)*J2*Re**2*(( \
      -2)+3*math.sin(incl)**2)+32*(a0*mu*(mu+a0*(deltaVtotal+(a3**(-1)*mu) \
      **(1/2))*(deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**( \
      1/2)))**(-1))**(5/2)*(20*a3**2+3*J2*Re**2*(2+(-3)*math.sin(incl)**2) \
      ))+(1/640)*A**(-1)*a0**(-5/2)*mu**(1/2)*(a0*mu*(mu+a0*( \
      deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+2*(a0**(-1)*mu) \
      **(1/2)+(a3**(-1)*mu)**(1/2)))**(-1))**(-5/2)*((-640)*a0**2*( \
      a0*mu*(mu+a0*(deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+ \
      2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-1))**(5/2)+ \
      96*J2*(a0*mu*(mu+a0*(deltaVtotal+(a3**(-1)*mu)**(1/2))*( \
      deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-1) \
      )**(5/2)*Re**2*((-2)+3*math.sin(incl)**2)+a0**(5/2)*(320*a0**2* \
      mu**2*(mu+a0*(deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+ \
      2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-2)+3*J2* \
      Re**2*(2+(-3)*math.sin(incl)**2))));
    
    deltaRAAN3_low = (-3/134217728)*A**(-1)*a0**(-8)*a3**(-8)*J2*mu**(-7)*(mu+ \
      a0*(deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+2*(a0**(-1) \
      *mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**8*Re**2*math.cos(incl)*(32768* \
      a0**4*a3**4*mu**4*(mu+a0*(deltaVtotal+(a3**(-1)*mu)**(1/2))* \
      (deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**( \
      -4)*((-1)*a3**4+256*a0**4*mu**4*(mu+a0*(deltaVtotal+(a3**( \
      -1)*mu)**(1/2))*(deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1) \
      *mu)**(1/2)))**(-4))+1024*a0**2*a3**2*J2*mu**2*(mu+a0*( \
      deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+2*(a0**(-1)*mu) \
      **(1/2)+(a3**(-1)*mu)**(1/2)))**(-2)*((-1)*a3**6+4096*a0**6* \
      mu**6*(mu+a0*(deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+ \
      2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-6))*Re**2*( \
      1+3*math.cos(2*incl))+9*J2**2*((-1)*a3**8+65536*a0**8*mu**8*(mu+ \
      a0*(deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+2*(a0**(-1) \
      *mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-8))*Re**4*(1+3*math.cos(2* \
      incl))**2);
    
    RAANdif_low = (3/134217728)*A**(-1)*a0**(-16)*J2*mu**(-7)*(mu+a0*( \
      deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+2*(a0**(-1)*mu) \
      **(1/2)+(a3**(-1)*mu)**(1/2)))**8*Re**2*math.cos(incl)*(32768*a0**8* \
      mu**4*(mu+a0*(deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+ \
      2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-4)*(a0**4+( \
      -256)*a0**4*mu**4*(mu+a0*(deltaVtotal+(a3**(-1)*mu)**(1/2))* \
      (deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**( \
      -4))+1024*a0**4*J2*mu**2*(mu+a0*(deltaVtotal+(a3**(-1)*mu) \
      **(1/2))*(deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**( \
      1/2)))**(-2)*(a0**6+(-4096)*a0**6*mu**6*(mu+a0*(deltaVtotal+( \
      a3**(-1)*mu)**(1/2))*(deltaVtotal+2*(a0**(-1)*mu)**(1/2)+( \
      a3**(-1)*mu)**(1/2)))**(-6))*Re**2*(1+3*math.cos(2*incl))+9*J2**2*( \
      a0**8+(-65536)*a0**8*mu**8*(mu+a0*(deltaVtotal+(a3**(-1)*mu) \
      **(1/2))*(deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**( \
      1/2)))**(-8))*Re**4*(1+3*math.cos(2*incl))**2)+(-3/134217728)*A**(-1) \
      *a0**(-8)*a3**(-8)*J2*mu**(-7)*(mu+a0*(deltaVtotal+(a3**(-1) \
      *mu)**(1/2))*(deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)* \
      mu)**(1/2)))**8*Re**2*math.cos(incl)*(32768*a0**4*a3**4*mu**4*(mu+ \
      a0*(deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+2*(a0**(-1) \
      *mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-4)*((-1)*a3**4+256* \
      a0**4*mu**4*(mu+a0*(deltaVtotal+(a3**(-1)*mu)**(1/2))*( \
      deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-4) \
      )+1024*a0**2*a3**2*J2*mu**2*(mu+a0*(deltaVtotal+(a3**(-1)* \
      mu)**(1/2))*(deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu) \
      **(1/2)))**(-2)*((-1)*a3**6+4096*a0**6*mu**6*(mu+a0*( \
      deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+2*(a0**(-1)*mu) \
      **(1/2)+(a3**(-1)*mu)**(1/2)))**(-6))*Re**2*(1+3*math.cos(2*incl))+ \
      9*J2**2*((-1)*a3**8+65536*a0**8*mu**8*(mu+a0*(deltaVtotal+( \
      a3**(-1)*mu)**(1/2))*(deltaVtotal+2*(a0**(-1)*mu)**(1/2)+( \
      a3**(-1)*mu)**(1/2)))**(-8))*Re**4*(1+3*math.cos(2*incl))**2)+(3/2)* \
      aref**(-2)*J2*(aref**(-3)*mu)**(1/2)*Re**2*tmaneuver*math.cos(incl)*( \
      1+(3/2)*aref**(-2)*J2*Re**2*(1+(-3/2)*math.sin(incl)**2))+(-3/256)* \
      a0**(-2)*J2*mu**(-2)*(mu+a0*(deltaVtotal+(a3**(-1)*mu)**(1/2) \
      )*(deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2))) \
      **2*(a0**(-3)*mu**(-2)*(mu+a0*(deltaVtotal+(a3**(-1)*mu)**( \
      1/2))*(deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2) \
      ))**3)**(1/2)*Re**2*math.cos(incl)*(1+(3/32)*a0**(-2)*J2*mu**(-2)*( \
      mu+a0*(deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+2*(a0**( \
      -1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**2*Re**2*(1+(-3/2)*math.sin( \
      incl)**2))*(tmaneuver+(-1/640)*A**(-1)*a3**(-5/2)*mu**(1/2)*(a0* \
      mu*(mu+a0*(deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+2*( \
      a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-1))**(-5/2)*(( \
      -320)*a0**2*a3**(5/2)*mu**2*(mu+a0*(deltaVtotal+(a3**(-1)* \
      mu)**(1/2))*(deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu) \
      **(1/2)))**(-2)+3*a3**(5/2)*J2*Re**2*((-2)+3*math.sin(incl)**2)+32*( \
      a0*mu*(mu+a0*(deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+ \
      2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-1))**(5/2)*( \
      20*a3**2+3*J2*Re**2*(2+(-3)*math.sin(incl)**2)))+(1/640)*A**(-1)* \
      a0**(-5/2)*mu**(1/2)*(a0*mu*(mu+a0*(deltaVtotal+(a3**(-1)* \
      mu)**(1/2))*(deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu) \
      **(1/2)))**(-1))**(-5/2)*((-640)*a0**2*(a0*mu*(mu+a0*( \
      deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+2*(a0**(-1)*mu) \
      **(1/2)+(a3**(-1)*mu)**(1/2)))**(-1))**(5/2)+96*J2*(a0*mu*( \
      mu+a0*(deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+2*(a0**( \
      -1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-1))**(5/2)*Re**2*(( \
      -2)+3*math.sin(incl)**2)+a0**(5/2)*(320*a0**2*mu**2*(mu+a0*( \
      deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+2*(a0**(-1)*mu) \
      **(1/2)+(a3**(-1)*mu)**(1/2)))**(-2)+3*J2*Re**2*(2+(-3)*math.sin( \
      incl)**2)))); 
    
    
    RAANtotal_low = RAAN0 + deltaRAAN1_low + deltaRAAN2_low + deltaRAAN3_low;
    
#    % ---------------------------
#    % AOL
#    % ---------------------------
    
    deltau1_low = (-1/536870912)*A**(-1)*a0**(-16)*mu**(-7)*(mu+a0*( \
      deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+2*(a0**(-1)*mu) \
      **(1/2)+(a3**(-1)*mu)**(1/2)))**8*(8388608*a0**12*mu**6*(mu+ \
      a0*(deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+2*(a0**(-1) \
      *mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-6)*(a0**2+(-16)*a0**2* \
      mu**2*(mu+a0*(deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+ \
      2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-2))+27* \
      J2**3*(a0**8+(-65536)*a0**8*mu**8*(mu+a0*(deltaVtotal+(a3**( \
      -1)*mu)**(1/2))*(deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1) \
      *mu)**(1/2)))**(-8))*Re**6*(1+3*math.cos(2*incl))**2*(3+5*math.cos(2*incl) \
      )+98304*a0**8*J2*mu**4*(mu+a0*(deltaVtotal+(a3**(-1)*mu)**( \
      1/2))*(deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2) \
      ))**(-4)*(a0**4+(-256)*a0**4*mu**4*(mu+a0*(deltaVtotal+(a3**( \
      -1)*mu)**(1/2))*(deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1) \
      *mu)**(1/2)))**(-4))*Re**2*(5+11*math.cos(2*incl))+768*a0**4* \
      J2**2*mu**2*(mu+a0*(deltaVtotal+(a3**(-1)*mu)**(1/2))*( \
      deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-2) \
      *(a0**6+(-4096)*a0**6*mu**6*(mu+a0*(deltaVtotal+(a3**(-1)* \
      mu)**(1/2))*(deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu) \
      **(1/2)))**(-6))*Re**4*(53+68*math.cos(2*incl)+39*math.cos(4*incl)));
    
    deltau2_low = (tmaneuver+(1/2)*A**(-1)*((-2)*a3**(-1/2)*mu**(1/2)+mu**(1/2)*( \
      a0*mu*(mu+a0*(deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+ \
      2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-1))**(-1/2)+( \
      -3/5)*a3**(-5/2)*J2*mu**(1/2)*Re**2+(3/160)*J2*mu**(1/2)*( \
      a0*mu*(mu+a0*(deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+ \
      2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-1))**(-5/2)* \
      Re**2+(9/10)*a3**(-5/2)*J2*mu**(1/2)*Re**2*math.sin(incl)**2+(-9/320) \
      *J2*mu**(1/2)*(a0*mu*(mu+a0*(deltaVtotal+(a3**(-1)*mu)**( \
      1/2))*(deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2) \
      ))**(-1))**(-5/2)*Re**2*math.sin(incl)**2)+(-1/2)*A**(-1)*(2*a0**( \
      -1/2)*mu**(1/2)+(-1)*mu**(1/2)*(a0*mu*(mu+a0*(deltaVtotal+( \
      a3**(-1)*mu)**(1/2))*(deltaVtotal+2*(a0**(-1)*mu)**(1/2)+( \
      a3**(-1)*mu)**(1/2)))**(-1))**(-1/2)+(3/5)*a0**(-5/2)*J2*mu**( \
      1/2)*Re**2+(-3/160)*J2*mu**(1/2)*(a0*mu*(mu+a0*( \
      deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+2*(a0**(-1)*mu) \
      **(1/2)+(a3**(-1)*mu)**(1/2)))**(-1))**(-5/2)*Re**2+(-9/10)* \
      a0**(-5/2)*J2*mu**(1/2)*Re**2*math.sin(incl)**2+(9/320)*J2*mu**(1/2) \
      *(a0*mu*(mu+a0*(deltaVtotal+(a3**(-1)*mu)**(1/2))*( \
      deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-1) \
      )**(-5/2)*Re**2*math.sin(incl)**2))*((1/8)*(a0**(-3)*mu**(-2)*(mu+ \
      a0*(deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+2*(a0**(-1) \
      *mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**3)**(1/2)*(1+(3/32)*a0**( \
      -2)*J2*mu**(-2)*(mu+a0*(deltaVtotal+(a3**(-1)*mu)**(1/2))*( \
      deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**2* \
      Re**2*(1+(-3/2)*math.sin(incl)**2))+(3/256)*a0**(-2)*J2*mu**(-2)*( \
      mu+a0*(deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+2*(a0**( \
      -1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**2*(a0**(-3)*mu**(-2)*( \
      mu+a0*(deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+2*(a0**( \
      -1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**3)**(1/2)*Re**2*(2+( \
      -5/2)*math.sin(incl)**2)*(1+(3/32)*a0**(-2)*J2*mu**(-2)*(mu+a0*( \
      deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+2*(a0**(-1)*mu) \
      **(1/2)+(a3**(-1)*mu)**(1/2)))**2*Re**2*(1+(-3/2)*math.sin(incl)**2))) \
      ;
    
    deltau3_low = (1/536870912)*A**(-1)*a0**(-8)*a3**(-8)*mu**(-7)*(mu+a0*( \
      deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+2*(a0**(-1)*mu) \
      **(1/2)+(a3**(-1)*mu)**(1/2)))**8*(8388608*a0**6*a3**6* \
      mu**6*(mu+a0*(deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+ \
      2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-6)*((-1)* \
      a3**2+16*a0**2*mu**2*(mu+a0*(deltaVtotal+(a3**(-1)*mu)**(1/2) \
      )*(deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2))) \
      **(-2))+27*J2**3*((-1)*a3**8+65536*a0**8*mu**8*(mu+a0*( \
      deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+2*(a0**(-1)*mu) \
      **(1/2)+(a3**(-1)*mu)**(1/2)))**(-8))*Re**6*(1+3*math.cos(2*incl)) \
      **2*(3+5*math.cos(2*incl))+98304*a0**4*a3**4*J2*mu**4*(mu+a0*( \
      deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+2*(a0**(-1)*mu) \
      **(1/2)+(a3**(-1)*mu)**(1/2)))**(-4)*((-1)*a3**4+256*a0**4* \
      mu**4*(mu+a0*(deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+ \
      2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-4))*Re**2*( \
      5+11*math.cos(2*incl))+768*a0**2*a3**2*J2**2*mu**2*(mu+a0*( \
      deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+2*(a0**(-1)*mu) \
      **(1/2)+(a3**(-1)*mu)**(1/2)))**(-2)*((-1)*a3**6+4096*a0**6* \
      mu**6*(mu+a0*(deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+ \
      2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-6))*Re**4*( \
      53+68*math.cos(2*incl)+39*math.cos(4*incl)));
    
    udif_low = (-1/536870912)*A**(-1)*a0**(-16)*mu**(-7)*(mu+a0*( \
      deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+2*(a0**(-1)*mu) \
      **(1/2)+(a3**(-1)*mu)**(1/2)))**8*(8388608*a0**12*mu**6*(mu+ \
      a0*(deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+2*(a0**(-1) \
      *mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-6)*(a0**2+(-16)*a0**2* \
      mu**2*(mu+a0*(deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+ \
      2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-2))+27* \
      J2**3*(a0**8+(-65536)*a0**8*mu**8*(mu+a0*(deltaVtotal+(a3**( \
      -1)*mu)**(1/2))*(deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1) \
      *mu)**(1/2)))**(-8))*Re**6*(1+3*math.cos(2*incl))**2*(3+5*math.cos(2*incl) \
      )+98304*a0**8*J2*mu**4*(mu+a0*(deltaVtotal+(a3**(-1)*mu)**( \
      1/2))*(deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2) \
      ))**(-4)*(a0**4+(-256)*a0**4*mu**4*(mu+a0*(deltaVtotal+(a3**( \
      -1)*mu)**(1/2))*(deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1) \
      *mu)**(1/2)))**(-4))*Re**2*(5+11*math.cos(2*incl))+768*a0**4* \
      J2**2*mu**2*(mu+a0*(deltaVtotal+(a3**(-1)*mu)**(1/2))*( \
      deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-2) \
      *(a0**6+(-4096)*a0**6*mu**6*(mu+a0*(deltaVtotal+(a3**(-1)* \
      mu)**(1/2))*(deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu) \
      **(1/2)))**(-6))*Re**4*(53+68*math.cos(2*incl)+39*math.cos(4*incl)))+( \
      1/536870912)*A**(-1)*a0**(-8)*a3**(-8)*mu**(-7)*(mu+a0*( \
      deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+2*(a0**(-1)*mu) \
      **(1/2)+(a3**(-1)*mu)**(1/2)))**8*(8388608*a0**6*a3**6* \
      mu**6*(mu+a0*(deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+ \
      2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-6)*((-1)* \
      a3**2+16*a0**2*mu**2*(mu+a0*(deltaVtotal+(a3**(-1)*mu)**(1/2) \
      )*(deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2))) \
      **(-2))+27*J2**3*((-1)*a3**8+65536*a0**8*mu**8*(mu+a0*( \
      deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+2*(a0**(-1)*mu) \
      **(1/2)+(a3**(-1)*mu)**(1/2)))**(-8))*Re**6*(1+3*math.cos(2*incl)) \
      **2*(3+5*math.cos(2*incl))+98304*a0**4*a3**4*J2*mu**4*(mu+a0*( \
      deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+2*(a0**(-1)*mu) \
      **(1/2)+(a3**(-1)*mu)**(1/2)))**(-4)*((-1)*a3**4+256*a0**4* \
      mu**4*(mu+a0*(deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+ \
      2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-4))*Re**2*( \
      5+11*math.cos(2*incl))+768*a0**2*a3**2*J2**2*mu**2*(mu+a0*( \
      deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+2*(a0**(-1)*mu) \
      **(1/2)+(a3**(-1)*mu)**(1/2)))**(-2)*((-1)*a3**6+4096*a0**6* \
      mu**6*(mu+a0*(deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+ \
      2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-6))*Re**4*( \
      53+68*math.cos(2*incl)+39*math.cos(4*incl)))+tmaneuver*((-1)*(aref**(-3)*mu) \
      **(1/2)*(1+(3/2)*aref**(-2)*J2*Re**2*(1+(-3/2)*math.sin(incl)**2))+( \
      -3/2)*aref**(-2)*J2*(aref**(-3)*mu)**(1/2)*Re**2*(2+(-5/2)* \
      math.sin(incl)**2)*(1+(3/2)*aref**(-2)*J2*Re**2*(1+(-3/2)*math.sin(incl)**2) \
      ))+(tmaneuver+(1/2)*A**(-1)*((-2)*a3**(-1/2)*mu**(1/2)+mu**(1/2) \
      *(a0*mu*(mu+a0*(deltaVtotal+(a3**(-1)*mu)**(1/2))*( \
      deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-1) \
      )**(-1/2)+(-3/5)*a3**(-5/2)*J2*mu**(1/2)*Re**2+(3/160)*J2* \
      mu**(1/2)*(a0*mu*(mu+a0*(deltaVtotal+(a3**(-1)*mu)**(1/2))*( \
      deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-1) \
      )**(-5/2)*Re**2+(9/10)*a3**(-5/2)*J2*mu**(1/2)*Re**2*math.sin(incl) \
      **2+(-9/320)*J2*mu**(1/2)*(a0*mu*(mu+a0*(deltaVtotal+(a3**( \
      -1)*mu)**(1/2))*(deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1) \
      *mu)**(1/2)))**(-1))**(-5/2)*Re**2*math.sin(incl)**2)+(-1/2)*A**(-1)* \
      (2*a0**(-1/2)*mu**(1/2)+(-1)*mu**(1/2)*(a0*mu*(mu+a0*( \
      deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+2*(a0**(-1)*mu) \
      **(1/2)+(a3**(-1)*mu)**(1/2)))**(-1))**(-1/2)+(3/5)*a0**(-5/2)* \
      J2*mu**(1/2)*Re**2+(-3/160)*J2*mu**(1/2)*(a0*mu*(mu+a0*( \
      deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+2*(a0**(-1)*mu) \
      **(1/2)+(a3**(-1)*mu)**(1/2)))**(-1))**(-5/2)*Re**2+(-9/10)* \
      a0**(-5/2)*J2*mu**(1/2)*Re**2*math.sin(incl)**2+(9/320)*J2*mu**(1/2) \
      *(a0*mu*(mu+a0*(deltaVtotal+(a3**(-1)*mu)**(1/2))*( \
      deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**(-1) \
      )**(-5/2)*Re**2*math.sin(incl)**2))*((1/8)*(a0**(-3)*mu**(-2)*(mu+ \
      a0*(deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+2*(a0**(-1) \
      *mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**3)**(1/2)*(1+(3/32)*a0**( \
      -2)*J2*mu**(-2)*(mu+a0*(deltaVtotal+(a3**(-1)*mu)**(1/2))*( \
      deltaVtotal+2*(a0**(-1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**2* \
      Re**2*(1+(-3/2)*math.sin(incl)**2))+(3/256)*a0**(-2)*J2*mu**(-2)*( \
      mu+a0*(deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+2*(a0**( \
      -1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**2*(a0**(-3)*mu**(-2)*( \
      mu+a0*(deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+2*(a0**( \
      -1)*mu)**(1/2)+(a3**(-1)*mu)**(1/2)))**3)**(1/2)*Re**2*(2+( \
      -5/2)*math.sin(incl)**2)*(1+(3/32)*a0**(-2)*J2*mu**(-2)*(mu+a0*( \
      deltaVtotal+(a3**(-1)*mu)**(1/2))*(deltaVtotal+2*(a0**(-1)*mu) \
      **(1/2)+(a3**(-1)*mu)**(1/2)))**2*Re**2*(1+(-3/2)*math.sin(incl)**2))) \
      ; 
    
    utotal_low = u0 + deltau1_low + deltau2_low + deltau3_low;
    
    new_sat[10] = sat[10]+ tmaneuver;  
    
    lat_SSPc = np.arcsin(np.sin(incl)*np.sin(utotal_low)); #this is geocentric
    #lat_SSP
    new_sat[8] = (np.arctan(np.tan(lat_SSPc)/(1 - flattening * (2 - flattening))))*180/math.pi;  
    #long_SSP
    new_sat[9] = (np.arctan2(np.cos(incl)*np.sin(utotal_low),np.cos(utotal_low))\
        -vel_e*(new_sat[10])+RAANtotal_low-RAAN_epoch)*180/math.pi;
    
    #RAAN       
    new_sat[4] = RAANtotal_low*180/math.pi;
    #AoL
    new_sat[6] = utotal_low*180/math.pi;

     
    return new_sat