Problem 2.10 from Thermal Physics -- 
This code:
1) Calculates multiplicity of energy levels for two Einstein solids. 
2) Prints a table for all possible states
3) Plots number of systems in each macrostate (qA vs. total multiplicity)
4) Calculates most probable macrostate (and how probable)
5) Calculates least probable macrostate (and how probable)

All values calculated in the code attached 'SilvaJ_p2.10.py'

A table (output of my code):

     $qA$   $Omega (N,qA)$    $qB$     $Omega (N,qB)$  $Omega_{total}$
0       1      1.000000e+00    100      4.527426e+58      4.527426e+58
1       2      2.000000e+02     99      2.275088e+58      4.550177e+60
2       3      2.010000e+04     98      1.137544e+58      2.286464e+62
3       4      1.353400e+06     97      5.658849e+57      7.658686e+63
4       5      6.868505e+07     96      2.800553e+57      1.923561e+65
5       6      2.802350e+09     95      1.378734e+57      3.863694e+66
6       7      9.574696e+10     94      6.751531e+56      6.464386e+67
7       8      2.817696e+12     93      3.288310e+56      9.265460e+68
8       9      7.290789e+13     92      1.592775e+56      1.161259e+70
9      10      1.684982e+15     91      7.672007e+55      1.292720e+71
10     11      3.521613e+16     90      3.674488e+55      1.294012e+72
11     12      6.723080e+17     89      1.749756e+55      1.176375e+73
12     13      1.182141e+19     88      8.283419e+54      9.792174e+73
13     14      1.927800e+20     87      3.898080e+54      7.514718e+74
14     15      2.933010e+21     86      1.823295e+54      5.347743e+75
15     16      4.184428e+22     85      8.475859e+53      3.546662e+76
16     17      5.622825e+23     84      3.915479e+53      2.201605e+77
17     18      7.144295e+24     83      1.797269e+53      1.284022e+78
18     19      8.612844e+25     82      8.196336e+52      7.059376e+78
19     20      9.882105e+26     81      3.713257e+52      3.669480e+79
20     21      1.082091e+28     80      1.670966e+52      1.808136e+80
21     22      1.133619e+29     79      7.468003e+51      8.465868e+80
22     23      1.138771e+30     78      3.314451e+51      3.774402e+81
23     24      1.099162e+31     77      1.460605e+51      1.605442e+82
24     25      1.021305e+32     76      6.390149e+50      6.526289e+82
25     26      9.150890e+32     75      2.775150e+50      2.539510e+83
26     27      7.919040e+33     74      1.196186e+50      9.472641e+83
27     28      6.628530e+34     73      5.116632e+49      3.391574e+84
28     29      5.373844e+35     72      2.171594e+49      1.166980e+85
29     30      4.224953e+36     71      9.143552e+48      3.863108e+85
..    ...               ...    ...               ...               ...
70     71      5.223777e+65     30      2.009491e+29      1.049713e+95
71     72      1.986507e+66     29      4.673235e+28      9.283413e+94
72     73      7.476991e+66     28      1.058780e+28      7.916487e+94
73     74      2.785947e+67     27      2.334318e+27      6.503286e+94
74     75      1.027789e+68     26      5.002109e+26      5.141111e+94
75     76      3.754854e+68     25      1.040439e+26      3.906696e+94
76     77      1.358664e+69     24      2.097659e+25      2.850014e+94
77     78      4.870018e+69     23      4.092993e+24      1.993295e+94
78     79      1.729481e+70     22      7.716298e+23      1.334519e+94
79     80      6.086021e+70     21      1.402963e+23      8.538463e+93
80     81      2.122500e+71     20      2.455186e+22      5.211131e+93
81     82      7.337036e+71     19      4.126362e+21      3.027527e+93
82     83      2.514277e+72     18      6.644143e+20      1.670522e+93
83     84      8.542483e+72     17      1.022176e+20      8.731920e+92
84     85      2.878003e+73     16      1.498016e+19      4.311296e+92
85     86      9.615917e+73     15      2.084197e+18      2.004146e+92
86     87      3.186670e+74     14      2.742364e+17      8.739009e+91
87     88      1.047572e+75     13      3.397619e+16      3.559251e+91
88     89      3.416513e+75     12      3.943665e+15      1.347358e+91
89     90      1.105568e+76     11      4.263422e+14      4.713504e+90
90     91      3.550103e+76     10      4.263422e+13      1.513558e+90
91     92      1.131351e+77      9      3.911396e+12      4.425163e+89
92     93      3.578514e+77      8      3.259497e+11      1.166415e+89
93     94      1.123576e+78      7      2.437007e+10      2.738163e+88
94     95      3.502212e+78      6      1.609344e+09      5.636263e+87
95     96      1.083842e+79      5      9.196252e+07      9.967287e+86
96     97      3.330557e+79      4      4.421275e+06      1.472531e+86
97     98      1.016335e+80      3      1.717000e+05      1.745047e+85
98     99      3.080117e+80      2      5.050000e+03      1.555459e+84
99    100      9.271464e+80      1      1.000000e+02      9.271464e+82

This does not show every single value, but variables could individually be printed to see multiplicities for specific energy levels.

A plot is included, called 'SilvaJ_p2.10plt'

The most probable macrostate, qA= 67
The most probable macrostate, qB= 33
Probability of most probable macrostate P= 0.073151
Probability (in percent) of most probable macrostate P= 7.315140

The least probable macrostate, qA= 0
The least probable macrostate, qB= 33
Probability of least probable macrostate P= 2.69266665552e-38
Probability (in percent) of least probable macrostate P=2.69266665552e-36