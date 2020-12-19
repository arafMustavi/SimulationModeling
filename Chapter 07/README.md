The first such arithmetic generator, proposed by von Neumann and Metropolis in the 1940s
The famous **midsquare method**, an example of which follows.

**EXAMPLE 7.1** 

Start with a four-digit positive integer Z0 and square it to obtain an integer with up to eight digits; 
if necessary, append zeros to the left to make it exactly eight digits. 
Take the middle four digits of this eight-digit number as the next four-digit number, Z1. 
Place a decimal point at the left of Z1 to obtain the first “U(0, 1) random number,” U1. 
Then let Z2 be the middle four digits of Z1^2 and let U2 be Z2 with a decimal  point at the left, and so on. 

Table 7.1 lists the fi rst few Zi’s and Ui ’s for Z0 = 7182 
(the first four digits to the right of the decimal point in the number e).