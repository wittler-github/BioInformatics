### Excerpt from article Immensely large sample spaces implies biological systems are ‘fine-tuned’ - Observable
#science is different to beliefs about the past" Journal of Theorethical biology 2021
#In contrast the notion of apparent
# Design is an intelligible scientific hypothesis, which we humans can observe in the present
# from our own experience of using meaningful highly specific combinatorial information in
# language, writing, computer-systems, mathematics etc. Take any article for instance, it is an
# incredibly complex combinatorial sequence of 95 characters (26 upper- and lower-case
# letters, 10 digits, 33 other characters); in particular, this article is a combinatorial sequence of
# nearly 11000 characters ( 95^11000 ~ 10^21755 ); still, it confers the meaning of the authors’
# minds. Consider then the combinatorial sequence of biological cells, which are on many
#
# dimensions immensely more complex. For example, a single human DNA strand has 4
# possible bases on billions of sites ( 4^(3∗10^9) ~ 10^(1.8∗10^9)

### Simplyfying rules about logarithms
#https://en.wikipedia.org/wiki/Logarithm
#Power	{\displaystyle \log _{b}\left(x^{p}\right)=p\log _{b}x}{\displaystyle \log _{b}\left(x^{p}\right)=p\log _{b}x}


import math
import numpy as np

### LARGE NUMBER COMBINATORIAL

## Short calculation of logarithmic article combinatorial
lart1 = 4200*np.log10(95)
print("lart1=",lart1)
print("lart1=",np.format_float_scientific(np.float32(lart1)))
lart2 = 8307*np.log10(10)
print("lart2=",lart2)
print("lart2=",np.format_float_scientific(np.float32(lart2)))

#print("95 ^4200", pow(95,4200))
#print("10 ^8307", pow(10,8307))


### DNA COMBINATORIAL

nbp = 4
nbpHG = 3*(10**9)

print("nbp=",nbp)
print("nbpHG=",nbpHG)

## Short calculation of logarithmic DNA combinatorial
ldnac = nbpHG*np.log10(4)
print("ldnac=",ldnac)
print("ldnac=",np.format_float_scientific(np.float32(ldnac)))

## Long calculation of logarithmic DNA combinatorial
#dnac = 4**(nbp)
#print("dnac=",dnac)
#ldnac = np.log10(dnac)
#print("ldnac=",ldnac)
