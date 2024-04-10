# This file was automatically created by FeynRules 2.4.91
# Mathematica version: 13.1.0 for Mac OS X ARM (64-bit) (June 16, 2022)
# Date: Wed 10 Apr 2024 18:04:25


from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.G0, P.G0, P.G0, P.G0 ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_24})

V_2 = Vertex(name = 'V_2',
             particles = [ P.G0, P.G0, P.G__minus__, P.G__plus__ ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_22})

V_3 = Vertex(name = 'V_3',
             particles = [ P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_23})

V_4 = Vertex(name = 'V_4',
             particles = [ P.G0, P.G0, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_22})

V_5 = Vertex(name = 'V_5',
             particles = [ P.G__minus__, P.G__plus__, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_22})

V_6 = Vertex(name = 'V_6',
             particles = [ P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_24})

V_7 = Vertex(name = 'V_7',
             particles = [ P.G0, P.G0, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_133})

V_8 = Vertex(name = 'V_8',
             particles = [ P.G__minus__, P.G__plus__, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_133})

V_9 = Vertex(name = 'V_9',
             particles = [ P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_134})

V_10 = Vertex(name = 'V_10',
              particles = [ P.a, P.a, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_10})

V_11 = Vertex(name = 'V_11',
              particles = [ P.a, P.a, P.YS1e1__tilde__, P.YS1e1 ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_10})

V_12 = Vertex(name = 'V_12',
              particles = [ P.a, P.a, P.YS1e2__tilde__, P.YS1e2 ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_10})

V_13 = Vertex(name = 'V_13',
              particles = [ P.a, P.a, P.YS1e3__tilde__, P.YS1e3 ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_10})

V_14 = Vertex(name = 'V_14',
              particles = [ P.a, P.a, P.YS1Le1__tilde__, P.YS1Le1 ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_10})

V_15 = Vertex(name = 'V_15',
              particles = [ P.a, P.a, P.YS1Le2__tilde__, P.YS1Le2 ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_10})

V_16 = Vertex(name = 'V_16',
              particles = [ P.a, P.a, P.YS1Le3__tilde__, P.YS1Le3 ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_10})

V_17 = Vertex(name = 'V_17',
              particles = [ P.a, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_5})

V_18 = Vertex(name = 'V_18',
              particles = [ P.a, P.YS1e1__tilde__, P.YS1e1 ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_6})

V_19 = Vertex(name = 'V_19',
              particles = [ P.a, P.YS1e2__tilde__, P.YS1e2 ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_6})

V_20 = Vertex(name = 'V_20',
              particles = [ P.a, P.YS1e3__tilde__, P.YS1e3 ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_6})

V_21 = Vertex(name = 'V_21',
              particles = [ P.a, P.YS1Le1__tilde__, P.YS1Le1 ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_6})

V_22 = Vertex(name = 'V_22',
              particles = [ P.a, P.YS1Le2__tilde__, P.YS1Le2 ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_6})

V_23 = Vertex(name = 'V_23',
              particles = [ P.a, P.YS1Le3__tilde__, P.YS1Le3 ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_6})

V_24 = Vertex(name = 'V_24',
              particles = [ P.ghA, P.ghWm__tilde__, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_5})

V_25 = Vertex(name = 'V_25',
              particles = [ P.ghA, P.ghWp__tilde__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_6})

V_26 = Vertex(name = 'V_26',
              particles = [ P.ghWm, P.ghA__tilde__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.UUS1 ],
              couplings = {(0,0):C.GC_140})

V_27 = Vertex(name = 'V_27',
              particles = [ P.ghWm, P.ghA__tilde__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_5})

V_28 = Vertex(name = 'V_28',
              particles = [ P.ghWm, P.ghWm__tilde__, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.UUS1 ],
              couplings = {(0,0):C.GC_135})

V_29 = Vertex(name = 'V_29',
              particles = [ P.ghWm, P.ghWm__tilde__, P.H ],
              color = [ '1' ],
              lorentz = [ L.UUS1 ],
              couplings = {(0,0):C.GC_136})

V_30 = Vertex(name = 'V_30',
              particles = [ P.ghWm, P.ghWm__tilde__, P.a ],
              color = [ '1' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_6})

V_31 = Vertex(name = 'V_31',
              particles = [ P.ghWm, P.ghWm__tilde__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_91})

V_32 = Vertex(name = 'V_32',
              particles = [ P.ghWm, P.ghZ__tilde__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.UUS1 ],
              couplings = {(0,0):C.GC_143})

V_33 = Vertex(name = 'V_33',
              particles = [ P.ghWm, P.ghZ__tilde__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_90})

V_34 = Vertex(name = 'V_34',
              particles = [ P.ghWp, P.ghA__tilde__, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.UUS1 ],
              couplings = {(0,0):C.GC_139})

V_35 = Vertex(name = 'V_35',
              particles = [ P.ghWp, P.ghA__tilde__, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_6})

V_36 = Vertex(name = 'V_36',
              particles = [ P.ghWp, P.ghWp__tilde__, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.UUS1 ],
              couplings = {(0,0):C.GC_138})

V_37 = Vertex(name = 'V_37',
              particles = [ P.ghWp, P.ghWp__tilde__, P.H ],
              color = [ '1' ],
              lorentz = [ L.UUS1 ],
              couplings = {(0,0):C.GC_136})

V_38 = Vertex(name = 'V_38',
              particles = [ P.ghWp, P.ghWp__tilde__, P.a ],
              color = [ '1' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_5})

V_39 = Vertex(name = 'V_39',
              particles = [ P.ghWp, P.ghWp__tilde__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_90})

V_40 = Vertex(name = 'V_40',
              particles = [ P.ghWp, P.ghZ__tilde__, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.UUS1 ],
              couplings = {(0,0):C.GC_142})

V_41 = Vertex(name = 'V_41',
              particles = [ P.ghWp, P.ghZ__tilde__, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_91})

V_42 = Vertex(name = 'V_42',
              particles = [ P.ghZ, P.ghWm__tilde__, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.UUS1 ],
              couplings = {(0,0):C.GC_144})

V_43 = Vertex(name = 'V_43',
              particles = [ P.ghZ, P.ghWm__tilde__, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_90})

V_44 = Vertex(name = 'V_44',
              particles = [ P.ghZ, P.ghWp__tilde__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.UUS1 ],
              couplings = {(0,0):C.GC_141})

V_45 = Vertex(name = 'V_45',
              particles = [ P.ghZ, P.ghWp__tilde__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_91})

V_46 = Vertex(name = 'V_46',
              particles = [ P.ghZ, P.ghZ__tilde__, P.H ],
              color = [ '1' ],
              lorentz = [ L.UUS1 ],
              couplings = {(0,0):C.GC_145})

V_47 = Vertex(name = 'V_47',
              particles = [ P.ghG, P.ghG__tilde__, P.g ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_16})

V_48 = Vertex(name = 'V_48',
              particles = [ P.g, P.g, P.g ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVV1 ],
              couplings = {(0,0):C.GC_16})

V_49 = Vertex(name = 'V_49',
              particles = [ P.g, P.g, P.g, P.g ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVV1, L.VVVV3, L.VVVV4 ],
              couplings = {(1,1):C.GC_21,(0,0):C.GC_21,(2,2):C.GC_21})

V_50 = Vertex(name = 'V_50',
              particles = [ P.YF1e1__tilde__, P.YF1e1, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_5})

V_51 = Vertex(name = 'V_51',
              particles = [ P.YF1e2__tilde__, P.YF1e2, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_5})

V_52 = Vertex(name = 'V_52',
              particles = [ P.YF1e3__tilde__, P.YF1e3, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_5})

V_53 = Vertex(name = 'V_53',
              particles = [ P.YF1Le1__tilde__, P.YF1Le1, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_5})

V_54 = Vertex(name = 'V_54',
              particles = [ P.YF1Le2__tilde__, P.YF1Le2, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_5})

V_55 = Vertex(name = 'V_55',
              particles = [ P.YF1Le3__tilde__, P.YF1Le3, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_5})

V_56 = Vertex(name = 'V_56',
              particles = [ P.YF3d1__tilde__, P.YF3d1, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_1})

V_57 = Vertex(name = 'V_57',
              particles = [ P.YF3d2__tilde__, P.YF3d2, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_1})

V_58 = Vertex(name = 'V_58',
              particles = [ P.YF3d3__tilde__, P.YF3d3, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_1})

V_59 = Vertex(name = 'V_59',
              particles = [ P.YF3Qd1__tilde__, P.YF3Qd1, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_1})

V_60 = Vertex(name = 'V_60',
              particles = [ P.YF3Qd2__tilde__, P.YF3Qd2, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_1})

V_61 = Vertex(name = 'V_61',
              particles = [ P.YF3Qd3__tilde__, P.YF3Qd3, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_1})

V_62 = Vertex(name = 'V_62',
              particles = [ P.YF3Qu1__tilde__, P.YF3Qu1, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_4})

V_63 = Vertex(name = 'V_63',
              particles = [ P.YF3Qu2__tilde__, P.YF3Qu2, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_4})

V_64 = Vertex(name = 'V_64',
              particles = [ P.YF3Qu3__tilde__, P.YF3Qu3, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_4})

V_65 = Vertex(name = 'V_65',
              particles = [ P.YF3u1__tilde__, P.YF3u1, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_4})

V_66 = Vertex(name = 'V_66',
              particles = [ P.YF3u2__tilde__, P.YF3u2, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_4})

V_67 = Vertex(name = 'V_67',
              particles = [ P.YF3u3__tilde__, P.YF3u3, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_4})

V_68 = Vertex(name = 'V_68',
              particles = [ P.ve__tilde__, P.YF1Lv1, P.Xc__tilde__ ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_28})

V_69 = Vertex(name = 'V_69',
              particles = [ P.ve__tilde__, P.YF1Lv1, P.Xs ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_28})

V_70 = Vertex(name = 'V_70',
              particles = [ P.e__plus__, P.YF1Le1, P.Xc__tilde__ ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_28})

V_71 = Vertex(name = 'V_71',
              particles = [ P.e__plus__, P.YF1Le1, P.Xs ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_28})

V_72 = Vertex(name = 'V_72',
              particles = [ P.vm__tilde__, P.YF1Lv2, P.Xc__tilde__ ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_29})

V_73 = Vertex(name = 'V_73',
              particles = [ P.vm__tilde__, P.YF1Lv2, P.Xs ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_29})

V_74 = Vertex(name = 'V_74',
              particles = [ P.mu__plus__, P.YF1Le2, P.Xc__tilde__ ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_29})

V_75 = Vertex(name = 'V_75',
              particles = [ P.mu__plus__, P.YF1Le2, P.Xs ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_29})

V_76 = Vertex(name = 'V_76',
              particles = [ P.vt__tilde__, P.YF1Lv3, P.Xc__tilde__ ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_30})

V_77 = Vertex(name = 'V_77',
              particles = [ P.vt__tilde__, P.YF1Lv3, P.Xs ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_30})

V_78 = Vertex(name = 'V_78',
              particles = [ P.ta__plus__, P.YF1Le3, P.Xc__tilde__ ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_30})

V_79 = Vertex(name = 'V_79',
              particles = [ P.ta__plus__, P.YF1Le3, P.Xs ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_30})

V_80 = Vertex(name = 'V_80',
              particles = [ P.u__tilde__, P.YF3Qu1, P.Xc__tilde__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_34})

V_81 = Vertex(name = 'V_81',
              particles = [ P.u__tilde__, P.YF3Qu1, P.Xs ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_34})

V_82 = Vertex(name = 'V_82',
              particles = [ P.b__tilde__, P.YF3Qd1, P.Xc__tilde__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_37})

V_83 = Vertex(name = 'V_83',
              particles = [ P.d__tilde__, P.YF3Qd1, P.Xc__tilde__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_35})

V_84 = Vertex(name = 'V_84',
              particles = [ P.s__tilde__, P.YF3Qd1, P.Xc__tilde__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_36})

V_85 = Vertex(name = 'V_85',
              particles = [ P.b__tilde__, P.YF3Qd1, P.Xs ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_37})

V_86 = Vertex(name = 'V_86',
              particles = [ P.d__tilde__, P.YF3Qd1, P.Xs ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_35})

V_87 = Vertex(name = 'V_87',
              particles = [ P.s__tilde__, P.YF3Qd1, P.Xs ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_36})

V_88 = Vertex(name = 'V_88',
              particles = [ P.c__tilde__, P.YF3Qu2, P.Xc__tilde__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_38})

V_89 = Vertex(name = 'V_89',
              particles = [ P.c__tilde__, P.YF3Qu2, P.Xs ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_38})

V_90 = Vertex(name = 'V_90',
              particles = [ P.b__tilde__, P.YF3Qd2, P.Xc__tilde__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_41})

V_91 = Vertex(name = 'V_91',
              particles = [ P.d__tilde__, P.YF3Qd2, P.Xc__tilde__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_39})

V_92 = Vertex(name = 'V_92',
              particles = [ P.s__tilde__, P.YF3Qd2, P.Xc__tilde__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_40})

V_93 = Vertex(name = 'V_93',
              particles = [ P.b__tilde__, P.YF3Qd2, P.Xs ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_41})

V_94 = Vertex(name = 'V_94',
              particles = [ P.d__tilde__, P.YF3Qd2, P.Xs ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_39})

V_95 = Vertex(name = 'V_95',
              particles = [ P.s__tilde__, P.YF3Qd2, P.Xs ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_40})

V_96 = Vertex(name = 'V_96',
              particles = [ P.t__tilde__, P.YF3Qu3, P.Xc__tilde__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_42})

V_97 = Vertex(name = 'V_97',
              particles = [ P.t__tilde__, P.YF3Qu3, P.Xs ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_42})

V_98 = Vertex(name = 'V_98',
              particles = [ P.b__tilde__, P.YF3Qd3, P.Xc__tilde__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_45})

V_99 = Vertex(name = 'V_99',
              particles = [ P.d__tilde__, P.YF3Qd3, P.Xc__tilde__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_43})

V_100 = Vertex(name = 'V_100',
               particles = [ P.s__tilde__, P.YF3Qd3, P.Xc__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_44})

V_101 = Vertex(name = 'V_101',
               particles = [ P.b__tilde__, P.YF3Qd3, P.Xs ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_45})

V_102 = Vertex(name = 'V_102',
               particles = [ P.d__tilde__, P.YF3Qd3, P.Xs ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_43})

V_103 = Vertex(name = 'V_103',
               particles = [ P.s__tilde__, P.YF3Qd3, P.Xs ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_44})

V_104 = Vertex(name = 'V_104',
               particles = [ P.ve__tilde__, P.Xd, P.YS1Lv1 ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_52})

V_105 = Vertex(name = 'V_105',
               particles = [ P.ve__tilde__, P.Xm, P.YS1Lv1 ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_52})

V_106 = Vertex(name = 'V_106',
               particles = [ P.vm__tilde__, P.Xd, P.YS1Lv2 ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_53})

V_107 = Vertex(name = 'V_107',
               particles = [ P.vm__tilde__, P.Xm, P.YS1Lv2 ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_53})

V_108 = Vertex(name = 'V_108',
               particles = [ P.vt__tilde__, P.Xd, P.YS1Lv3 ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_54})

V_109 = Vertex(name = 'V_109',
               particles = [ P.vt__tilde__, P.Xm, P.YS1Lv3 ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_54})

V_110 = Vertex(name = 'V_110',
               particles = [ P.e__plus__, P.Xd, P.YS1Le1 ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_52})

V_111 = Vertex(name = 'V_111',
               particles = [ P.e__plus__, P.Xm, P.YS1Le1 ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_52})

V_112 = Vertex(name = 'V_112',
               particles = [ P.mu__plus__, P.Xd, P.YS1Le2 ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_53})

V_113 = Vertex(name = 'V_113',
               particles = [ P.mu__plus__, P.Xm, P.YS1Le2 ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_53})

V_114 = Vertex(name = 'V_114',
               particles = [ P.ta__plus__, P.Xd, P.YS1Le3 ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_54})

V_115 = Vertex(name = 'V_115',
               particles = [ P.ta__plus__, P.Xm, P.YS1Le3 ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_54})

V_116 = Vertex(name = 'V_116',
               particles = [ P.YF1e1__tilde__, P.e__minus__, P.Xc ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_25})

V_117 = Vertex(name = 'V_117',
               particles = [ P.YF1e2__tilde__, P.mu__minus__, P.Xc ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_26})

V_118 = Vertex(name = 'V_118',
               particles = [ P.YF1e3__tilde__, P.ta__minus__, P.Xc ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_27})

V_119 = Vertex(name = 'V_119',
               particles = [ P.YF1e1__tilde__, P.e__minus__, P.Xs ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_25})

V_120 = Vertex(name = 'V_120',
               particles = [ P.YF1e2__tilde__, P.mu__minus__, P.Xs ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_26})

V_121 = Vertex(name = 'V_121',
               particles = [ P.YF1e3__tilde__, P.ta__minus__, P.Xs ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_27})

V_122 = Vertex(name = 'V_122',
               particles = [ P.YF3d1__tilde__, P.d, P.Xc ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_31})

V_123 = Vertex(name = 'V_123',
               particles = [ P.YF3d2__tilde__, P.s, P.Xc ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_32})

V_124 = Vertex(name = 'V_124',
               particles = [ P.YF3d3__tilde__, P.b, P.Xc ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_33})

V_125 = Vertex(name = 'V_125',
               particles = [ P.YF3d1__tilde__, P.d, P.Xs ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_31})

V_126 = Vertex(name = 'V_126',
               particles = [ P.YF3d2__tilde__, P.s, P.Xs ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_32})

V_127 = Vertex(name = 'V_127',
               particles = [ P.YF3d3__tilde__, P.b, P.Xs ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_33})

V_128 = Vertex(name = 'V_128',
               particles = [ P.YF3u1__tilde__, P.u, P.Xc ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_46})

V_129 = Vertex(name = 'V_129',
               particles = [ P.YF3u2__tilde__, P.c, P.Xc ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_47})

V_130 = Vertex(name = 'V_130',
               particles = [ P.YF3u3__tilde__, P.t, P.Xc ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_48})

V_131 = Vertex(name = 'V_131',
               particles = [ P.YF3u1__tilde__, P.u, P.Xs ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_46})

V_132 = Vertex(name = 'V_132',
               particles = [ P.YF3u2__tilde__, P.c, P.Xs ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_47})

V_133 = Vertex(name = 'V_133',
               particles = [ P.YF3u3__tilde__, P.t, P.Xs ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_48})

V_134 = Vertex(name = 'V_134',
               particles = [ P.b__tilde__, P.c, P.G__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_155,(0,1):C.GC_148})

V_135 = Vertex(name = 'V_135',
               particles = [ P.d__tilde__, P.c, P.G__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_153,(0,1):C.GC_157})

V_136 = Vertex(name = 'V_136',
               particles = [ P.s__tilde__, P.c, P.G__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_154,(0,1):C.GC_170})

V_137 = Vertex(name = 'V_137',
               particles = [ P.b__tilde__, P.t, P.G__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_177,(0,1):C.GC_149})

V_138 = Vertex(name = 'V_138',
               particles = [ P.d__tilde__, P.t, P.G__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_175,(0,1):C.GC_158})

V_139 = Vertex(name = 'V_139',
               particles = [ P.s__tilde__, P.t, P.G__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_176,(0,1):C.GC_171})

V_140 = Vertex(name = 'V_140',
               particles = [ P.b__tilde__, P.u, P.G__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_188,(0,1):C.GC_147})

V_141 = Vertex(name = 'V_141',
               particles = [ P.d__tilde__, P.u, P.G__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_186,(0,1):C.GC_156})

V_142 = Vertex(name = 'V_142',
               particles = [ P.s__tilde__, P.u, P.G__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_187,(0,1):C.GC_169})

V_143 = Vertex(name = 'V_143',
               particles = [ P.c__tilde__, P.c, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_152,(0,1):C.GC_150})

V_144 = Vertex(name = 'V_144',
               particles = [ P.c__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_151,(0,1):C.GC_151})

V_145 = Vertex(name = 'V_145',
               particles = [ P.t__tilde__, P.t, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_174,(0,1):C.GC_172})

V_146 = Vertex(name = 'V_146',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_173,(0,1):C.GC_173})

V_147 = Vertex(name = 'V_147',
               particles = [ P.u__tilde__, P.u, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_185,(0,1):C.GC_183})

V_148 = Vertex(name = 'V_148',
               particles = [ P.u__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_184,(0,1):C.GC_184})

V_149 = Vertex(name = 'V_149',
               particles = [ P.u__tilde__, P.d, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_192,(0,1):C.GC_193})

V_150 = Vertex(name = 'V_150',
               particles = [ P.b__tilde__, P.d, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_240,(0,1):C.GC_234})

V_151 = Vertex(name = 'V_151',
               particles = [ P.b__tilde__, P.d, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_241,(0,1):C.GC_233})

V_152 = Vertex(name = 'V_152',
               particles = [ P.d__tilde__, P.d, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_235,(0,1):C.GC_237})

V_153 = Vertex(name = 'V_153',
               particles = [ P.d__tilde__, P.d, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_236,(0,1):C.GC_236})

V_154 = Vertex(name = 'V_154',
               particles = [ P.s__tilde__, P.d, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_238,(0,1):C.GC_243})

V_155 = Vertex(name = 'V_155',
               particles = [ P.s__tilde__, P.d, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_239,(0,1):C.GC_242})

V_156 = Vertex(name = 'V_156',
               particles = [ P.c__tilde__, P.d, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_208,(0,1):C.GC_207})

V_157 = Vertex(name = 'V_157',
               particles = [ P.t__tilde__, P.d, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_222,(0,1):C.GC_223})

V_158 = Vertex(name = 'V_158',
               particles = [ P.u__tilde__, P.s, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_197,(0,1):C.GC_198})

V_159 = Vertex(name = 'V_159',
               particles = [ P.b__tilde__, P.s, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_267,(0,1):C.GC_259})

V_160 = Vertex(name = 'V_160',
               particles = [ P.b__tilde__, P.s, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_268,(0,1):C.GC_258})

V_161 = Vertex(name = 'V_161',
               particles = [ P.d__tilde__, P.s, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_262,(0,1):C.GC_261})

V_162 = Vertex(name = 'V_162',
               particles = [ P.d__tilde__, P.s, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_263,(0,1):C.GC_260})

V_163 = Vertex(name = 'V_163',
               particles = [ P.s__tilde__, P.s, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_264,(0,1):C.GC_266})

V_164 = Vertex(name = 'V_164',
               particles = [ P.s__tilde__, P.s, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_265,(0,1):C.GC_265})

V_165 = Vertex(name = 'V_165',
               particles = [ P.c__tilde__, P.s, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_213,(0,1):C.GC_212})

V_166 = Vertex(name = 'V_166',
               particles = [ P.t__tilde__, P.s, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_247,(0,1):C.GC_248})

V_167 = Vertex(name = 'V_167',
               particles = [ P.u__tilde__, P.b, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_202,(0,1):C.GC_203})

V_168 = Vertex(name = 'V_168',
               particles = [ P.b__tilde__, P.b, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_287,(0,1):C.GC_289})

V_169 = Vertex(name = 'V_169',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_288,(0,1):C.GC_288})

V_170 = Vertex(name = 'V_170',
               particles = [ P.d__tilde__, P.b, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_283,(0,1):C.GC_291})

V_171 = Vertex(name = 'V_171',
               particles = [ P.d__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_284,(0,1):C.GC_290})

V_172 = Vertex(name = 'V_172',
               particles = [ P.s__tilde__, P.b, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_285,(0,1):C.GC_293})

V_173 = Vertex(name = 'V_173',
               particles = [ P.s__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_286,(0,1):C.GC_292})

V_174 = Vertex(name = 'V_174',
               particles = [ P.c__tilde__, P.b, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_217,(0,1):C.GC_218})

V_175 = Vertex(name = 'V_175',
               particles = [ P.t__tilde__, P.b, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_272,(0,1):C.GC_273})

V_176 = Vertex(name = 'V_176',
               particles = [ P.ve__tilde__, P.e__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_160})

V_177 = Vertex(name = 'V_177',
               particles = [ P.e__plus__, P.e__minus__, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_161,(0,1):C.GC_163})

V_178 = Vertex(name = 'V_178',
               particles = [ P.e__plus__, P.e__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_162,(0,1):C.GC_162})

V_179 = Vertex(name = 'V_179',
               particles = [ P.vm__tilde__, P.mu__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_165})

V_180 = Vertex(name = 'V_180',
               particles = [ P.mu__plus__, P.mu__minus__, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_166,(0,1):C.GC_168})

V_181 = Vertex(name = 'V_181',
               particles = [ P.mu__plus__, P.mu__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_167,(0,1):C.GC_167})

V_182 = Vertex(name = 'V_182',
               particles = [ P.vt__tilde__, P.ta__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_179})

V_183 = Vertex(name = 'V_183',
               particles = [ P.ta__plus__, P.ta__minus__, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_180,(0,1):C.GC_182})

V_184 = Vertex(name = 'V_184',
               particles = [ P.ta__plus__, P.ta__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_181,(0,1):C.GC_181})

V_185 = Vertex(name = 'V_185',
               particles = [ P.Xd__tilde__, P.e__minus__, P.YS1e1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_49})

V_186 = Vertex(name = 'V_186',
               particles = [ P.Xd__tilde__, P.mu__minus__, P.YS1e2__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_50})

V_187 = Vertex(name = 'V_187',
               particles = [ P.Xd__tilde__, P.ta__minus__, P.YS1e3__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_51})

V_188 = Vertex(name = 'V_188',
               particles = [ P.Xm, P.e__minus__, P.YS1e1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_49})

V_189 = Vertex(name = 'V_189',
               particles = [ P.Xm, P.mu__minus__, P.YS1e2__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_50})

V_190 = Vertex(name = 'V_190',
               particles = [ P.Xm, P.ta__minus__, P.YS1e3__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_51})

V_191 = Vertex(name = 'V_191',
               particles = [ P.e__plus__, P.YF1e1, P.Xc__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_25})

V_192 = Vertex(name = 'V_192',
               particles = [ P.mu__plus__, P.YF1e2, P.Xc__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_26})

V_193 = Vertex(name = 'V_193',
               particles = [ P.ta__plus__, P.YF1e3, P.Xc__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_27})

V_194 = Vertex(name = 'V_194',
               particles = [ P.e__plus__, P.YF1e1, P.Xs ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_25})

V_195 = Vertex(name = 'V_195',
               particles = [ P.mu__plus__, P.YF1e2, P.Xs ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_26})

V_196 = Vertex(name = 'V_196',
               particles = [ P.ta__plus__, P.YF1e3, P.Xs ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_27})

V_197 = Vertex(name = 'V_197',
               particles = [ P.d__tilde__, P.YF3d1, P.Xc__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_31})

V_198 = Vertex(name = 'V_198',
               particles = [ P.s__tilde__, P.YF3d2, P.Xc__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_32})

V_199 = Vertex(name = 'V_199',
               particles = [ P.b__tilde__, P.YF3d3, P.Xc__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_33})

V_200 = Vertex(name = 'V_200',
               particles = [ P.d__tilde__, P.YF3d1, P.Xs ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_31})

V_201 = Vertex(name = 'V_201',
               particles = [ P.s__tilde__, P.YF3d2, P.Xs ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_32})

V_202 = Vertex(name = 'V_202',
               particles = [ P.b__tilde__, P.YF3d3, P.Xs ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_33})

V_203 = Vertex(name = 'V_203',
               particles = [ P.u__tilde__, P.YF3u1, P.Xc__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_46})

V_204 = Vertex(name = 'V_204',
               particles = [ P.c__tilde__, P.YF3u2, P.Xc__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_47})

V_205 = Vertex(name = 'V_205',
               particles = [ P.t__tilde__, P.YF3u3, P.Xc__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_48})

V_206 = Vertex(name = 'V_206',
               particles = [ P.u__tilde__, P.YF3u1, P.Xs ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_46})

V_207 = Vertex(name = 'V_207',
               particles = [ P.c__tilde__, P.YF3u2, P.Xs ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_47})

V_208 = Vertex(name = 'V_208',
               particles = [ P.t__tilde__, P.YF3u3, P.Xs ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_48})

V_209 = Vertex(name = 'V_209',
               particles = [ P.e__plus__, P.Xd, P.YS1e1 ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_49})

V_210 = Vertex(name = 'V_210',
               particles = [ P.mu__plus__, P.Xd, P.YS1e2 ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_50})

V_211 = Vertex(name = 'V_211',
               particles = [ P.ta__plus__, P.Xd, P.YS1e3 ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_51})

V_212 = Vertex(name = 'V_212',
               particles = [ P.e__plus__, P.Xm, P.YS1e1 ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_49})

V_213 = Vertex(name = 'V_213',
               particles = [ P.mu__plus__, P.Xm, P.YS1e2 ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_50})

V_214 = Vertex(name = 'V_214',
               particles = [ P.ta__plus__, P.Xm, P.YS1e3 ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_51})

V_215 = Vertex(name = 'V_215',
               particles = [ P.YF1Lv1__tilde__, P.ve, P.Xc ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_28})

V_216 = Vertex(name = 'V_216',
               particles = [ P.YF1Lv1__tilde__, P.ve, P.Xs ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_28})

V_217 = Vertex(name = 'V_217',
               particles = [ P.YF1Le1__tilde__, P.e__minus__, P.Xc ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_28})

V_218 = Vertex(name = 'V_218',
               particles = [ P.YF1Le1__tilde__, P.e__minus__, P.Xs ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_28})

V_219 = Vertex(name = 'V_219',
               particles = [ P.YF1Lv2__tilde__, P.vm, P.Xc ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_29})

V_220 = Vertex(name = 'V_220',
               particles = [ P.YF1Lv2__tilde__, P.vm, P.Xs ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_29})

V_221 = Vertex(name = 'V_221',
               particles = [ P.YF1Le2__tilde__, P.mu__minus__, P.Xc ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_29})

V_222 = Vertex(name = 'V_222',
               particles = [ P.YF1Le2__tilde__, P.mu__minus__, P.Xs ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_29})

V_223 = Vertex(name = 'V_223',
               particles = [ P.YF1Lv3__tilde__, P.vt, P.Xc ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_30})

V_224 = Vertex(name = 'V_224',
               particles = [ P.YF1Lv3__tilde__, P.vt, P.Xs ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_30})

V_225 = Vertex(name = 'V_225',
               particles = [ P.YF1Le3__tilde__, P.ta__minus__, P.Xc ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_30})

V_226 = Vertex(name = 'V_226',
               particles = [ P.YF1Le3__tilde__, P.ta__minus__, P.Xs ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_30})

V_227 = Vertex(name = 'V_227',
               particles = [ P.YF3Qu1__tilde__, P.u, P.Xc ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_34})

V_228 = Vertex(name = 'V_228',
               particles = [ P.YF3Qu1__tilde__, P.u, P.Xs ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_34})

V_229 = Vertex(name = 'V_229',
               particles = [ P.YF3Qd1__tilde__, P.b, P.Xc ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_199})

V_230 = Vertex(name = 'V_230',
               particles = [ P.YF3Qd1__tilde__, P.d, P.Xc ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_189})

V_231 = Vertex(name = 'V_231',
               particles = [ P.YF3Qd1__tilde__, P.s, P.Xc ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_194})

V_232 = Vertex(name = 'V_232',
               particles = [ P.YF3Qd1__tilde__, P.b, P.Xs ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_199})

V_233 = Vertex(name = 'V_233',
               particles = [ P.YF3Qd1__tilde__, P.d, P.Xs ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_189})

V_234 = Vertex(name = 'V_234',
               particles = [ P.YF3Qd1__tilde__, P.s, P.Xs ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_194})

V_235 = Vertex(name = 'V_235',
               particles = [ P.YF3Qu2__tilde__, P.c, P.Xc ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_38})

V_236 = Vertex(name = 'V_236',
               particles = [ P.YF3Qu2__tilde__, P.c, P.Xs ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_38})

V_237 = Vertex(name = 'V_237',
               particles = [ P.YF3Qd2__tilde__, P.b, P.Xc ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_214})

V_238 = Vertex(name = 'V_238',
               particles = [ P.YF3Qd2__tilde__, P.d, P.Xc ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_204})

V_239 = Vertex(name = 'V_239',
               particles = [ P.YF3Qd2__tilde__, P.s, P.Xc ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_209})

V_240 = Vertex(name = 'V_240',
               particles = [ P.YF3Qd2__tilde__, P.b, P.Xs ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_214})

V_241 = Vertex(name = 'V_241',
               particles = [ P.YF3Qd2__tilde__, P.d, P.Xs ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_204})

V_242 = Vertex(name = 'V_242',
               particles = [ P.YF3Qd2__tilde__, P.s, P.Xs ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_209})

V_243 = Vertex(name = 'V_243',
               particles = [ P.YF3Qu3__tilde__, P.t, P.Xc ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_42})

V_244 = Vertex(name = 'V_244',
               particles = [ P.YF3Qu3__tilde__, P.t, P.Xs ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_42})

V_245 = Vertex(name = 'V_245',
               particles = [ P.YF3Qd3__tilde__, P.b, P.Xc ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_269})

V_246 = Vertex(name = 'V_246',
               particles = [ P.YF3Qd3__tilde__, P.d, P.Xc ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_219})

V_247 = Vertex(name = 'V_247',
               particles = [ P.YF3Qd3__tilde__, P.s, P.Xc ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_244})

V_248 = Vertex(name = 'V_248',
               particles = [ P.YF3Qd3__tilde__, P.b, P.Xs ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_269})

V_249 = Vertex(name = 'V_249',
               particles = [ P.YF3Qd3__tilde__, P.d, P.Xs ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_219})

V_250 = Vertex(name = 'V_250',
               particles = [ P.YF3Qd3__tilde__, P.s, P.Xs ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_244})

V_251 = Vertex(name = 'V_251',
               particles = [ P.Xd__tilde__, P.ve, P.YS1Lv1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_52})

V_252 = Vertex(name = 'V_252',
               particles = [ P.Xm, P.ve, P.YS1Lv1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_52})

V_253 = Vertex(name = 'V_253',
               particles = [ P.Xd__tilde__, P.vm, P.YS1Lv2__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_53})

V_254 = Vertex(name = 'V_254',
               particles = [ P.Xm, P.vm, P.YS1Lv2__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_53})

V_255 = Vertex(name = 'V_255',
               particles = [ P.Xd__tilde__, P.vt, P.YS1Lv3__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_54})

V_256 = Vertex(name = 'V_256',
               particles = [ P.Xm, P.vt, P.YS1Lv3__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_54})

V_257 = Vertex(name = 'V_257',
               particles = [ P.Xd__tilde__, P.e__minus__, P.YS1Le1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_52})

V_258 = Vertex(name = 'V_258',
               particles = [ P.Xm, P.e__minus__, P.YS1Le1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_52})

V_259 = Vertex(name = 'V_259',
               particles = [ P.Xd__tilde__, P.mu__minus__, P.YS1Le2__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_53})

V_260 = Vertex(name = 'V_260',
               particles = [ P.Xm, P.mu__minus__, P.YS1Le2__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_53})

V_261 = Vertex(name = 'V_261',
               particles = [ P.Xd__tilde__, P.ta__minus__, P.YS1Le3__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_54})

V_262 = Vertex(name = 'V_262',
               particles = [ P.Xm, P.ta__minus__, P.YS1Le3__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_54})

V_263 = Vertex(name = 'V_263',
               particles = [ P.YF3Qd1__tilde__, P.YF3Qd1, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_18})

V_264 = Vertex(name = 'V_264',
               particles = [ P.YF3Qd2__tilde__, P.YF3Qd2, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_18})

V_265 = Vertex(name = 'V_265',
               particles = [ P.YF3Qd3__tilde__, P.YF3Qd3, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_18})

V_266 = Vertex(name = 'V_266',
               particles = [ P.YF3Qu1__tilde__, P.YF3Qu1, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_18})

V_267 = Vertex(name = 'V_267',
               particles = [ P.YF3Qu2__tilde__, P.YF3Qu2, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_18})

V_268 = Vertex(name = 'V_268',
               particles = [ P.YF3Qu3__tilde__, P.YF3Qu3, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_18})

V_269 = Vertex(name = 'V_269',
               particles = [ P.YF3u1__tilde__, P.YF3u1, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_18})

V_270 = Vertex(name = 'V_270',
               particles = [ P.YF3u2__tilde__, P.YF3u2, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_18})

V_271 = Vertex(name = 'V_271',
               particles = [ P.YF3u3__tilde__, P.YF3u3, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_18})

V_272 = Vertex(name = 'V_272',
               particles = [ P.YF3d1__tilde__, P.YF3d1, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_18})

V_273 = Vertex(name = 'V_273',
               particles = [ P.YF3d2__tilde__, P.YF3d2, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_18})

V_274 = Vertex(name = 'V_274',
               particles = [ P.YF3d3__tilde__, P.YF3d3, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_18})

V_275 = Vertex(name = 'V_275',
               particles = [ P.a, P.W__minus__, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_93})

V_276 = Vertex(name = 'V_276',
               particles = [ P.a, P.W__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_92})

V_277 = Vertex(name = 'V_277',
               particles = [ P.a, P.W__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_139})

V_278 = Vertex(name = 'V_278',
               particles = [ P.a, P.W__minus__, P.YS1Le1__tilde__, P.YS1Lv1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_96})

V_279 = Vertex(name = 'V_279',
               particles = [ P.a, P.W__minus__, P.YS1Le2__tilde__, P.YS1Lv2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_96})

V_280 = Vertex(name = 'V_280',
               particles = [ P.a, P.W__minus__, P.YS1Le3__tilde__, P.YS1Lv3 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_96})

V_281 = Vertex(name = 'V_281',
               particles = [ P.W__minus__, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_78})

V_282 = Vertex(name = 'V_282',
               particles = [ P.W__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_76})

V_283 = Vertex(name = 'V_283',
               particles = [ P.W__minus__, P.YS1Le1__tilde__, P.YS1Lv1 ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_79})

V_284 = Vertex(name = 'V_284',
               particles = [ P.W__minus__, P.YS1Le2__tilde__, P.YS1Lv2 ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_79})

V_285 = Vertex(name = 'V_285',
               particles = [ P.W__minus__, P.YS1Le3__tilde__, P.YS1Lv3 ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_79})

V_286 = Vertex(name = 'V_286',
               particles = [ P.a, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_6})

V_287 = Vertex(name = 'V_287',
               particles = [ P.YF3Qd1__tilde__, P.YF3Qu1, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_80})

V_288 = Vertex(name = 'V_288',
               particles = [ P.YF3Qd2__tilde__, P.YF3Qu2, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_80})

V_289 = Vertex(name = 'V_289',
               particles = [ P.YF3Qd3__tilde__, P.YF3Qu3, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_80})

V_290 = Vertex(name = 'V_290',
               particles = [ P.YF1Le1__tilde__, P.YF1Lv1, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_80})

V_291 = Vertex(name = 'V_291',
               particles = [ P.YF1Le2__tilde__, P.YF1Lv2, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_80})

V_292 = Vertex(name = 'V_292',
               particles = [ P.YF1Le3__tilde__, P.YF1Lv3, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_80})

V_293 = Vertex(name = 'V_293',
               particles = [ P.a, P.W__plus__, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_93})

V_294 = Vertex(name = 'V_294',
               particles = [ P.a, P.W__plus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_94})

V_295 = Vertex(name = 'V_295',
               particles = [ P.a, P.W__plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_140})

V_296 = Vertex(name = 'V_296',
               particles = [ P.a, P.W__plus__, P.YS1Le1, P.YS1Lv1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_96})

V_297 = Vertex(name = 'V_297',
               particles = [ P.a, P.W__plus__, P.YS1Le2, P.YS1Lv2__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_96})

V_298 = Vertex(name = 'V_298',
               particles = [ P.a, P.W__plus__, P.YS1Le3, P.YS1Lv3__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_96})

V_299 = Vertex(name = 'V_299',
               particles = [ P.W__plus__, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_77})

V_300 = Vertex(name = 'V_300',
               particles = [ P.W__plus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_76})

V_301 = Vertex(name = 'V_301',
               particles = [ P.W__plus__, P.YS1Le1, P.YS1Lv1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_80})

V_302 = Vertex(name = 'V_302',
               particles = [ P.W__plus__, P.YS1Le2, P.YS1Lv2__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_80})

V_303 = Vertex(name = 'V_303',
               particles = [ P.W__plus__, P.YS1Le3, P.YS1Lv3__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_80})

V_304 = Vertex(name = 'V_304',
               particles = [ P.YF3Qu1__tilde__, P.YF3Qd1, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_80})

V_305 = Vertex(name = 'V_305',
               particles = [ P.YF3Qu2__tilde__, P.YF3Qd2, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_80})

V_306 = Vertex(name = 'V_306',
               particles = [ P.YF3Qu3__tilde__, P.YF3Qd3, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_80})

V_307 = Vertex(name = 'V_307',
               particles = [ P.YF1Lv1__tilde__, P.YF1Le1, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_80})

V_308 = Vertex(name = 'V_308',
               particles = [ P.YF1Lv2__tilde__, P.YF1Le2, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_80})

V_309 = Vertex(name = 'V_309',
               particles = [ P.YF1Lv3__tilde__, P.YF1Le3, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_80})

V_310 = Vertex(name = 'V_310',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_73})

V_311 = Vertex(name = 'V_311',
               particles = [ P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_73})

V_312 = Vertex(name = 'V_312',
               particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_73})

V_313 = Vertex(name = 'V_313',
               particles = [ P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_137})

V_314 = Vertex(name = 'V_314',
               particles = [ P.W__minus__, P.W__plus__, P.YS1Le1__tilde__, P.YS1Le1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_73})

V_315 = Vertex(name = 'V_315',
               particles = [ P.W__minus__, P.W__plus__, P.YS1Le2__tilde__, P.YS1Le2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_73})

V_316 = Vertex(name = 'V_316',
               particles = [ P.W__minus__, P.W__plus__, P.YS1Le3__tilde__, P.YS1Le3 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_73})

V_317 = Vertex(name = 'V_317',
               particles = [ P.W__minus__, P.W__plus__, P.YS1Lv1__tilde__, P.YS1Lv1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_73})

V_318 = Vertex(name = 'V_318',
               particles = [ P.W__minus__, P.W__plus__, P.YS1Lv2__tilde__, P.YS1Lv2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_73})

V_319 = Vertex(name = 'V_319',
               particles = [ P.W__minus__, P.W__plus__, P.YS1Lv3__tilde__, P.YS1Lv3 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_73})

V_320 = Vertex(name = 'V_320',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_9})

V_321 = Vertex(name = 'V_321',
               particles = [ P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_91})

V_322 = Vertex(name = 'V_322',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_74})

V_323 = Vertex(name = 'V_323',
               particles = [ P.e__plus__, P.ve, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_159})

V_324 = Vertex(name = 'V_324',
               particles = [ P.mu__plus__, P.vm, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_164})

V_325 = Vertex(name = 'V_325',
               particles = [ P.ta__plus__, P.vt, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_178})

V_326 = Vertex(name = 'V_326',
               particles = [ P.a, P.YS3d1__tilde__, P.YS3d1 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_2})

V_327 = Vertex(name = 'V_327',
               particles = [ P.Xd__tilde__, P.d, P.YS3d1__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_55})

V_328 = Vertex(name = 'V_328',
               particles = [ P.Xm, P.d, P.YS3d1__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_55})

V_329 = Vertex(name = 'V_329',
               particles = [ P.g, P.YS3d1__tilde__, P.YS3d1 ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_17})

V_330 = Vertex(name = 'V_330',
               particles = [ P.d__tilde__, P.Xd, P.YS3d1 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_55})

V_331 = Vertex(name = 'V_331',
               particles = [ P.d__tilde__, P.Xm, P.YS3d1 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_55})

V_332 = Vertex(name = 'V_332',
               particles = [ P.a, P.a, P.YS3d1__tilde__, P.YS3d1 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_7})

V_333 = Vertex(name = 'V_333',
               particles = [ P.a, P.g, P.YS3d1__tilde__, P.YS3d1 ],
               color = [ 'T(2,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_19})

V_334 = Vertex(name = 'V_334',
               particles = [ P.g, P.g, P.YS3d1__tilde__, P.YS3d1 ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(1,0):C.GC_21,(0,0):C.GC_21})

V_335 = Vertex(name = 'V_335',
               particles = [ P.a, P.YS3d2__tilde__, P.YS3d2 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_2})

V_336 = Vertex(name = 'V_336',
               particles = [ P.Xd__tilde__, P.s, P.YS3d2__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_56})

V_337 = Vertex(name = 'V_337',
               particles = [ P.Xm, P.s, P.YS3d2__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_56})

V_338 = Vertex(name = 'V_338',
               particles = [ P.g, P.YS3d2__tilde__, P.YS3d2 ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_17})

V_339 = Vertex(name = 'V_339',
               particles = [ P.s__tilde__, P.Xd, P.YS3d2 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_56})

V_340 = Vertex(name = 'V_340',
               particles = [ P.s__tilde__, P.Xm, P.YS3d2 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_56})

V_341 = Vertex(name = 'V_341',
               particles = [ P.a, P.a, P.YS3d2__tilde__, P.YS3d2 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_7})

V_342 = Vertex(name = 'V_342',
               particles = [ P.a, P.g, P.YS3d2__tilde__, P.YS3d2 ],
               color = [ 'T(2,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_19})

V_343 = Vertex(name = 'V_343',
               particles = [ P.g, P.g, P.YS3d2__tilde__, P.YS3d2 ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(1,0):C.GC_21,(0,0):C.GC_21})

V_344 = Vertex(name = 'V_344',
               particles = [ P.a, P.YS3d3__tilde__, P.YS3d3 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_2})

V_345 = Vertex(name = 'V_345',
               particles = [ P.Xd__tilde__, P.b, P.YS3d3__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_57})

V_346 = Vertex(name = 'V_346',
               particles = [ P.Xm, P.b, P.YS3d3__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_57})

V_347 = Vertex(name = 'V_347',
               particles = [ P.g, P.YS3d3__tilde__, P.YS3d3 ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_17})

V_348 = Vertex(name = 'V_348',
               particles = [ P.b__tilde__, P.Xd, P.YS3d3 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_57})

V_349 = Vertex(name = 'V_349',
               particles = [ P.b__tilde__, P.Xm, P.YS3d3 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_57})

V_350 = Vertex(name = 'V_350',
               particles = [ P.a, P.a, P.YS3d3__tilde__, P.YS3d3 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_7})

V_351 = Vertex(name = 'V_351',
               particles = [ P.a, P.g, P.YS3d3__tilde__, P.YS3d3 ],
               color = [ 'T(2,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_19})

V_352 = Vertex(name = 'V_352',
               particles = [ P.g, P.g, P.YS3d3__tilde__, P.YS3d3 ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(1,0):C.GC_21,(0,0):C.GC_21})

V_353 = Vertex(name = 'V_353',
               particles = [ P.a, P.YS3Qd1__tilde__, P.YS3Qd1 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_2})

V_354 = Vertex(name = 'V_354',
               particles = [ P.Xd__tilde__, P.b, P.YS3Qd1__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_200})

V_355 = Vertex(name = 'V_355',
               particles = [ P.Xd__tilde__, P.d, P.YS3Qd1__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_190})

V_356 = Vertex(name = 'V_356',
               particles = [ P.Xd__tilde__, P.s, P.YS3Qd1__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_195})

V_357 = Vertex(name = 'V_357',
               particles = [ P.Xm, P.b, P.YS3Qd1__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_200})

V_358 = Vertex(name = 'V_358',
               particles = [ P.Xm, P.d, P.YS3Qd1__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_190})

V_359 = Vertex(name = 'V_359',
               particles = [ P.Xm, P.s, P.YS3Qd1__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_195})

V_360 = Vertex(name = 'V_360',
               particles = [ P.W__minus__, P.YS3Qd1__tilde__, P.YS3Qu1 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_79})

V_361 = Vertex(name = 'V_361',
               particles = [ P.g, P.YS3Qd1__tilde__, P.YS3Qd1 ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_17})

V_362 = Vertex(name = 'V_362',
               particles = [ P.b__tilde__, P.Xd, P.YS3Qd1 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_61})

V_363 = Vertex(name = 'V_363',
               particles = [ P.d__tilde__, P.Xd, P.YS3Qd1 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_59})

V_364 = Vertex(name = 'V_364',
               particles = [ P.s__tilde__, P.Xd, P.YS3Qd1 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_60})

V_365 = Vertex(name = 'V_365',
               particles = [ P.b__tilde__, P.Xm, P.YS3Qd1 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_61})

V_366 = Vertex(name = 'V_366',
               particles = [ P.d__tilde__, P.Xm, P.YS3Qd1 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_59})

V_367 = Vertex(name = 'V_367',
               particles = [ P.s__tilde__, P.Xm, P.YS3Qd1 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_60})

V_368 = Vertex(name = 'V_368',
               particles = [ P.W__plus__, P.YS3Qd1, P.YS3Qu1__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_80})

V_369 = Vertex(name = 'V_369',
               particles = [ P.a, P.a, P.YS3Qd1__tilde__, P.YS3Qd1 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_7})

V_370 = Vertex(name = 'V_370',
               particles = [ P.W__minus__, P.W__plus__, P.YS3Qd1__tilde__, P.YS3Qd1 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_73})

V_371 = Vertex(name = 'V_371',
               particles = [ P.a, P.g, P.YS3Qd1__tilde__, P.YS3Qd1 ],
               color = [ 'T(2,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_19})

V_372 = Vertex(name = 'V_372',
               particles = [ P.g, P.g, P.YS3Qd1__tilde__, P.YS3Qd1 ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(1,0):C.GC_21,(0,0):C.GC_21})

V_373 = Vertex(name = 'V_373',
               particles = [ P.a, P.YS3Qd2__tilde__, P.YS3Qd2 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_2})

V_374 = Vertex(name = 'V_374',
               particles = [ P.Xd__tilde__, P.b, P.YS3Qd2__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_215})

V_375 = Vertex(name = 'V_375',
               particles = [ P.Xd__tilde__, P.d, P.YS3Qd2__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_205})

V_376 = Vertex(name = 'V_376',
               particles = [ P.Xd__tilde__, P.s, P.YS3Qd2__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_210})

V_377 = Vertex(name = 'V_377',
               particles = [ P.Xm, P.b, P.YS3Qd2__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_215})

V_378 = Vertex(name = 'V_378',
               particles = [ P.Xm, P.d, P.YS3Qd2__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_205})

V_379 = Vertex(name = 'V_379',
               particles = [ P.Xm, P.s, P.YS3Qd2__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_210})

V_380 = Vertex(name = 'V_380',
               particles = [ P.W__minus__, P.YS3Qd2__tilde__, P.YS3Qu2 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_79})

V_381 = Vertex(name = 'V_381',
               particles = [ P.g, P.YS3Qd2__tilde__, P.YS3Qd2 ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_17})

V_382 = Vertex(name = 'V_382',
               particles = [ P.b__tilde__, P.Xd, P.YS3Qd2 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_65})

V_383 = Vertex(name = 'V_383',
               particles = [ P.d__tilde__, P.Xd, P.YS3Qd2 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_63})

V_384 = Vertex(name = 'V_384',
               particles = [ P.s__tilde__, P.Xd, P.YS3Qd2 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_64})

V_385 = Vertex(name = 'V_385',
               particles = [ P.b__tilde__, P.Xm, P.YS3Qd2 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_65})

V_386 = Vertex(name = 'V_386',
               particles = [ P.d__tilde__, P.Xm, P.YS3Qd2 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_63})

V_387 = Vertex(name = 'V_387',
               particles = [ P.s__tilde__, P.Xm, P.YS3Qd2 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_64})

V_388 = Vertex(name = 'V_388',
               particles = [ P.W__plus__, P.YS3Qd2, P.YS3Qu2__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_80})

V_389 = Vertex(name = 'V_389',
               particles = [ P.a, P.a, P.YS3Qd2__tilde__, P.YS3Qd2 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_7})

V_390 = Vertex(name = 'V_390',
               particles = [ P.W__minus__, P.W__plus__, P.YS3Qd2__tilde__, P.YS3Qd2 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_73})

V_391 = Vertex(name = 'V_391',
               particles = [ P.a, P.g, P.YS3Qd2__tilde__, P.YS3Qd2 ],
               color = [ 'T(2,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_19})

V_392 = Vertex(name = 'V_392',
               particles = [ P.g, P.g, P.YS3Qd2__tilde__, P.YS3Qd2 ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(1,0):C.GC_21,(0,0):C.GC_21})

V_393 = Vertex(name = 'V_393',
               particles = [ P.a, P.YS3Qd3__tilde__, P.YS3Qd3 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_2})

V_394 = Vertex(name = 'V_394',
               particles = [ P.Xd__tilde__, P.b, P.YS3Qd3__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_270})

V_395 = Vertex(name = 'V_395',
               particles = [ P.Xd__tilde__, P.d, P.YS3Qd3__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_220})

V_396 = Vertex(name = 'V_396',
               particles = [ P.Xd__tilde__, P.s, P.YS3Qd3__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_245})

V_397 = Vertex(name = 'V_397',
               particles = [ P.Xm, P.b, P.YS3Qd3__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_270})

V_398 = Vertex(name = 'V_398',
               particles = [ P.Xm, P.d, P.YS3Qd3__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_220})

V_399 = Vertex(name = 'V_399',
               particles = [ P.Xm, P.s, P.YS3Qd3__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_245})

V_400 = Vertex(name = 'V_400',
               particles = [ P.W__minus__, P.YS3Qd3__tilde__, P.YS3Qu3 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_79})

V_401 = Vertex(name = 'V_401',
               particles = [ P.g, P.YS3Qd3__tilde__, P.YS3Qd3 ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_17})

V_402 = Vertex(name = 'V_402',
               particles = [ P.b__tilde__, P.Xd, P.YS3Qd3 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_69})

V_403 = Vertex(name = 'V_403',
               particles = [ P.d__tilde__, P.Xd, P.YS3Qd3 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_67})

V_404 = Vertex(name = 'V_404',
               particles = [ P.s__tilde__, P.Xd, P.YS3Qd3 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_68})

V_405 = Vertex(name = 'V_405',
               particles = [ P.b__tilde__, P.Xm, P.YS3Qd3 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_69})

V_406 = Vertex(name = 'V_406',
               particles = [ P.d__tilde__, P.Xm, P.YS3Qd3 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_67})

V_407 = Vertex(name = 'V_407',
               particles = [ P.s__tilde__, P.Xm, P.YS3Qd3 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_68})

V_408 = Vertex(name = 'V_408',
               particles = [ P.W__plus__, P.YS3Qd3, P.YS3Qu3__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_80})

V_409 = Vertex(name = 'V_409',
               particles = [ P.a, P.a, P.YS3Qd3__tilde__, P.YS3Qd3 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_7})

V_410 = Vertex(name = 'V_410',
               particles = [ P.W__minus__, P.W__plus__, P.YS3Qd3__tilde__, P.YS3Qd3 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_73})

V_411 = Vertex(name = 'V_411',
               particles = [ P.a, P.g, P.YS3Qd3__tilde__, P.YS3Qd3 ],
               color = [ 'T(2,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_19})

V_412 = Vertex(name = 'V_412',
               particles = [ P.g, P.g, P.YS3Qd3__tilde__, P.YS3Qd3 ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(1,0):C.GC_21,(0,0):C.GC_21})

V_413 = Vertex(name = 'V_413',
               particles = [ P.a, P.YS3Qu1__tilde__, P.YS3Qu1 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_3})

V_414 = Vertex(name = 'V_414',
               particles = [ P.Xd__tilde__, P.u, P.YS3Qu1__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_58})

V_415 = Vertex(name = 'V_415',
               particles = [ P.Xm, P.u, P.YS3Qu1__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_58})

V_416 = Vertex(name = 'V_416',
               particles = [ P.a, P.W__plus__, P.YS3Qd1, P.YS3Qu1__tilde__ ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_95})

V_417 = Vertex(name = 'V_417',
               particles = [ P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu1__tilde__ ],
               color = [ 'T(1,3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_98})

V_418 = Vertex(name = 'V_418',
               particles = [ P.g, P.YS3Qu1__tilde__, P.YS3Qu1 ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_17})

V_419 = Vertex(name = 'V_419',
               particles = [ P.u__tilde__, P.Xd, P.YS3Qu1 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_58})

V_420 = Vertex(name = 'V_420',
               particles = [ P.u__tilde__, P.Xm, P.YS3Qu1 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_58})

V_421 = Vertex(name = 'V_421',
               particles = [ P.a, P.W__minus__, P.YS3Qd1__tilde__, P.YS3Qu1 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_95})

V_422 = Vertex(name = 'V_422',
               particles = [ P.g, P.W__minus__, P.YS3Qd1__tilde__, P.YS3Qu1 ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_98})

V_423 = Vertex(name = 'V_423',
               particles = [ P.a, P.a, P.YS3Qu1__tilde__, P.YS3Qu1 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_8})

V_424 = Vertex(name = 'V_424',
               particles = [ P.W__minus__, P.W__plus__, P.YS3Qu1__tilde__, P.YS3Qu1 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_73})

V_425 = Vertex(name = 'V_425',
               particles = [ P.a, P.g, P.YS3Qu1__tilde__, P.YS3Qu1 ],
               color = [ 'T(2,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_20})

V_426 = Vertex(name = 'V_426',
               particles = [ P.g, P.g, P.YS3Qu1__tilde__, P.YS3Qu1 ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(1,0):C.GC_21,(0,0):C.GC_21})

V_427 = Vertex(name = 'V_427',
               particles = [ P.a, P.YS3Qu2__tilde__, P.YS3Qu2 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_3})

V_428 = Vertex(name = 'V_428',
               particles = [ P.Xd__tilde__, P.c, P.YS3Qu2__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_62})

V_429 = Vertex(name = 'V_429',
               particles = [ P.Xm, P.c, P.YS3Qu2__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_62})

V_430 = Vertex(name = 'V_430',
               particles = [ P.a, P.W__plus__, P.YS3Qd2, P.YS3Qu2__tilde__ ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_95})

V_431 = Vertex(name = 'V_431',
               particles = [ P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu2__tilde__ ],
               color = [ 'T(1,3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_98})

V_432 = Vertex(name = 'V_432',
               particles = [ P.g, P.YS3Qu2__tilde__, P.YS3Qu2 ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_17})

V_433 = Vertex(name = 'V_433',
               particles = [ P.c__tilde__, P.Xd, P.YS3Qu2 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_62})

V_434 = Vertex(name = 'V_434',
               particles = [ P.c__tilde__, P.Xm, P.YS3Qu2 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_62})

V_435 = Vertex(name = 'V_435',
               particles = [ P.a, P.W__minus__, P.YS3Qd2__tilde__, P.YS3Qu2 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_95})

V_436 = Vertex(name = 'V_436',
               particles = [ P.g, P.W__minus__, P.YS3Qd2__tilde__, P.YS3Qu2 ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_98})

V_437 = Vertex(name = 'V_437',
               particles = [ P.a, P.a, P.YS3Qu2__tilde__, P.YS3Qu2 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_8})

V_438 = Vertex(name = 'V_438',
               particles = [ P.W__minus__, P.W__plus__, P.YS3Qu2__tilde__, P.YS3Qu2 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_73})

V_439 = Vertex(name = 'V_439',
               particles = [ P.a, P.g, P.YS3Qu2__tilde__, P.YS3Qu2 ],
               color = [ 'T(2,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_20})

V_440 = Vertex(name = 'V_440',
               particles = [ P.g, P.g, P.YS3Qu2__tilde__, P.YS3Qu2 ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(1,0):C.GC_21,(0,0):C.GC_21})

V_441 = Vertex(name = 'V_441',
               particles = [ P.a, P.YS3Qu3__tilde__, P.YS3Qu3 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_3})

V_442 = Vertex(name = 'V_442',
               particles = [ P.Xd__tilde__, P.t, P.YS3Qu3__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_66})

V_443 = Vertex(name = 'V_443',
               particles = [ P.Xm, P.t, P.YS3Qu3__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_66})

V_444 = Vertex(name = 'V_444',
               particles = [ P.a, P.W__plus__, P.YS3Qd3, P.YS3Qu3__tilde__ ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_95})

V_445 = Vertex(name = 'V_445',
               particles = [ P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu3__tilde__ ],
               color = [ 'T(1,3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_98})

V_446 = Vertex(name = 'V_446',
               particles = [ P.g, P.YS3Qu3__tilde__, P.YS3Qu3 ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_17})

V_447 = Vertex(name = 'V_447',
               particles = [ P.t__tilde__, P.Xd, P.YS3Qu3 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_66})

V_448 = Vertex(name = 'V_448',
               particles = [ P.t__tilde__, P.Xm, P.YS3Qu3 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_66})

V_449 = Vertex(name = 'V_449',
               particles = [ P.a, P.W__minus__, P.YS3Qd3__tilde__, P.YS3Qu3 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_95})

V_450 = Vertex(name = 'V_450',
               particles = [ P.g, P.W__minus__, P.YS3Qd3__tilde__, P.YS3Qu3 ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_98})

V_451 = Vertex(name = 'V_451',
               particles = [ P.a, P.a, P.YS3Qu3__tilde__, P.YS3Qu3 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_8})

V_452 = Vertex(name = 'V_452',
               particles = [ P.W__minus__, P.W__plus__, P.YS3Qu3__tilde__, P.YS3Qu3 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_73})

V_453 = Vertex(name = 'V_453',
               particles = [ P.a, P.g, P.YS3Qu3__tilde__, P.YS3Qu3 ],
               color = [ 'T(2,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_20})

V_454 = Vertex(name = 'V_454',
               particles = [ P.g, P.g, P.YS3Qu3__tilde__, P.YS3Qu3 ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(1,0):C.GC_21,(0,0):C.GC_21})

V_455 = Vertex(name = 'V_455',
               particles = [ P.a, P.YS3u1__tilde__, P.YS3u1 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_3})

V_456 = Vertex(name = 'V_456',
               particles = [ P.Xd__tilde__, P.u, P.YS3u1__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_70})

V_457 = Vertex(name = 'V_457',
               particles = [ P.Xm, P.u, P.YS3u1__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_70})

V_458 = Vertex(name = 'V_458',
               particles = [ P.g, P.YS3u1__tilde__, P.YS3u1 ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_17})

V_459 = Vertex(name = 'V_459',
               particles = [ P.u__tilde__, P.Xd, P.YS3u1 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_70})

V_460 = Vertex(name = 'V_460',
               particles = [ P.u__tilde__, P.Xm, P.YS3u1 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_70})

V_461 = Vertex(name = 'V_461',
               particles = [ P.a, P.a, P.YS3u1__tilde__, P.YS3u1 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_8})

V_462 = Vertex(name = 'V_462',
               particles = [ P.a, P.g, P.YS3u1__tilde__, P.YS3u1 ],
               color = [ 'T(2,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_20})

V_463 = Vertex(name = 'V_463',
               particles = [ P.g, P.g, P.YS3u1__tilde__, P.YS3u1 ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(1,0):C.GC_21,(0,0):C.GC_21})

V_464 = Vertex(name = 'V_464',
               particles = [ P.a, P.YS3u2__tilde__, P.YS3u2 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_3})

V_465 = Vertex(name = 'V_465',
               particles = [ P.Xd__tilde__, P.c, P.YS3u2__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_71})

V_466 = Vertex(name = 'V_466',
               particles = [ P.Xm, P.c, P.YS3u2__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_71})

V_467 = Vertex(name = 'V_467',
               particles = [ P.g, P.YS3u2__tilde__, P.YS3u2 ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_17})

V_468 = Vertex(name = 'V_468',
               particles = [ P.c__tilde__, P.Xd, P.YS3u2 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_71})

V_469 = Vertex(name = 'V_469',
               particles = [ P.c__tilde__, P.Xm, P.YS3u2 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_71})

V_470 = Vertex(name = 'V_470',
               particles = [ P.a, P.a, P.YS3u2__tilde__, P.YS3u2 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_8})

V_471 = Vertex(name = 'V_471',
               particles = [ P.a, P.g, P.YS3u2__tilde__, P.YS3u2 ],
               color = [ 'T(2,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_20})

V_472 = Vertex(name = 'V_472',
               particles = [ P.g, P.g, P.YS3u2__tilde__, P.YS3u2 ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(1,0):C.GC_21,(0,0):C.GC_21})

V_473 = Vertex(name = 'V_473',
               particles = [ P.a, P.YS3u3__tilde__, P.YS3u3 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_3})

V_474 = Vertex(name = 'V_474',
               particles = [ P.Xd__tilde__, P.t, P.YS3u3__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_72})

V_475 = Vertex(name = 'V_475',
               particles = [ P.Xm, P.t, P.YS3u3__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_72})

V_476 = Vertex(name = 'V_476',
               particles = [ P.g, P.YS3u3__tilde__, P.YS3u3 ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_17})

V_477 = Vertex(name = 'V_477',
               particles = [ P.t__tilde__, P.Xd, P.YS3u3 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_72})

V_478 = Vertex(name = 'V_478',
               particles = [ P.t__tilde__, P.Xm, P.YS3u3 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_72})

V_479 = Vertex(name = 'V_479',
               particles = [ P.a, P.a, P.YS3u3__tilde__, P.YS3u3 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_8})

V_480 = Vertex(name = 'V_480',
               particles = [ P.a, P.g, P.YS3u3__tilde__, P.YS3u3 ],
               color = [ 'T(2,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_20})

V_481 = Vertex(name = 'V_481',
               particles = [ P.g, P.g, P.YS3u3__tilde__, P.YS3u3 ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(1,0):C.GC_21,(0,0):C.GC_21})

V_482 = Vertex(name = 'V_482',
               particles = [ P.a, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_124})

V_483 = Vertex(name = 'V_483',
               particles = [ P.a, P.Z, P.YS1e1__tilde__, P.YS1e1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_107})

V_484 = Vertex(name = 'V_484',
               particles = [ P.a, P.Z, P.YS1e2__tilde__, P.YS1e2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_107})

V_485 = Vertex(name = 'V_485',
               particles = [ P.a, P.Z, P.YS1e3__tilde__, P.YS1e3 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_107})

V_486 = Vertex(name = 'V_486',
               particles = [ P.a, P.Z, P.YS1Le1__tilde__, P.YS1Le1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_124})

V_487 = Vertex(name = 'V_487',
               particles = [ P.a, P.Z, P.YS1Le2__tilde__, P.YS1Le2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_124})

V_488 = Vertex(name = 'V_488',
               particles = [ P.a, P.Z, P.YS1Le3__tilde__, P.YS1Le3 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_124})

V_489 = Vertex(name = 'V_489',
               particles = [ P.Z, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_113})

V_490 = Vertex(name = 'V_490',
               particles = [ P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_120})

V_491 = Vertex(name = 'V_491',
               particles = [ P.Z, P.YS1e1__tilde__, P.YS1e1 ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_103})

V_492 = Vertex(name = 'V_492',
               particles = [ P.Z, P.YS1e2__tilde__, P.YS1e2 ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_103})

V_493 = Vertex(name = 'V_493',
               particles = [ P.Z, P.YS1e3__tilde__, P.YS1e3 ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_103})

V_494 = Vertex(name = 'V_494',
               particles = [ P.Z, P.YS1Le1__tilde__, P.YS1Le1 ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_119})

V_495 = Vertex(name = 'V_495',
               particles = [ P.Z, P.YS1Le2__tilde__, P.YS1Le2 ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_119})

V_496 = Vertex(name = 'V_496',
               particles = [ P.Z, P.YS1Le3__tilde__, P.YS1Le3 ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_119})

V_497 = Vertex(name = 'V_497',
               particles = [ P.Z, P.YS1Lv1__tilde__, P.YS1Lv1 ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_118})

V_498 = Vertex(name = 'V_498',
               particles = [ P.Z, P.YS1Lv2__tilde__, P.YS1Lv2 ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_118})

V_499 = Vertex(name = 'V_499',
               particles = [ P.Z, P.YS1Lv3__tilde__, P.YS1Lv3 ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_118})

V_500 = Vertex(name = 'V_500',
               particles = [ P.YF3Qd1__tilde__, P.YF3Qd1, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_114})

V_501 = Vertex(name = 'V_501',
               particles = [ P.YF3Qd2__tilde__, P.YF3Qd2, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_114})

V_502 = Vertex(name = 'V_502',
               particles = [ P.YF3Qd3__tilde__, P.YF3Qd3, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_114})

V_503 = Vertex(name = 'V_503',
               particles = [ P.YF3Qu1__tilde__, P.YF3Qu1, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_115})

V_504 = Vertex(name = 'V_504',
               particles = [ P.YF3Qu2__tilde__, P.YF3Qu2, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_115})

V_505 = Vertex(name = 'V_505',
               particles = [ P.YF3Qu3__tilde__, P.YF3Qu3, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_115})

V_506 = Vertex(name = 'V_506',
               particles = [ P.YF1Le1__tilde__, P.YF1Le1, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_120})

V_507 = Vertex(name = 'V_507',
               particles = [ P.YF1Le2__tilde__, P.YF1Le2, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_120})

V_508 = Vertex(name = 'V_508',
               particles = [ P.YF1Le3__tilde__, P.YF1Le3, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_120})

V_509 = Vertex(name = 'V_509',
               particles = [ P.YF1Lv1__tilde__, P.YF1Lv1, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_121})

V_510 = Vertex(name = 'V_510',
               particles = [ P.YF1Lv2__tilde__, P.YF1Lv2, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_121})

V_511 = Vertex(name = 'V_511',
               particles = [ P.YF1Lv3__tilde__, P.YF1Lv3, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_121})

V_512 = Vertex(name = 'V_512',
               particles = [ P.YF1e1__tilde__, P.YF1e1, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_104})

V_513 = Vertex(name = 'V_513',
               particles = [ P.YF1e2__tilde__, P.YF1e2, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_104})

V_514 = Vertex(name = 'V_514',
               particles = [ P.YF1e3__tilde__, P.YF1e3, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_104})

V_515 = Vertex(name = 'V_515',
               particles = [ P.YF3d1__tilde__, P.YF3d1, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_100})

V_516 = Vertex(name = 'V_516',
               particles = [ P.YF3d2__tilde__, P.YF3d2, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_100})

V_517 = Vertex(name = 'V_517',
               particles = [ P.YF3d3__tilde__, P.YF3d3, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_100})

V_518 = Vertex(name = 'V_518',
               particles = [ P.YF3u1__tilde__, P.YF3u1, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_101})

V_519 = Vertex(name = 'V_519',
               particles = [ P.YF3u2__tilde__, P.YF3u2, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_101})

V_520 = Vertex(name = 'V_520',
               particles = [ P.YF3u3__tilde__, P.YF3u3, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_101})

V_521 = Vertex(name = 'V_521',
               particles = [ P.W__minus__, P.Z, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_12})

V_522 = Vertex(name = 'V_522',
               particles = [ P.W__minus__, P.Z, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_13})

V_523 = Vertex(name = 'V_523',
               particles = [ P.W__minus__, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_132})

V_524 = Vertex(name = 'V_524',
               particles = [ P.W__minus__, P.Z, P.YS1Le1__tilde__, P.YS1Lv1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_15})

V_525 = Vertex(name = 'V_525',
               particles = [ P.W__minus__, P.Z, P.YS1Le2__tilde__, P.YS1Lv2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_15})

V_526 = Vertex(name = 'V_526',
               particles = [ P.W__minus__, P.Z, P.YS1Le3__tilde__, P.YS1Lv3 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_15})

V_527 = Vertex(name = 'V_527',
               particles = [ P.W__plus__, P.Z, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_12})

V_528 = Vertex(name = 'V_528',
               particles = [ P.W__plus__, P.Z, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_11})

V_529 = Vertex(name = 'V_529',
               particles = [ P.W__plus__, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_131})

V_530 = Vertex(name = 'V_530',
               particles = [ P.W__plus__, P.Z, P.YS1Le1, P.YS1Lv1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_15})

V_531 = Vertex(name = 'V_531',
               particles = [ P.W__plus__, P.Z, P.YS1Le2, P.YS1Lv2__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_15})

V_532 = Vertex(name = 'V_532',
               particles = [ P.W__plus__, P.Z, P.YS1Le3, P.YS1Lv3__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_15})

V_533 = Vertex(name = 'V_533',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV5 ],
               couplings = {(0,0):C.GC_97})

V_534 = Vertex(name = 'V_534',
               particles = [ P.Z, P.YS3d1__tilde__, P.YS3d1 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_99})

V_535 = Vertex(name = 'V_535',
               particles = [ P.a, P.Z, P.YS3d1__tilde__, P.YS3d1 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_105})

V_536 = Vertex(name = 'V_536',
               particles = [ P.g, P.Z, P.YS3d1__tilde__, P.YS3d1 ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_108})

V_537 = Vertex(name = 'V_537',
               particles = [ P.Z, P.YS3d2__tilde__, P.YS3d2 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_99})

V_538 = Vertex(name = 'V_538',
               particles = [ P.a, P.Z, P.YS3d2__tilde__, P.YS3d2 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_105})

V_539 = Vertex(name = 'V_539',
               particles = [ P.g, P.Z, P.YS3d2__tilde__, P.YS3d2 ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_108})

V_540 = Vertex(name = 'V_540',
               particles = [ P.Z, P.YS3d3__tilde__, P.YS3d3 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_99})

V_541 = Vertex(name = 'V_541',
               particles = [ P.a, P.Z, P.YS3d3__tilde__, P.YS3d3 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_105})

V_542 = Vertex(name = 'V_542',
               particles = [ P.g, P.Z, P.YS3d3__tilde__, P.YS3d3 ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_108})

V_543 = Vertex(name = 'V_543',
               particles = [ P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_117})

V_544 = Vertex(name = 'V_544',
               particles = [ P.a, P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_122})

V_545 = Vertex(name = 'V_545',
               particles = [ P.g, P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_125})

V_546 = Vertex(name = 'V_546',
               particles = [ P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_117})

V_547 = Vertex(name = 'V_547',
               particles = [ P.a, P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_122})

V_548 = Vertex(name = 'V_548',
               particles = [ P.g, P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_125})

V_549 = Vertex(name = 'V_549',
               particles = [ P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_117})

V_550 = Vertex(name = 'V_550',
               particles = [ P.a, P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_122})

V_551 = Vertex(name = 'V_551',
               particles = [ P.g, P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_125})

V_552 = Vertex(name = 'V_552',
               particles = [ P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_116})

V_553 = Vertex(name = 'V_553',
               particles = [ P.W__plus__, P.Z, P.YS3Qd1, P.YS3Qu1__tilde__ ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_14})

V_554 = Vertex(name = 'V_554',
               particles = [ P.W__minus__, P.Z, P.YS3Qd1__tilde__, P.YS3Qu1 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_14})

V_555 = Vertex(name = 'V_555',
               particles = [ P.a, P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_123})

V_556 = Vertex(name = 'V_556',
               particles = [ P.g, P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_126})

V_557 = Vertex(name = 'V_557',
               particles = [ P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_116})

V_558 = Vertex(name = 'V_558',
               particles = [ P.W__plus__, P.Z, P.YS3Qd2, P.YS3Qu2__tilde__ ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_14})

V_559 = Vertex(name = 'V_559',
               particles = [ P.W__minus__, P.Z, P.YS3Qd2__tilde__, P.YS3Qu2 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_14})

V_560 = Vertex(name = 'V_560',
               particles = [ P.a, P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_123})

V_561 = Vertex(name = 'V_561',
               particles = [ P.g, P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_126})

V_562 = Vertex(name = 'V_562',
               particles = [ P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_116})

V_563 = Vertex(name = 'V_563',
               particles = [ P.W__plus__, P.Z, P.YS3Qd3, P.YS3Qu3__tilde__ ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_14})

V_564 = Vertex(name = 'V_564',
               particles = [ P.W__minus__, P.Z, P.YS3Qd3__tilde__, P.YS3Qu3 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_14})

V_565 = Vertex(name = 'V_565',
               particles = [ P.a, P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_123})

V_566 = Vertex(name = 'V_566',
               particles = [ P.g, P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_126})

V_567 = Vertex(name = 'V_567',
               particles = [ P.Z, P.YS3u1__tilde__, P.YS3u1 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_102})

V_568 = Vertex(name = 'V_568',
               particles = [ P.a, P.Z, P.YS3u1__tilde__, P.YS3u1 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_106})

V_569 = Vertex(name = 'V_569',
               particles = [ P.g, P.Z, P.YS3u1__tilde__, P.YS3u1 ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_109})

V_570 = Vertex(name = 'V_570',
               particles = [ P.Z, P.YS3u2__tilde__, P.YS3u2 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_102})

V_571 = Vertex(name = 'V_571',
               particles = [ P.a, P.Z, P.YS3u2__tilde__, P.YS3u2 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_106})

V_572 = Vertex(name = 'V_572',
               particles = [ P.g, P.Z, P.YS3u2__tilde__, P.YS3u2 ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_109})

V_573 = Vertex(name = 'V_573',
               particles = [ P.Z, P.YS3u3__tilde__, P.YS3u3 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_102})

V_574 = Vertex(name = 'V_574',
               particles = [ P.a, P.Z, P.YS3u3__tilde__, P.YS3u3 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_106})

V_575 = Vertex(name = 'V_575',
               particles = [ P.g, P.Z, P.YS3u3__tilde__, P.YS3u3 ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_109})

V_576 = Vertex(name = 'V_576',
               particles = [ P.Z, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_130})

V_577 = Vertex(name = 'V_577',
               particles = [ P.Z, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_129})

V_578 = Vertex(name = 'V_578',
               particles = [ P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_130})

V_579 = Vertex(name = 'V_579',
               particles = [ P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_146})

V_580 = Vertex(name = 'V_580',
               particles = [ P.Z, P.Z, P.YS1e1__tilde__, P.YS1e1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_112})

V_581 = Vertex(name = 'V_581',
               particles = [ P.Z, P.Z, P.YS1e2__tilde__, P.YS1e2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_112})

V_582 = Vertex(name = 'V_582',
               particles = [ P.Z, P.Z, P.YS1e3__tilde__, P.YS1e3 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_112})

V_583 = Vertex(name = 'V_583',
               particles = [ P.Z, P.Z, P.YS1Le1__tilde__, P.YS1Le1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_129})

V_584 = Vertex(name = 'V_584',
               particles = [ P.Z, P.Z, P.YS1Le2__tilde__, P.YS1Le2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_129})

V_585 = Vertex(name = 'V_585',
               particles = [ P.Z, P.Z, P.YS1Le3__tilde__, P.YS1Le3 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_129})

V_586 = Vertex(name = 'V_586',
               particles = [ P.Z, P.Z, P.YS1Lv1__tilde__, P.YS1Lv1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_130})

V_587 = Vertex(name = 'V_587',
               particles = [ P.Z, P.Z, P.YS1Lv2__tilde__, P.YS1Lv2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_130})

V_588 = Vertex(name = 'V_588',
               particles = [ P.Z, P.Z, P.YS1Lv3__tilde__, P.YS1Lv3 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_130})

V_589 = Vertex(name = 'V_589',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_75})

V_590 = Vertex(name = 'V_590',
               particles = [ P.Z, P.Z, P.YS3d1__tilde__, P.YS3d1 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_110})

V_591 = Vertex(name = 'V_591',
               particles = [ P.Z, P.Z, P.YS3d2__tilde__, P.YS3d2 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_110})

V_592 = Vertex(name = 'V_592',
               particles = [ P.Z, P.Z, P.YS3d3__tilde__, P.YS3d3 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_110})

V_593 = Vertex(name = 'V_593',
               particles = [ P.Z, P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_128})

V_594 = Vertex(name = 'V_594',
               particles = [ P.Z, P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_128})

V_595 = Vertex(name = 'V_595',
               particles = [ P.Z, P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_128})

V_596 = Vertex(name = 'V_596',
               particles = [ P.Z, P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_127})

V_597 = Vertex(name = 'V_597',
               particles = [ P.Z, P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_127})

V_598 = Vertex(name = 'V_598',
               particles = [ P.Z, P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_127})

V_599 = Vertex(name = 'V_599',
               particles = [ P.Z, P.Z, P.YS3u1__tilde__, P.YS3u1 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_111})

V_600 = Vertex(name = 'V_600',
               particles = [ P.Z, P.Z, P.YS3u2__tilde__, P.YS3u2 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_111})

V_601 = Vertex(name = 'V_601',
               particles = [ P.Z, P.Z, P.YS3u3__tilde__, P.YS3u3 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_111})

V_602 = Vertex(name = 'V_602',
               particles = [ P.ve__tilde__, P.YF1Lv1, P.Xv ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_28})

V_603 = Vertex(name = 'V_603',
               particles = [ P.e__plus__, P.YF1Le1, P.Xv ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_28})

V_604 = Vertex(name = 'V_604',
               particles = [ P.vm__tilde__, P.YF1Lv2, P.Xv ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_29})

V_605 = Vertex(name = 'V_605',
               particles = [ P.mu__plus__, P.YF1Le2, P.Xv ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_29})

V_606 = Vertex(name = 'V_606',
               particles = [ P.vt__tilde__, P.YF1Lv3, P.Xv ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_30})

V_607 = Vertex(name = 'V_607',
               particles = [ P.ta__plus__, P.YF1Le3, P.Xv ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_30})

V_608 = Vertex(name = 'V_608',
               particles = [ P.u__tilde__, P.YF3Qu1, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_34})

V_609 = Vertex(name = 'V_609',
               particles = [ P.b__tilde__, P.YF3Qd1, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_37})

V_610 = Vertex(name = 'V_610',
               particles = [ P.d__tilde__, P.YF3Qd1, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_35})

V_611 = Vertex(name = 'V_611',
               particles = [ P.s__tilde__, P.YF3Qd1, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_36})

V_612 = Vertex(name = 'V_612',
               particles = [ P.c__tilde__, P.YF3Qu2, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_38})

V_613 = Vertex(name = 'V_613',
               particles = [ P.b__tilde__, P.YF3Qd2, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_41})

V_614 = Vertex(name = 'V_614',
               particles = [ P.d__tilde__, P.YF3Qd2, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_39})

V_615 = Vertex(name = 'V_615',
               particles = [ P.s__tilde__, P.YF3Qd2, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_40})

V_616 = Vertex(name = 'V_616',
               particles = [ P.t__tilde__, P.YF3Qu3, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_42})

V_617 = Vertex(name = 'V_617',
               particles = [ P.b__tilde__, P.YF3Qd3, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_45})

V_618 = Vertex(name = 'V_618',
               particles = [ P.d__tilde__, P.YF3Qd3, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_43})

V_619 = Vertex(name = 'V_619',
               particles = [ P.s__tilde__, P.YF3Qd3, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_44})

V_620 = Vertex(name = 'V_620',
               particles = [ P.ve__tilde__, P.YF1Lv1, P.Xw__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_28})

V_621 = Vertex(name = 'V_621',
               particles = [ P.e__plus__, P.YF1Le1, P.Xw__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_28})

V_622 = Vertex(name = 'V_622',
               particles = [ P.vm__tilde__, P.YF1Lv2, P.Xw__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_29})

V_623 = Vertex(name = 'V_623',
               particles = [ P.mu__plus__, P.YF1Le2, P.Xw__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_29})

V_624 = Vertex(name = 'V_624',
               particles = [ P.vt__tilde__, P.YF1Lv3, P.Xw__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_30})

V_625 = Vertex(name = 'V_625',
               particles = [ P.ta__plus__, P.YF1Le3, P.Xw__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_30})

V_626 = Vertex(name = 'V_626',
               particles = [ P.u__tilde__, P.YF3Qu1, P.Xw__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_34})

V_627 = Vertex(name = 'V_627',
               particles = [ P.b__tilde__, P.YF3Qd1, P.Xw__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_37})

V_628 = Vertex(name = 'V_628',
               particles = [ P.d__tilde__, P.YF3Qd1, P.Xw__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_35})

V_629 = Vertex(name = 'V_629',
               particles = [ P.s__tilde__, P.YF3Qd1, P.Xw__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_36})

V_630 = Vertex(name = 'V_630',
               particles = [ P.c__tilde__, P.YF3Qu2, P.Xw__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_38})

V_631 = Vertex(name = 'V_631',
               particles = [ P.b__tilde__, P.YF3Qd2, P.Xw__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_41})

V_632 = Vertex(name = 'V_632',
               particles = [ P.d__tilde__, P.YF3Qd2, P.Xw__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_39})

V_633 = Vertex(name = 'V_633',
               particles = [ P.s__tilde__, P.YF3Qd2, P.Xw__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_40})

V_634 = Vertex(name = 'V_634',
               particles = [ P.t__tilde__, P.YF3Qu3, P.Xw__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_42})

V_635 = Vertex(name = 'V_635',
               particles = [ P.b__tilde__, P.YF3Qd3, P.Xw__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_45})

V_636 = Vertex(name = 'V_636',
               particles = [ P.d__tilde__, P.YF3Qd3, P.Xw__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_43})

V_637 = Vertex(name = 'V_637',
               particles = [ P.s__tilde__, P.YF3Qd3, P.Xw__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_44})

V_638 = Vertex(name = 'V_638',
               particles = [ P.e__plus__, P.e__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_5})

V_639 = Vertex(name = 'V_639',
               particles = [ P.mu__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_5})

V_640 = Vertex(name = 'V_640',
               particles = [ P.ta__plus__, P.ta__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_5})

V_641 = Vertex(name = 'V_641',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_4})

V_642 = Vertex(name = 'V_642',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_4})

V_643 = Vertex(name = 'V_643',
               particles = [ P.t__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_4})

V_644 = Vertex(name = 'V_644',
               particles = [ P.b__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_276,(0,1):C.GC_1})

V_645 = Vertex(name = 'V_645',
               particles = [ P.d__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_274})

V_646 = Vertex(name = 'V_646',
               particles = [ P.s__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_275})

V_647 = Vertex(name = 'V_647',
               particles = [ P.b__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_226})

V_648 = Vertex(name = 'V_648',
               particles = [ P.d__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_224,(0,1):C.GC_1})

V_649 = Vertex(name = 'V_649',
               particles = [ P.s__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_225})

V_650 = Vertex(name = 'V_650',
               particles = [ P.b__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_251})

V_651 = Vertex(name = 'V_651',
               particles = [ P.d__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_249})

V_652 = Vertex(name = 'V_652',
               particles = [ P.s__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_250,(0,1):C.GC_1})

V_653 = Vertex(name = 'V_653',
               particles = [ P.u__tilde__, P.u, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_18})

V_654 = Vertex(name = 'V_654',
               particles = [ P.c__tilde__, P.c, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_18})

V_655 = Vertex(name = 'V_655',
               particles = [ P.t__tilde__, P.t, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_18})

V_656 = Vertex(name = 'V_656',
               particles = [ P.b__tilde__, P.b, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_279,(0,1):C.GC_18})

V_657 = Vertex(name = 'V_657',
               particles = [ P.d__tilde__, P.b, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_277})

V_658 = Vertex(name = 'V_658',
               particles = [ P.s__tilde__, P.b, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_278})

V_659 = Vertex(name = 'V_659',
               particles = [ P.b__tilde__, P.d, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_229})

V_660 = Vertex(name = 'V_660',
               particles = [ P.d__tilde__, P.d, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_227,(0,1):C.GC_18})

V_661 = Vertex(name = 'V_661',
               particles = [ P.s__tilde__, P.d, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_228})

V_662 = Vertex(name = 'V_662',
               particles = [ P.b__tilde__, P.s, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_254})

V_663 = Vertex(name = 'V_663',
               particles = [ P.d__tilde__, P.s, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_252})

V_664 = Vertex(name = 'V_664',
               particles = [ P.s__tilde__, P.s, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_253,(0,1):C.GC_18})

V_665 = Vertex(name = 'V_665',
               particles = [ P.b__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_83})

V_666 = Vertex(name = 'V_666',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_81})

V_667 = Vertex(name = 'V_667',
               particles = [ P.s__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_82})

V_668 = Vertex(name = 'V_668',
               particles = [ P.b__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_86})

V_669 = Vertex(name = 'V_669',
               particles = [ P.d__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_84})

V_670 = Vertex(name = 'V_670',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_85})

V_671 = Vertex(name = 'V_671',
               particles = [ P.b__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_89})

V_672 = Vertex(name = 'V_672',
               particles = [ P.d__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_87})

V_673 = Vertex(name = 'V_673',
               particles = [ P.s__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_88})

V_674 = Vertex(name = 'V_674',
               particles = [ P.u__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_201})

V_675 = Vertex(name = 'V_675',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_191})

V_676 = Vertex(name = 'V_676',
               particles = [ P.u__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_196})

V_677 = Vertex(name = 'V_677',
               particles = [ P.c__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_216})

V_678 = Vertex(name = 'V_678',
               particles = [ P.c__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_206})

V_679 = Vertex(name = 'V_679',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_211})

V_680 = Vertex(name = 'V_680',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_271})

V_681 = Vertex(name = 'V_681',
               particles = [ P.t__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_221})

V_682 = Vertex(name = 'V_682',
               particles = [ P.t__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_246})

V_683 = Vertex(name = 'V_683',
               particles = [ P.e__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_80})

V_684 = Vertex(name = 'V_684',
               particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_80})

V_685 = Vertex(name = 'V_685',
               particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_80})

V_686 = Vertex(name = 'V_686',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_80})

V_687 = Vertex(name = 'V_687',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_80})

V_688 = Vertex(name = 'V_688',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_80})

V_689 = Vertex(name = 'V_689',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_115,(0,1):C.GC_101})

V_690 = Vertex(name = 'V_690',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_115,(0,1):C.GC_101})

V_691 = Vertex(name = 'V_691',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_115,(0,1):C.GC_101})

V_692 = Vertex(name = 'V_692',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_282,(0,1):C.GC_100})

V_693 = Vertex(name = 'V_693',
               particles = [ P.d__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_280})

V_694 = Vertex(name = 'V_694',
               particles = [ P.s__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_281})

V_695 = Vertex(name = 'V_695',
               particles = [ P.b__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_232})

V_696 = Vertex(name = 'V_696',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_230,(0,1):C.GC_100})

V_697 = Vertex(name = 'V_697',
               particles = [ P.s__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_231})

V_698 = Vertex(name = 'V_698',
               particles = [ P.b__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_257})

V_699 = Vertex(name = 'V_699',
               particles = [ P.d__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_255})

V_700 = Vertex(name = 'V_700',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_256,(0,1):C.GC_100})

V_701 = Vertex(name = 'V_701',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_121})

V_702 = Vertex(name = 'V_702',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_121})

V_703 = Vertex(name = 'V_703',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_121})

V_704 = Vertex(name = 'V_704',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_120,(0,1):C.GC_104})

V_705 = Vertex(name = 'V_705',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_120,(0,1):C.GC_104})

V_706 = Vertex(name = 'V_706',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_120,(0,1):C.GC_104})

V_707 = Vertex(name = 'V_707',
               particles = [ P.YF1Lv1__tilde__, P.ve, P.Xv ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_28})

V_708 = Vertex(name = 'V_708',
               particles = [ P.YF1Le1__tilde__, P.e__minus__, P.Xv ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_28})

V_709 = Vertex(name = 'V_709',
               particles = [ P.YF1Lv2__tilde__, P.vm, P.Xv ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_29})

V_710 = Vertex(name = 'V_710',
               particles = [ P.YF1Le2__tilde__, P.mu__minus__, P.Xv ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_29})

V_711 = Vertex(name = 'V_711',
               particles = [ P.YF1Lv3__tilde__, P.vt, P.Xv ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_30})

V_712 = Vertex(name = 'V_712',
               particles = [ P.YF1Le3__tilde__, P.ta__minus__, P.Xv ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_30})

V_713 = Vertex(name = 'V_713',
               particles = [ P.YF3Qu1__tilde__, P.u, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_34})

V_714 = Vertex(name = 'V_714',
               particles = [ P.YF3Qd1__tilde__, P.b, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_199})

V_715 = Vertex(name = 'V_715',
               particles = [ P.YF3Qd1__tilde__, P.d, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_189})

V_716 = Vertex(name = 'V_716',
               particles = [ P.YF3Qd1__tilde__, P.s, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_194})

V_717 = Vertex(name = 'V_717',
               particles = [ P.YF3Qu2__tilde__, P.c, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_38})

V_718 = Vertex(name = 'V_718',
               particles = [ P.YF3Qd2__tilde__, P.b, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_214})

V_719 = Vertex(name = 'V_719',
               particles = [ P.YF3Qd2__tilde__, P.d, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_204})

V_720 = Vertex(name = 'V_720',
               particles = [ P.YF3Qd2__tilde__, P.s, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_209})

V_721 = Vertex(name = 'V_721',
               particles = [ P.YF3Qu3__tilde__, P.t, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_42})

V_722 = Vertex(name = 'V_722',
               particles = [ P.YF3Qd3__tilde__, P.b, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_269})

V_723 = Vertex(name = 'V_723',
               particles = [ P.YF3Qd3__tilde__, P.d, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_219})

V_724 = Vertex(name = 'V_724',
               particles = [ P.YF3Qd3__tilde__, P.s, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_244})

V_725 = Vertex(name = 'V_725',
               particles = [ P.YF1Lv1__tilde__, P.ve, P.Xw ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_28})

V_726 = Vertex(name = 'V_726',
               particles = [ P.YF1Le1__tilde__, P.e__minus__, P.Xw ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_28})

V_727 = Vertex(name = 'V_727',
               particles = [ P.YF1Lv2__tilde__, P.vm, P.Xw ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_29})

V_728 = Vertex(name = 'V_728',
               particles = [ P.YF1Le2__tilde__, P.mu__minus__, P.Xw ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_29})

V_729 = Vertex(name = 'V_729',
               particles = [ P.YF1Lv3__tilde__, P.vt, P.Xw ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_30})

V_730 = Vertex(name = 'V_730',
               particles = [ P.YF1Le3__tilde__, P.ta__minus__, P.Xw ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_30})

V_731 = Vertex(name = 'V_731',
               particles = [ P.YF3Qu1__tilde__, P.u, P.Xw ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_34})

V_732 = Vertex(name = 'V_732',
               particles = [ P.YF3Qd1__tilde__, P.b, P.Xw ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_199})

V_733 = Vertex(name = 'V_733',
               particles = [ P.YF3Qd1__tilde__, P.d, P.Xw ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_189})

V_734 = Vertex(name = 'V_734',
               particles = [ P.YF3Qd1__tilde__, P.s, P.Xw ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_194})

V_735 = Vertex(name = 'V_735',
               particles = [ P.YF3Qu2__tilde__, P.c, P.Xw ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_38})

V_736 = Vertex(name = 'V_736',
               particles = [ P.YF3Qd2__tilde__, P.b, P.Xw ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_214})

V_737 = Vertex(name = 'V_737',
               particles = [ P.YF3Qd2__tilde__, P.d, P.Xw ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_204})

V_738 = Vertex(name = 'V_738',
               particles = [ P.YF3Qd2__tilde__, P.s, P.Xw ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_209})

V_739 = Vertex(name = 'V_739',
               particles = [ P.YF3Qu3__tilde__, P.t, P.Xw ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_42})

V_740 = Vertex(name = 'V_740',
               particles = [ P.YF3Qd3__tilde__, P.b, P.Xw ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_269})

V_741 = Vertex(name = 'V_741',
               particles = [ P.YF3Qd3__tilde__, P.d, P.Xw ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_219})

V_742 = Vertex(name = 'V_742',
               particles = [ P.YF3Qd3__tilde__, P.s, P.Xw ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_244})

V_743 = Vertex(name = 'V_743',
               particles = [ P.e__plus__, P.YF1e1, P.Xv ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_25})

V_744 = Vertex(name = 'V_744',
               particles = [ P.mu__plus__, P.YF1e2, P.Xv ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_26})

V_745 = Vertex(name = 'V_745',
               particles = [ P.ta__plus__, P.YF1e3, P.Xv ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_27})

V_746 = Vertex(name = 'V_746',
               particles = [ P.d__tilde__, P.YF3d1, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_31})

V_747 = Vertex(name = 'V_747',
               particles = [ P.s__tilde__, P.YF3d2, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_32})

V_748 = Vertex(name = 'V_748',
               particles = [ P.b__tilde__, P.YF3d3, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_33})

V_749 = Vertex(name = 'V_749',
               particles = [ P.u__tilde__, P.YF3u1, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_46})

V_750 = Vertex(name = 'V_750',
               particles = [ P.c__tilde__, P.YF3u2, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_47})

V_751 = Vertex(name = 'V_751',
               particles = [ P.t__tilde__, P.YF3u3, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_48})

V_752 = Vertex(name = 'V_752',
               particles = [ P.e__plus__, P.YF1e1, P.Xw__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_25})

V_753 = Vertex(name = 'V_753',
               particles = [ P.mu__plus__, P.YF1e2, P.Xw__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_26})

V_754 = Vertex(name = 'V_754',
               particles = [ P.ta__plus__, P.YF1e3, P.Xw__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_27})

V_755 = Vertex(name = 'V_755',
               particles = [ P.d__tilde__, P.YF3d1, P.Xw__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_31})

V_756 = Vertex(name = 'V_756',
               particles = [ P.s__tilde__, P.YF3d2, P.Xw__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_32})

V_757 = Vertex(name = 'V_757',
               particles = [ P.b__tilde__, P.YF3d3, P.Xw__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_33})

V_758 = Vertex(name = 'V_758',
               particles = [ P.u__tilde__, P.YF3u1, P.Xw__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_46})

V_759 = Vertex(name = 'V_759',
               particles = [ P.c__tilde__, P.YF3u2, P.Xw__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_47})

V_760 = Vertex(name = 'V_760',
               particles = [ P.t__tilde__, P.YF3u3, P.Xw__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_48})

V_761 = Vertex(name = 'V_761',
               particles = [ P.YF1e1__tilde__, P.e__minus__, P.Xv ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_25})

V_762 = Vertex(name = 'V_762',
               particles = [ P.YF1e2__tilde__, P.mu__minus__, P.Xv ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_26})

V_763 = Vertex(name = 'V_763',
               particles = [ P.YF1e3__tilde__, P.ta__minus__, P.Xv ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_27})

V_764 = Vertex(name = 'V_764',
               particles = [ P.YF3d1__tilde__, P.d, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_31})

V_765 = Vertex(name = 'V_765',
               particles = [ P.YF3d2__tilde__, P.s, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_32})

V_766 = Vertex(name = 'V_766',
               particles = [ P.YF3d3__tilde__, P.b, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_33})

V_767 = Vertex(name = 'V_767',
               particles = [ P.YF3u1__tilde__, P.u, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_46})

V_768 = Vertex(name = 'V_768',
               particles = [ P.YF3u2__tilde__, P.c, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_47})

V_769 = Vertex(name = 'V_769',
               particles = [ P.YF3u3__tilde__, P.t, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_48})

V_770 = Vertex(name = 'V_770',
               particles = [ P.YF1e1__tilde__, P.e__minus__, P.Xw ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_25})

V_771 = Vertex(name = 'V_771',
               particles = [ P.YF1e2__tilde__, P.mu__minus__, P.Xw ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_26})

V_772 = Vertex(name = 'V_772',
               particles = [ P.YF1e3__tilde__, P.ta__minus__, P.Xw ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_27})

V_773 = Vertex(name = 'V_773',
               particles = [ P.YF3d1__tilde__, P.d, P.Xw ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_31})

V_774 = Vertex(name = 'V_774',
               particles = [ P.YF3d2__tilde__, P.s, P.Xw ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_32})

V_775 = Vertex(name = 'V_775',
               particles = [ P.YF3d3__tilde__, P.b, P.Xw ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_33})

V_776 = Vertex(name = 'V_776',
               particles = [ P.YF3u1__tilde__, P.u, P.Xw ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_46})

V_777 = Vertex(name = 'V_777',
               particles = [ P.YF3u2__tilde__, P.c, P.Xw ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_47})

V_778 = Vertex(name = 'V_778',
               particles = [ P.YF3u3__tilde__, P.t, P.Xw ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_48})

