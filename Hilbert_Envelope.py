    # function [hilbert_envelope] = Hilbert_Envelope(input_signal, sampling_frequency,figures)
    
    # This function finds the Hilbert envelope of a signal. This is taken from:
    
    # Choi et al, Comparison of envelope extraction algorithms for cardiac sound
# signal segmentation, Expert Systems with Applications, 2008
    
    ## Inputs:
# input_signal: the original signal
# samplingFrequency: the signal's sampling frequency
# figures: (optional) boolean variable to display a figure of both the
# original and normalised signal
    
    ## Outputs:
# hilbert_envelope is the hilbert envelope of the original signal
    
    # This code was developed by David Springer for comparison purposes in the
# paper:
# D. Springer et al., "Logistic Regression-HSMM-based Heart Sound
# Segmentation," IEEE Trans. Biomed. Eng., In Press, 2015.
    
    ## Copyright (C) 2016  David Springer
# dave.springer@gmail.com
    
    # This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
    
    # This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
    
    # You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
    
    
@function
def Hilbert_Envelope(input_signal=None,sampling_frequency=None,figures=None,*args,**kwargs):
    varargin = Hilbert_Envelope.varargin
    nargin = Hilbert_Envelope.nargin

    if nargin < 3:
        figures=0

    
    hilbert_envelope=abs(hilbert(input_signal))

    
    if (figures):
        figure('Name','Hilbert Envelope')
        plot(input_signal.T)
        hold('on')
        plot(hilbert_envelope,'r')
        legend('Original Signal','Hilbert Envelope')
        pause()
    