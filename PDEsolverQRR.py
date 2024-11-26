import numpy as np
from numpy import sqrt, log, sin, exp, cos, pi, heaviside
import json
import matplotlib.pyplot as plt
import glob as glob
import h5py
from tqdm import trange
from scipy.constants import alpha, hbar, m_e, c, e
from scipy.integrate import quad
from scipy.special import kv
from scipy.integrate import solve_ivp
from scipy.integrate import odeint
from scipy.linalg import expm

ES = m_e**2*c**3/(e*hbar) # ~10^18 [V/m] Schwinger electric field
BS = m_e**2*c**2/(e*hbar) # 4.41e9 [T] Schwinger magnetic field
lbdc = hbar/(m_e*c); # Compton wavelength
tauC = hbar/(m_e*c**2) # Compton time

def g25(chi):
    """Niel2018 equation 25"""
    res = 9*sqrt(3)/(8*pi) * quad(lambda v: 2*v**2 * kv(5/3,v)/(2+3*v*chi)**2 + 4*v* (3*v*chi)**2 *kv(2/3,v)/(2+3*v*chi)**4, 0, np.inf)[0]
    return res

def h41(chi):
    """Niel2018 equation 41"""
    res = 9*sqrt(3)/(4*pi) * quad(lambda v: 2*chi**3 * v**3 * kv(5/3,v)/(2+3*v*chi)**3 + 54* chi**5 * v**4 *kv(2/3,v)/(2+3*v*chi)**5, 0, np.inf)[0]
    return res

def S39(chi,Kalpha):
    """Niel2018 equation 39"""
    res = 2/3 * Kalpha * chi**2 * g25(chi); #fine_structure**2/taue
    return res

def R40(chi,gm,Kalpha):
    """Niel2018 equation 40"""
    res = 2/3 * Kalpha * gm * h41(chi);
    return res

def getL(B=2.5e3, tmax=20, tdim=20, gmlst=np.array([0,1]), g0=1800):
    # building the matrix is actually slower with pennylane's np

    wc = e*B/(m_e*g0) #s-1
    Kalpha = alpha * m_e * c**2 / (hbar * wc) #[?]
    
    # gm
    gmdim = len(gmlst)
    dx = (gmlst[1] - gmlst[0])/g0

    # time
    dt = tmax/tdim # time step
    tlst = np.linspace(0,tmax,tdim) # time steps array

    # define matrix
    dfdt_mat = np.zeros((gmdim,gmdim))

    # mu (Kubo) = -S (Niel), sigma (Kubo) = sqrt(R) (Niel)
    for i in trange(gmdim):
        ip1 = np.mod(i+1,gmdim)
        im1 = np.mod(i-1,gmdim)
        mukp1 = -S39(gmlst[ip1]*B/BS,Kalpha) / g0
        mukm1 = -S39(gmlst[im1]*B/BS,Kalpha) / g0
        sigmakp1 = sqrt(R40(gmlst[ip1]*B/BS,gmlst[ip1],Kalpha) ) / g0
        sigmakm1 = sqrt(R40(gmlst[im1]*B/BS,gmlst[im1],Kalpha) ) / g0
        
        dfdt_mat[i,ip1] = 0.5*((sigmakp1/dx)**2-mukp1/dx) # i=k-1
        dfdt_mat[i,im1] = 0.5*((sigmakm1/dx)**2+mukm1/dx) # i=k+1
        dfdt_mat[i,i] = -(dfdt_mat[i,im1]+dfdt_mat[i,ip1]) # i=k -sigmak(xk)**2/dx**2
        
    return dfdt_mat


"""
n = 6
sigma0 = 0.06 * 2**n
tau = -0.25 # 0.5 is moving half of the register periodically
x = np.arange(0,2**n)
psi0 = exp(-0.5*(x-(2**n*0.5))**2 / (sigma0)**2)
psi0 /= sqrt( np.sum( np.abs(psi0)**2 ) )
plt.plot(x, psi0, 'k-', label=r'Initial wavefunction $\psi(t=0)$' )
psi = exp(-0.5*(x-(2**n* (0.5+tau) ))**2 / (sigma0)**2)
psi /= sqrt( np.sum( np.abs(psi)**2 ) )
plt.plot(x, psi, 'b-', label=r'$\psi(t)$' )
#
tTrotter = 700
plt.plot(x, get_UFD(n, tau)@psi0, 'r--', label='Scipy expm FD' )
#
plt.legend(frameon=False)
plt.show()
"""

def qft_matrix(n):
    """Generate the Quantum Fourier Transform matrix for n qubits (2^n x 2^n matrix)."""
    N = 2**n  # Dimension of the matrix
    omega = np.exp(2j * np.pi / N)  # Primitive N-th root of unity
    qft = np.zeros((N, N), dtype=complex)
    for j in range(N):
        for k in range(N):
            qft[j, k] = omega**(j * k) / np.sqrt(N)
    return qft

def iqft_matrix(n):
    """Generate the Inverse Quantum Fourier Transform matrix for n qubits (2^n x 2^n matrix)."""
    N = 2**n  # Dimension of the matrix
    omega_inv = np.exp(-2j * np.pi / N)  # Primitive N-th root of unity for inverse
    iqft = np.zeros((N, N), dtype=complex)
    for j in range(N):
        for k in range(N):
            iqft[j, k] = omega_inv**(j * k) / np.sqrt(N)
    return iqft

def get_UFD(n,tau):
    ell = 1/(2**n+1)
    Id = np.eye(2**n, dtype=complex)
    H = -1j * (np.roll(Id,-1,axis=0)-np.roll(Id,1,axis=0))/(2*ell)
    return expm(-1j*H*tau)