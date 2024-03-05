# -*- coding: utf-8 -*-
"""
PI compensator

@author: Alonso
"""
from math import pi, log10, sqrt
from control import tf, bode_plot
# Components
R1=2.24e3; R2=2.24e3; C2=10e-9
# Opamp response parameters
Ao=1e5; fo= 1e6; fc= fo/Ao; wc=2*pi*fc

s = tf('s')
# Opamp response (red)
Ad = Ao/(1 + s/wc)
# 1/beta response (green)
beta_1= (1+(R1+R2)*C2*s)/(R1*C2*s)
# alpha response (orange)
alpha= (1 + R2*C2*s)/(1 + (R1+R2)*C2*s)
# ideal compensator response (blue)
Ci= (1+R2*C2*s)/(R1*C2*s)
# actual compensator response (black)
C=Ci*1/(1 + beta_1/Ad)

# Plot Plant's Bode
# Note that once Hz is true, omega_limits are in Hz
mag, phase, omega = bode_plot(Ad, dB=True, Hz=True, omega_limits=(0.01,10e6), \
                              omega_num=100, color='red' )
mag, phase, omega = bode_plot(beta_1, dB=True, Hz=True, omega_limits=(0.01,10e6), \
                              omega_num=100, color='green' )
mag, phase, omega = bode_plot(alpha, dB=True, Hz=True, omega_limits=(0.01,10e6), \
                              omega_num=100, color='orange' ) 
mag, phase, omega = bode_plot(Ci, dB=True, Hz=True, omega_limits=(0.01,10e6), \
                              omega_num=100, color='blue' )
mag, phase, omega = bode_plot(C, dB=True, Hz=True, omega_limits=(0.01,10e6), \
                              omega_num=100, color='black' )


    