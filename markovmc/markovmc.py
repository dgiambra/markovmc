def schrodinger(V_0 , c, n_basis_set, fxn, d_0 , d_1):
    '''
    This function solves Schrodingers wave equation in two dimensions.
    
    Parameters
    ----------
           V_0 : int
                 Potential Energy Constant
          
             c : int
                 constant
          
   n_basis_set : int
                  number of basis sets to use
    
           d_0 : int
                 lower bound of domain
        
           d_1 : int
                 upperbound of domain
                 
    Output
    ------
    energy : tuple
             first element is an array of eigenvalues
             second element is the eigen vector corresponding to the basis set coefficients
    
    
    '''
    import scipy.ndimage.filters as snf
    import numpy as np
    import scipy.integrate as integrate
    from numpy.polynomial import Polynomial, Legendre
    from numpy import polyder as deriv
    import numpy.linalg as linalg
    ## crs = open(file_name, "r")
    x = np.linspace(d_0,d_1,1000)
    ## fps = []
    ## for columns in (raw.strip().split() for raw in crs):
        ## fps.append(float(columns[2]))
        ## x.append(float(columns[1]))
    ## fxn_x = fxn(x)
    ai=[]
    h=np.zeros((n_basis_set,n_basis_set))

        ## for i in list(range((n_basis_set))):
            ## b.append(np.exp(1j*2*np.pi*i*x))
            ## ai.append(integrate.quad(lambda x:fxn(x)*np.exp(1j*2*np.pi*i*x),d_0,d_1  )[0])
            ## h.append([])
    for i in list(range((n_basis_set))):
        for z in list(range((n_basis_set))):
            h[i][z]=integrate.quad(lambda x:(float(-c*-i**2*np.pi**2*np.exp(1j*2*np.pi*i*x)+V_0*np.exp(1j*2*np.pi*i*x))*np.exp(1j*2*np.pi*z*x)),d_0,d_1  )[0]
        ## ai = np.matrix(ai)
    h = np.matrix(h)
    energy = linalg.eig(h)
    return energy
