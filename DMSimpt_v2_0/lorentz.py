# This file was automatically created by FeynRules 2.4.91
# Mathematica version: 13.1.0 for Mac OS X ARM (64-bit) (June 16, 2022)
# Date: Thu 28 Mar 2024 20:48:08


from object_library import all_lorentz, Lorentz

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot
try:
   import form_factors as ForFac 
except ImportError:
   pass


SS1 = Lorentz(name = 'SS1',
              spins = [ 1, 1 ],
              structure = '1')

SS2 = Lorentz(name = 'SS2',
              spins = [ 1, 1 ],
              structure = 'P(-1,1)**2')

FF1 = Lorentz(name = 'FF1',
              spins = [ 2, 2 ],
              structure = 'P(-1,1)*Gamma(-1,2,1)')

FF2 = Lorentz(name = 'FF2',
              spins = [ 2, 2 ],
              structure = 'P(-1,1)*Gamma(-1,2,-2)*ProjM(-2,1)')

FF3 = Lorentz(name = 'FF3',
              spins = [ 2, 2 ],
              structure = '(ProjM(2,1))+(ProjP(2,1))')

FF4 = Lorentz(name = 'FF4',
              spins = [ 2, 2 ],
              structure = 'P(-1,1)*Gamma(-1,2,-2)*ProjP(-2,1)')

FF5 = Lorentz(name = 'FF5',
              spins = [ 2, 2 ],
              structure = '(P(-1,1)*Gamma(-1,2,-2)*ProjM(-2,1))+(P(-1,1)*Gamma(-1,2,-2)*ProjP(-2,1))')

VV1 = Lorentz(name = 'VV1',
              spins = [ 3, 3 ],
              structure = 'Metric(1,2)')

VV2 = Lorentz(name = 'VV2',
              spins = [ 3, 3 ],
              structure = 'P(-1,2)**2*Metric(1,2)')

VV3 = Lorentz(name = 'VV3',
              spins = [ 3, 3 ],
              structure = '(P(1,2)*P(2,2))+(-3*P(-1,2)**2*Metric(1,2))/(2)')

VV4 = Lorentz(name = 'VV4',
              spins = [ 3, 3 ],
              structure = '(P(1,2)*P(2,2))+(-(P(-1,2)**2*Metric(1,2)))')

VV5 = Lorentz(name = 'VV5',
              spins = [ 3, 3 ],
              structure = '(P(1,2)*P(2,2))+(-19*P(-1,2)**2*Metric(1,2))/(22)')

VV6 = Lorentz(name = 'VV6',
              spins = [ 3, 3 ],
              structure = '(P(1,2)*P(2,2))+(P(-1,2)**2*Metric(1,2))/(2)')

UUS1 = Lorentz(name = 'UUS1',
               spins = [ -1, -1, 1 ],
               structure = '1')

UUV1 = Lorentz(name = 'UUV1',
               spins = [ -1, -1, 3 ],
               structure = '(P(3,2))+(P(3,3))')

SSS1 = Lorentz(name = 'SSS1',
               spins = [ 1, 1, 1 ],
               structure = '1')

FFS1 = Lorentz(name = 'FFS1',
               spins = [ 2, 2, 1 ],
               structure = 'Gamma5(2,1)')

FFS2 = Lorentz(name = 'FFS2',
               spins = [ 2, 2, 1 ],
               structure = 'Identity(2,1)')

FFS3 = Lorentz(name = 'FFS3',
               spins = [ 2, 2, 1 ],
               structure = 'ProjM(2,1)')

FFS4 = Lorentz(name = 'FFS4',
               spins = [ 2, 2, 1 ],
               structure = 'ProjP(2,1)')

FFV1 = Lorentz(name = 'FFV1',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,1)')

FFV2 = Lorentz(name = 'FFV2',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjM(-1,1)')

FFV3 = Lorentz(name = 'FFV3',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjP(-1,1)')

FFV4 = Lorentz(name = 'FFV4',
               spins = [ 2, 2, 3 ],
               structure = '(Gamma(3,2,-1)*ProjM(-1,1))+(Gamma(3,2,-1)*ProjP(-1,1))')

VSS1 = Lorentz(name = 'VSS1',
               spins = [ 3, 1, 1 ],
               structure = 'P(1,2)')

VSS2 = Lorentz(name = 'VSS2',
               spins = [ 3, 1, 1 ],
               structure = '(P(1,2))+(-P(1,3))')

VSS3 = Lorentz(name = 'VSS3',
               spins = [ 3, 1, 1 ],
               structure = 'P(1,3)')

VVS1 = Lorentz(name = 'VVS1',
               spins = [ 3, 3, 1 ],
               structure = 'Metric(1,2)')

VVV1 = Lorentz(name = 'VVV1',
               spins = [ 3, 3, 3 ],
               structure = '(-(Epsilon(1,2,3,-1)*P(-1,1)))+(Epsilon(1,2,3,-1)*P(-1,2))')

VVV2 = Lorentz(name = 'VVV2',
               spins = [ 3, 3, 3 ],
               structure = '(P(3,1)*Metric(1,2))+(-(P(3,2)*Metric(1,2)))+(-(P(2,1)*Metric(1,3)))+(P(2,3)*Metric(1,3))+(P(1,2)*Metric(2,3))+(-(P(1,3)*Metric(2,3)))')

SSSS1 = Lorentz(name = 'SSSS1',
                spins = [ 1, 1, 1, 1 ],
                structure = '1')

VVSS1 = Lorentz(name = 'VVSS1',
                spins = [ 3, 3, 1, 1 ],
                structure = 'Metric(1,2)')

VVVV1 = Lorentz(name = 'VVVV1',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Epsilon(1,2,3,4)')

VVVV2 = Lorentz(name = 'VVVV2',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3)')

VVVV3 = Lorentz(name = 'VVVV3',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,3)*Metric(2,4)')

VVVV4 = Lorentz(name = 'VVVV4',
                spins = [ 3, 3, 3, 3 ],
                structure = '(Metric(1,4)*Metric(2,3))+(-(Metric(1,3)*Metric(2,4)))')

VVVV5 = Lorentz(name = 'VVVV5',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,2)*Metric(3,4)')

VVVV6 = Lorentz(name = 'VVVV6',
                spins = [ 3, 3, 3, 3 ],
                structure = '(Metric(1,4)*Metric(2,3))+(Metric(1,3)*Metric(2,4))+(-2*Metric(1,2)*Metric(3,4))')

VVVV7 = Lorentz(name = 'VVVV7',
                spins = [ 3, 3, 3, 3 ],
                structure = '(Metric(1,4)*Metric(2,3))+(-(Metric(1,2)*Metric(3,4)))')

VVVV8 = Lorentz(name = 'VVVV8',
                spins = [ 3, 3, 3, 3 ],
                structure = '(Metric(1,3)*Metric(2,4))+(-(Metric(1,2)*Metric(3,4)))')

VVVV9 = Lorentz(name = 'VVVV9',
                spins = [ 3, 3, 3, 3 ],
                structure = '(Metric(1,4)*Metric(2,3))+(-(Metric(1,3)*Metric(2,4)))/(2)+(-(Metric(1,2)*Metric(3,4)))/(2)')

VVVV10 = Lorentz(name = 'VVVV10',
                 spins = [ 3, 3, 3, 3 ],
                 structure = '(Metric(1,4)*Metric(2,3))+(Metric(1,3)*Metric(2,4))+(Metric(1,2)*Metric(3,4))')

