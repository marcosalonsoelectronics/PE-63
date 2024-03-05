# -*- coding: utf-8 -*-
"""
closed-loop buck converter loop gain

@author: Alonso
"""
from math import pi, log10, sqrt
from control import tf, bode_plot
# Components
R1=2.24e3; R2=2.24e3; C2=10e-9
# Opamp response parameters
Ao=1e5; fo= 1e6; fc= fo/Ao; wc=2*pi*fc
# buck converter parameters
Lb= 50e-6; Cb=10e-6; R=1; rl=0.05; rc=0.15
VB= 10

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
# buck control-to-output transfer function
G = VB*(1+rc*Cb*s)/( Lb*Cb*(1+rc/R)*s**2 + (Lb/R+rc*Cb+rl*Cb+rl*rc*Cb/R)*s + 1+rl/R )
# PWM modulator and voltage sensor gains
Vpp=10; H=1
# loop gain with ideal compensator
Ti=Ci*(1/Vpp)*G*H
# loop gain with real compensator
T=C*(1/Vpp)*G*H

# Plot Plant's Bode
# Note that once Hz is true, omega_limits are in Hz
mag, phase, omega = bode_plot(Ti, dB=True, Hz=True, omega_limits=(0.01,10e6), \
                              omega_num=100, color='blue' )
mag, phase, omega = bode_plot(T, dB=True, Hz=True, omega_limits=(0.01,10e6), \
                              omega_num=100, color='red' )

i=20
print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)
i=40
print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)
i=56
print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)
i=70
print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)
