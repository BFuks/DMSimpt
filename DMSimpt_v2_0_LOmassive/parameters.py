# This file was automatically created by FeynRules 2.4.91
# Mathematica version: 13.1.0 for Mac OS X ARM (64-bit) (June 16, 2022)
# Date: Wed 10 Apr 2024 18:04:25



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
cabi = Parameter(name = 'cabi',
                 nature = 'external',
                 type = 'real',
                 value = 0.227736,
                 texname = '\\theta _c',
                 lhablock = 'CKMBLOCK',
                 lhacode = [ 1 ])

lamF1e1x1 = Parameter(name = 'lamF1e1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.212,
                      texname = '\\text{lamF1e1x1}',
                      lhablock = 'DMF1E',
                      lhacode = [ 1, 1 ])

lamF1e2x2 = Parameter(name = 'lamF1e2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.213,
                      texname = '\\text{lamF1e2x2}',
                      lhablock = 'DMF1E',
                      lhacode = [ 2, 2 ])

lamF1e3x3 = Parameter(name = 'lamF1e3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.214,
                      texname = '\\text{lamF1e3x3}',
                      lhablock = 'DMF1E',
                      lhacode = [ 3, 3 ])

lamF1L1x1 = Parameter(name = 'lamF1L1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.209,
                      texname = '\\text{lamF1L1x1}',
                      lhablock = 'DMF1L',
                      lhacode = [ 1, 1 ])

lamF1L2x2 = Parameter(name = 'lamF1L2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.21,
                      texname = '\\text{lamF1L2x2}',
                      lhablock = 'DMF1L',
                      lhacode = [ 2, 2 ])

lamF1L3x3 = Parameter(name = 'lamF1L3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.211,
                      texname = '\\text{lamF1L3x3}',
                      lhablock = 'DMF1L',
                      lhacode = [ 3, 3 ])

lamF3d1x1 = Parameter(name = 'lamF3d1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.206,
                      texname = '\\text{lamF3d1x1}',
                      lhablock = 'DMF3D',
                      lhacode = [ 1, 1 ])

lamF3d2x2 = Parameter(name = 'lamF3d2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.207,
                      texname = '\\text{lamF3d2x2}',
                      lhablock = 'DMF3D',
                      lhacode = [ 2, 2 ])

lamF3d3x3 = Parameter(name = 'lamF3d3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.208,
                      texname = '\\text{lamF3d3x3}',
                      lhablock = 'DMF3D',
                      lhacode = [ 3, 3 ])

lamF3Q1x1 = Parameter(name = 'lamF3Q1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.2,
                      texname = '\\text{lamF3Q1x1}',
                      lhablock = 'DMF3Q',
                      lhacode = [ 1, 1 ])

lamF3Q2x2 = Parameter(name = 'lamF3Q2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.201,
                      texname = '\\text{lamF3Q2x2}',
                      lhablock = 'DMF3Q',
                      lhacode = [ 2, 2 ])

lamF3Q3x3 = Parameter(name = 'lamF3Q3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.202,
                      texname = '\\text{lamF3Q3x3}',
                      lhablock = 'DMF3Q',
                      lhacode = [ 3, 3 ])

lamF3u1x1 = Parameter(name = 'lamF3u1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.203,
                      texname = '\\text{lamF3u1x1}',
                      lhablock = 'DMF3U',
                      lhacode = [ 1, 1 ])

lamF3u2x2 = Parameter(name = 'lamF3u2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.204,
                      texname = '\\text{lamF3u2x2}',
                      lhablock = 'DMF3U',
                      lhacode = [ 2, 2 ])

lamF3u3x3 = Parameter(name = 'lamF3u3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.205,
                      texname = '\\text{lamF3u3x3}',
                      lhablock = 'DMF3U',
                      lhacode = [ 3, 3 ])

lamS1e1x1 = Parameter(name = 'lamS1e1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.112,
                      texname = '\\text{lamS1e1x1}',
                      lhablock = 'DMS1E',
                      lhacode = [ 1, 1 ])

lamS1e2x2 = Parameter(name = 'lamS1e2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.113,
                      texname = '\\text{lamS1e2x2}',
                      lhablock = 'DMS1E',
                      lhacode = [ 2, 2 ])

lamS1e3x3 = Parameter(name = 'lamS1e3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.114,
                      texname = '\\text{lamS1e3x3}',
                      lhablock = 'DMS1E',
                      lhacode = [ 3, 3 ])

lamS1L1x1 = Parameter(name = 'lamS1L1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.109,
                      texname = '\\text{lamS1L1x1}',
                      lhablock = 'DMS1L',
                      lhacode = [ 1, 1 ])

lamS1L2x2 = Parameter(name = 'lamS1L2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.11,
                      texname = '\\text{lamS1L2x2}',
                      lhablock = 'DMS1L',
                      lhacode = [ 2, 2 ])

lamS1L3x3 = Parameter(name = 'lamS1L3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.111,
                      texname = '\\text{lamS1L3x3}',
                      lhablock = 'DMS1L',
                      lhacode = [ 3, 3 ])

lamS3d1x1 = Parameter(name = 'lamS3d1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.106,
                      texname = '\\text{lamS3d1x1}',
                      lhablock = 'DMS3D',
                      lhacode = [ 1, 1 ])

lamS3d2x2 = Parameter(name = 'lamS3d2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.107,
                      texname = '\\text{lamS3d2x2}',
                      lhablock = 'DMS3D',
                      lhacode = [ 2, 2 ])

lamS3d3x3 = Parameter(name = 'lamS3d3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.108,
                      texname = '\\text{lamS3d3x3}',
                      lhablock = 'DMS3D',
                      lhacode = [ 3, 3 ])

lamS3Q1x1 = Parameter(name = 'lamS3Q1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{lamS3Q1x1}',
                      lhablock = 'DMS3Q',
                      lhacode = [ 1, 1 ])

lamS3Q2x2 = Parameter(name = 'lamS3Q2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.101,
                      texname = '\\text{lamS3Q2x2}',
                      lhablock = 'DMS3Q',
                      lhacode = [ 2, 2 ])

lamS3Q3x3 = Parameter(name = 'lamS3Q3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.102,
                      texname = '\\text{lamS3Q3x3}',
                      lhablock = 'DMS3Q',
                      lhacode = [ 3, 3 ])

lamS3u1x1 = Parameter(name = 'lamS3u1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.103,
                      texname = '\\text{lamS3u1x1}',
                      lhablock = 'DMS3U',
                      lhacode = [ 1, 1 ])

lamS3u2x2 = Parameter(name = 'lamS3u2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.104,
                      texname = '\\text{lamS3u2x2}',
                      lhablock = 'DMS3U',
                      lhacode = [ 2, 2 ])

lamS3u3x3 = Parameter(name = 'lamS3u3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.105,
                      texname = '\\text{lamS3u3x3}',
                      lhablock = 'DMS3U',
                      lhacode = [ 3, 3 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymdo = Parameter(name = 'ymdo',
                 nature = 'external',
                 type = 'real',
                 value = 0.00504,
                 texname = '\\text{ymdo}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 1 ])

ymup = Parameter(name = 'ymup',
                 nature = 'external',
                 type = 'real',
                 value = 0.00255,
                 texname = '\\text{ymup}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 2 ])

yms = Parameter(name = 'yms',
                nature = 'external',
                type = 'real',
                value = 0.101,
                texname = '\\text{yms}',
                lhablock = 'YUKAWA',
                lhacode = [ 3 ])

ymc = Parameter(name = 'ymc',
                nature = 'external',
                type = 'real',
                value = 1.27,
                texname = '\\text{ymc}',
                lhablock = 'YUKAWA',
                lhacode = [ 4 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

yme = Parameter(name = 'yme',
                nature = 'external',
                type = 'real',
                value = 0.000511,
                texname = '\\text{yme}',
                lhablock = 'YUKAWA',
                lhacode = [ 11 ])

ymm = Parameter(name = 'ymm',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{ymm}',
                lhablock = 'YUKAWA',
                lhacode = [ 13 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

Me = Parameter(name = 'Me',
               nature = 'external',
               type = 'real',
               value = 0.000511,
               texname = '\\text{Me}',
               lhablock = 'MASS',
               lhacode = [ 11 ])

MMU = Parameter(name = 'MMU',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{MMU}',
                lhablock = 'MASS',
                lhacode = [ 13 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MU = Parameter(name = 'MU',
               nature = 'external',
               type = 'real',
               value = 0.00255,
               texname = 'M',
               lhablock = 'MASS',
               lhacode = [ 2 ])

MC = Parameter(name = 'MC',
               nature = 'external',
               type = 'real',
               value = 1.27,
               texname = '\\text{MC}',
               lhablock = 'MASS',
               lhacode = [ 4 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MD = Parameter(name = 'MD',
               nature = 'external',
               type = 'real',
               value = 0.00504,
               texname = '\\text{MD}',
               lhablock = 'MASS',
               lhacode = [ 1 ])

MS = Parameter(name = 'MS',
               nature = 'external',
               type = 'real',
               value = 0.101,
               texname = '\\text{MS}',
               lhablock = 'MASS',
               lhacode = [ 3 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

MXs = Parameter(name = 'MXs',
                nature = 'external',
                type = 'real',
                value = 11.,
                texname = '\\text{MXs}',
                lhablock = 'MASS',
                lhacode = [ 51 ])

MXm = Parameter(name = 'MXm',
                nature = 'external',
                type = 'real',
                value = 10.,
                texname = '\\text{MXm}',
                lhablock = 'MASS',
                lhacode = [ 52 ])

MXv = Parameter(name = 'MXv',
                nature = 'external',
                type = 'real',
                value = 12.,
                texname = '\\text{MXv}',
                lhablock = 'MASS',
                lhacode = [ 53 ])

MXd = Parameter(name = 'MXd',
                nature = 'external',
                type = 'real',
                value = 13.,
                texname = '\\text{MXd}',
                lhablock = 'MASS',
                lhacode = [ 57 ])

MXc = Parameter(name = 'MXc',
                nature = 'external',
                type = 'real',
                value = 14.,
                texname = '\\text{MXc}',
                lhablock = 'MASS',
                lhacode = [ 56 ])

MXw = Parameter(name = 'MXw',
                nature = 'external',
                type = 'real',
                value = 15.,
                texname = '\\text{MXw}',
                lhablock = 'MASS',
                lhacode = [ 58 ])

MYS3Qu1 = Parameter(name = 'MYS3Qu1',
                    nature = 'external',
                    type = 'real',
                    value = 1000.,
                    texname = '\\text{MYS3Qu1}',
                    lhablock = 'MASS',
                    lhacode = [ 1000002 ])

MYS3Qu2 = Parameter(name = 'MYS3Qu2',
                    nature = 'external',
                    type = 'real',
                    value = 1001.,
                    texname = '\\text{MYS3Qu2}',
                    lhablock = 'MASS',
                    lhacode = [ 1000004 ])

MYS3Qu3 = Parameter(name = 'MYS3Qu3',
                    nature = 'external',
                    type = 'real',
                    value = 1002.,
                    texname = '\\text{MYS3Qu3}',
                    lhablock = 'MASS',
                    lhacode = [ 1000006 ])

MYS3Qd1 = Parameter(name = 'MYS3Qd1',
                    nature = 'external',
                    type = 'real',
                    value = 1003.,
                    texname = '\\text{MYS3Qd1}',
                    lhablock = 'MASS',
                    lhacode = [ 1000001 ])

MYS3Qd2 = Parameter(name = 'MYS3Qd2',
                    nature = 'external',
                    type = 'real',
                    value = 1004.,
                    texname = '\\text{MYS3Qd2}',
                    lhablock = 'MASS',
                    lhacode = [ 1000003 ])

MYS3Qd3 = Parameter(name = 'MYS3Qd3',
                    nature = 'external',
                    type = 'real',
                    value = 1005.,
                    texname = '\\text{MYS3Qd3}',
                    lhablock = 'MASS',
                    lhacode = [ 1000005 ])

MYS3u1 = Parameter(name = 'MYS3u1',
                   nature = 'external',
                   type = 'real',
                   value = 2000.,
                   texname = '\\text{MYS3u1}',
                   lhablock = 'MASS',
                   lhacode = [ 2000002 ])

MYS3u2 = Parameter(name = 'MYS3u2',
                   nature = 'external',
                   type = 'real',
                   value = 2001.,
                   texname = '\\text{MYS3u2}',
                   lhablock = 'MASS',
                   lhacode = [ 2000004 ])

MYS3u3 = Parameter(name = 'MYS3u3',
                   nature = 'external',
                   type = 'real',
                   value = 2002.,
                   texname = '\\text{MYS3u3}',
                   lhablock = 'MASS',
                   lhacode = [ 2000006 ])

MYS3d1 = Parameter(name = 'MYS3d1',
                   nature = 'external',
                   type = 'real',
                   value = 2003.,
                   texname = '\\text{MYS3d1}',
                   lhablock = 'MASS',
                   lhacode = [ 2000001 ])

MYS3d2 = Parameter(name = 'MYS3d2',
                   nature = 'external',
                   type = 'real',
                   value = 2004.,
                   texname = '\\text{MYS3d2}',
                   lhablock = 'MASS',
                   lhacode = [ 2000003 ])

MYS3d3 = Parameter(name = 'MYS3d3',
                   nature = 'external',
                   type = 'real',
                   value = 2005.,
                   texname = '\\text{MYS3d3}',
                   lhablock = 'MASS',
                   lhacode = [ 2000005 ])

MYS1Lv1 = Parameter(name = 'MYS1Lv1',
                    nature = 'external',
                    type = 'real',
                    value = 1006.,
                    texname = '\\text{MYS1Lv1}',
                    lhablock = 'MASS',
                    lhacode = [ 1000012 ])

MYS1Lv2 = Parameter(name = 'MYS1Lv2',
                    nature = 'external',
                    type = 'real',
                    value = 1007.,
                    texname = '\\text{MYS1Lv2}',
                    lhablock = 'MASS',
                    lhacode = [ 1000014 ])

MYS1Lv3 = Parameter(name = 'MYS1Lv3',
                    nature = 'external',
                    type = 'real',
                    value = 1008.,
                    texname = '\\text{MYS1Lv3}',
                    lhablock = 'MASS',
                    lhacode = [ 1000016 ])

MYS1Le1 = Parameter(name = 'MYS1Le1',
                    nature = 'external',
                    type = 'real',
                    value = 1009.,
                    texname = '\\text{MYS1Le1}',
                    lhablock = 'MASS',
                    lhacode = [ 1000011 ])

MYS1Le2 = Parameter(name = 'MYS1Le2',
                    nature = 'external',
                    type = 'real',
                    value = 1010.,
                    texname = '\\text{MYS1Le2}',
                    lhablock = 'MASS',
                    lhacode = [ 1000013 ])

MYS1Le3 = Parameter(name = 'MYS1Le3',
                    nature = 'external',
                    type = 'real',
                    value = 1011.,
                    texname = '\\text{MYS1Le3}',
                    lhablock = 'MASS',
                    lhacode = [ 1000015 ])

MYS1e1 = Parameter(name = 'MYS1e1',
                   nature = 'external',
                   type = 'real',
                   value = 2006.,
                   texname = '\\text{MYS1e1}',
                   lhablock = 'MASS',
                   lhacode = [ 2000011 ])

MYS1e2 = Parameter(name = 'MYS1e2',
                   nature = 'external',
                   type = 'real',
                   value = 2007.,
                   texname = '\\text{MYS1e2}',
                   lhablock = 'MASS',
                   lhacode = [ 2000013 ])

MYS1e3 = Parameter(name = 'MYS1e3',
                   nature = 'external',
                   type = 'real',
                   value = 2008.,
                   texname = '\\text{MYS1e3}',
                   lhablock = 'MASS',
                   lhacode = [ 2000015 ])

MYF3Qu1 = Parameter(name = 'MYF3Qu1',
                    nature = 'external',
                    type = 'real',
                    value = 3000.,
                    texname = '\\text{MYF3Qu1}',
                    lhablock = 'MASS',
                    lhacode = [ 5910002 ])

MYF3Qu2 = Parameter(name = 'MYF3Qu2',
                    nature = 'external',
                    type = 'real',
                    value = 3001.,
                    texname = '\\text{MYF3Qu2}',
                    lhablock = 'MASS',
                    lhacode = [ 5910004 ])

MYF3Qu3 = Parameter(name = 'MYF3Qu3',
                    nature = 'external',
                    type = 'real',
                    value = 3002.,
                    texname = '\\text{MYF3Qu3}',
                    lhablock = 'MASS',
                    lhacode = [ 5910006 ])

MYF3Qd1 = Parameter(name = 'MYF3Qd1',
                    nature = 'external',
                    type = 'real',
                    value = 3003.,
                    texname = '\\text{MYF3Qd1}',
                    lhablock = 'MASS',
                    lhacode = [ 5910001 ])

MYF3Qd2 = Parameter(name = 'MYF3Qd2',
                    nature = 'external',
                    type = 'real',
                    value = 3004.,
                    texname = '\\text{MYF3Qd2}',
                    lhablock = 'MASS',
                    lhacode = [ 5910003 ])

MYF3Qd3 = Parameter(name = 'MYF3Qd3',
                    nature = 'external',
                    type = 'real',
                    value = 3005.,
                    texname = '\\text{MYF3Qd3}',
                    lhablock = 'MASS',
                    lhacode = [ 5910005 ])

MYF3u1 = Parameter(name = 'MYF3u1',
                   nature = 'external',
                   type = 'real',
                   value = 4000.,
                   texname = '\\text{MYF3u1}',
                   lhablock = 'MASS',
                   lhacode = [ 5920002 ])

MYF3u2 = Parameter(name = 'MYF3u2',
                   nature = 'external',
                   type = 'real',
                   value = 4001.,
                   texname = '\\text{MYF3u2}',
                   lhablock = 'MASS',
                   lhacode = [ 5920004 ])

MYF3u3 = Parameter(name = 'MYF3u3',
                   nature = 'external',
                   type = 'real',
                   value = 4002.,
                   texname = '\\text{MYF3u3}',
                   lhablock = 'MASS',
                   lhacode = [ 5920006 ])

MYF3d1 = Parameter(name = 'MYF3d1',
                   nature = 'external',
                   type = 'real',
                   value = 4003.,
                   texname = '\\text{MYF3d1}',
                   lhablock = 'MASS',
                   lhacode = [ 5920001 ])

MYF3d2 = Parameter(name = 'MYF3d2',
                   nature = 'external',
                   type = 'real',
                   value = 4004.,
                   texname = '\\text{MYF3d2}',
                   lhablock = 'MASS',
                   lhacode = [ 5920003 ])

MYF3d3 = Parameter(name = 'MYF3d3',
                   nature = 'external',
                   type = 'real',
                   value = 4005.,
                   texname = '\\text{MYF3d3}',
                   lhablock = 'MASS',
                   lhacode = [ 5920005 ])

MYF1Lv1 = Parameter(name = 'MYF1Lv1',
                    nature = 'external',
                    type = 'real',
                    value = 3006.,
                    texname = '\\text{MYF1Lv1}',
                    lhablock = 'MASS',
                    lhacode = [ 5910012 ])

MYF1Lv2 = Parameter(name = 'MYF1Lv2',
                    nature = 'external',
                    type = 'real',
                    value = 3007.,
                    texname = '\\text{MYF1Lv2}',
                    lhablock = 'MASS',
                    lhacode = [ 5910014 ])

MYF1Lv3 = Parameter(name = 'MYF1Lv3',
                    nature = 'external',
                    type = 'real',
                    value = 3008.,
                    texname = '\\text{MYF1Lv3}',
                    lhablock = 'MASS',
                    lhacode = [ 5910016 ])

MYF1Le1 = Parameter(name = 'MYF1Le1',
                    nature = 'external',
                    type = 'real',
                    value = 3009.,
                    texname = '\\text{MYF1Le1}',
                    lhablock = 'MASS',
                    lhacode = [ 5910011 ])

MYF1Le2 = Parameter(name = 'MYF1Le2',
                    nature = 'external',
                    type = 'real',
                    value = 3010.,
                    texname = '\\text{MYF1Le2}',
                    lhablock = 'MASS',
                    lhacode = [ 5910013 ])

MYF1Le3 = Parameter(name = 'MYF1Le3',
                    nature = 'external',
                    type = 'real',
                    value = 3011.,
                    texname = '\\text{MYF1Le3}',
                    lhablock = 'MASS',
                    lhacode = [ 5910015 ])

MYF1e1 = Parameter(name = 'MYF1e1',
                   nature = 'external',
                   type = 'real',
                   value = 4006.,
                   texname = '\\text{MYF1e1}',
                   lhablock = 'MASS',
                   lhacode = [ 5920011 ])

MYF1e2 = Parameter(name = 'MYF1e2',
                   nature = 'external',
                   type = 'real',
                   value = 4007.,
                   texname = '\\text{MYF1e2}',
                   lhablock = 'MASS',
                   lhacode = [ 5920013 ])

MYF1e3 = Parameter(name = 'MYF1e3',
                   nature = 'external',
                   type = 'real',
                   value = 4008.,
                   texname = '\\text{MYF1e3}',
                   lhablock = 'MASS',
                   lhacode = [ 5920015 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00407,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

WXs = Parameter(name = 'WXs',
                nature = 'external',
                type = 'real',
                value = 1.e-6,
                texname = '\\text{WXs}',
                lhablock = 'DECAY',
                lhacode = [ 51 ])

WXm = Parameter(name = 'WXm',
                nature = 'external',
                type = 'real',
                value = 1.e-6,
                texname = '\\text{WXm}',
                lhablock = 'DECAY',
                lhacode = [ 52 ])

WXv = Parameter(name = 'WXv',
                nature = 'external',
                type = 'real',
                value = 1.e-6,
                texname = '\\text{WXv}',
                lhablock = 'DECAY',
                lhacode = [ 53 ])

WXd = Parameter(name = 'WXd',
                nature = 'external',
                type = 'real',
                value = 1.e-6,
                texname = '\\text{WXd}',
                lhablock = 'DECAY',
                lhacode = [ 57 ])

WXc = Parameter(name = 'WXc',
                nature = 'external',
                type = 'real',
                value = 1.e-6,
                texname = '\\text{WXc}',
                lhablock = 'DECAY',
                lhacode = [ 56 ])

WXw = Parameter(name = 'WXw',
                nature = 'external',
                type = 'real',
                value = 1.e-6,
                texname = '\\text{WXw}',
                lhablock = 'DECAY',
                lhacode = [ 58 ])

WYS3Qu1 = Parameter(name = 'WYS3Qu1',
                    nature = 'external',
                    type = 'real',
                    value = 10.,
                    texname = '\\text{WYS3Qu1}',
                    lhablock = 'DECAY',
                    lhacode = [ 1000002 ])

WYS3Qu2 = Parameter(name = 'WYS3Qu2',
                    nature = 'external',
                    type = 'real',
                    value = 10.01,
                    texname = '\\text{WYS3Qu2}',
                    lhablock = 'DECAY',
                    lhacode = [ 1000004 ])

WYS3Qu3 = Parameter(name = 'WYS3Qu3',
                    nature = 'external',
                    type = 'real',
                    value = 10.02,
                    texname = '\\text{WYS3Qu3}',
                    lhablock = 'DECAY',
                    lhacode = [ 1000006 ])

WYS3Qd1 = Parameter(name = 'WYS3Qd1',
                    nature = 'external',
                    type = 'real',
                    value = 10.03,
                    texname = '\\text{WYS3Qd1}',
                    lhablock = 'DECAY',
                    lhacode = [ 1000001 ])

WYS3Qd2 = Parameter(name = 'WYS3Qd2',
                    nature = 'external',
                    type = 'real',
                    value = 10.04,
                    texname = '\\text{WYS3Qd2}',
                    lhablock = 'DECAY',
                    lhacode = [ 1000003 ])

WYS3Qd3 = Parameter(name = 'WYS3Qd3',
                    nature = 'external',
                    type = 'real',
                    value = 10.05,
                    texname = '\\text{WYS3Qd3}',
                    lhablock = 'DECAY',
                    lhacode = [ 1000005 ])

WYS3u1 = Parameter(name = 'WYS3u1',
                   nature = 'external',
                   type = 'real',
                   value = 20.,
                   texname = '\\text{WYS3u1}',
                   lhablock = 'DECAY',
                   lhacode = [ 2000002 ])

WYS3u2 = Parameter(name = 'WYS3u2',
                   nature = 'external',
                   type = 'real',
                   value = 20.01,
                   texname = '\\text{WYS3u2}',
                   lhablock = 'DECAY',
                   lhacode = [ 2000004 ])

WYS3u3 = Parameter(name = 'WYS3u3',
                   nature = 'external',
                   type = 'real',
                   value = 20.02,
                   texname = '\\text{WYS3u3}',
                   lhablock = 'DECAY',
                   lhacode = [ 2000006 ])

WYS3d1 = Parameter(name = 'WYS3d1',
                   nature = 'external',
                   type = 'real',
                   value = 20.03,
                   texname = '\\text{WYS3d1}',
                   lhablock = 'DECAY',
                   lhacode = [ 2000001 ])

WYS3d2 = Parameter(name = 'WYS3d2',
                   nature = 'external',
                   type = 'real',
                   value = 20.04,
                   texname = '\\text{WYS3d2}',
                   lhablock = 'DECAY',
                   lhacode = [ 2000003 ])

WYS3d3 = Parameter(name = 'WYS3d3',
                   nature = 'external',
                   type = 'real',
                   value = 20.05,
                   texname = '\\text{WYS3d3}',
                   lhablock = 'DECAY',
                   lhacode = [ 2000005 ])

WYS1Lv1 = Parameter(name = 'WYS1Lv1',
                    nature = 'external',
                    type = 'real',
                    value = 10.06,
                    texname = '\\text{WYS1Lv1}',
                    lhablock = 'DECAY',
                    lhacode = [ 1000012 ])

WYS1Lv2 = Parameter(name = 'WYS1Lv2',
                    nature = 'external',
                    type = 'real',
                    value = 10.07,
                    texname = '\\text{WYS1Lv2}',
                    lhablock = 'DECAY',
                    lhacode = [ 1000014 ])

WYS1Lv3 = Parameter(name = 'WYS1Lv3',
                    nature = 'external',
                    type = 'real',
                    value = 10.08,
                    texname = '\\text{WYS1Lv3}',
                    lhablock = 'DECAY',
                    lhacode = [ 1000016 ])

WYS1Le1 = Parameter(name = 'WYS1Le1',
                    nature = 'external',
                    type = 'real',
                    value = 10.09,
                    texname = '\\text{WYS1Le1}',
                    lhablock = 'DECAY',
                    lhacode = [ 1000011 ])

WYS1Le2 = Parameter(name = 'WYS1Le2',
                    nature = 'external',
                    type = 'real',
                    value = 10.1,
                    texname = '\\text{WYS1Le2}',
                    lhablock = 'DECAY',
                    lhacode = [ 1000013 ])

WYS1Le3 = Parameter(name = 'WYS1Le3',
                    nature = 'external',
                    type = 'real',
                    value = 10.11,
                    texname = '\\text{WYS1Le3}',
                    lhablock = 'DECAY',
                    lhacode = [ 1000015 ])

WYS1e1 = Parameter(name = 'WYS1e1',
                   nature = 'external',
                   type = 'real',
                   value = 20.06,
                   texname = '\\text{WYS1e1}',
                   lhablock = 'DECAY',
                   lhacode = [ 2000011 ])

WYS1e2 = Parameter(name = 'WYS1e2',
                   nature = 'external',
                   type = 'real',
                   value = 20.07,
                   texname = '\\text{WYS1e2}',
                   lhablock = 'DECAY',
                   lhacode = [ 2000013 ])

WYS1e3 = Parameter(name = 'WYS1e3',
                   nature = 'external',
                   type = 'real',
                   value = 20.08,
                   texname = '\\text{WYS1e3}',
                   lhablock = 'DECAY',
                   lhacode = [ 2000015 ])

WYF3Qu1 = Parameter(name = 'WYF3Qu1',
                    nature = 'external',
                    type = 'real',
                    value = 30.,
                    texname = '\\text{WYF3Qu1}',
                    lhablock = 'DECAY',
                    lhacode = [ 5910002 ])

WYF3Qu2 = Parameter(name = 'WYF3Qu2',
                    nature = 'external',
                    type = 'real',
                    value = 30.01,
                    texname = '\\text{WYF3Qu2}',
                    lhablock = 'DECAY',
                    lhacode = [ 5910004 ])

WYF3Qu3 = Parameter(name = 'WYF3Qu3',
                    nature = 'external',
                    type = 'real',
                    value = 30.02,
                    texname = '\\text{WYF3Qu3}',
                    lhablock = 'DECAY',
                    lhacode = [ 5910006 ])

WYF3Qd1 = Parameter(name = 'WYF3Qd1',
                    nature = 'external',
                    type = 'real',
                    value = 30.03,
                    texname = '\\text{WYF3Qd1}',
                    lhablock = 'DECAY',
                    lhacode = [ 5910001 ])

WYF3Qd2 = Parameter(name = 'WYF3Qd2',
                    nature = 'external',
                    type = 'real',
                    value = 30.04,
                    texname = '\\text{WYF3Qd2}',
                    lhablock = 'DECAY',
                    lhacode = [ 5910003 ])

WYF3Qd3 = Parameter(name = 'WYF3Qd3',
                    nature = 'external',
                    type = 'real',
                    value = 30.05,
                    texname = '\\text{WYF3Qd3}',
                    lhablock = 'DECAY',
                    lhacode = [ 5910005 ])

WYF3u1 = Parameter(name = 'WYF3u1',
                   nature = 'external',
                   type = 'real',
                   value = 40.,
                   texname = '\\text{WYF3u1}',
                   lhablock = 'DECAY',
                   lhacode = [ 5920002 ])

WYF3u2 = Parameter(name = 'WYF3u2',
                   nature = 'external',
                   type = 'real',
                   value = 40.01,
                   texname = '\\text{WYF3u2}',
                   lhablock = 'DECAY',
                   lhacode = [ 5920004 ])

WYF3u3 = Parameter(name = 'WYF3u3',
                   nature = 'external',
                   type = 'real',
                   value = 40.02,
                   texname = '\\text{WYF3u3}',
                   lhablock = 'DECAY',
                   lhacode = [ 5920006 ])

WYF3d1 = Parameter(name = 'WYF3d1',
                   nature = 'external',
                   type = 'real',
                   value = 40.03,
                   texname = '\\text{WYF3d1}',
                   lhablock = 'DECAY',
                   lhacode = [ 5920001 ])

WYF3d2 = Parameter(name = 'WYF3d2',
                   nature = 'external',
                   type = 'real',
                   value = 40.04,
                   texname = '\\text{WYF3d2}',
                   lhablock = 'DECAY',
                   lhacode = [ 5920003 ])

WYF3d3 = Parameter(name = 'WYF3d3',
                   nature = 'external',
                   type = 'real',
                   value = 40.05,
                   texname = '\\text{WYF3d3}',
                   lhablock = 'DECAY',
                   lhacode = [ 5920005 ])

WYF1Lv1 = Parameter(name = 'WYF1Lv1',
                    nature = 'external',
                    type = 'real',
                    value = 30.06,
                    texname = '\\text{WYF1Lv1}',
                    lhablock = 'DECAY',
                    lhacode = [ 5910012 ])

WYF1Lv2 = Parameter(name = 'WYF1Lv2',
                    nature = 'external',
                    type = 'real',
                    value = 30.07,
                    texname = '\\text{WYF1Lv2}',
                    lhablock = 'DECAY',
                    lhacode = [ 5910014 ])

WYF1Lv3 = Parameter(name = 'WYF1Lv3',
                    nature = 'external',
                    type = 'real',
                    value = 30.08,
                    texname = '\\text{WYF1Lv3}',
                    lhablock = 'DECAY',
                    lhacode = [ 5910016 ])

WYF1Le1 = Parameter(name = 'WYF1Le1',
                    nature = 'external',
                    type = 'real',
                    value = 30.09,
                    texname = '\\text{WYF1Le1}',
                    lhablock = 'DECAY',
                    lhacode = [ 5910011 ])

WYF1Le2 = Parameter(name = 'WYF1Le2',
                    nature = 'external',
                    type = 'real',
                    value = 30.1,
                    texname = '\\text{WYF1Le2}',
                    lhablock = 'DECAY',
                    lhacode = [ 5910013 ])

WYF1Le3 = Parameter(name = 'WYF1Le3',
                    nature = 'external',
                    type = 'real',
                    value = 30.11,
                    texname = '\\text{WYF1Le3}',
                    lhablock = 'DECAY',
                    lhacode = [ 5910015 ])

WYF1e1 = Parameter(name = 'WYF1e1',
                   nature = 'external',
                   type = 'real',
                   value = 40.06,
                   texname = '\\text{WYF1e1}',
                   lhablock = 'DECAY',
                   lhacode = [ 5920011 ])

WYF1e2 = Parameter(name = 'WYF1e2',
                   nature = 'external',
                   type = 'real',
                   value = 40.07,
                   texname = '\\text{WYF1e2}',
                   lhablock = 'DECAY',
                   lhacode = [ 5920013 ])

WYF1e3 = Parameter(name = 'WYF1e3',
                   nature = 'external',
                   type = 'real',
                   value = 40.08,
                   texname = '\\text{WYF1e3}',
                   lhablock = 'DECAY',
                   lhacode = [ 5920015 ])

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '(1)/(aEWM1)',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

CKM1x1 = Parameter(name = 'CKM1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM1x1}')

CKM1x2 = Parameter(name = 'CKM1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.sin(cabi)',
                   texname = '\\text{CKM1x2}')

CKM1x3 = Parameter(name = 'CKM1x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM1x3}')

CKM2x1 = Parameter(name = 'CKM2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '-cmath.sin(cabi)',
                   texname = '\\text{CKM2x1}')

CKM2x2 = Parameter(name = 'CKM2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM2x2}')

CKM2x3 = Parameter(name = 'CKM2x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM2x3}')

CKM3x1 = Parameter(name = 'CKM3x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM3x1}')

CKM3x2 = Parameter(name = 'CKM3x2',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM3x2}')

CKM3x3 = Parameter(name = 'CKM3x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '1',
                   texname = '\\text{CKM3x3}')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '(1)+(-MW**2)/(MZ**2)',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = '(ee)/(cw)',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = '(ee)/(sw)',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/(ee)',
                texname = '\\text{vev}')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = '(MH**2)/(2*vev**2)',
                texname = '\\text{lam}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/(vev)',
               texname = '\\text{yb}')

yc = Parameter(name = 'yc',
               nature = 'internal',
               type = 'real',
               value = '(ymc*cmath.sqrt(2))/(vev)',
               texname = '\\text{yc}')

ydo = Parameter(name = 'ydo',
                nature = 'internal',
                type = 'real',
                value = '(ymdo*cmath.sqrt(2))/(vev)',
                texname = '\\text{ydo}')

ye = Parameter(name = 'ye',
               nature = 'internal',
               type = 'real',
               value = '(yme*cmath.sqrt(2))/(vev)',
               texname = '\\text{ye}')

ym = Parameter(name = 'ym',
               nature = 'internal',
               type = 'real',
               value = '(ymm*cmath.sqrt(2))/(vev)',
               texname = '\\text{ym}')

ys = Parameter(name = 'ys',
               nature = 'internal',
               type = 'real',
               value = '(yms*cmath.sqrt(2))/(vev)',
               texname = '\\text{ys}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/(vev)',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/(vev)',
                 texname = '\\text{ytau}')

yup = Parameter(name = 'yup',
                nature = 'internal',
                type = 'real',
                value = '(ymup*cmath.sqrt(2))/(vev)',
                texname = '\\text{yup}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')

