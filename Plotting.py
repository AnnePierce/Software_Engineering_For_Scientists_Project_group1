#Start up code chunk (Import required packages)

import matplotlib.pyplot as plt #Import matplotlib library
import numpy as np #Import numpy library
from scipy.optimize import curve_fit #Import non-linear weighted least squares fit from scipy

#Part 1
#Visualize raw data
#Not done with biexponential fit yet

#Animal 1
def plot_female_raw(fTimeGreen,f1green,fTimeIsosbestic,f1isosbestic,fTimeRed,f1red):
    plt.subplot(3, 1, 1)
    plt.plot(fTimeGreen,f1green) #Plot fTimeGreen in x-axis and f1green in y-axis
    plt.xlabel('Time (min)') #Naming x-axis
    plt.ylabel('Green') #Naming y-axis
      
    plt.subplot(3, 1, 2)
    plt.plot(fTimeIsosbestic,f1isosbestic)
    plt.xlabel('Time (min)')
    plt.ylabel('Isosbestic')
    
    plt.subplot(3, 1, 3)
    plt.plot(fTimeRed,f1red)
    plt.xlabel('Time (min)')
    plt.ylabel('Red')
    
    plt.title('Subject', loc='left') #Title of the plot
    
    plt.show()
    plt.savefig('female_raw.png')
    
    plt.clf()
    
    return 'female_raw.png'

#Animal 2
def plot_male_raw(fTimeGreen,f2green,fTimeIsosbestic,f2isosbestic,fTimeRed,f2red):
    
    plt.subplot(3, 1, 1) 
    plt.plot(fTimeGreen,f2green)
    plt.xlabel('Time (min)')
    plt.ylabel('Green')
    
    plt.subplot(3, 1, 2)
    plt.plot(fTimeIsosbestic,f2isosbestic)
    plt.xlabel('Time (min)')
    plt.ylabel('Isosbestic')
    
    plt.subplot(3, 1, 3)
    plt.plot(fTimeRed,f2red)
    plt.xlabel('Time (min)')
    plt.ylabel('Red')
    
    plt.title('Partner', loc='left')
    
    plt.show()
    plt.savefig('male_raw.png')
    
    plt.clf()
    
    return 'male_raw.png'

#Green overlay animals
def plot_female_and_male_raw(fTimeGreen,f1green,f2green):
    
    plt.plot(fTimeGreen,f1green-np.mean(f1green))
    plt.plot(fTimeGreen,f2green-np.mean(f2green))
    plt.xlabel('Time (min)')
    plt.ylabel('Green (adjusted y intercept)')
    
    plt.legend(["Subject", "Partner"])
    
    plt.title('Both Animals', loc='left')
    plt.title('Raw Signal Both Animals', loc='right')
    
    plt.show()
    plt.savefig('female_and_male_raw.png')
    
    plt.clf()
    return 'female_and_male_raw.png'


#Part 2
#Visualization of distribution fitted data

#Animal 1
def plot_female_norm(Timemin,signal1):
    # Biexponential fitting
    def funct(m):
        l=0.5*np.exp(m)
        return l
    y1 = funct(Timein)
    sagesFit1 = curve_fit(funct, Timemin, y1)
    plt.subplot(2,1,1)
    plt.plot(Timemin, signal1)
    plt.plot(Timemin, sagesFit1)
    plt.xlabel('Time(min)')
    plt.ylabel('total fluorescence')
    plt.legend("signal", "exponential fit")
    plt.title('Sages Process Animal 1', loc='left')
    plt.title('Signal fit to exp (Animal #1)', loc='right')
    plt.show()
    
    sages2ndFit1=signal1/sagesFit1
    plt.subplot(2,1,2)
    plt.plot(Timemin, sages2ndFit1)
    plt.xlabel('Time(min)')
    plt.ylabel('Normalized Fluorescence')
    
    plt.title('Signal Normalized to Exp (Animal #1)', loc='right')
    
    plt.show()
    
    plt.savefig('female_norm.png')
    
    plt.clf()
    return 'female_norm.png'

# Animal 2
# fit the reference to exp and normalize by dividing
#sagesFit2 = fit(Time, signal2, 'exp2')


##Biexponential fitting
def plot_male_norm(Timemin,signal2):
    # Biexponential fitting
    def funct(m):
        l=0.5*np.exp(m)
        return l
    y2 = funct(Timein)
    sagesFit2 = curve_fit(funct, Timemin, y2)
    plt.subplot(2,1,1)
    plt.plot(Timemin, signal2)
    plt.plot(Timemin, sagesFit2)
    plt.xlabel('Time(min)')
    plt.ylabel('total fluorescence')
    
    plt.legend("signal", "exponential fit")
    
    plt.title('Sages Process Animal 2', loc='left')
    plt.title('Signal fit to exp (Animal #2)', loc='right')
    
    plt.show()
    
    sages2ndFit2=signal2/sagesFit2
    plt.subplot(2,1,2)
    plt.plot(Timemin, sages2ndFit2)
    plt.xlabel('Time(min)')
    plt.ylabel('Normalized Fluorescence')
    
    plt.title('Reference Normalized to Exp (Animal #2)', loc='right')
    
    plt.show()
    plt.savefig('male_norm.png')
    
    plt.clf()
    
    return 'male_norm.png'

def plot_female_and_male_norm(Timemin, signal1, signal2):
    
    def funct(m):
        l=0.5*np.exp(m)
        return l
    y1 = funct(Timein)
    sagesFit1 = curve_fit(funct, Timemin, y1)
    sages2ndFit1=signal1/sagesFit1
    y2 = funct(Timein)
    sagesFit2 = curve_fit(funct, Timemin, y2)
    sages2ndFit2=signal2/sagesFit2
    
    plt.plot(Timemin, sages2ndFit1)
    plt.plot(Timemin, sages2ndFit2)
    plt.xlabel('Time(min)')
    plt.ylabel('Normalized fluorescence')
    
    plt.legend("Animal #1", "Animal #2")
    
    plt.title('Sages Final', loc='left')
    plt.title('Sages normalization', loc='right')
    
    plt.show()
    plt.savefig('female_and_male_norm.png')
    
    plt.clf()
    return 'female_and_male_norm.png'


def main(fTimeRed, fTimeIsosbestic, fTimeGreen, f1red, f1isosbestic, f1green, f2red, f2isosbestic, f2green):
    
    plot_female_raw(fTimeGreen,f1green,fTimeIsosbestic,f1isosbestic,fTimeRed,f1red)
    plot_male_raw(fTimeGreen,f2green,fTimeIsosbestic,f2isosbestic,fTimeRed,f2red)
#     plot_female_and_male_raw(fTimeGreen,f1green,f2green)
#     plot_female_norm(Timemin,signal1)
#     plot_male_norm(Timemin,signal2)
#     plot_female_and_male_norm(Timemin, signal1, signal2)


if __name__ == "__main__":
    main()
