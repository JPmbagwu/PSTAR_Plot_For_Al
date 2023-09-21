#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 16:44:41 2023

@author: johnpaulmbagwu
"""

import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel data file
df = pd.read_csv('Alum.csv', delimiter=' ')

# Get the stopping power and energy columns
stopping_power = df['TotalStp.Pow']
energy = df['KineticEnergy']

# Create a line plot (remove scatter points)
ax1 = df.plot.line(x='KineticEnergy', y='TotalStp.Pow', label='Total Stopping Power')

# Set the x and y-axis scales to logarithmic
ax1.set_xscale('log')
ax1.set_yscale('log')

# Set the x-axis and y-axis limits
ax1.set_xlim(1e-2, 1e4)

# Set the y-axis label
ax1.set_ylabel('Stopping Power (MeV cm^2/g)')

# Set the x-axis label
ax1.set_xlabel('Energy (MeV)')

# Add a legend with the label 'Total Stopping Power'
ax1.legend(['Total Stopping Power'])

# Show the plot
plt.show()