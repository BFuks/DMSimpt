# This file was automatically created by FeynRules 2.4.91
# Mathematica version: 13.1.0 for Mac OS X ARM (64-bit) (June 16, 2022)
# Date: Tue 4 Jun 2024 14:31:18


from object_library import all_vertices, all_CTvertices, Vertex, CTVertex
import particles as P
import CT_couplings as C
import lorentz as L


V_1 = CTVertex(name = 'V_1',
               type = 'R2',
               particles = [ P.g, P.g, P.g ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVV2 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u], [P.YF3d1], [P.YF3d2], [P.YF3d3], [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3], [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3], [P.YF3u1], [P.YF3u2], [P.YF3u3] ], [ [P.g] ] ],
               couplings = {(0,0,0):C.R2GC_294_95,(0,0,1):C.R2GC_294_96})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV10, L.VVVV2, L.VVVV3, L.VVVV5 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u], [P.YF3d1], [P.YF3d2], [P.YF3d3], [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3], [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3], [P.YF3u1], [P.YF3u2], [P.YF3u3] ], [ [P.g] ] ],
               couplings = {(0,1,0):C.R2GC_289_90,(0,1,1):C.R2GC_289_91,(2,1,0):C.R2GC_289_90,(2,1,1):C.R2GC_289_91,(5,1,0):C.R2GC_287_86,(5,1,1):C.R2GC_287_87,(1,1,0):C.R2GC_287_86,(1,1,1):C.R2GC_287_87,(7,1,0):C.R2GC_297_101,(7,1,1):C.R2GC_297_102,(4,1,0):C.R2GC_287_86,(4,1,1):C.R2GC_287_87,(3,1,0):C.R2GC_287_86,(3,1,1):C.R2GC_287_87,(8,1,0):C.R2GC_288_88,(8,1,1):C.R2GC_288_89,(6,1,0):C.R2GC_296_99,(6,1,1):C.R2GC_296_100,(11,0,0):C.R2GC_291_93,(11,0,1):C.R2GC_291_94,(10,0,0):C.R2GC_291_93,(10,0,1):C.R2GC_291_94,(9,0,1):C.R2GC_290_92,(0,2,0):C.R2GC_289_90,(0,2,1):C.R2GC_289_91,(2,2,0):C.R2GC_289_90,(2,2,1):C.R2GC_289_91,(7,2,0):C.R2GC_297_101,(7,2,1):C.R2GC_288_89,(5,2,0):C.R2GC_287_86,(5,2,1):C.R2GC_287_87,(1,2,0):C.R2GC_287_86,(1,2,1):C.R2GC_287_87,(4,2,0):C.R2GC_287_86,(4,2,1):C.R2GC_287_87,(3,2,0):C.R2GC_287_86,(3,2,1):C.R2GC_287_87,(8,2,0):C.R2GC_288_88,(8,2,1):C.R2GC_297_102,(6,2,0):C.R2GC_302_103,(6,2,1):C.R2GC_302_104,(0,3,0):C.R2GC_289_90,(0,3,1):C.R2GC_289_91,(2,3,0):C.R2GC_289_90,(2,3,1):C.R2GC_289_91,(7,3,0):C.R2GC_295_97,(7,3,1):C.R2GC_295_98,(5,3,0):C.R2GC_287_86,(5,3,1):C.R2GC_287_87,(1,3,0):C.R2GC_287_86,(1,3,1):C.R2GC_287_87,(4,3,0):C.R2GC_287_86,(4,3,1):C.R2GC_287_87,(3,3,0):C.R2GC_287_86,(3,3,1):C.R2GC_287_87,(8,3,0):C.R2GC_288_88,(8,3,1):C.R2GC_295_98,(6,3,0):C.R2GC_296_99})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.YF3d1__tilde__, P.YF3d1, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.YF3d1] ] ],
               couplings = {(0,0,0):C.R2GC_304_106})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.YF3d2__tilde__, P.YF3d2, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.YF3d2] ] ],
               couplings = {(0,0,0):C.R2GC_304_106})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.YF3d3__tilde__, P.YF3d3, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.YF3d3] ] ],
               couplings = {(0,0,0):C.R2GC_304_106})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.YF3Qd1__tilde__, P.YF3Qd1, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.YF3Qd1] ] ],
               couplings = {(0,0,0):C.R2GC_304_106})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.YF3Qd2__tilde__, P.YF3Qd2, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.YF3Qd2] ] ],
               couplings = {(0,0,0):C.R2GC_304_106})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.YF3Qd3__tilde__, P.YF3Qd3, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.YF3Qd3] ] ],
               couplings = {(0,0,0):C.R2GC_304_106})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.YF3Qu1__tilde__, P.YF3Qu1, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.YF3Qu1] ] ],
               couplings = {(0,0,0):C.R2GC_312_113})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.YF3Qu2__tilde__, P.YF3Qu2, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qu2] ] ],
                couplings = {(0,0,0):C.R2GC_312_113})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.YF3Qu3__tilde__, P.YF3Qu3, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qu3] ] ],
                couplings = {(0,0,0):C.R2GC_312_113})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.YF3u1__tilde__, P.YF3u1, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3u1] ] ],
                couplings = {(0,0,0):C.R2GC_312_113})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.YF3u2__tilde__, P.YF3u2, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3u2] ] ],
                couplings = {(0,0,0):C.R2GC_312_113})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.YF3u3__tilde__, P.YF3u3, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3u3] ] ],
                couplings = {(0,0,0):C.R2GC_312_113})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.u__tilde__, P.YF3Qu1, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.u, P.YF3Qu1] ] ],
                couplings = {(0,0,0):C.R2GC_608_196})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.u__tilde__, P.YF3Qu1, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.u, P.YF3Qu1] ] ],
                couplings = {(0,0,0):C.R2GC_608_196})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.d__tilde__, P.YF3Qd1, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.YF3Qd1] ] ],
                couplings = {(0,0,0):C.R2GC_608_196})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.d__tilde__, P.YF3Qd1, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.YF3Qd1] ] ],
                couplings = {(0,0,0):C.R2GC_608_196})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.c__tilde__, P.YF3Qu2, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.c, P.g, P.YF3Qu2] ] ],
                couplings = {(0,0,0):C.R2GC_600_188})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.c__tilde__, P.YF3Qu2, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.c, P.g, P.YF3Qu2] ] ],
                couplings = {(0,0,0):C.R2GC_600_188})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.s__tilde__, P.YF3Qd2, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s, P.YF3Qd2] ] ],
                couplings = {(0,0,0):C.R2GC_600_188})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.s__tilde__, P.YF3Qd2, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s, P.YF3Qd2] ] ],
                couplings = {(0,0,0):C.R2GC_600_188})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.t__tilde__, P.YF3Qu3, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.t, P.YF3Qu3] ] ],
                couplings = {(0,0,0):C.R2GC_595_183})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.t__tilde__, P.YF3Qu3, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.t, P.YF3Qu3] ] ],
                couplings = {(0,0,0):C.R2GC_595_183})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.b__tilde__, P.YF3Qd3, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g, P.YF3Qd3] ] ],
                couplings = {(0,0,0):C.R2GC_595_183})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.b__tilde__, P.YF3Qd3, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g, P.YF3Qd3] ] ],
                couplings = {(0,0,0):C.R2GC_595_183})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.YF3d1__tilde__, P.d, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.YF3d1] ] ],
                couplings = {(0,0,0):C.R2GC_606_194})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.YF3d2__tilde__, P.s, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s, P.YF3d2] ] ],
                couplings = {(0,0,0):C.R2GC_770_213})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.YF3d3__tilde__, P.b, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g, P.YF3d3] ] ],
                couplings = {(0,0,0):C.R2GC_593_181})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.YF3d1__tilde__, P.d, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.YF3d1] ] ],
                couplings = {(0,0,0):C.R2GC_606_194})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.YF3d2__tilde__, P.s, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s, P.YF3d2] ] ],
                couplings = {(0,0,0):C.R2GC_770_213})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.YF3d3__tilde__, P.b, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g, P.YF3d3] ] ],
                couplings = {(0,0,0):C.R2GC_593_181})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.YF3u1__tilde__, P.u, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.u, P.YF3u1] ] ],
                couplings = {(0,0,0):C.R2GC_790_223})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.YF3u2__tilde__, P.c, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.c, P.g, P.YF3u2] ] ],
                couplings = {(0,0,0):C.R2GC_602_190})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.YF3u3__tilde__, P.t, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.t, P.YF3u3] ] ],
                couplings = {(0,0,0):C.R2GC_783_220})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.YF3u1__tilde__, P.u, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.u, P.YF3u1] ] ],
                couplings = {(0,0,0):C.R2GC_790_223})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.YF3u2__tilde__, P.c, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.c, P.g, P.YF3u2] ] ],
                couplings = {(0,0,0):C.R2GC_602_190})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.YF3u3__tilde__, P.t, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.t, P.YF3u3] ] ],
                couplings = {(0,0,0):C.R2GC_783_220})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_776_216,(0,1,0):C.R2GC_775_215})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_506_161})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_505_160})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_774_214,(0,1,0):C.R2GC_777_217})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_309_111})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_310_112})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.d__tilde__, P.YF3d1, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.d, P.g, P.YF3d1] ] ],
                couplings = {(0,0,0):C.R2GC_606_194})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.s__tilde__, P.YF3d2, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.s, P.YF3d2] ] ],
                couplings = {(0,0,0):C.R2GC_770_213})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.b__tilde__, P.YF3d3, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.b, P.g, P.YF3d3] ] ],
                couplings = {(0,0,0):C.R2GC_593_181})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.d__tilde__, P.YF3d1, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.d, P.g, P.YF3d1] ] ],
                couplings = {(0,0,0):C.R2GC_606_194})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.s__tilde__, P.YF3d2, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.s, P.YF3d2] ] ],
                couplings = {(0,0,0):C.R2GC_770_213})

V_50 = CTVertex(name = 'V_50',
                type = 'R2',
                particles = [ P.b__tilde__, P.YF3d3, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.b, P.g, P.YF3d3] ] ],
                couplings = {(0,0,0):C.R2GC_593_181})

V_51 = CTVertex(name = 'V_51',
                type = 'R2',
                particles = [ P.u__tilde__, P.YF3u1, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.u, P.YF3u1] ] ],
                couplings = {(0,0,0):C.R2GC_790_223})

V_52 = CTVertex(name = 'V_52',
                type = 'R2',
                particles = [ P.c__tilde__, P.YF3u2, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.c, P.g, P.YF3u2] ] ],
                couplings = {(0,0,0):C.R2GC_602_190})

V_53 = CTVertex(name = 'V_53',
                type = 'R2',
                particles = [ P.t__tilde__, P.YF3u3, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.t, P.YF3u3] ] ],
                couplings = {(0,0,0):C.R2GC_783_220})

V_54 = CTVertex(name = 'V_54',
                type = 'R2',
                particles = [ P.u__tilde__, P.YF3u1, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.u, P.YF3u1] ] ],
                couplings = {(0,0,0):C.R2GC_790_223})

V_55 = CTVertex(name = 'V_55',
                type = 'R2',
                particles = [ P.c__tilde__, P.YF3u2, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.c, P.g, P.YF3u2] ] ],
                couplings = {(0,0,0):C.R2GC_602_190})

V_56 = CTVertex(name = 'V_56',
                type = 'R2',
                particles = [ P.t__tilde__, P.YF3u3, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.t, P.YF3u3] ] ],
                couplings = {(0,0,0):C.R2GC_783_220})

V_57 = CTVertex(name = 'V_57',
                type = 'R2',
                particles = [ P.YF3Qu1__tilde__, P.u, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.u, P.YF3Qu1] ] ],
                couplings = {(0,0,0):C.R2GC_608_196})

V_58 = CTVertex(name = 'V_58',
                type = 'R2',
                particles = [ P.YF3Qu1__tilde__, P.u, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.u, P.YF3Qu1] ] ],
                couplings = {(0,0,0):C.R2GC_608_196})

V_59 = CTVertex(name = 'V_59',
                type = 'R2',
                particles = [ P.YF3Qd1__tilde__, P.d, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.d, P.g, P.YF3Qd1] ] ],
                couplings = {(0,0,0):C.R2GC_608_196})

V_60 = CTVertex(name = 'V_60',
                type = 'R2',
                particles = [ P.YF3Qd1__tilde__, P.d, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.d, P.g, P.YF3Qd1] ] ],
                couplings = {(0,0,0):C.R2GC_608_196})

V_61 = CTVertex(name = 'V_61',
                type = 'R2',
                particles = [ P.YF3Qu2__tilde__, P.c, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.c, P.g, P.YF3Qu2] ] ],
                couplings = {(0,0,0):C.R2GC_600_188})

V_62 = CTVertex(name = 'V_62',
                type = 'R2',
                particles = [ P.YF3Qu2__tilde__, P.c, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.c, P.g, P.YF3Qu2] ] ],
                couplings = {(0,0,0):C.R2GC_600_188})

V_63 = CTVertex(name = 'V_63',
                type = 'R2',
                particles = [ P.YF3Qd2__tilde__, P.s, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.s, P.YF3Qd2] ] ],
                couplings = {(0,0,0):C.R2GC_600_188})

V_64 = CTVertex(name = 'V_64',
                type = 'R2',
                particles = [ P.YF3Qd2__tilde__, P.s, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.s, P.YF3Qd2] ] ],
                couplings = {(0,0,0):C.R2GC_600_188})

V_65 = CTVertex(name = 'V_65',
                type = 'R2',
                particles = [ P.YF3Qu3__tilde__, P.t, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.t, P.YF3Qu3] ] ],
                couplings = {(0,0,0):C.R2GC_595_183})

V_66 = CTVertex(name = 'V_66',
                type = 'R2',
                particles = [ P.YF3Qu3__tilde__, P.t, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.t, P.YF3Qu3] ] ],
                couplings = {(0,0,0):C.R2GC_595_183})

V_67 = CTVertex(name = 'V_67',
                type = 'R2',
                particles = [ P.YF3Qd3__tilde__, P.b, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.b, P.g, P.YF3Qd3] ] ],
                couplings = {(0,0,0):C.R2GC_595_183})

V_68 = CTVertex(name = 'V_68',
                type = 'R2',
                particles = [ P.YF3Qd3__tilde__, P.b, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.b, P.g, P.YF3Qd3] ] ],
                couplings = {(0,0,0):C.R2GC_595_183})

V_69 = CTVertex(name = 'V_69',
                type = 'R2',
                particles = [ P.YF3Qd1__tilde__, P.YF3Qd1, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd1] ] ],
                couplings = {(0,0,0):C.R2GC_305_107})

V_70 = CTVertex(name = 'V_70',
                type = 'R2',
                particles = [ P.YF3Qd2__tilde__, P.YF3Qd2, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd2] ] ],
                couplings = {(0,0,0):C.R2GC_305_107})

V_71 = CTVertex(name = 'V_71',
                type = 'R2',
                particles = [ P.YF3Qd3__tilde__, P.YF3Qd3, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd3] ] ],
                couplings = {(0,0,0):C.R2GC_305_107})

V_72 = CTVertex(name = 'V_72',
                type = 'R2',
                particles = [ P.YF3Qu1__tilde__, P.YF3Qu1, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qu1] ] ],
                couplings = {(0,0,0):C.R2GC_305_107})

V_73 = CTVertex(name = 'V_73',
                type = 'R2',
                particles = [ P.YF3Qu2__tilde__, P.YF3Qu2, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qu2] ] ],
                couplings = {(0,0,0):C.R2GC_305_107})

V_74 = CTVertex(name = 'V_74',
                type = 'R2',
                particles = [ P.YF3Qu3__tilde__, P.YF3Qu3, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qu3] ] ],
                couplings = {(0,0,0):C.R2GC_305_107})

V_75 = CTVertex(name = 'V_75',
                type = 'R2',
                particles = [ P.YF3u1__tilde__, P.YF3u1, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3u1] ] ],
                couplings = {(0,0,0):C.R2GC_305_107})

V_76 = CTVertex(name = 'V_76',
                type = 'R2',
                particles = [ P.YF3u2__tilde__, P.YF3u2, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3u2] ] ],
                couplings = {(0,0,0):C.R2GC_305_107})

V_77 = CTVertex(name = 'V_77',
                type = 'R2',
                particles = [ P.YF3u3__tilde__, P.YF3u3, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3u3] ] ],
                couplings = {(0,0,0):C.R2GC_305_107})

V_78 = CTVertex(name = 'V_78',
                type = 'R2',
                particles = [ P.YF3d1__tilde__, P.YF3d1, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3d1] ] ],
                couplings = {(0,0,0):C.R2GC_305_107})

V_79 = CTVertex(name = 'V_79',
                type = 'R2',
                particles = [ P.YF3d2__tilde__, P.YF3d2, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3d2] ] ],
                couplings = {(0,0,0):C.R2GC_305_107})

V_80 = CTVertex(name = 'V_80',
                type = 'R2',
                particles = [ P.YF3d3__tilde__, P.YF3d3, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3d3] ] ],
                couplings = {(0,0,0):C.R2GC_305_107})

V_81 = CTVertex(name = 'V_81',
                type = 'R2',
                particles = [ P.YF3Qd1__tilde__, P.YF3Qu1, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd1, P.YF3Qu1] ] ],
                couplings = {(0,0,0):C.R2GC_598_186})

V_82 = CTVertex(name = 'V_82',
                type = 'R2',
                particles = [ P.YF3Qd2__tilde__, P.YF3Qu2, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd2, P.YF3Qu2] ] ],
                couplings = {(0,0,0):C.R2GC_598_186})

V_83 = CTVertex(name = 'V_83',
                type = 'R2',
                particles = [ P.YF3Qd3__tilde__, P.YF3Qu3, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd3, P.YF3Qu3] ] ],
                couplings = {(0,0,0):C.R2GC_598_186})

V_84 = CTVertex(name = 'V_84',
                type = 'R2',
                particles = [ P.YF3Qu1__tilde__, P.YF3Qd1, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd1, P.YF3Qu1] ] ],
                couplings = {(0,0,0):C.R2GC_598_186})

V_85 = CTVertex(name = 'V_85',
                type = 'R2',
                particles = [ P.YF3Qu2__tilde__, P.YF3Qd2, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd2, P.YF3Qu2] ] ],
                couplings = {(0,0,0):C.R2GC_598_186})

V_86 = CTVertex(name = 'V_86',
                type = 'R2',
                particles = [ P.YF3Qu3__tilde__, P.YF3Qd3, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd3, P.YF3Qu3] ] ],
                couplings = {(0,0,0):C.R2GC_598_186})

V_87 = CTVertex(name = 'V_87',
                type = 'R2',
                particles = [ P.a, P.YS3d1__tilde__, P.YS3d1 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.YS3d1] ] ],
                couplings = {(0,0,0):C.R2GC_322_116})

V_88 = CTVertex(name = 'V_88',
                type = 'R2',
                particles = [ P.Xd__tilde__, P.d, P.YS3d1__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.YS3d1] ] ],
                couplings = {(0,0,0):C.R2GC_603_191})

V_89 = CTVertex(name = 'V_89',
                type = 'R2',
                particles = [ P.Xm, P.d, P.YS3d1__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.YS3d1] ] ],
                couplings = {(0,0,0):C.R2GC_603_191})

V_90 = CTVertex(name = 'V_90',
                type = 'R2',
                particles = [ P.g, P.YS3d1__tilde__, P.YS3d1 ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.YS3d1] ] ],
                couplings = {(0,0,0):C.R2GC_324_118})

V_91 = CTVertex(name = 'V_91',
                type = 'R2',
                particles = [ P.d__tilde__, P.Xd, P.YS3d1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.d, P.g, P.YS3d1] ] ],
                couplings = {(0,0,0):C.R2GC_603_191})

V_92 = CTVertex(name = 'V_92',
                type = 'R2',
                particles = [ P.d__tilde__, P.Xm, P.YS3d1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.d, P.g, P.YS3d1] ] ],
                couplings = {(0,0,0):C.R2GC_603_191})

V_93 = CTVertex(name = 'V_93',
                type = 'R2',
                particles = [ P.a, P.a, P.YS3d1__tilde__, P.YS3d1 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.YS3d1] ] ],
                couplings = {(0,0,0):C.R2GC_323_117})

V_94 = CTVertex(name = 'V_94',
                type = 'R2',
                particles = [ P.a, P.g, P.YS3d1__tilde__, P.YS3d1 ],
                color = [ 'T(2,4,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.YS3d1] ] ],
                couplings = {(0,0,0):C.R2GC_325_119})

V_95 = CTVertex(name = 'V_95',
                type = 'R2',
                particles = [ P.g, P.g, P.YS3d1__tilde__, P.YS3d1 ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g] ], [ [P.g, P.YS3d1] ] ],
                couplings = {(2,0,0):C.R2GC_328_123,(2,0,1):C.R2GC_328_124,(1,0,0):C.R2GC_328_123,(1,0,1):C.R2GC_328_124,(0,0,0):C.R2GC_291_94,(0,0,1):C.R2GC_327_122})

V_96 = CTVertex(name = 'V_96',
                type = 'R2',
                particles = [ P.a, P.YS3d2__tilde__, P.YS3d2 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.YS3d2] ] ],
                couplings = {(0,0,0):C.R2GC_322_116})

V_97 = CTVertex(name = 'V_97',
                type = 'R2',
                particles = [ P.Xd__tilde__, P.s, P.YS3d2__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s, P.YS3d2] ] ],
                couplings = {(0,0,0):C.R2GC_767_211})

V_98 = CTVertex(name = 'V_98',
                type = 'R2',
                particles = [ P.Xm, P.s, P.YS3d2__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s, P.YS3d2] ] ],
                couplings = {(0,0,0):C.R2GC_767_211})

V_99 = CTVertex(name = 'V_99',
                type = 'R2',
                particles = [ P.g, P.YS3d2__tilde__, P.YS3d2 ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.YS3d2] ] ],
                couplings = {(0,0,0):C.R2GC_324_118})

V_100 = CTVertex(name = 'V_100',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.Xd, P.YS3d2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_767_211})

V_101 = CTVertex(name = 'V_101',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.Xm, P.YS3d2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_767_211})

V_102 = CTVertex(name = 'V_102',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_323_117})

V_103 = CTVertex(name = 'V_103',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_325_119})

V_104 = CTVertex(name = 'V_104',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3d2] ] ],
                 couplings = {(2,0,0):C.R2GC_328_123,(2,0,1):C.R2GC_328_124,(1,0,0):C.R2GC_328_123,(1,0,1):C.R2GC_328_124,(0,0,0):C.R2GC_291_94,(0,0,1):C.R2GC_327_122})

V_105 = CTVertex(name = 'V_105',
                 type = 'R2',
                 particles = [ P.a, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_322_116})

V_106 = CTVertex(name = 'V_106',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.b, P.YS3d3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_590_178})

V_107 = CTVertex(name = 'V_107',
                 type = 'R2',
                 particles = [ P.Xm, P.b, P.YS3d3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_590_178})

V_108 = CTVertex(name = 'V_108',
                 type = 'R2',
                 particles = [ P.g, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_324_118})

V_109 = CTVertex(name = 'V_109',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.Xd, P.YS3d3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_590_178})

V_110 = CTVertex(name = 'V_110',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.Xm, P.YS3d3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_590_178})

V_111 = CTVertex(name = 'V_111',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_323_117})

V_112 = CTVertex(name = 'V_112',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_325_119})

V_113 = CTVertex(name = 'V_113',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3d3] ] ],
                 couplings = {(2,0,0):C.R2GC_328_123,(2,0,1):C.R2GC_328_124,(1,0,0):C.R2GC_328_123,(1,0,1):C.R2GC_328_124,(0,0,0):C.R2GC_291_94,(0,0,1):C.R2GC_327_122})

V_114 = CTVertex(name = 'V_114',
                 type = 'R2',
                 particles = [ P.a, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_322_116})

V_115 = CTVertex(name = 'V_115',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.d, P.YS3Qd1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_604_192})

V_116 = CTVertex(name = 'V_116',
                 type = 'R2',
                 particles = [ P.Xm, P.d, P.YS3Qd1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_604_192})

V_117 = CTVertex(name = 'V_117',
                 type = 'R2',
                 particles = [ P.W__minus__, P.YS3Qd1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_669_207})

V_118 = CTVertex(name = 'V_118',
                 type = 'R2',
                 particles = [ P.g, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_324_118,(0,1,0):C.R2GC_363_132})

V_119 = CTVertex(name = 'V_119',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.Xd, P.YS3Qd1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_604_192})

V_120 = CTVertex(name = 'V_120',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.Xm, P.YS3Qd1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_604_192})

V_121 = CTVertex(name = 'V_121',
                 type = 'R2',
                 particles = [ P.W__plus__, P.YS3Qd1, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_668_206,(0,1,0):C.R2GC_669_207})

V_122 = CTVertex(name = 'V_122',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_323_117})

V_123 = CTVertex(name = 'V_123',
                 type = 'R2',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_666_204,(0,0,1):C.R2GC_666_205})

V_124 = CTVertex(name = 'V_124',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_325_119})

V_125 = CTVertex(name = 'V_125',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(2,0,0):C.R2GC_328_123,(2,0,1):C.R2GC_328_124,(1,0,0):C.R2GC_328_123,(1,0,1):C.R2GC_328_124,(0,0,0):C.R2GC_291_94,(0,0,1):C.R2GC_327_122})

V_126 = CTVertex(name = 'V_126',
                 type = 'R2',
                 particles = [ P.a, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_322_116,(0,1,0):C.R2GC_375_138})

V_127 = CTVertex(name = 'V_127',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.s, P.YS3Qd2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_596_184})

V_128 = CTVertex(name = 'V_128',
                 type = 'R2',
                 particles = [ P.Xm, P.s, P.YS3Qd2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_596_184})

V_129 = CTVertex(name = 'V_129',
                 type = 'R2',
                 particles = [ P.W__minus__, P.YS3Qd2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_669_207,(0,1,0):C.R2GC_668_206})

V_130 = CTVertex(name = 'V_130',
                 type = 'R2',
                 particles = [ P.g, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_324_118,(0,1,0):C.R2GC_363_132})

V_131 = CTVertex(name = 'V_131',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.Xd, P.YS3Qd2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_596_184})

V_132 = CTVertex(name = 'V_132',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.Xm, P.YS3Qd2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_596_184})

V_133 = CTVertex(name = 'V_133',
                 type = 'R2',
                 particles = [ P.W__plus__, P.YS3Qd2, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_668_206,(0,1,0):C.R2GC_669_207})

V_134 = CTVertex(name = 'V_134',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_323_117})

V_135 = CTVertex(name = 'V_135',
                 type = 'R2',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_666_204,(0,0,1):C.R2GC_666_205})

V_136 = CTVertex(name = 'V_136',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_325_119})

V_137 = CTVertex(name = 'V_137',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(2,0,0):C.R2GC_328_123,(2,0,1):C.R2GC_328_124,(1,0,0):C.R2GC_328_123,(1,0,1):C.R2GC_328_124,(0,0,0):C.R2GC_291_94,(0,0,1):C.R2GC_327_122})

V_138 = CTVertex(name = 'V_138',
                 type = 'R2',
                 particles = [ P.a, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_322_116,(0,1,0):C.R2GC_375_138})

V_139 = CTVertex(name = 'V_139',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.b, P.YS3Qd3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_591_179})

V_140 = CTVertex(name = 'V_140',
                 type = 'R2',
                 particles = [ P.Xm, P.b, P.YS3Qd3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_591_179})

V_141 = CTVertex(name = 'V_141',
                 type = 'R2',
                 particles = [ P.W__minus__, P.YS3Qd3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_669_207,(0,1,0):C.R2GC_668_206})

V_142 = CTVertex(name = 'V_142',
                 type = 'R2',
                 particles = [ P.g, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_324_118,(0,1,0):C.R2GC_363_132})

V_143 = CTVertex(name = 'V_143',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.Xd, P.YS3Qd3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_591_179})

V_144 = CTVertex(name = 'V_144',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.Xm, P.YS3Qd3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_591_179})

V_145 = CTVertex(name = 'V_145',
                 type = 'R2',
                 particles = [ P.W__plus__, P.YS3Qd3, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_668_206,(0,1,0):C.R2GC_669_207})

V_146 = CTVertex(name = 'V_146',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_323_117})

V_147 = CTVertex(name = 'V_147',
                 type = 'R2',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_666_204,(0,0,1):C.R2GC_666_205})

V_148 = CTVertex(name = 'V_148',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_325_119})

V_149 = CTVertex(name = 'V_149',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(2,0,0):C.R2GC_328_123,(2,0,1):C.R2GC_328_124,(1,0,0):C.R2GC_328_123,(1,0,1):C.R2GC_328_124,(0,0,0):C.R2GC_291_94,(0,0,1):C.R2GC_327_122})

V_150 = CTVertex(name = 'V_150',
                 type = 'R2',
                 particles = [ P.a, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_405_141,(0,1,0):C.R2GC_406_142})

V_151 = CTVertex(name = 'V_151',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.u, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_604_192})

V_152 = CTVertex(name = 'V_152',
                 type = 'R2',
                 particles = [ P.Xm, P.u, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_604_192})

V_153 = CTVertex(name = 'V_153',
                 type = 'R2',
                 particles = [ P.a, P.W__plus__, P.YS3Qd1, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_671_208})

V_154 = CTVertex(name = 'V_154',
                 type = 'R2',
                 particles = [ P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu1__tilde__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_672_209,(0,0,1):C.R2GC_672_210})

V_155 = CTVertex(name = 'V_155',
                 type = 'R2',
                 particles = [ P.g, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_324_118,(0,1,0):C.R2GC_363_132})

V_156 = CTVertex(name = 'V_156',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.Xd, P.YS3Qu1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_604_192})

V_157 = CTVertex(name = 'V_157',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.Xm, P.YS3Qu1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_604_192})

V_158 = CTVertex(name = 'V_158',
                 type = 'R2',
                 particles = [ P.a, P.W__minus__, P.YS3Qd1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_671_208})

V_159 = CTVertex(name = 'V_159',
                 type = 'R2',
                 particles = [ P.g, P.W__minus__, P.YS3Qd1__tilde__, P.YS3Qu1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_672_209,(0,0,1):C.R2GC_672_210})

V_160 = CTVertex(name = 'V_160',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_407_143})

V_161 = CTVertex(name = 'V_161',
                 type = 'R2',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,1):C.R2GC_666_204,(0,0,0):C.R2GC_666_205})

V_162 = CTVertex(name = 'V_162',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_410_144})

V_163 = CTVertex(name = 'V_163',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(2,0,0):C.R2GC_328_123,(2,0,1):C.R2GC_328_124,(1,0,0):C.R2GC_328_123,(1,0,1):C.R2GC_328_124,(0,0,0):C.R2GC_291_94,(0,0,1):C.R2GC_327_122})

V_164 = CTVertex(name = 'V_164',
                 type = 'R2',
                 particles = [ P.a, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_405_141,(0,1,0):C.R2GC_406_142})

V_165 = CTVertex(name = 'V_165',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.c, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_596_184})

V_166 = CTVertex(name = 'V_166',
                 type = 'R2',
                 particles = [ P.Xm, P.c, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_596_184})

V_167 = CTVertex(name = 'V_167',
                 type = 'R2',
                 particles = [ P.a, P.W__plus__, P.YS3Qd2, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_671_208})

V_168 = CTVertex(name = 'V_168',
                 type = 'R2',
                 particles = [ P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu2__tilde__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_672_209,(0,0,1):C.R2GC_672_210})

V_169 = CTVertex(name = 'V_169',
                 type = 'R2',
                 particles = [ P.g, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_324_118,(0,1,0):C.R2GC_363_132})

V_170 = CTVertex(name = 'V_170',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.Xd, P.YS3Qu2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_596_184})

V_171 = CTVertex(name = 'V_171',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.Xm, P.YS3Qu2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_596_184})

V_172 = CTVertex(name = 'V_172',
                 type = 'R2',
                 particles = [ P.a, P.W__minus__, P.YS3Qd2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_671_208})

V_173 = CTVertex(name = 'V_173',
                 type = 'R2',
                 particles = [ P.g, P.W__minus__, P.YS3Qd2__tilde__, P.YS3Qu2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_672_209,(0,0,1):C.R2GC_672_210})

V_174 = CTVertex(name = 'V_174',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_407_143})

V_175 = CTVertex(name = 'V_175',
                 type = 'R2',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,1):C.R2GC_666_204,(0,0,0):C.R2GC_666_205})

V_176 = CTVertex(name = 'V_176',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_410_144})

V_177 = CTVertex(name = 'V_177',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(2,0,0):C.R2GC_328_123,(2,0,1):C.R2GC_328_124,(1,0,0):C.R2GC_328_123,(1,0,1):C.R2GC_328_124,(0,0,0):C.R2GC_291_94,(0,0,1):C.R2GC_327_122})

V_178 = CTVertex(name = 'V_178',
                 type = 'R2',
                 particles = [ P.a, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_405_141,(0,1,0):C.R2GC_406_142})

V_179 = CTVertex(name = 'V_179',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.t, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_591_179})

V_180 = CTVertex(name = 'V_180',
                 type = 'R2',
                 particles = [ P.Xm, P.t, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_591_179})

V_181 = CTVertex(name = 'V_181',
                 type = 'R2',
                 particles = [ P.a, P.W__plus__, P.YS3Qd3, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_671_208})

V_182 = CTVertex(name = 'V_182',
                 type = 'R2',
                 particles = [ P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu3__tilde__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_672_209,(0,0,1):C.R2GC_672_210})

V_183 = CTVertex(name = 'V_183',
                 type = 'R2',
                 particles = [ P.g, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_324_118,(0,1,0):C.R2GC_363_132})

V_184 = CTVertex(name = 'V_184',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.Xd, P.YS3Qu3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_591_179})

V_185 = CTVertex(name = 'V_185',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.Xm, P.YS3Qu3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_591_179})

V_186 = CTVertex(name = 'V_186',
                 type = 'R2',
                 particles = [ P.a, P.W__minus__, P.YS3Qd3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_671_208})

V_187 = CTVertex(name = 'V_187',
                 type = 'R2',
                 particles = [ P.g, P.W__minus__, P.YS3Qd3__tilde__, P.YS3Qu3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_672_209,(0,0,1):C.R2GC_672_210})

V_188 = CTVertex(name = 'V_188',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_407_143})

V_189 = CTVertex(name = 'V_189',
                 type = 'R2',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,1):C.R2GC_666_204,(0,0,0):C.R2GC_666_205})

V_190 = CTVertex(name = 'V_190',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_410_144})

V_191 = CTVertex(name = 'V_191',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(2,0,0):C.R2GC_328_123,(2,0,1):C.R2GC_328_124,(1,0,0):C.R2GC_328_123,(1,0,1):C.R2GC_328_124,(0,0,0):C.R2GC_291_94,(0,0,1):C.R2GC_327_122})

V_192 = CTVertex(name = 'V_192',
                 type = 'R2',
                 particles = [ P.a, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_405_141,(0,1,0):C.R2GC_406_142})

V_193 = CTVertex(name = 'V_193',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.u, P.YS3u1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_786_221})

V_194 = CTVertex(name = 'V_194',
                 type = 'R2',
                 particles = [ P.Xm, P.u, P.YS3u1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_786_221})

V_195 = CTVertex(name = 'V_195',
                 type = 'R2',
                 particles = [ P.g, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_324_118,(0,1,0):C.R2GC_363_132})

V_196 = CTVertex(name = 'V_196',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.Xd, P.YS3u1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_786_221})

V_197 = CTVertex(name = 'V_197',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.Xm, P.YS3u1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_786_221})

V_198 = CTVertex(name = 'V_198',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_407_143})

V_199 = CTVertex(name = 'V_199',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_410_144})

V_200 = CTVertex(name = 'V_200',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3u1] ] ],
                 couplings = {(2,0,0):C.R2GC_328_123,(2,0,1):C.R2GC_328_124,(1,0,0):C.R2GC_328_123,(1,0,1):C.R2GC_328_124,(0,0,0):C.R2GC_291_94,(0,0,1):C.R2GC_327_122})

V_201 = CTVertex(name = 'V_201',
                 type = 'R2',
                 particles = [ P.a, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_405_141,(0,1,0):C.R2GC_406_142})

V_202 = CTVertex(name = 'V_202',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.c, P.YS3u2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_597_185})

V_203 = CTVertex(name = 'V_203',
                 type = 'R2',
                 particles = [ P.Xm, P.c, P.YS3u2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_597_185})

V_204 = CTVertex(name = 'V_204',
                 type = 'R2',
                 particles = [ P.g, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_324_118,(0,1,0):C.R2GC_363_132})

V_205 = CTVertex(name = 'V_205',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.Xd, P.YS3u2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_597_185})

V_206 = CTVertex(name = 'V_206',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.Xm, P.YS3u2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_597_185})

V_207 = CTVertex(name = 'V_207',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_407_143})

V_208 = CTVertex(name = 'V_208',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_410_144})

V_209 = CTVertex(name = 'V_209',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3u2] ] ],
                 couplings = {(2,0,0):C.R2GC_328_123,(2,0,1):C.R2GC_328_124,(1,0,0):C.R2GC_328_123,(1,0,1):C.R2GC_328_124,(0,0,0):C.R2GC_291_94,(0,0,1):C.R2GC_327_122})

V_210 = CTVertex(name = 'V_210',
                 type = 'R2',
                 particles = [ P.a, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_405_141,(0,1,0):C.R2GC_406_142})

V_211 = CTVertex(name = 'V_211',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.t, P.YS3u3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_779_218})

V_212 = CTVertex(name = 'V_212',
                 type = 'R2',
                 particles = [ P.Xm, P.t, P.YS3u3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_779_218})

V_213 = CTVertex(name = 'V_213',
                 type = 'R2',
                 particles = [ P.g, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_324_118,(0,1,0):C.R2GC_363_132})

V_214 = CTVertex(name = 'V_214',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.Xd, P.YS3u3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_779_218})

V_215 = CTVertex(name = 'V_215',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.Xm, P.YS3u3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_779_218})

V_216 = CTVertex(name = 'V_216',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_407_143})

V_217 = CTVertex(name = 'V_217',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_410_144})

V_218 = CTVertex(name = 'V_218',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3u3] ] ],
                 couplings = {(2,0,0):C.R2GC_328_123,(2,0,1):C.R2GC_328_124,(1,0,0):C.R2GC_328_123,(1,0,1):C.R2GC_328_124,(0,0,0):C.R2GC_291_94,(0,0,1):C.R2GC_327_122})

V_219 = CTVertex(name = 'V_219',
                 type = 'R2',
                 particles = [ P.YF3Qd1__tilde__, P.YF3Qd1, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_533_167})

V_220 = CTVertex(name = 'V_220',
                 type = 'R2',
                 particles = [ P.YF3Qd2__tilde__, P.YF3Qd2, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_533_167})

V_221 = CTVertex(name = 'V_221',
                 type = 'R2',
                 particles = [ P.YF3Qd3__tilde__, P.YF3Qd3, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_533_167})

V_222 = CTVertex(name = 'V_222',
                 type = 'R2',
                 particles = [ P.YF3Qu1__tilde__, P.YF3Qu1, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_556_171})

V_223 = CTVertex(name = 'V_223',
                 type = 'R2',
                 particles = [ P.YF3Qu2__tilde__, P.YF3Qu2, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_556_171})

V_224 = CTVertex(name = 'V_224',
                 type = 'R2',
                 particles = [ P.YF3Qu3__tilde__, P.YF3Qu3, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_556_171})

V_225 = CTVertex(name = 'V_225',
                 type = 'R2',
                 particles = [ P.YF3d1__tilde__, P.YF3d1, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_516_163})

V_226 = CTVertex(name = 'V_226',
                 type = 'R2',
                 particles = [ P.YF3d2__tilde__, P.YF3d2, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_516_163})

V_227 = CTVertex(name = 'V_227',
                 type = 'R2',
                 particles = [ P.YF3d3__tilde__, P.YF3d3, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_516_163})

V_228 = CTVertex(name = 'V_228',
                 type = 'R2',
                 particles = [ P.YF3u1__tilde__, P.YF3u1, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_579_175})

V_229 = CTVertex(name = 'V_229',
                 type = 'R2',
                 particles = [ P.YF3u2__tilde__, P.YF3u2, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_579_175})

V_230 = CTVertex(name = 'V_230',
                 type = 'R2',
                 particles = [ P.YF3u3__tilde__, P.YF3u3, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_579_175})

V_231 = CTVertex(name = 'V_231',
                 type = 'R2',
                 particles = [ P.Z, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_330_126})

V_232 = CTVertex(name = 'V_232',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_331_127})

V_233 = CTVertex(name = 'V_233',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_332_128})

V_234 = CTVertex(name = 'V_234',
                 type = 'R2',
                 particles = [ P.Z, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_330_126})

V_235 = CTVertex(name = 'V_235',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_331_127})

V_236 = CTVertex(name = 'V_236',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_332_128})

V_237 = CTVertex(name = 'V_237',
                 type = 'R2',
                 particles = [ P.Z, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_330_126})

V_238 = CTVertex(name = 'V_238',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_331_127})

V_239 = CTVertex(name = 'V_239',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_332_128})

V_240 = CTVertex(name = 'V_240',
                 type = 'R2',
                 particles = [ P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_370_134})

V_241 = CTVertex(name = 'V_241',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_371_135})

V_242 = CTVertex(name = 'V_242',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_372_136})

V_243 = CTVertex(name = 'V_243',
                 type = 'R2',
                 particles = [ P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_370_134})

V_244 = CTVertex(name = 'V_244',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_371_135})

V_245 = CTVertex(name = 'V_245',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_372_136})

V_246 = CTVertex(name = 'V_246',
                 type = 'R2',
                 particles = [ P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_370_134})

V_247 = CTVertex(name = 'V_247',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_371_135})

V_248 = CTVertex(name = 'V_248',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_372_136})

V_249 = CTVertex(name = 'V_249',
                 type = 'R2',
                 particles = [ P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_415_146})

V_250 = CTVertex(name = 'V_250',
                 type = 'R2',
                 particles = [ P.W__plus__, P.Z, P.YS3Qd1, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_663_203})

V_251 = CTVertex(name = 'V_251',
                 type = 'R2',
                 particles = [ P.W__minus__, P.Z, P.YS3Qd1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_663_203})

V_252 = CTVertex(name = 'V_252',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_416_147})

V_253 = CTVertex(name = 'V_253',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_417_148})

V_254 = CTVertex(name = 'V_254',
                 type = 'R2',
                 particles = [ P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_415_146})

V_255 = CTVertex(name = 'V_255',
                 type = 'R2',
                 particles = [ P.W__plus__, P.Z, P.YS3Qd2, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_663_203})

V_256 = CTVertex(name = 'V_256',
                 type = 'R2',
                 particles = [ P.W__minus__, P.Z, P.YS3Qd2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_663_203})

V_257 = CTVertex(name = 'V_257',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_416_147})

V_258 = CTVertex(name = 'V_258',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_417_148})

V_259 = CTVertex(name = 'V_259',
                 type = 'R2',
                 particles = [ P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_415_146})

V_260 = CTVertex(name = 'V_260',
                 type = 'R2',
                 particles = [ P.W__plus__, P.Z, P.YS3Qd3, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_663_203})

V_261 = CTVertex(name = 'V_261',
                 type = 'R2',
                 particles = [ P.W__minus__, P.Z, P.YS3Qd3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_663_203})

V_262 = CTVertex(name = 'V_262',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_416_147})

V_263 = CTVertex(name = 'V_263',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_417_148})

V_264 = CTVertex(name = 'V_264',
                 type = 'R2',
                 particles = [ P.Z, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_460_153})

V_265 = CTVertex(name = 'V_265',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_461_154})

V_266 = CTVertex(name = 'V_266',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_462_155})

V_267 = CTVertex(name = 'V_267',
                 type = 'R2',
                 particles = [ P.Z, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_460_153})

V_268 = CTVertex(name = 'V_268',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_461_154})

V_269 = CTVertex(name = 'V_269',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_462_155})

V_270 = CTVertex(name = 'V_270',
                 type = 'R2',
                 particles = [ P.Z, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_460_153})

V_271 = CTVertex(name = 'V_271',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_461_154})

V_272 = CTVertex(name = 'V_272',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_462_155})

V_273 = CTVertex(name = 'V_273',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_333_129})

V_274 = CTVertex(name = 'V_274',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_333_129})

V_275 = CTVertex(name = 'V_275',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_333_129})

V_276 = CTVertex(name = 'V_276',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_373_137})

V_277 = CTVertex(name = 'V_277',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_373_137})

V_278 = CTVertex(name = 'V_278',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_373_137})

V_279 = CTVertex(name = 'V_279',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_418_149})

V_280 = CTVertex(name = 'V_280',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_418_149})

V_281 = CTVertex(name = 'V_281',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_418_149})

V_282 = CTVertex(name = 'V_282',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_463_156})

V_283 = CTVertex(name = 'V_283',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_463_156})

V_284 = CTVertex(name = 'V_284',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_463_156})

V_285 = CTVertex(name = 'V_285',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.YF3Qu1, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.u, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_607_195})

V_286 = CTVertex(name = 'V_286',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.YF3Qd1, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_607_195})

V_287 = CTVertex(name = 'V_287',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.YF3Qu2, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_599_187})

V_288 = CTVertex(name = 'V_288',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.YF3Qd2, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_599_187})

V_289 = CTVertex(name = 'V_289',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.YF3Qu3, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.t, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_594_182})

V_290 = CTVertex(name = 'V_290',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.YF3Qd3, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_594_182})

V_291 = CTVertex(name = 'V_291',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.YF3Qu1, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.u, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_607_195})

V_292 = CTVertex(name = 'V_292',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.YF3Qd1, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_607_195})

V_293 = CTVertex(name = 'V_293',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.YF3Qu2, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_599_187})

V_294 = CTVertex(name = 'V_294',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.YF3Qd2, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_599_187})

V_295 = CTVertex(name = 'V_295',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.YF3Qu3, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.t, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_594_182})

V_296 = CTVertex(name = 'V_296',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.YF3Qd3, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_594_182})

V_297 = CTVertex(name = 'V_297',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_312_113})

V_298 = CTVertex(name = 'V_298',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_312_113})

V_299 = CTVertex(name = 'V_299',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_312_113})

V_300 = CTVertex(name = 'V_300',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_304_106})

V_301 = CTVertex(name = 'V_301',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_304_106})

V_302 = CTVertex(name = 'V_302',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_304_106})

V_303 = CTVertex(name = 'V_303',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_305_107})

V_304 = CTVertex(name = 'V_304',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_305_107})

V_305 = CTVertex(name = 'V_305',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_305_107})

V_306 = CTVertex(name = 'V_306',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_305_107})

V_307 = CTVertex(name = 'V_307',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_305_107})

V_308 = CTVertex(name = 'V_308',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_305_107})

V_309 = CTVertex(name = 'V_309',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_598_186})

V_310 = CTVertex(name = 'V_310',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_598_186})

V_311 = CTVertex(name = 'V_311',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_598_186})

V_312 = CTVertex(name = 'V_312',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_598_186})

V_313 = CTVertex(name = 'V_313',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_598_186})

V_314 = CTVertex(name = 'V_314',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_598_186})

V_315 = CTVertex(name = 'V_315',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV7 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_314_114,(0,1,0):C.R2GC_308_110})

V_316 = CTVertex(name = 'V_316',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV7 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_314_114,(0,1,0):C.R2GC_308_110})

V_317 = CTVertex(name = 'V_317',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV7 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_314_114,(0,1,0):C.R2GC_308_110})

V_318 = CTVertex(name = 'V_318',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV4 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_307_109,(0,1,0):C.R2GC_308_110})

V_319 = CTVertex(name = 'V_319',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV4 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_307_109,(0,1,0):C.R2GC_308_110})

V_320 = CTVertex(name = 'V_320',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV4 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_307_109,(0,1,0):C.R2GC_308_110})

V_321 = CTVertex(name = 'V_321',
                 type = 'R2',
                 particles = [ P.YF3Qu1__tilde__, P.u, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.u, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_607_195})

V_322 = CTVertex(name = 'V_322',
                 type = 'R2',
                 particles = [ P.YF3Qd1__tilde__, P.d, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_607_195})

V_323 = CTVertex(name = 'V_323',
                 type = 'R2',
                 particles = [ P.YF3Qu2__tilde__, P.c, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_599_187})

V_324 = CTVertex(name = 'V_324',
                 type = 'R2',
                 particles = [ P.YF3Qd2__tilde__, P.s, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_599_187})

V_325 = CTVertex(name = 'V_325',
                 type = 'R2',
                 particles = [ P.YF3Qu3__tilde__, P.t, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.t, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_594_182})

V_326 = CTVertex(name = 'V_326',
                 type = 'R2',
                 particles = [ P.YF3Qd3__tilde__, P.b, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_594_182})

V_327 = CTVertex(name = 'V_327',
                 type = 'R2',
                 particles = [ P.YF3Qu1__tilde__, P.u, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.u, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_607_195})

V_328 = CTVertex(name = 'V_328',
                 type = 'R2',
                 particles = [ P.YF3Qd1__tilde__, P.d, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_607_195})

V_329 = CTVertex(name = 'V_329',
                 type = 'R2',
                 particles = [ P.YF3Qu2__tilde__, P.c, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_599_187})

V_330 = CTVertex(name = 'V_330',
                 type = 'R2',
                 particles = [ P.YF3Qd2__tilde__, P.s, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_599_187})

V_331 = CTVertex(name = 'V_331',
                 type = 'R2',
                 particles = [ P.YF3Qu3__tilde__, P.t, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.t, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_594_182})

V_332 = CTVertex(name = 'V_332',
                 type = 'R2',
                 particles = [ P.YF3Qd3__tilde__, P.b, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_594_182})

V_333 = CTVertex(name = 'V_333',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.YF3d1, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_605_193})

V_334 = CTVertex(name = 'V_334',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.YF3d2, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_769_212})

V_335 = CTVertex(name = 'V_335',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.YF3d3, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_592_180})

V_336 = CTVertex(name = 'V_336',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.YF3u1, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_789_222})

V_337 = CTVertex(name = 'V_337',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.YF3u2, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_601_189})

V_338 = CTVertex(name = 'V_338',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.YF3u3, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_782_219})

V_339 = CTVertex(name = 'V_339',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.YF3d1, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_605_193})

V_340 = CTVertex(name = 'V_340',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.YF3d2, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_769_212})

V_341 = CTVertex(name = 'V_341',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.YF3d3, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_592_180})

V_342 = CTVertex(name = 'V_342',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.YF3u1, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_789_222})

V_343 = CTVertex(name = 'V_343',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.YF3u2, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_601_189})

V_344 = CTVertex(name = 'V_344',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.YF3u3, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_782_219})

V_345 = CTVertex(name = 'V_345',
                 type = 'R2',
                 particles = [ P.YF3d1__tilde__, P.d, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_605_193})

V_346 = CTVertex(name = 'V_346',
                 type = 'R2',
                 particles = [ P.YF3d2__tilde__, P.s, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_769_212})

V_347 = CTVertex(name = 'V_347',
                 type = 'R2',
                 particles = [ P.YF3d3__tilde__, P.b, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_592_180})

V_348 = CTVertex(name = 'V_348',
                 type = 'R2',
                 particles = [ P.YF3u1__tilde__, P.u, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_789_222})

V_349 = CTVertex(name = 'V_349',
                 type = 'R2',
                 particles = [ P.YF3u2__tilde__, P.c, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_601_189})

V_350 = CTVertex(name = 'V_350',
                 type = 'R2',
                 particles = [ P.YF3u3__tilde__, P.t, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_782_219})

V_351 = CTVertex(name = 'V_351',
                 type = 'R2',
                 particles = [ P.YF3d1__tilde__, P.d, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_605_193})

V_352 = CTVertex(name = 'V_352',
                 type = 'R2',
                 particles = [ P.YF3d2__tilde__, P.s, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_769_212})

V_353 = CTVertex(name = 'V_353',
                 type = 'R2',
                 particles = [ P.YF3d3__tilde__, P.b, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_592_180})

V_354 = CTVertex(name = 'V_354',
                 type = 'R2',
                 particles = [ P.YF3u1__tilde__, P.u, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_789_222})

V_355 = CTVertex(name = 'V_355',
                 type = 'R2',
                 particles = [ P.YF3u2__tilde__, P.c, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_601_189})

V_356 = CTVertex(name = 'V_356',
                 type = 'R2',
                 particles = [ P.YF3u3__tilde__, P.t, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_782_219})

V_357 = CTVertex(name = 'V_357',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_303_105})

V_358 = CTVertex(name = 'V_358',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_303_105})

V_359 = CTVertex(name = 'V_359',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_502_159,(0,1,0):C.R2GC_303_105})

V_360 = CTVertex(name = 'V_360',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_303_105})

V_361 = CTVertex(name = 'V_361',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_303_105})

V_362 = CTVertex(name = 'V_362',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_306_108,(0,1,0):C.R2GC_303_105})

V_363 = CTVertex(name = 'V_363',
                 type = 'R2',
                 particles = [ P.YF3Qu1__tilde__, P.YF3Qu1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_551_170,(0,1,0):C.R2GC_303_105})

V_364 = CTVertex(name = 'V_364',
                 type = 'R2',
                 particles = [ P.YF3Qu2__tilde__, P.YF3Qu2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_560_172,(0,1,0):C.R2GC_303_105})

V_365 = CTVertex(name = 'V_365',
                 type = 'R2',
                 particles = [ P.YF3Qu3__tilde__, P.YF3Qu3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_569_173,(0,1,0):C.R2GC_303_105})

V_366 = CTVertex(name = 'V_366',
                 type = 'R2',
                 particles = [ P.YF3Qd1__tilde__, P.YF3Qd1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_530_166,(0,1,0):C.R2GC_303_105})

V_367 = CTVertex(name = 'V_367',
                 type = 'R2',
                 particles = [ P.YF3Qd2__tilde__, P.YF3Qd2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_537_168,(0,1,0):C.R2GC_303_105})

V_368 = CTVertex(name = 'V_368',
                 type = 'R2',
                 particles = [ P.YF3Qd3__tilde__, P.YF3Qd3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_544_169,(0,1,0):C.R2GC_303_105})

V_369 = CTVertex(name = 'V_369',
                 type = 'R2',
                 particles = [ P.YF3u1__tilde__, P.YF3u1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_578_174,(0,1,0):C.R2GC_303_105})

V_370 = CTVertex(name = 'V_370',
                 type = 'R2',
                 particles = [ P.YF3u2__tilde__, P.YF3u2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_583_176,(0,1,0):C.R2GC_303_105})

V_371 = CTVertex(name = 'V_371',
                 type = 'R2',
                 particles = [ P.YF3u3__tilde__, P.YF3u3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_588_177,(0,1,0):C.R2GC_303_105})

V_372 = CTVertex(name = 'V_372',
                 type = 'R2',
                 particles = [ P.YF3d1__tilde__, P.YF3d1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_515_162,(0,1,0):C.R2GC_303_105})

V_373 = CTVertex(name = 'V_373',
                 type = 'R2',
                 particles = [ P.YF3d2__tilde__, P.YF3d2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_520_164,(0,1,0):C.R2GC_303_105})

V_374 = CTVertex(name = 'V_374',
                 type = 'R2',
                 particles = [ P.YF3d3__tilde__, P.YF3d3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_525_165,(0,1,0):C.R2GC_303_105})

V_375 = CTVertex(name = 'V_375',
                 type = 'R2',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV1, L.VV2, L.VV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u], [P.YF3d1], [P.YF3d2], [P.YF3d3], [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3], [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3], [P.YF3u1], [P.YF3u2], [P.YF3u3] ], [ [P.g] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ] ],
                 couplings = {(0,2,2):C.R2GC_139_1,(0,0,0):C.R2GC_147_15,(0,0,3):C.R2GC_147_16,(0,0,4):C.R2GC_147_17,(0,0,5):C.R2GC_147_18,(0,0,6):C.R2GC_147_19,(0,0,7):C.R2GC_147_20,(0,0,8):C.R2GC_147_21,(0,0,9):C.R2GC_147_22,(0,0,10):C.R2GC_147_23,(0,0,11):C.R2GC_147_24,(0,0,12):C.R2GC_147_25,(0,0,13):C.R2GC_147_26,(0,0,14):C.R2GC_147_27,(0,0,15):C.R2GC_147_28,(0,1,1):C.R2GC_144_10})

V_376 = CTVertex(name = 'V_376',
                 type = 'R2',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_414_145,(0,1,0):C.R2GC_321_115})

V_377 = CTVertex(name = 'V_377',
                 type = 'R2',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_429_150,(0,1,0):C.R2GC_321_115})

V_378 = CTVertex(name = 'V_378',
                 type = 'R2',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_444_151,(0,1,0):C.R2GC_321_115})

V_379 = CTVertex(name = 'V_379',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_369_133,(0,1,0):C.R2GC_321_115})

V_380 = CTVertex(name = 'V_380',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_384_139,(0,1,0):C.R2GC_321_115})

V_381 = CTVertex(name = 'V_381',
                 type = 'R2',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_399_140,(0,1,0):C.R2GC_321_115})

V_382 = CTVertex(name = 'V_382',
                 type = 'R2',
                 particles = [ P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_459_152,(0,1,0):C.R2GC_321_115})

V_383 = CTVertex(name = 'V_383',
                 type = 'R2',
                 particles = [ P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_474_157,(0,1,0):C.R2GC_321_115})

V_384 = CTVertex(name = 'V_384',
                 type = 'R2',
                 particles = [ P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_489_158,(0,1,0):C.R2GC_321_115})

V_385 = CTVertex(name = 'V_385',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_329_125,(0,1,0):C.R2GC_321_115})

V_386 = CTVertex(name = 'V_386',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_342_130,(0,1,0):C.R2GC_321_115})

V_387 = CTVertex(name = 'V_387',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_355_131,(0,1,0):C.R2GC_321_115})

V_388 = CTVertex(name = 'V_388',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVV1 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_142_6,(0,0,1):C.R2GC_142_7})

V_389 = CTVertex(name = 'V_389',
                 type = 'R2',
                 particles = [ P.g, P.g, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_140_2,(0,0,1):C.R2GC_140_3})

V_390 = CTVertex(name = 'V_390',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Xv, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV10 ],
                 loop_particles = [ [ [P.b, P.YF3d3] ], [ [P.b, P.YF3Qd3], [P.t, P.YF3Qu3] ], [ [P.c, P.YF3Qu2], [P.s, P.YF3Qd2] ], [ [P.c, P.YF3u2] ], [ [P.d, P.YF3d1] ], [ [P.d, P.YF3Qd1], [P.u, P.YF3Qu1] ], [ [P.s, P.YF3d2] ], [ [P.t, P.YF3u3] ], [ [P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_153_57,(0,0,1):C.R2GC_153_58,(0,0,2):C.R2GC_153_59,(0,0,3):C.R2GC_153_60,(0,0,4):C.R2GC_153_61,(0,0,5):C.R2GC_153_62,(0,0,6):C.R2GC_153_63,(0,0,7):C.R2GC_153_64,(0,0,8):C.R2GC_153_65})

V_391 = CTVertex(name = 'V_391',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Xv, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV10 ],
                 loop_particles = [ [ [P.b, P.YF3d3] ], [ [P.b, P.YF3Qd3], [P.t, P.YF3Qu3] ], [ [P.c, P.YF3Qu2], [P.s, P.YF3Qd2] ], [ [P.c, P.YF3u2] ], [ [P.d, P.YF3d1] ], [ [P.d, P.YF3Qd1], [P.u, P.YF3Qu1] ], [ [P.s, P.YF3d2] ], [ [P.t, P.YF3u3] ], [ [P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_152_48,(0,0,1):C.R2GC_152_49,(0,0,2):C.R2GC_152_50,(0,0,3):C.R2GC_152_51,(0,0,4):C.R2GC_152_52,(0,0,5):C.R2GC_152_53,(0,0,6):C.R2GC_152_54,(0,0,7):C.R2GC_152_55,(0,0,8):C.R2GC_152_56})

V_392 = CTVertex(name = 'V_392',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Xv, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV10 ],
                 loop_particles = [ [ [P.b, P.YF3d3] ], [ [P.b, P.YF3Qd3], [P.t, P.YF3Qu3] ], [ [P.c, P.YF3Qu2], [P.s, P.YF3Qd2] ], [ [P.c, P.YF3u2] ], [ [P.d, P.YF3d1] ], [ [P.d, P.YF3Qd1], [P.u, P.YF3Qu1] ], [ [P.s, P.YF3d2] ], [ [P.t, P.YF3u3] ], [ [P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_152_48,(0,0,1):C.R2GC_152_49,(0,0,2):C.R2GC_152_50,(0,0,3):C.R2GC_152_51,(0,0,4):C.R2GC_152_52,(0,0,5):C.R2GC_152_53,(0,0,6):C.R2GC_152_54,(0,0,7):C.R2GC_152_55,(0,0,8):C.R2GC_152_56})

V_393 = CTVertex(name = 'V_393',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Xw__tilde__, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV10 ],
                 loop_particles = [ [ [P.b, P.YF3d3] ], [ [P.b, P.YF3Qd3], [P.t, P.YF3Qu3] ], [ [P.c, P.YF3Qu2], [P.s, P.YF3Qd2] ], [ [P.c, P.YF3u2] ], [ [P.d, P.YF3d1] ], [ [P.d, P.YF3Qd1], [P.u, P.YF3Qu1] ], [ [P.s, P.YF3d2] ], [ [P.t, P.YF3u3] ], [ [P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_152_48,(0,0,1):C.R2GC_152_49,(0,0,2):C.R2GC_152_50,(0,0,3):C.R2GC_152_51,(0,0,4):C.R2GC_152_52,(0,0,5):C.R2GC_152_53,(0,0,6):C.R2GC_152_54,(0,0,7):C.R2GC_152_55,(0,0,8):C.R2GC_152_56})

V_394 = CTVertex(name = 'V_394',
                 type = 'R2',
                 particles = [ P.a, P.a, P.g, P.g ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVVV10 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s], [P.YF3d1], [P.YF3d2], [P.YF3d3], [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3] ], [ [P.c], [P.t], [P.u], [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3], [P.YF3u1], [P.YF3u2], [P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_145_11,(0,0,1):C.R2GC_145_12})

V_395 = CTVertex(name = 'V_395',
                 type = 'R2',
                 particles = [ P.a, P.g, P.g, P.Z ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VVVV10 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ], [ [P.YF3d1], [P.YF3d2], [P.YF3d3] ], [ [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3] ], [ [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3] ], [ [P.YF3u1], [P.YF3u2], [P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_148_29,(0,0,1):C.R2GC_148_30,(0,0,2):C.R2GC_148_31,(0,0,3):C.R2GC_148_32,(0,0,4):C.R2GC_148_33,(0,0,5):C.R2GC_148_34})

V_396 = CTVertex(name = 'V_396',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Z, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV10 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ], [ [P.YF3d1], [P.YF3d2], [P.YF3d3] ], [ [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3] ], [ [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3] ], [ [P.YF3u1], [P.YF3u2], [P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_150_41,(0,0,1):C.R2GC_150_42,(0,0,2):C.R2GC_150_43,(0,0,3):C.R2GC_150_44,(0,0,4):C.R2GC_150_45,(0,0,5):C.R2GC_150_46})

V_397 = CTVertex(name = 'V_397',
                 type = 'R2',
                 particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV10 ],
                 loop_particles = [ [ [P.b, P.t], [P.c, P.s], [P.d, P.u] ], [ [P.YF3Qd1, P.YF3Qu1], [P.YF3Qd2, P.YF3Qu2], [P.YF3Qd3, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_156_84,(0,0,1):C.R2GC_156_85})

V_398 = CTVertex(name = 'V_398',
                 type = 'R2',
                 particles = [ P.a, P.g, P.g, P.g ],
                 color = [ 'd(2,3,4)' ],
                 lorentz = [ L.VVVV10 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s], [P.YF3d1], [P.YF3d2], [P.YF3d3], [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3] ], [ [P.c], [P.t], [P.u], [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3], [P.YF3u1], [P.YF3u2], [P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_146_13,(0,0,1):C.R2GC_146_14})

V_399 = CTVertex(name = 'V_399',
                 type = 'R2',
                 particles = [ P.g, P.g, P.g, P.Z ],
                 color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                 lorentz = [ L.VVVV1, L.VVVV10 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ], [ [P.YF3d1], [P.YF3d2], [P.YF3d3] ], [ [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3] ], [ [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3] ], [ [P.YF3u1], [P.YF3u2], [P.YF3u3] ] ],
                 couplings = {(1,0,0):C.R2GC_143_8,(1,0,1):C.R2GC_143_9,(0,1,0):C.R2GC_149_35,(0,1,1):C.R2GC_149_36,(0,1,2):C.R2GC_149_37,(0,1,3):C.R2GC_149_38,(0,1,4):C.R2GC_149_39,(0,1,5):C.R2GC_149_40})

V_400 = CTVertex(name = 'V_400',
                 type = 'R2',
                 particles = [ P.g, P.g, P.H, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_141_4,(0,0,1):C.R2GC_141_5})

V_401 = CTVertex(name = 'V_401',
                 type = 'R2',
                 particles = [ P.g, P.g, P.G0, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_141_4,(0,0,1):C.R2GC_141_5})

V_402 = CTVertex(name = 'V_402',
                 type = 'R2',
                 particles = [ P.g, P.g, P.G__minus__, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_151_47})

V_403 = CTVertex(name = 'V_403',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Xs, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.YF3d3] ], [ [P.b, P.YF3Qd3], [P.t, P.YF3Qu3] ], [ [P.c, P.YF3Qu2], [P.s, P.YF3Qd2] ], [ [P.c, P.YF3u2] ], [ [P.d, P.YF3d1] ], [ [P.d, P.YF3Qd1], [P.u, P.YF3Qu1] ], [ [P.s, P.YF3d2] ], [ [P.t, P.YF3u3] ], [ [P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_155_75,(0,0,1):C.R2GC_155_76,(0,0,2):C.R2GC_155_77,(0,0,3):C.R2GC_155_78,(0,0,4):C.R2GC_155_79,(0,0,5):C.R2GC_155_80,(0,0,6):C.R2GC_155_81,(0,0,7):C.R2GC_155_82,(0,0,8):C.R2GC_155_83})

V_404 = CTVertex(name = 'V_404',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Xc, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.YF3d3] ], [ [P.b, P.YF3Qd3], [P.t, P.YF3Qu3] ], [ [P.c, P.YF3Qu2], [P.s, P.YF3Qd2] ], [ [P.c, P.YF3u2] ], [ [P.d, P.YF3d1] ], [ [P.d, P.YF3Qd1], [P.u, P.YF3Qu1] ], [ [P.s, P.YF3d2] ], [ [P.t, P.YF3u3] ], [ [P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_154_66,(0,0,1):C.R2GC_154_67,(0,0,2):C.R2GC_154_68,(0,0,3):C.R2GC_154_69,(0,0,4):C.R2GC_154_70,(0,0,5):C.R2GC_154_71,(0,0,6):C.R2GC_154_72,(0,0,7):C.R2GC_154_73,(0,0,8):C.R2GC_154_74})

V_405 = CTVertex(name = 'V_405',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Xc__tilde__, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.YF3d3] ], [ [P.b, P.YF3Qd3], [P.t, P.YF3Qu3] ], [ [P.c, P.YF3Qu2], [P.s, P.YF3Qd2] ], [ [P.c, P.YF3u2] ], [ [P.d, P.YF3d1] ], [ [P.d, P.YF3Qd1], [P.u, P.YF3Qu1] ], [ [P.s, P.YF3d2] ], [ [P.t, P.YF3u3] ], [ [P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_154_66,(0,0,1):C.R2GC_154_67,(0,0,2):C.R2GC_154_68,(0,0,3):C.R2GC_154_69,(0,0,4):C.R2GC_154_70,(0,0,5):C.R2GC_154_71,(0,0,6):C.R2GC_154_72,(0,0,7):C.R2GC_154_73,(0,0,8):C.R2GC_154_74})

V_406 = CTVertex(name = 'V_406',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Xc__tilde__, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.YF3d3] ], [ [P.b, P.YF3Qd3], [P.t, P.YF3Qu3] ], [ [P.c, P.YF3Qu2], [P.s, P.YF3Qd2] ], [ [P.c, P.YF3u2] ], [ [P.d, P.YF3d1] ], [ [P.d, P.YF3Qd1], [P.u, P.YF3Qu1] ], [ [P.s, P.YF3d2] ], [ [P.t, P.YF3u3] ], [ [P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_154_66,(0,0,1):C.R2GC_154_67,(0,0,2):C.R2GC_154_68,(0,0,3):C.R2GC_154_69,(0,0,4):C.R2GC_154_70,(0,0,5):C.R2GC_154_71,(0,0,6):C.R2GC_154_72,(0,0,7):C.R2GC_154_73,(0,0,8):C.R2GC_154_74})

V_407 = CTVertex(name = 'V_407',
                 type = 'R2',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3Qu1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_326_120,(1,0,3):C.R2GC_326_121,(1,0,0):C.R2GC_800_230,(1,0,5):C.R2GC_800_231,(1,0,1):C.R2GC_800_232,(1,0,4):C.R2GC_800_233,(0,0,2):C.R2GC_326_120,(0,0,3):C.R2GC_326_121,(0,0,0):C.R2GC_800_230,(0,0,5):C.R2GC_800_231,(0,0,1):C.R2GC_800_232,(0,0,4):C.R2GC_800_233})

V_408 = CTVertex(name = 'V_408',
                 type = 'R2',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3Qu1, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qu1, P.YS3Qu2] ], [ [P.g, P.YS3Qu1, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_873_298,(1,0,8):C.R2GC_873_299,(1,0,1):C.R2GC_873_300,(1,0,7):C.R2GC_873_301,(1,0,2):C.R2GC_873_302,(1,0,6):C.R2GC_873_303,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_872_292,(0,0,8):C.R2GC_872_293,(0,0,1):C.R2GC_872_294,(0,0,7):C.R2GC_872_295,(0,0,2):C.R2GC_872_296,(0,0,6):C.R2GC_872_297})

V_409 = CTVertex(name = 'V_409',
                 type = 'R2',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3Qu2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_326_120,(1,0,3):C.R2GC_326_121,(1,0,0):C.R2GC_800_230,(1,0,5):C.R2GC_800_231,(1,0,1):C.R2GC_800_232,(1,0,4):C.R2GC_800_233,(0,0,2):C.R2GC_326_120,(0,0,3):C.R2GC_326_121,(0,0,0):C.R2GC_800_230,(0,0,5):C.R2GC_800_231,(0,0,1):C.R2GC_800_232,(0,0,4):C.R2GC_800_233})

V_410 = CTVertex(name = 'V_410',
                 type = 'R2',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qu1, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qu1, P.YS3Qu3] ], [ [P.g, P.YS3Qu1, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_873_298,(1,0,8):C.R2GC_873_299,(1,0,1):C.R2GC_873_300,(1,0,7):C.R2GC_873_301,(1,0,2):C.R2GC_873_302,(1,0,6):C.R2GC_873_303,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_872_292,(0,0,8):C.R2GC_872_293,(0,0,1):C.R2GC_872_294,(0,0,7):C.R2GC_872_295,(0,0,2):C.R2GC_872_296,(0,0,6):C.R2GC_872_297})

V_411 = CTVertex(name = 'V_411',
                 type = 'R2',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qu2, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qu2], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qu2, P.YS3Qu3] ], [ [P.g, P.YS3Qu2, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qu2, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_873_298,(1,0,8):C.R2GC_873_299,(1,0,1):C.R2GC_873_300,(1,0,7):C.R2GC_873_301,(1,0,2):C.R2GC_873_302,(1,0,6):C.R2GC_873_303,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_872_292,(0,0,8):C.R2GC_872_293,(0,0,1):C.R2GC_872_294,(0,0,7):C.R2GC_872_295,(0,0,2):C.R2GC_872_296,(0,0,6):C.R2GC_872_297})

V_412 = CTVertex(name = 'V_412',
                 type = 'R2',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3__tilde__, P.YS3Qu3, P.YS3Qu3 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_326_120,(1,0,3):C.R2GC_326_121,(1,0,0):C.R2GC_800_230,(1,0,5):C.R2GC_800_231,(1,0,1):C.R2GC_800_232,(1,0,4):C.R2GC_800_233,(0,0,2):C.R2GC_326_120,(0,0,3):C.R2GC_326_121,(0,0,0):C.R2GC_800_230,(0,0,5):C.R2GC_800_231,(0,0,1):C.R2GC_800_232,(0,0,4):C.R2GC_800_233})

V_413 = CTVertex(name = 'V_413',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qu1] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,7):C.R2GC_610_201,(1,0,8):C.R2GC_610_202,(1,0,0):C.R2GC_829_270,(1,0,4):C.R2GC_806_236,(1,0,11):C.R2GC_867_287,(1,0,1):C.R2GC_829_272,(1,0,5):C.R2GC_867_288,(1,0,10):C.R2GC_867_289,(1,0,2):C.R2GC_829_274,(1,0,6):C.R2GC_867_290,(1,0,9):C.R2GC_867_291,(0,0,3):C.R2GC_609_197,(0,0,7):C.R2GC_609_198,(0,0,8):C.R2GC_609_199,(0,0,0):C.R2GC_794_224,(0,0,4):C.R2GC_807_239,(0,0,11):C.R2GC_866_282,(0,0,1):C.R2GC_145_11,(0,0,5):C.R2GC_866_283,(0,0,10):C.R2GC_866_284,(0,0,2):C.R2GC_828_268,(0,0,6):C.R2GC_866_285,(0,0,9):C.R2GC_866_286})

V_414 = CTVertex(name = 'V_414',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qd1, P.YS3Qu2] ], [ [P.g, P.YS3Qd1, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_829_270,(1,0,8):C.R2GC_867_287,(1,0,1):C.R2GC_829_272,(1,0,7):C.R2GC_867_289,(1,0,2):C.R2GC_829_274,(1,0,6):C.R2GC_867_291,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_794_224,(0,0,8):C.R2GC_866_282,(0,0,1):C.R2GC_145_11,(0,0,7):C.R2GC_866_284,(0,0,2):C.R2GC_828_268,(0,0,6):C.R2GC_866_286})

V_415 = CTVertex(name = 'V_415',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qd1, P.YS3Qu3] ], [ [P.g, P.YS3Qd1, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_829_270,(1,0,8):C.R2GC_867_287,(1,0,1):C.R2GC_829_272,(1,0,7):C.R2GC_867_289,(1,0,2):C.R2GC_829_274,(1,0,6):C.R2GC_867_291,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_794_224,(0,0,8):C.R2GC_866_282,(0,0,1):C.R2GC_145_11,(0,0,7):C.R2GC_866_284,(0,0,2):C.R2GC_828_268,(0,0,6):C.R2GC_866_286})

V_416 = CTVertex(name = 'V_416',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qd1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1] ], [ [P.g] ], [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_326_120,(1,0,3):C.R2GC_326_121,(1,0,0):C.R2GC_794_224,(1,0,5):C.R2GC_797_228,(1,0,1):C.R2GC_794_226,(1,0,4):C.R2GC_797_229,(0,0,2):C.R2GC_326_120,(0,0,3):C.R2GC_326_121,(0,0,0):C.R2GC_794_224,(0,0,5):C.R2GC_797_228,(0,0,1):C.R2GC_794_226,(0,0,4):C.R2GC_797_229})

V_417 = CTVertex(name = 'V_417',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd2, P.YS3Qu1, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu2] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu1, P.YS3Qu2] ] ],
                 couplings = {(1,0,0):C.R2GC_806_236,(1,0,1):C.R2GC_806_237,(1,0,2):C.R2GC_806_238,(0,0,0):C.R2GC_807_239,(0,0,1):C.R2GC_807_240,(0,0,2):C.R2GC_807_241})

V_418 = CTVertex(name = 'V_418',
                 type = 'R2',
                 particles = [ P.YS3Qd1, P.YS3Qd2__tilde__, P.YS3Qu1__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu2] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu1, P.YS3Qu2] ] ],
                 couplings = {(1,0,0):C.R2GC_806_236,(1,0,1):C.R2GC_806_237,(1,0,2):C.R2GC_806_238,(0,0,0):C.R2GC_807_239,(0,0,1):C.R2GC_807_240,(0,0,2):C.R2GC_807_241})

V_419 = CTVertex(name = 'V_419',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3Qd2, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qd2, P.YS3Qu1] ], [ [P.g, P.YS3Qd2, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_829_270,(1,0,8):C.R2GC_867_287,(1,0,1):C.R2GC_829_272,(1,0,7):C.R2GC_867_289,(1,0,2):C.R2GC_829_274,(1,0,6):C.R2GC_867_291,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_794_224,(0,0,8):C.R2GC_866_282,(0,0,1):C.R2GC_145_11,(0,0,7):C.R2GC_866_284,(0,0,2):C.R2GC_828_268,(0,0,6):C.R2GC_866_286})

V_420 = CTVertex(name = 'V_420',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qu2] ], [ [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,7):C.R2GC_610_201,(1,0,8):C.R2GC_610_202,(1,0,0):C.R2GC_829_270,(1,0,4):C.R2GC_806_236,(1,0,11):C.R2GC_867_287,(1,0,1):C.R2GC_829_272,(1,0,5):C.R2GC_867_288,(1,0,10):C.R2GC_867_289,(1,0,2):C.R2GC_829_274,(1,0,6):C.R2GC_867_290,(1,0,9):C.R2GC_867_291,(0,0,3):C.R2GC_609_197,(0,0,7):C.R2GC_609_198,(0,0,8):C.R2GC_609_199,(0,0,0):C.R2GC_794_224,(0,0,4):C.R2GC_807_239,(0,0,11):C.R2GC_866_282,(0,0,1):C.R2GC_145_11,(0,0,5):C.R2GC_866_283,(0,0,10):C.R2GC_866_284,(0,0,2):C.R2GC_828_268,(0,0,6):C.R2GC_866_285,(0,0,9):C.R2GC_866_286})

V_421 = CTVertex(name = 'V_421',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qd2, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qd2, P.YS3Qu3] ], [ [P.g, P.YS3Qd2, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_829_270,(1,0,8):C.R2GC_867_287,(1,0,1):C.R2GC_829_272,(1,0,7):C.R2GC_867_289,(1,0,2):C.R2GC_829_274,(1,0,6):C.R2GC_867_291,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_794_224,(0,0,8):C.R2GC_866_282,(0,0,1):C.R2GC_145_11,(0,0,7):C.R2GC_866_284,(0,0,2):C.R2GC_828_268,(0,0,6):C.R2GC_866_286})

V_422 = CTVertex(name = 'V_422',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qd2] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd1, P.YS3Qd2] ], [ [P.g, P.YS3Qd1, P.YS3Qd2, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_813_248,(1,0,8):C.R2GC_825_263,(1,0,1):C.R2GC_813_250,(1,0,7):C.R2GC_825_264,(1,0,2):C.R2GC_813_252,(1,0,6):C.R2GC_825_265,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_812_242,(0,0,8):C.R2GC_824_260,(0,0,1):C.R2GC_812_244,(0,0,7):C.R2GC_824_261,(0,0,2):C.R2GC_812_246,(0,0,6):C.R2GC_824_262})

V_423 = CTVertex(name = 'V_423',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qd2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_326_120,(1,0,3):C.R2GC_326_121,(1,0,0):C.R2GC_794_224,(1,0,5):C.R2GC_797_228,(1,0,1):C.R2GC_794_226,(1,0,4):C.R2GC_797_229,(0,0,2):C.R2GC_326_120,(0,0,3):C.R2GC_326_121,(0,0,0):C.R2GC_794_224,(0,0,5):C.R2GC_797_228,(0,0,1):C.R2GC_794_226,(0,0,4):C.R2GC_797_229})

V_424 = CTVertex(name = 'V_424',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd3, P.YS3Qu1, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu3], [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu1, P.YS3Qu3] ] ],
                 couplings = {(1,0,0):C.R2GC_806_236,(1,0,1):C.R2GC_806_237,(1,0,2):C.R2GC_806_238,(0,0,0):C.R2GC_807_239,(0,0,1):C.R2GC_807_240,(0,0,2):C.R2GC_807_241})

V_425 = CTVertex(name = 'V_425',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd3, P.YS3Qu2, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu3], [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qu2, P.YS3Qu3] ] ],
                 couplings = {(1,0,0):C.R2GC_806_236,(1,0,1):C.R2GC_806_237,(1,0,2):C.R2GC_806_238,(0,0,0):C.R2GC_807_239,(0,0,1):C.R2GC_807_240,(0,0,2):C.R2GC_807_241})

V_426 = CTVertex(name = 'V_426',
                 type = 'R2',
                 particles = [ P.YS3Qd1, P.YS3Qd3__tilde__, P.YS3Qu1__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu3], [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu1, P.YS3Qu3] ] ],
                 couplings = {(1,0,0):C.R2GC_806_236,(1,0,1):C.R2GC_806_237,(1,0,2):C.R2GC_806_238,(0,0,0):C.R2GC_807_239,(0,0,1):C.R2GC_807_240,(0,0,2):C.R2GC_807_241})

V_427 = CTVertex(name = 'V_427',
                 type = 'R2',
                 particles = [ P.YS3Qd2, P.YS3Qd3__tilde__, P.YS3Qu2__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu3], [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qu2, P.YS3Qu3] ] ],
                 couplings = {(1,0,0):C.R2GC_806_236,(1,0,1):C.R2GC_806_237,(1,0,2):C.R2GC_806_238,(0,0,0):C.R2GC_807_239,(0,0,1):C.R2GC_807_240,(0,0,2):C.R2GC_807_241})

V_428 = CTVertex(name = 'V_428',
                 type = 'R2',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3Qd3, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qd3, P.YS3Qu1] ], [ [P.g, P.YS3Qd3, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_829_270,(1,0,8):C.R2GC_867_287,(1,0,1):C.R2GC_829_272,(1,0,7):C.R2GC_867_289,(1,0,2):C.R2GC_829_274,(1,0,6):C.R2GC_867_291,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_794_224,(0,0,8):C.R2GC_866_282,(0,0,1):C.R2GC_145_11,(0,0,7):C.R2GC_866_284,(0,0,2):C.R2GC_828_268,(0,0,6):C.R2GC_866_286})

V_429 = CTVertex(name = 'V_429',
                 type = 'R2',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3Qd3, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qd3, P.YS3Qu2] ], [ [P.g, P.YS3Qd3, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_829_270,(1,0,8):C.R2GC_867_287,(1,0,1):C.R2GC_829_272,(1,0,7):C.R2GC_867_289,(1,0,2):C.R2GC_829_274,(1,0,6):C.R2GC_867_291,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_794_224,(0,0,8):C.R2GC_866_282,(0,0,1):C.R2GC_145_11,(0,0,7):C.R2GC_866_284,(0,0,2):C.R2GC_828_268,(0,0,6):C.R2GC_866_286})

V_430 = CTVertex(name = 'V_430',
                 type = 'R2',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,7):C.R2GC_610_201,(1,0,8):C.R2GC_610_202,(1,0,0):C.R2GC_829_270,(1,0,4):C.R2GC_806_236,(1,0,11):C.R2GC_867_287,(1,0,1):C.R2GC_829_272,(1,0,5):C.R2GC_867_288,(1,0,10):C.R2GC_867_289,(1,0,2):C.R2GC_829_274,(1,0,6):C.R2GC_867_290,(1,0,9):C.R2GC_867_291,(0,0,3):C.R2GC_609_197,(0,0,7):C.R2GC_609_198,(0,0,8):C.R2GC_609_199,(0,0,0):C.R2GC_794_224,(0,0,4):C.R2GC_807_239,(0,0,11):C.R2GC_866_282,(0,0,1):C.R2GC_145_11,(0,0,5):C.R2GC_866_283,(0,0,10):C.R2GC_866_284,(0,0,2):C.R2GC_828_268,(0,0,6):C.R2GC_866_285,(0,0,9):C.R2GC_866_286})

V_431 = CTVertex(name = 'V_431',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd1, P.YS3Qd3] ], [ [P.g, P.YS3Qd1, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_813_248,(1,0,8):C.R2GC_825_263,(1,0,1):C.R2GC_813_250,(1,0,7):C.R2GC_825_264,(1,0,2):C.R2GC_813_252,(1,0,6):C.R2GC_825_265,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_812_242,(0,0,8):C.R2GC_824_260,(0,0,1):C.R2GC_812_244,(0,0,7):C.R2GC_824_261,(0,0,2):C.R2GC_812_246,(0,0,6):C.R2GC_824_262})

V_432 = CTVertex(name = 'V_432',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3Qd2, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd2, P.YS3Qd3] ], [ [P.g, P.YS3Qd2, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_813_248,(1,0,8):C.R2GC_825_263,(1,0,1):C.R2GC_813_250,(1,0,7):C.R2GC_825_264,(1,0,2):C.R2GC_813_252,(1,0,6):C.R2GC_825_265,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_812_242,(0,0,8):C.R2GC_824_260,(0,0,1):C.R2GC_812_244,(0,0,7):C.R2GC_824_261,(0,0,2):C.R2GC_812_246,(0,0,6):C.R2GC_824_262})

V_433 = CTVertex(name = 'V_433',
                 type = 'R2',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3Qd3 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_326_120,(1,0,3):C.R2GC_326_121,(1,0,0):C.R2GC_794_224,(1,0,5):C.R2GC_797_228,(1,0,1):C.R2GC_794_226,(1,0,4):C.R2GC_797_229,(0,0,2):C.R2GC_326_120,(0,0,3):C.R2GC_326_121,(0,0,0):C.R2GC_794_224,(0,0,5):C.R2GC_797_228,(0,0,1):C.R2GC_794_226,(0,0,4):C.R2GC_797_229})

V_434 = CTVertex(name = 'V_434',
                 type = 'R2',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qu1, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qu1, P.YS3u1] ], [ [P.g, P.YS3Qu1, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_873_298,(1,0,8):C.R2GC_877_307,(1,0,1):C.R2GC_873_300,(1,0,7):C.R2GC_877_308,(1,0,2):C.R2GC_873_302,(1,0,6):C.R2GC_877_309,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_872_292,(0,0,8):C.R2GC_876_304,(0,0,1):C.R2GC_872_294,(0,0,7):C.R2GC_876_305,(0,0,2):C.R2GC_872_296,(0,0,6):C.R2GC_876_306})

V_435 = CTVertex(name = 'V_435',
                 type = 'R2',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qu2, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qu2], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qu2, P.YS3u1] ], [ [P.g, P.YS3Qu2, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qu2, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_873_298,(1,0,8):C.R2GC_877_307,(1,0,1):C.R2GC_873_300,(1,0,7):C.R2GC_877_308,(1,0,2):C.R2GC_873_302,(1,0,6):C.R2GC_877_309,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_872_292,(0,0,8):C.R2GC_876_304,(0,0,1):C.R2GC_872_294,(0,0,7):C.R2GC_876_305,(0,0,2):C.R2GC_872_296,(0,0,6):C.R2GC_876_306})

V_436 = CTVertex(name = 'V_436',
                 type = 'R2',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu3], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qu3, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qu3], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qu3, P.YS3u1] ], [ [P.g, P.YS3Qu3, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qu3, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_873_298,(1,0,8):C.R2GC_877_307,(1,0,1):C.R2GC_873_300,(1,0,7):C.R2GC_877_308,(1,0,2):C.R2GC_873_302,(1,0,6):C.R2GC_877_309,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_872_292,(0,0,8):C.R2GC_876_304,(0,0,1):C.R2GC_872_294,(0,0,7):C.R2GC_876_305,(0,0,2):C.R2GC_872_296,(0,0,6):C.R2GC_876_306})

V_437 = CTVertex(name = 'V_437',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qd1, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qd1, P.YS3u1] ], [ [P.g, P.YS3Qd1, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_829_270,(1,0,8):C.R2GC_829_271,(1,0,1):C.R2GC_829_272,(1,0,7):C.R2GC_829_273,(1,0,2):C.R2GC_829_274,(1,0,6):C.R2GC_829_275,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_794_224,(0,0,8):C.R2GC_828_266,(0,0,1):C.R2GC_145_11,(0,0,7):C.R2GC_828_267,(0,0,2):C.R2GC_828_268,(0,0,6):C.R2GC_828_269})

V_438 = CTVertex(name = 'V_438',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qd2, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qd2, P.YS3u1] ], [ [P.g, P.YS3Qd2, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_829_270,(1,0,8):C.R2GC_829_271,(1,0,1):C.R2GC_829_272,(1,0,7):C.R2GC_829_273,(1,0,2):C.R2GC_829_274,(1,0,6):C.R2GC_829_275,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_794_224,(0,0,8):C.R2GC_828_266,(0,0,1):C.R2GC_145_11,(0,0,7):C.R2GC_828_267,(0,0,2):C.R2GC_828_268,(0,0,6):C.R2GC_828_269})

V_439 = CTVertex(name = 'V_439',
                 type = 'R2',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qd3, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qd3, P.YS3u1] ], [ [P.g, P.YS3Qd3, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_829_270,(1,0,8):C.R2GC_829_271,(1,0,1):C.R2GC_829_272,(1,0,7):C.R2GC_829_273,(1,0,2):C.R2GC_829_274,(1,0,6):C.R2GC_829_275,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_794_224,(0,0,8):C.R2GC_828_266,(0,0,1):C.R2GC_145_11,(0,0,7):C.R2GC_828_267,(0,0,2):C.R2GC_828_268,(0,0,6):C.R2GC_828_269})

V_440 = CTVertex(name = 'V_440',
                 type = 'R2',
                 particles = [ P.YS3u1__tilde__, P.YS3u1__tilde__, P.YS3u1, P.YS3u1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3u1] ], [ [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_326_120,(1,0,3):C.R2GC_326_121,(1,0,0):C.R2GC_800_230,(1,0,5):C.R2GC_803_234,(1,0,1):C.R2GC_800_232,(1,0,4):C.R2GC_803_235,(0,0,2):C.R2GC_326_120,(0,0,3):C.R2GC_326_121,(0,0,0):C.R2GC_800_230,(0,0,5):C.R2GC_803_234,(0,0,1):C.R2GC_800_232,(0,0,4):C.R2GC_803_235})

V_441 = CTVertex(name = 'V_441',
                 type = 'R2',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qu1, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qu1, P.YS3u2] ], [ [P.g, P.YS3Qu1, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_873_298,(1,0,8):C.R2GC_877_307,(1,0,1):C.R2GC_873_300,(1,0,7):C.R2GC_877_308,(1,0,2):C.R2GC_873_302,(1,0,6):C.R2GC_877_309,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_872_292,(0,0,8):C.R2GC_876_304,(0,0,1):C.R2GC_872_294,(0,0,7):C.R2GC_876_305,(0,0,2):C.R2GC_872_296,(0,0,6):C.R2GC_876_306})

V_442 = CTVertex(name = 'V_442',
                 type = 'R2',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qu2, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qu2], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qu2, P.YS3u2] ], [ [P.g, P.YS3Qu2, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qu2, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_873_298,(1,0,8):C.R2GC_877_307,(1,0,1):C.R2GC_873_300,(1,0,7):C.R2GC_877_308,(1,0,2):C.R2GC_873_302,(1,0,6):C.R2GC_877_309,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_872_292,(0,0,8):C.R2GC_876_304,(0,0,1):C.R2GC_872_294,(0,0,7):C.R2GC_876_305,(0,0,2):C.R2GC_872_296,(0,0,6):C.R2GC_876_306})

V_443 = CTVertex(name = 'V_443',
                 type = 'R2',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu3], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qu3, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qu3], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qu3, P.YS3u2] ], [ [P.g, P.YS3Qu3, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qu3, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_873_298,(1,0,8):C.R2GC_877_307,(1,0,1):C.R2GC_873_300,(1,0,7):C.R2GC_877_308,(1,0,2):C.R2GC_873_302,(1,0,6):C.R2GC_877_309,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_872_292,(0,0,8):C.R2GC_876_304,(0,0,1):C.R2GC_872_294,(0,0,7):C.R2GC_876_305,(0,0,2):C.R2GC_872_296,(0,0,6):C.R2GC_876_306})

V_444 = CTVertex(name = 'V_444',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qd1, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qd1, P.YS3u2] ], [ [P.g, P.YS3Qd1, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_829_270,(1,0,8):C.R2GC_829_271,(1,0,1):C.R2GC_829_272,(1,0,7):C.R2GC_829_273,(1,0,2):C.R2GC_829_274,(1,0,6):C.R2GC_829_275,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_794_224,(0,0,8):C.R2GC_828_266,(0,0,1):C.R2GC_145_11,(0,0,7):C.R2GC_828_267,(0,0,2):C.R2GC_828_268,(0,0,6):C.R2GC_828_269})

V_445 = CTVertex(name = 'V_445',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qd2, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qd2, P.YS3u2] ], [ [P.g, P.YS3Qd2, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_829_270,(1,0,8):C.R2GC_829_271,(1,0,1):C.R2GC_829_272,(1,0,7):C.R2GC_829_273,(1,0,2):C.R2GC_829_274,(1,0,6):C.R2GC_829_275,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_794_224,(0,0,8):C.R2GC_828_266,(0,0,1):C.R2GC_145_11,(0,0,7):C.R2GC_828_267,(0,0,2):C.R2GC_828_268,(0,0,6):C.R2GC_828_269})

V_446 = CTVertex(name = 'V_446',
                 type = 'R2',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qd3, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qd3, P.YS3u2] ], [ [P.g, P.YS3Qd3, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_829_270,(1,0,8):C.R2GC_829_271,(1,0,1):C.R2GC_829_272,(1,0,7):C.R2GC_829_273,(1,0,2):C.R2GC_829_274,(1,0,6):C.R2GC_829_275,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_794_224,(0,0,8):C.R2GC_828_266,(0,0,1):C.R2GC_145_11,(0,0,7):C.R2GC_828_267,(0,0,2):C.R2GC_828_268,(0,0,6):C.R2GC_828_269})

V_447 = CTVertex(name = 'V_447',
                 type = 'R2',
                 particles = [ P.YS3u1__tilde__, P.YS3u1, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u1], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3u1, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3u1], [P.g, P.YS3u2] ], [ [P.g, P.YS3u1, P.YS3u2] ], [ [P.g, P.YS3u1, P.YS3u2, P.Z] ], [ [P.g, P.YS3u1, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_873_298,(1,0,8):C.R2GC_927_317,(1,0,1):C.R2GC_873_300,(1,0,7):C.R2GC_927_318,(1,0,2):C.R2GC_873_302,(1,0,6):C.R2GC_927_319,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_872_292,(0,0,8):C.R2GC_926_314,(0,0,1):C.R2GC_872_294,(0,0,7):C.R2GC_926_315,(0,0,2):C.R2GC_872_296,(0,0,6):C.R2GC_926_316})

V_448 = CTVertex(name = 'V_448',
                 type = 'R2',
                 particles = [ P.YS3u2__tilde__, P.YS3u2__tilde__, P.YS3u2, P.YS3u2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3u2] ], [ [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_326_120,(1,0,3):C.R2GC_326_121,(1,0,0):C.R2GC_800_230,(1,0,5):C.R2GC_803_234,(1,0,1):C.R2GC_800_232,(1,0,4):C.R2GC_803_235,(0,0,2):C.R2GC_326_120,(0,0,3):C.R2GC_326_121,(0,0,0):C.R2GC_800_230,(0,0,5):C.R2GC_803_234,(0,0,1):C.R2GC_800_232,(0,0,4):C.R2GC_803_235})

V_449 = CTVertex(name = 'V_449',
                 type = 'R2',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qu1, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qu1, P.YS3u3] ], [ [P.g, P.YS3Qu1, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_873_298,(1,0,8):C.R2GC_877_307,(1,0,1):C.R2GC_873_300,(1,0,7):C.R2GC_877_308,(1,0,2):C.R2GC_873_302,(1,0,6):C.R2GC_877_309,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_872_292,(0,0,8):C.R2GC_876_304,(0,0,1):C.R2GC_872_294,(0,0,7):C.R2GC_876_305,(0,0,2):C.R2GC_872_296,(0,0,6):C.R2GC_876_306})

V_450 = CTVertex(name = 'V_450',
                 type = 'R2',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qu2, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qu2], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qu2, P.YS3u3] ], [ [P.g, P.YS3Qu2, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qu2, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_873_298,(1,0,8):C.R2GC_877_307,(1,0,1):C.R2GC_873_300,(1,0,7):C.R2GC_877_308,(1,0,2):C.R2GC_873_302,(1,0,6):C.R2GC_877_309,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_872_292,(0,0,8):C.R2GC_876_304,(0,0,1):C.R2GC_872_294,(0,0,7):C.R2GC_876_305,(0,0,2):C.R2GC_872_296,(0,0,6):C.R2GC_876_306})

V_451 = CTVertex(name = 'V_451',
                 type = 'R2',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu3], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qu3, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qu3], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qu3, P.YS3u3] ], [ [P.g, P.YS3Qu3, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qu3, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_873_298,(1,0,8):C.R2GC_877_307,(1,0,1):C.R2GC_873_300,(1,0,7):C.R2GC_877_308,(1,0,2):C.R2GC_873_302,(1,0,6):C.R2GC_877_309,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_872_292,(0,0,8):C.R2GC_876_304,(0,0,1):C.R2GC_872_294,(0,0,7):C.R2GC_876_305,(0,0,2):C.R2GC_872_296,(0,0,6):C.R2GC_876_306})

V_452 = CTVertex(name = 'V_452',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qd1, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qd1, P.YS3u3] ], [ [P.g, P.YS3Qd1, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_829_270,(1,0,8):C.R2GC_829_271,(1,0,1):C.R2GC_829_272,(1,0,7):C.R2GC_829_273,(1,0,2):C.R2GC_829_274,(1,0,6):C.R2GC_829_275,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_794_224,(0,0,8):C.R2GC_828_266,(0,0,1):C.R2GC_145_11,(0,0,7):C.R2GC_828_267,(0,0,2):C.R2GC_828_268,(0,0,6):C.R2GC_828_269})

V_453 = CTVertex(name = 'V_453',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qd2, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qd2, P.YS3u3] ], [ [P.g, P.YS3Qd2, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_829_270,(1,0,8):C.R2GC_829_271,(1,0,1):C.R2GC_829_272,(1,0,7):C.R2GC_829_273,(1,0,2):C.R2GC_829_274,(1,0,6):C.R2GC_829_275,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_794_224,(0,0,8):C.R2GC_828_266,(0,0,1):C.R2GC_145_11,(0,0,7):C.R2GC_828_267,(0,0,2):C.R2GC_828_268,(0,0,6):C.R2GC_828_269})

V_454 = CTVertex(name = 'V_454',
                 type = 'R2',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qd3, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qd3, P.YS3u3] ], [ [P.g, P.YS3Qd3, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_829_270,(1,0,8):C.R2GC_829_271,(1,0,1):C.R2GC_829_272,(1,0,7):C.R2GC_829_273,(1,0,2):C.R2GC_829_274,(1,0,6):C.R2GC_829_275,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_794_224,(0,0,8):C.R2GC_828_266,(0,0,1):C.R2GC_145_11,(0,0,7):C.R2GC_828_267,(0,0,2):C.R2GC_828_268,(0,0,6):C.R2GC_828_269})

V_455 = CTVertex(name = 'V_455',
                 type = 'R2',
                 particles = [ P.YS3u1__tilde__, P.YS3u1, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u1], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3u1, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3u1], [P.g, P.YS3u3] ], [ [P.g, P.YS3u1, P.YS3u3] ], [ [P.g, P.YS3u1, P.YS3u3, P.Z] ], [ [P.g, P.YS3u1, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_873_298,(1,0,8):C.R2GC_927_317,(1,0,1):C.R2GC_873_300,(1,0,7):C.R2GC_927_318,(1,0,2):C.R2GC_873_302,(1,0,6):C.R2GC_927_319,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_872_292,(0,0,8):C.R2GC_926_314,(0,0,1):C.R2GC_872_294,(0,0,7):C.R2GC_926_315,(0,0,2):C.R2GC_872_296,(0,0,6):C.R2GC_926_316})

V_456 = CTVertex(name = 'V_456',
                 type = 'R2',
                 particles = [ P.YS3u2__tilde__, P.YS3u2, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u2], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3u2, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3u2], [P.g, P.YS3u3] ], [ [P.g, P.YS3u2, P.YS3u3] ], [ [P.g, P.YS3u2, P.YS3u3, P.Z] ], [ [P.g, P.YS3u2, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_873_298,(1,0,8):C.R2GC_927_317,(1,0,1):C.R2GC_873_300,(1,0,7):C.R2GC_927_318,(1,0,2):C.R2GC_873_302,(1,0,6):C.R2GC_927_319,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_872_292,(0,0,8):C.R2GC_926_314,(0,0,1):C.R2GC_872_294,(0,0,7):C.R2GC_926_315,(0,0,2):C.R2GC_872_296,(0,0,6):C.R2GC_926_316})

V_457 = CTVertex(name = 'V_457',
                 type = 'R2',
                 particles = [ P.YS3u3__tilde__, P.YS3u3__tilde__, P.YS3u3, P.YS3u3 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3u3] ], [ [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_326_120,(1,0,3):C.R2GC_326_121,(1,0,0):C.R2GC_800_230,(1,0,5):C.R2GC_803_234,(1,0,1):C.R2GC_800_232,(1,0,4):C.R2GC_803_235,(0,0,2):C.R2GC_326_120,(0,0,3):C.R2GC_326_121,(0,0,0):C.R2GC_800_230,(0,0,5):C.R2GC_803_234,(0,0,1):C.R2GC_800_232,(0,0,4):C.R2GC_803_235})

V_458 = CTVertex(name = 'V_458',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3d1, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3d1, P.YS3Qu1] ], [ [P.g, P.YS3d1, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_829_270,(1,0,8):C.R2GC_861_279,(1,0,1):C.R2GC_829_272,(1,0,7):C.R2GC_861_280,(1,0,2):C.R2GC_829_274,(1,0,6):C.R2GC_861_281,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_794_224,(0,0,8):C.R2GC_860_276,(0,0,1):C.R2GC_145_11,(0,0,7):C.R2GC_860_277,(0,0,2):C.R2GC_828_268,(0,0,6):C.R2GC_860_278})

V_459 = CTVertex(name = 'V_459',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3d1, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3d1, P.YS3Qu2] ], [ [P.g, P.YS3d1, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_829_270,(1,0,8):C.R2GC_861_279,(1,0,1):C.R2GC_829_272,(1,0,7):C.R2GC_861_280,(1,0,2):C.R2GC_829_274,(1,0,6):C.R2GC_861_281,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_794_224,(0,0,8):C.R2GC_860_276,(0,0,1):C.R2GC_145_11,(0,0,7):C.R2GC_860_277,(0,0,2):C.R2GC_828_268,(0,0,6):C.R2GC_860_278})

V_460 = CTVertex(name = 'V_460',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3d1, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3d1, P.YS3Qu3] ], [ [P.g, P.YS3d1, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_829_270,(1,0,8):C.R2GC_861_279,(1,0,1):C.R2GC_829_272,(1,0,7):C.R2GC_861_280,(1,0,2):C.R2GC_829_274,(1,0,6):C.R2GC_861_281,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_794_224,(0,0,8):C.R2GC_860_276,(0,0,1):C.R2GC_145_11,(0,0,7):C.R2GC_860_277,(0,0,2):C.R2GC_828_268,(0,0,6):C.R2GC_860_278})

V_461 = CTVertex(name = 'V_461',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qd1] ], [ [P.a, P.g, P.YS3d1, P.YS3Qd1] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qd1] ], [ [P.g, P.YS3d1, P.YS3Qd1] ], [ [P.g, P.YS3d1, P.YS3Qd1, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qd1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_813_248,(1,0,8):C.R2GC_819_257,(1,0,1):C.R2GC_813_250,(1,0,7):C.R2GC_819_258,(1,0,2):C.R2GC_813_252,(1,0,6):C.R2GC_819_259,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_812_242,(0,0,8):C.R2GC_818_254,(0,0,1):C.R2GC_812_244,(0,0,7):C.R2GC_818_255,(0,0,2):C.R2GC_812_246,(0,0,6):C.R2GC_818_256})

V_462 = CTVertex(name = 'V_462',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qd2] ], [ [P.a, P.g, P.YS3d1, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qd2] ], [ [P.g, P.YS3d1, P.YS3Qd2] ], [ [P.g, P.YS3d1, P.YS3Qd2, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_813_248,(1,0,8):C.R2GC_819_257,(1,0,1):C.R2GC_813_250,(1,0,7):C.R2GC_819_258,(1,0,2):C.R2GC_813_252,(1,0,6):C.R2GC_819_259,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_812_242,(0,0,8):C.R2GC_818_254,(0,0,1):C.R2GC_812_244,(0,0,7):C.R2GC_818_255,(0,0,2):C.R2GC_812_246,(0,0,6):C.R2GC_818_256})

V_463 = CTVertex(name = 'V_463',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3d1, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3d1, P.YS3Qd3] ], [ [P.g, P.YS3d1, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_813_248,(1,0,8):C.R2GC_819_257,(1,0,1):C.R2GC_813_250,(1,0,7):C.R2GC_819_258,(1,0,2):C.R2GC_813_252,(1,0,6):C.R2GC_819_259,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_812_242,(0,0,8):C.R2GC_818_254,(0,0,1):C.R2GC_812_244,(0,0,7):C.R2GC_818_255,(0,0,2):C.R2GC_812_246,(0,0,6):C.R2GC_818_256})

V_464 = CTVertex(name = 'V_464',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3d1, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3u1] ], [ [P.g, P.YS3d1, P.YS3u1] ], [ [P.g, P.YS3d1, P.YS3u1, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_829_270,(1,0,8):C.R2GC_921_311,(1,0,1):C.R2GC_829_272,(1,0,7):C.R2GC_921_312,(1,0,2):C.R2GC_829_274,(1,0,6):C.R2GC_921_313,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_794_224,(0,0,8):C.R2GC_794_225,(0,0,1):C.R2GC_145_11,(0,0,7):C.R2GC_150_43,(0,0,2):C.R2GC_828_268,(0,0,6):C.R2GC_920_310})

V_465 = CTVertex(name = 'V_465',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3d1, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3u2] ], [ [P.g, P.YS3d1, P.YS3u2] ], [ [P.g, P.YS3d1, P.YS3u2, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_829_270,(1,0,8):C.R2GC_921_311,(1,0,1):C.R2GC_829_272,(1,0,7):C.R2GC_921_312,(1,0,2):C.R2GC_829_274,(1,0,6):C.R2GC_921_313,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_794_224,(0,0,8):C.R2GC_794_225,(0,0,1):C.R2GC_145_11,(0,0,7):C.R2GC_150_43,(0,0,2):C.R2GC_828_268,(0,0,6):C.R2GC_920_310})

V_466 = CTVertex(name = 'V_466',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3d1, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3u3] ], [ [P.g, P.YS3d1, P.YS3u3] ], [ [P.g, P.YS3d1, P.YS3u3, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_829_270,(1,0,8):C.R2GC_921_311,(1,0,1):C.R2GC_829_272,(1,0,7):C.R2GC_921_312,(1,0,2):C.R2GC_829_274,(1,0,6):C.R2GC_921_313,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_794_224,(0,0,8):C.R2GC_794_225,(0,0,1):C.R2GC_145_11,(0,0,7):C.R2GC_150_43,(0,0,2):C.R2GC_828_268,(0,0,6):C.R2GC_920_310})

V_467 = CTVertex(name = 'V_467',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1__tilde__, P.YS3d1, P.YS3d1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1] ], [ [P.g] ], [ [P.g, P.YS3d1] ], [ [P.g, P.YS3d1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_326_120,(1,0,3):C.R2GC_326_121,(1,0,0):C.R2GC_794_224,(1,0,5):C.R2GC_794_225,(1,0,1):C.R2GC_794_226,(1,0,4):C.R2GC_794_227,(0,0,2):C.R2GC_326_120,(0,0,3):C.R2GC_326_121,(0,0,0):C.R2GC_794_224,(0,0,5):C.R2GC_794_225,(0,0,1):C.R2GC_794_226,(0,0,4):C.R2GC_794_227})

V_468 = CTVertex(name = 'V_468',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3d2, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3d2, P.YS3Qu1] ], [ [P.g, P.YS3d2, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_829_270,(1,0,8):C.R2GC_861_279,(1,0,1):C.R2GC_829_272,(1,0,7):C.R2GC_861_280,(1,0,2):C.R2GC_829_274,(1,0,6):C.R2GC_861_281,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_794_224,(0,0,8):C.R2GC_860_276,(0,0,1):C.R2GC_145_11,(0,0,7):C.R2GC_860_277,(0,0,2):C.R2GC_828_268,(0,0,6):C.R2GC_860_278})

V_469 = CTVertex(name = 'V_469',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3d2, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3d2, P.YS3Qu2] ], [ [P.g, P.YS3d2, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_829_270,(1,0,8):C.R2GC_861_279,(1,0,1):C.R2GC_829_272,(1,0,7):C.R2GC_861_280,(1,0,2):C.R2GC_829_274,(1,0,6):C.R2GC_861_281,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_794_224,(0,0,8):C.R2GC_860_276,(0,0,1):C.R2GC_145_11,(0,0,7):C.R2GC_860_277,(0,0,2):C.R2GC_828_268,(0,0,6):C.R2GC_860_278})

V_470 = CTVertex(name = 'V_470',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3d2, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3d2, P.YS3Qu3] ], [ [P.g, P.YS3d2, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_829_270,(1,0,8):C.R2GC_861_279,(1,0,1):C.R2GC_829_272,(1,0,7):C.R2GC_861_280,(1,0,2):C.R2GC_829_274,(1,0,6):C.R2GC_861_281,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_794_224,(0,0,8):C.R2GC_860_276,(0,0,1):C.R2GC_145_11,(0,0,7):C.R2GC_860_277,(0,0,2):C.R2GC_828_268,(0,0,6):C.R2GC_860_278})

V_471 = CTVertex(name = 'V_471',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qd1] ], [ [P.a, P.g, P.YS3d2, P.YS3Qd1] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qd1] ], [ [P.g, P.YS3d2, P.YS3Qd1] ], [ [P.g, P.YS3d2, P.YS3Qd1, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qd1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_813_248,(1,0,8):C.R2GC_819_257,(1,0,1):C.R2GC_813_250,(1,0,7):C.R2GC_819_258,(1,0,2):C.R2GC_813_252,(1,0,6):C.R2GC_819_259,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_812_242,(0,0,8):C.R2GC_818_254,(0,0,1):C.R2GC_812_244,(0,0,7):C.R2GC_818_255,(0,0,2):C.R2GC_812_246,(0,0,6):C.R2GC_818_256})

V_472 = CTVertex(name = 'V_472',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qd2] ], [ [P.a, P.g, P.YS3d2, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qd2] ], [ [P.g, P.YS3d2, P.YS3Qd2] ], [ [P.g, P.YS3d2, P.YS3Qd2, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_813_248,(1,0,8):C.R2GC_819_257,(1,0,1):C.R2GC_813_250,(1,0,7):C.R2GC_819_258,(1,0,2):C.R2GC_813_252,(1,0,6):C.R2GC_819_259,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_812_242,(0,0,8):C.R2GC_818_254,(0,0,1):C.R2GC_812_244,(0,0,7):C.R2GC_818_255,(0,0,2):C.R2GC_812_246,(0,0,6):C.R2GC_818_256})

V_473 = CTVertex(name = 'V_473',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3d2, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3d2, P.YS3Qd3] ], [ [P.g, P.YS3d2, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_813_248,(1,0,8):C.R2GC_819_257,(1,0,1):C.R2GC_813_250,(1,0,7):C.R2GC_819_258,(1,0,2):C.R2GC_813_252,(1,0,6):C.R2GC_819_259,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_812_242,(0,0,8):C.R2GC_818_254,(0,0,1):C.R2GC_812_244,(0,0,7):C.R2GC_818_255,(0,0,2):C.R2GC_812_246,(0,0,6):C.R2GC_818_256})

V_474 = CTVertex(name = 'V_474',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3d2, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3u1] ], [ [P.g, P.YS3d2, P.YS3u1] ], [ [P.g, P.YS3d2, P.YS3u1, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_829_270,(1,0,8):C.R2GC_921_311,(1,0,1):C.R2GC_829_272,(1,0,7):C.R2GC_921_312,(1,0,2):C.R2GC_829_274,(1,0,6):C.R2GC_921_313,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_794_224,(0,0,8):C.R2GC_794_225,(0,0,1):C.R2GC_145_11,(0,0,7):C.R2GC_150_43,(0,0,2):C.R2GC_828_268,(0,0,6):C.R2GC_920_310})

V_475 = CTVertex(name = 'V_475',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3d2, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3u2] ], [ [P.g, P.YS3d2, P.YS3u2] ], [ [P.g, P.YS3d2, P.YS3u2, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_829_270,(1,0,8):C.R2GC_921_311,(1,0,1):C.R2GC_829_272,(1,0,7):C.R2GC_921_312,(1,0,2):C.R2GC_829_274,(1,0,6):C.R2GC_921_313,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_794_224,(0,0,8):C.R2GC_794_225,(0,0,1):C.R2GC_145_11,(0,0,7):C.R2GC_150_43,(0,0,2):C.R2GC_828_268,(0,0,6):C.R2GC_920_310})

V_476 = CTVertex(name = 'V_476',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3d2, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3u3] ], [ [P.g, P.YS3d2, P.YS3u3] ], [ [P.g, P.YS3d2, P.YS3u3, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_829_270,(1,0,8):C.R2GC_921_311,(1,0,1):C.R2GC_829_272,(1,0,7):C.R2GC_921_312,(1,0,2):C.R2GC_829_274,(1,0,6):C.R2GC_921_313,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_794_224,(0,0,8):C.R2GC_794_225,(0,0,1):C.R2GC_145_11,(0,0,7):C.R2GC_150_43,(0,0,2):C.R2GC_828_268,(0,0,6):C.R2GC_920_310})

V_477 = CTVertex(name = 'V_477',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3d2] ], [ [P.a, P.g, P.YS3d1, P.YS3d2] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3d2] ], [ [P.g, P.YS3d1, P.YS3d2] ], [ [P.g, P.YS3d1, P.YS3d2, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3d2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_813_248,(1,0,8):C.R2GC_813_249,(1,0,1):C.R2GC_813_250,(1,0,7):C.R2GC_813_251,(1,0,2):C.R2GC_813_252,(1,0,6):C.R2GC_813_253,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_812_242,(0,0,8):C.R2GC_812_243,(0,0,1):C.R2GC_812_244,(0,0,7):C.R2GC_812_245,(0,0,2):C.R2GC_812_246,(0,0,6):C.R2GC_812_247})

V_478 = CTVertex(name = 'V_478',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2__tilde__, P.YS3d2, P.YS3d2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2] ], [ [P.g] ], [ [P.g, P.YS3d2] ], [ [P.g, P.YS3d2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_326_120,(1,0,3):C.R2GC_326_121,(1,0,0):C.R2GC_794_224,(1,0,5):C.R2GC_794_225,(1,0,1):C.R2GC_794_226,(1,0,4):C.R2GC_794_227,(0,0,2):C.R2GC_326_120,(0,0,3):C.R2GC_326_121,(0,0,0):C.R2GC_794_224,(0,0,5):C.R2GC_794_225,(0,0,1):C.R2GC_794_226,(0,0,4):C.R2GC_794_227})

V_479 = CTVertex(name = 'V_479',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3d3, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3d3, P.YS3Qu1] ], [ [P.g, P.YS3d3, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_829_270,(1,0,8):C.R2GC_861_279,(1,0,1):C.R2GC_829_272,(1,0,7):C.R2GC_861_280,(1,0,2):C.R2GC_829_274,(1,0,6):C.R2GC_861_281,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_794_224,(0,0,8):C.R2GC_860_276,(0,0,1):C.R2GC_145_11,(0,0,7):C.R2GC_860_277,(0,0,2):C.R2GC_828_268,(0,0,6):C.R2GC_860_278})

V_480 = CTVertex(name = 'V_480',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3d3, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3d3, P.YS3Qu2] ], [ [P.g, P.YS3d3, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_829_270,(1,0,8):C.R2GC_861_279,(1,0,1):C.R2GC_829_272,(1,0,7):C.R2GC_861_280,(1,0,2):C.R2GC_829_274,(1,0,6):C.R2GC_861_281,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_794_224,(0,0,8):C.R2GC_860_276,(0,0,1):C.R2GC_145_11,(0,0,7):C.R2GC_860_277,(0,0,2):C.R2GC_828_268,(0,0,6):C.R2GC_860_278})

V_481 = CTVertex(name = 'V_481',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3d3, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3d3, P.YS3Qu3] ], [ [P.g, P.YS3d3, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_829_270,(1,0,8):C.R2GC_861_279,(1,0,1):C.R2GC_829_272,(1,0,7):C.R2GC_861_280,(1,0,2):C.R2GC_829_274,(1,0,6):C.R2GC_861_281,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_794_224,(0,0,8):C.R2GC_860_276,(0,0,1):C.R2GC_145_11,(0,0,7):C.R2GC_860_277,(0,0,2):C.R2GC_828_268,(0,0,6):C.R2GC_860_278})

V_482 = CTVertex(name = 'V_482',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qd1] ], [ [P.a, P.g, P.YS3d3, P.YS3Qd1] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qd1] ], [ [P.g, P.YS3d3, P.YS3Qd1] ], [ [P.g, P.YS3d3, P.YS3Qd1, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qd1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_813_248,(1,0,8):C.R2GC_819_257,(1,0,1):C.R2GC_813_250,(1,0,7):C.R2GC_819_258,(1,0,2):C.R2GC_813_252,(1,0,6):C.R2GC_819_259,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_812_242,(0,0,8):C.R2GC_818_254,(0,0,1):C.R2GC_812_244,(0,0,7):C.R2GC_818_255,(0,0,2):C.R2GC_812_246,(0,0,6):C.R2GC_818_256})

V_483 = CTVertex(name = 'V_483',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qd2] ], [ [P.a, P.g, P.YS3d3, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qd2] ], [ [P.g, P.YS3d3, P.YS3Qd2] ], [ [P.g, P.YS3d3, P.YS3Qd2, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_813_248,(1,0,8):C.R2GC_819_257,(1,0,1):C.R2GC_813_250,(1,0,7):C.R2GC_819_258,(1,0,2):C.R2GC_813_252,(1,0,6):C.R2GC_819_259,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_812_242,(0,0,8):C.R2GC_818_254,(0,0,1):C.R2GC_812_244,(0,0,7):C.R2GC_818_255,(0,0,2):C.R2GC_812_246,(0,0,6):C.R2GC_818_256})

V_484 = CTVertex(name = 'V_484',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3d3, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3d3, P.YS3Qd3] ], [ [P.g, P.YS3d3, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_813_248,(1,0,8):C.R2GC_819_257,(1,0,1):C.R2GC_813_250,(1,0,7):C.R2GC_819_258,(1,0,2):C.R2GC_813_252,(1,0,6):C.R2GC_819_259,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_812_242,(0,0,8):C.R2GC_818_254,(0,0,1):C.R2GC_812_244,(0,0,7):C.R2GC_818_255,(0,0,2):C.R2GC_812_246,(0,0,6):C.R2GC_818_256})

V_485 = CTVertex(name = 'V_485',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3d3, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3u1] ], [ [P.g, P.YS3d3, P.YS3u1] ], [ [P.g, P.YS3d3, P.YS3u1, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_829_270,(1,0,8):C.R2GC_921_311,(1,0,1):C.R2GC_829_272,(1,0,7):C.R2GC_921_312,(1,0,2):C.R2GC_829_274,(1,0,6):C.R2GC_921_313,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_794_224,(0,0,8):C.R2GC_794_225,(0,0,1):C.R2GC_145_11,(0,0,7):C.R2GC_150_43,(0,0,2):C.R2GC_828_268,(0,0,6):C.R2GC_920_310})

V_486 = CTVertex(name = 'V_486',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3d3, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3u2] ], [ [P.g, P.YS3d3, P.YS3u2] ], [ [P.g, P.YS3d3, P.YS3u2, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_829_270,(1,0,8):C.R2GC_921_311,(1,0,1):C.R2GC_829_272,(1,0,7):C.R2GC_921_312,(1,0,2):C.R2GC_829_274,(1,0,6):C.R2GC_921_313,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_794_224,(0,0,8):C.R2GC_794_225,(0,0,1):C.R2GC_145_11,(0,0,7):C.R2GC_150_43,(0,0,2):C.R2GC_828_268,(0,0,6):C.R2GC_920_310})

V_487 = CTVertex(name = 'V_487',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3d3, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3u3] ], [ [P.g, P.YS3d3, P.YS3u3] ], [ [P.g, P.YS3d3, P.YS3u3, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_829_270,(1,0,8):C.R2GC_921_311,(1,0,1):C.R2GC_829_272,(1,0,7):C.R2GC_921_312,(1,0,2):C.R2GC_829_274,(1,0,6):C.R2GC_921_313,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_794_224,(0,0,8):C.R2GC_794_225,(0,0,1):C.R2GC_145_11,(0,0,7):C.R2GC_150_43,(0,0,2):C.R2GC_828_268,(0,0,6):C.R2GC_920_310})

V_488 = CTVertex(name = 'V_488',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3d3] ], [ [P.a, P.g, P.YS3d1, P.YS3d3] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3d3] ], [ [P.g, P.YS3d1, P.YS3d3] ], [ [P.g, P.YS3d1, P.YS3d3, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3d3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_813_248,(1,0,8):C.R2GC_813_249,(1,0,1):C.R2GC_813_250,(1,0,7):C.R2GC_813_251,(1,0,2):C.R2GC_813_252,(1,0,6):C.R2GC_813_253,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_812_242,(0,0,8):C.R2GC_812_243,(0,0,1):C.R2GC_812_244,(0,0,7):C.R2GC_812_245,(0,0,2):C.R2GC_812_246,(0,0,6):C.R2GC_812_247})

V_489 = CTVertex(name = 'V_489',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3d3] ], [ [P.a, P.g, P.YS3d2, P.YS3d3] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3d3] ], [ [P.g, P.YS3d2, P.YS3d3] ], [ [P.g, P.YS3d2, P.YS3d3, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3d3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_610_200,(1,0,4):C.R2GC_610_201,(1,0,5):C.R2GC_610_202,(1,0,0):C.R2GC_813_248,(1,0,8):C.R2GC_813_249,(1,0,1):C.R2GC_813_250,(1,0,7):C.R2GC_813_251,(1,0,2):C.R2GC_813_252,(1,0,6):C.R2GC_813_253,(0,0,3):C.R2GC_609_197,(0,0,4):C.R2GC_609_198,(0,0,5):C.R2GC_609_199,(0,0,0):C.R2GC_812_242,(0,0,8):C.R2GC_812_243,(0,0,1):C.R2GC_812_244,(0,0,7):C.R2GC_812_245,(0,0,2):C.R2GC_812_246,(0,0,6):C.R2GC_812_247})

V_490 = CTVertex(name = 'V_490',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3__tilde__, P.YS3d3, P.YS3d3 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3] ], [ [P.g] ], [ [P.g, P.YS3d3] ], [ [P.g, P.YS3d3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_326_120,(1,0,3):C.R2GC_326_121,(1,0,0):C.R2GC_794_224,(1,0,5):C.R2GC_794_225,(1,0,1):C.R2GC_794_226,(1,0,4):C.R2GC_794_227,(0,0,2):C.R2GC_326_120,(0,0,3):C.R2GC_326_121,(0,0,0):C.R2GC_794_224,(0,0,5):C.R2GC_794_225,(0,0,1):C.R2GC_794_226,(0,0,4):C.R2GC_794_227})

V_491 = CTVertex(name = 'V_491',
                 type = 'UV',
                 particles = [ P.g, P.g, P.g ],
                 color = [ 'f(1,2,3)' ],
                 lorentz = [ L.VVV2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_294_203,(0,0,1):C.UVGC_294_204,(0,0,2):C.UVGC_294_205,(0,0,3):C.UVGC_294_206,(0,0,4):C.UVGC_294_207,(0,0,5):C.UVGC_294_208,(0,0,6):C.UVGC_294_209,(0,0,7):C.UVGC_294_210,(0,0,8):C.UVGC_294_211,(0,0,9):C.UVGC_294_212,(0,0,10):C.UVGC_294_213,(0,0,11):C.UVGC_294_214,(0,0,12):C.UVGC_294_215,(0,0,13):C.UVGC_294_216,(0,0,14):C.UVGC_294_217,(0,0,15):C.UVGC_294_218,(0,0,16):C.UVGC_294_219,(0,0,17):C.UVGC_294_220,(0,0,18):C.UVGC_294_221,(0,0,19):C.UVGC_294_222,(0,0,20):C.UVGC_294_223,(0,0,21):C.UVGC_294_224,(0,0,22):C.UVGC_294_225,(0,0,23):C.UVGC_294_226,(0,0,24):C.UVGC_294_227,(0,0,25):C.UVGC_294_228,(0,0,26):C.UVGC_294_229,(0,0,27):C.UVGC_294_230,(0,0,28):C.UVGC_294_231,(0,0,29):C.UVGC_294_232,(0,0,30):C.UVGC_294_233,(0,0,31):C.UVGC_294_234})

V_492 = CTVertex(name = 'V_492',
                 type = 'UV',
                 particles = [ P.g, P.g, P.g, P.g ],
                 color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.VVVV10, L.VVVV2, L.VVVV3, L.VVVV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u], [P.YF3d1], [P.YF3d2], [P.YF3d3], [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3], [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3], [P.YF3u1], [P.YF3u2], [P.YF3u3] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u], [P.YF3d1], [P.YF3d2], [P.YF3d3], [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3], [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3], [P.YF3u1], [P.YF3u2], [P.YF3u3], [P.YS3d1], [P.YS3d2], [P.YS3d3], [P.YS3Qd1], [P.YS3Qd2], [P.YS3Qd3], [P.YS3Qu1], [P.YS3Qu2], [P.YS3Qu3], [P.YS3u1], [P.YS3u2], [P.YS3u3] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d1], [P.YS3d2], [P.YS3d3], [P.YS3Qd1], [P.YS3Qd2], [P.YS3Qd3], [P.YS3Qu1], [P.YS3Qu2], [P.YS3Qu3], [P.YS3u1], [P.YS3u2], [P.YS3u3] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,1,5):C.UVGC_288_134,(0,1,6):C.UVGC_288_133,(2,1,5):C.UVGC_288_134,(2,1,6):C.UVGC_288_133,(5,1,5):C.UVGC_287_131,(5,1,6):C.UVGC_287_132,(1,1,5):C.UVGC_287_131,(1,1,6):C.UVGC_287_132,(7,1,0):C.UVGC_296_267,(7,1,3):C.UVGC_296_268,(7,1,4):C.UVGC_296_269,(7,1,5):C.UVGC_297_299,(7,1,6):C.UVGC_297_300,(7,1,7):C.UVGC_296_272,(7,1,8):C.UVGC_296_273,(7,1,9):C.UVGC_296_274,(7,1,10):C.UVGC_296_275,(7,1,11):C.UVGC_296_276,(7,1,12):C.UVGC_296_277,(7,1,13):C.UVGC_296_278,(7,1,14):C.UVGC_296_279,(7,1,15):C.UVGC_296_280,(7,1,16):C.UVGC_296_281,(7,1,17):C.UVGC_296_282,(7,1,18):C.UVGC_296_283,(7,1,19):C.UVGC_296_284,(7,1,20):C.UVGC_296_285,(7,1,21):C.UVGC_296_286,(7,1,22):C.UVGC_296_287,(7,1,24):C.UVGC_296_288,(7,1,25):C.UVGC_296_289,(7,1,26):C.UVGC_296_290,(7,1,27):C.UVGC_296_291,(7,1,28):C.UVGC_296_292,(7,1,29):C.UVGC_296_293,(7,1,30):C.UVGC_296_294,(7,1,31):C.UVGC_296_295,(7,1,32):C.UVGC_296_296,(7,1,33):C.UVGC_296_297,(7,1,34):C.UVGC_296_298,(4,1,5):C.UVGC_287_131,(4,1,6):C.UVGC_287_132,(3,1,5):C.UVGC_287_131,(3,1,6):C.UVGC_287_132,(8,1,5):C.UVGC_288_133,(8,1,6):C.UVGC_288_134,(6,1,0):C.UVGC_296_267,(6,1,3):C.UVGC_296_268,(6,1,4):C.UVGC_296_269,(6,1,5):C.UVGC_296_270,(6,1,6):C.UVGC_296_271,(6,1,7):C.UVGC_296_272,(6,1,8):C.UVGC_296_273,(6,1,9):C.UVGC_296_274,(6,1,10):C.UVGC_296_275,(6,1,11):C.UVGC_296_276,(6,1,12):C.UVGC_296_277,(6,1,13):C.UVGC_296_278,(6,1,14):C.UVGC_296_279,(6,1,15):C.UVGC_296_280,(6,1,16):C.UVGC_296_281,(6,1,17):C.UVGC_296_282,(6,1,18):C.UVGC_296_283,(6,1,19):C.UVGC_296_284,(6,1,20):C.UVGC_296_285,(6,1,21):C.UVGC_296_286,(6,1,22):C.UVGC_296_287,(6,1,24):C.UVGC_296_288,(6,1,25):C.UVGC_296_289,(6,1,26):C.UVGC_296_290,(6,1,27):C.UVGC_296_291,(6,1,28):C.UVGC_296_292,(6,1,29):C.UVGC_296_293,(6,1,30):C.UVGC_296_294,(6,1,31):C.UVGC_296_295,(6,1,32):C.UVGC_296_296,(6,1,33):C.UVGC_296_297,(6,1,34):C.UVGC_296_298,(11,0,5):C.UVGC_291_137,(11,0,6):C.UVGC_291_138,(10,0,5):C.UVGC_291_137,(10,0,6):C.UVGC_291_138,(9,0,5):C.UVGC_290_135,(9,0,6):C.UVGC_290_136,(0,2,5):C.UVGC_288_134,(0,2,6):C.UVGC_288_133,(2,2,5):C.UVGC_288_134,(2,2,6):C.UVGC_288_133,(7,2,2):C.UVGC_298_301,(7,2,5):C.UVGC_288_133,(7,2,6):C.UVGC_301_365,(5,2,5):C.UVGC_287_131,(5,2,6):C.UVGC_287_132,(1,2,5):C.UVGC_287_131,(1,2,6):C.UVGC_287_132,(4,2,5):C.UVGC_287_131,(4,2,6):C.UVGC_287_132,(3,2,5):C.UVGC_287_131,(3,2,6):C.UVGC_287_132,(8,2,0):C.UVGC_300_334,(8,2,3):C.UVGC_300_335,(8,2,4):C.UVGC_300_336,(8,2,5):C.UVGC_297_299,(8,2,6):C.UVGC_300_337,(8,2,7):C.UVGC_300_338,(8,2,8):C.UVGC_300_339,(8,2,9):C.UVGC_300_340,(8,2,10):C.UVGC_300_341,(8,2,11):C.UVGC_300_342,(8,2,12):C.UVGC_300_343,(8,2,13):C.UVGC_300_344,(8,2,14):C.UVGC_300_345,(8,2,15):C.UVGC_300_346,(8,2,16):C.UVGC_300_347,(8,2,17):C.UVGC_300_348,(8,2,18):C.UVGC_300_349,(8,2,19):C.UVGC_300_350,(8,2,20):C.UVGC_300_351,(8,2,21):C.UVGC_300_352,(8,2,22):C.UVGC_300_353,(8,2,24):C.UVGC_300_354,(8,2,25):C.UVGC_300_355,(8,2,26):C.UVGC_300_356,(8,2,27):C.UVGC_300_357,(8,2,28):C.UVGC_300_358,(8,2,29):C.UVGC_300_359,(8,2,30):C.UVGC_300_360,(8,2,31):C.UVGC_300_361,(8,2,32):C.UVGC_300_362,(8,2,33):C.UVGC_300_363,(8,2,34):C.UVGC_300_364,(6,2,0):C.UVGC_295_235,(6,2,3):C.UVGC_295_236,(6,2,4):C.UVGC_295_237,(6,2,5):C.UVGC_302_366,(6,2,6):C.UVGC_302_367,(6,2,7):C.UVGC_295_240,(6,2,8):C.UVGC_295_241,(6,2,9):C.UVGC_295_242,(6,2,10):C.UVGC_295_243,(6,2,11):C.UVGC_295_244,(6,2,12):C.UVGC_295_245,(6,2,13):C.UVGC_295_246,(6,2,14):C.UVGC_295_247,(6,2,15):C.UVGC_295_248,(6,2,16):C.UVGC_295_249,(6,2,17):C.UVGC_295_250,(6,2,18):C.UVGC_295_251,(6,2,19):C.UVGC_295_252,(6,2,20):C.UVGC_295_253,(6,2,21):C.UVGC_295_254,(6,2,22):C.UVGC_302_368,(6,2,24):C.UVGC_302_369,(6,2,25):C.UVGC_302_370,(6,2,26):C.UVGC_302_371,(6,2,27):C.UVGC_302_372,(6,2,28):C.UVGC_302_373,(6,2,29):C.UVGC_302_374,(6,2,30):C.UVGC_302_375,(6,2,31):C.UVGC_302_376,(6,2,32):C.UVGC_302_377,(6,2,33):C.UVGC_302_378,(6,2,34):C.UVGC_302_379,(0,3,5):C.UVGC_288_134,(0,3,6):C.UVGC_288_133,(2,3,5):C.UVGC_288_134,(2,3,6):C.UVGC_288_133,(7,3,0):C.UVGC_295_235,(7,3,3):C.UVGC_295_236,(7,3,4):C.UVGC_295_237,(7,3,5):C.UVGC_295_238,(7,3,6):C.UVGC_295_239,(7,3,7):C.UVGC_295_240,(7,3,8):C.UVGC_295_241,(7,3,9):C.UVGC_295_242,(7,3,10):C.UVGC_295_243,(7,3,11):C.UVGC_295_244,(7,3,12):C.UVGC_295_245,(7,3,13):C.UVGC_295_246,(7,3,14):C.UVGC_295_247,(7,3,15):C.UVGC_295_248,(7,3,16):C.UVGC_295_249,(7,3,17):C.UVGC_295_250,(7,3,18):C.UVGC_295_251,(7,3,19):C.UVGC_295_252,(7,3,20):C.UVGC_295_253,(7,3,21):C.UVGC_295_254,(7,3,22):C.UVGC_295_255,(7,3,24):C.UVGC_295_256,(7,3,25):C.UVGC_295_257,(7,3,26):C.UVGC_295_258,(7,3,27):C.UVGC_295_259,(7,3,28):C.UVGC_295_260,(7,3,29):C.UVGC_295_261,(7,3,30):C.UVGC_295_262,(7,3,31):C.UVGC_295_263,(7,3,32):C.UVGC_295_264,(7,3,33):C.UVGC_295_265,(7,3,34):C.UVGC_295_266,(5,3,5):C.UVGC_287_131,(5,3,6):C.UVGC_287_132,(1,3,5):C.UVGC_287_131,(1,3,6):C.UVGC_287_132,(4,3,5):C.UVGC_287_131,(4,3,6):C.UVGC_287_132,(3,3,5):C.UVGC_287_131,(3,3,6):C.UVGC_287_132,(8,3,0):C.UVGC_299_303,(8,3,3):C.UVGC_299_304,(8,3,4):C.UVGC_299_305,(8,3,5):C.UVGC_295_238,(8,3,6):C.UVGC_299_306,(8,3,7):C.UVGC_299_307,(8,3,8):C.UVGC_299_308,(8,3,9):C.UVGC_299_309,(8,3,10):C.UVGC_299_310,(8,3,11):C.UVGC_299_311,(8,3,12):C.UVGC_299_312,(8,3,13):C.UVGC_299_313,(8,3,14):C.UVGC_299_314,(8,3,15):C.UVGC_299_315,(8,3,16):C.UVGC_299_316,(8,3,17):C.UVGC_299_317,(8,3,18):C.UVGC_299_318,(8,3,19):C.UVGC_299_319,(8,3,20):C.UVGC_299_320,(8,3,21):C.UVGC_299_321,(8,3,22):C.UVGC_299_322,(8,3,24):C.UVGC_299_323,(8,3,25):C.UVGC_299_324,(8,3,26):C.UVGC_299_325,(8,3,27):C.UVGC_299_326,(8,3,28):C.UVGC_299_327,(8,3,29):C.UVGC_299_328,(8,3,30):C.UVGC_299_329,(8,3,31):C.UVGC_299_330,(8,3,32):C.UVGC_299_331,(8,3,33):C.UVGC_299_332,(8,3,34):C.UVGC_299_333,(6,3,1):C.UVGC_298_301,(6,3,6):C.UVGC_290_135,(6,3,23):C.UVGC_298_302})

V_493 = CTVertex(name = 'V_493',
                 type = 'UV',
                 particles = [ P.YF3d1__tilde__, P.YF3d1, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_304_381,(0,1,0):C.UVGC_204_48,(0,2,0):C.UVGC_206_50})

V_494 = CTVertex(name = 'V_494',
                 type = 'UV',
                 particles = [ P.YF3d2__tilde__, P.YF3d2, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_304_381,(0,1,0):C.UVGC_212_56,(0,2,0):C.UVGC_214_58})

V_495 = CTVertex(name = 'V_495',
                 type = 'UV',
                 particles = [ P.YF3d3__tilde__, P.YF3d3, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_304_381,(0,1,0):C.UVGC_220_64,(0,2,0):C.UVGC_222_66})

V_496 = CTVertex(name = 'V_496',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.YF3Qd1, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_304_381,(0,1,0):C.UVGC_228_72,(0,2,0):C.UVGC_230_74})

V_497 = CTVertex(name = 'V_497',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.YF3Qd2, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_304_381,(0,1,0):C.UVGC_234_78,(0,2,0):C.UVGC_236_80})

V_498 = CTVertex(name = 'V_498',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.YF3Qd3, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_304_381,(0,1,0):C.UVGC_240_84,(0,2,0):C.UVGC_242_86})

V_499 = CTVertex(name = 'V_499',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.YF3Qu1, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_312_388,(0,1,0):C.UVGC_246_90,(0,2,0):C.UVGC_248_92})

V_500 = CTVertex(name = 'V_500',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.YF3Qu2, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_312_388,(0,1,0):C.UVGC_252_96,(0,2,0):C.UVGC_254_98})

V_501 = CTVertex(name = 'V_501',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.YF3Qu3, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_312_388,(0,1,0):C.UVGC_258_102,(0,2,0):C.UVGC_260_104})

V_502 = CTVertex(name = 'V_502',
                 type = 'UV',
                 particles = [ P.YF3u1__tilde__, P.YF3u1, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_312_388,(0,1,0):C.UVGC_264_108,(0,2,0):C.UVGC_266_110})

V_503 = CTVertex(name = 'V_503',
                 type = 'UV',
                 particles = [ P.YF3u2__tilde__, P.YF3u2, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_312_388,(0,1,0):C.UVGC_272_116,(0,2,0):C.UVGC_274_118})

V_504 = CTVertex(name = 'V_504',
                 type = 'UV',
                 particles = [ P.YF3u3__tilde__, P.YF3u3, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_312_388,(0,1,0):C.UVGC_280_124,(0,2,0):C.UVGC_282_126})

V_505 = CTVertex(name = 'V_505',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.YF3Qu1, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_787_1033,(0,0,2):C.UVGC_788_1035,(0,0,1):C.UVGC_608_896})

V_506 = CTVertex(name = 'V_506',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.YF3Qu1, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_787_1033,(0,0,2):C.UVGC_788_1035,(0,0,1):C.UVGC_608_896})

V_507 = CTVertex(name = 'V_507',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.YF3Qd1, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_607_892,(0,0,2):C.UVGC_608_895,(0,0,1):C.UVGC_608_896})

V_508 = CTVertex(name = 'V_508',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.YF3Qd1, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_607_892,(0,0,2):C.UVGC_608_895,(0,0,1):C.UVGC_608_896})

V_509 = CTVertex(name = 'V_509',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.YF3Qu2, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_599_871,(0,0,2):C.UVGC_600_874,(0,0,1):C.UVGC_600_875})

V_510 = CTVertex(name = 'V_510',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.YF3Qu2, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_599_871,(0,0,2):C.UVGC_600_874,(0,0,1):C.UVGC_600_875})

V_511 = CTVertex(name = 'V_511',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.YF3Qd2, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3Qd2] ], [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_771_996,(0,0,2):C.UVGC_772_998,(0,0,1):C.UVGC_600_875})

V_512 = CTVertex(name = 'V_512',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.YF3Qd2, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3Qd2] ], [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_771_996,(0,0,2):C.UVGC_772_998,(0,0,1):C.UVGC_600_875})

V_513 = CTVertex(name = 'V_513',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.YF3Qu3, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_780_1018,(0,0,2):C.UVGC_781_1020,(0,0,1):C.UVGC_595_861})

V_514 = CTVertex(name = 'V_514',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.YF3Qu3, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_780_1018,(0,0,2):C.UVGC_781_1020,(0,0,1):C.UVGC_595_861})

V_515 = CTVertex(name = 'V_515',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.YF3Qd3, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_594_857,(0,0,2):C.UVGC_595_860,(0,0,1):C.UVGC_595_861})

V_516 = CTVertex(name = 'V_516',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.YF3Qd3, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_594_857,(0,0,2):C.UVGC_595_860,(0,0,1):C.UVGC_595_861})

V_517 = CTVertex(name = 'V_517',
                 type = 'UV',
                 particles = [ P.YF3d1__tilde__, P.d, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3d1] ], [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_605_887,(0,0,2):C.UVGC_606_890,(0,0,1):C.UVGC_606_891})

V_518 = CTVertex(name = 'V_518',
                 type = 'UV',
                 particles = [ P.YF3d2__tilde__, P.s, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3d2] ], [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_769_991,(0,0,2):C.UVGC_770_994,(0,0,1):C.UVGC_770_995})

V_519 = CTVertex(name = 'V_519',
                 type = 'UV',
                 particles = [ P.YF3d3__tilde__, P.b, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3d3] ], [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_592_852,(0,0,2):C.UVGC_593_855,(0,0,1):C.UVGC_593_856})

V_520 = CTVertex(name = 'V_520',
                 type = 'UV',
                 particles = [ P.YF3d1__tilde__, P.d, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3d1] ], [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_605_887,(0,0,2):C.UVGC_606_890,(0,0,1):C.UVGC_606_891})

V_521 = CTVertex(name = 'V_521',
                 type = 'UV',
                 particles = [ P.YF3d2__tilde__, P.s, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3d2] ], [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_769_991,(0,0,2):C.UVGC_770_994,(0,0,1):C.UVGC_770_995})

V_522 = CTVertex(name = 'V_522',
                 type = 'UV',
                 particles = [ P.YF3d3__tilde__, P.b, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3d3] ], [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_592_852,(0,0,2):C.UVGC_593_855,(0,0,1):C.UVGC_593_856})

V_523 = CTVertex(name = 'V_523',
                 type = 'UV',
                 particles = [ P.YF3u1__tilde__, P.u, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3u1] ], [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_789_1036,(0,0,2):C.UVGC_790_1039,(0,0,1):C.UVGC_790_1040})

V_524 = CTVertex(name = 'V_524',
                 type = 'UV',
                 particles = [ P.YF3u2__tilde__, P.c, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3u2] ], [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_601_876,(0,0,2):C.UVGC_602_879,(0,0,1):C.UVGC_602_880})

V_525 = CTVertex(name = 'V_525',
                 type = 'UV',
                 particles = [ P.YF3u3__tilde__, P.t, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3u3] ], [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_782_1021,(0,0,2):C.UVGC_783_1024,(0,0,1):C.UVGC_783_1025})

V_526 = CTVertex(name = 'V_526',
                 type = 'UV',
                 particles = [ P.YF3u1__tilde__, P.u, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3u1] ], [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_789_1036,(0,0,2):C.UVGC_790_1039,(0,0,1):C.UVGC_790_1040})

V_527 = CTVertex(name = 'V_527',
                 type = 'UV',
                 particles = [ P.YF3u2__tilde__, P.c, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3u2] ], [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_601_876,(0,0,2):C.UVGC_602_879,(0,0,1):C.UVGC_602_880})

V_528 = CTVertex(name = 'V_528',
                 type = 'UV',
                 particles = [ P.YF3u3__tilde__, P.t, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3u3] ], [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_782_1021,(0,0,2):C.UVGC_783_1024,(0,0,1):C.UVGC_783_1025})

V_529 = CTVertex(name = 'V_529',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_776_1007,(0,0,2):C.UVGC_776_1008,(0,0,1):C.UVGC_776_1009,(0,1,0):C.UVGC_775_1004,(0,1,2):C.UVGC_775_1005,(0,1,1):C.UVGC_775_1006})

V_530 = CTVertex(name = 'V_530',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_506_804})

V_531 = CTVertex(name = 'V_531',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_505_803})

V_532 = CTVertex(name = 'V_532',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_774_1001,(0,0,2):C.UVGC_774_1002,(0,0,1):C.UVGC_774_1003,(0,1,0):C.UVGC_777_1010,(0,1,2):C.UVGC_777_1011,(0,1,1):C.UVGC_777_1012})

V_533 = CTVertex(name = 'V_533',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_309_386})

V_534 = CTVertex(name = 'V_534',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_310_387})

V_535 = CTVertex(name = 'V_535',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.YF3d1, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3d1] ], [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_605_887,(0,0,2):C.UVGC_606_890,(0,0,1):C.UVGC_606_891})

V_536 = CTVertex(name = 'V_536',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.YF3d2, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3d2] ], [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_769_991,(0,0,2):C.UVGC_770_994,(0,0,1):C.UVGC_770_995})

V_537 = CTVertex(name = 'V_537',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.YF3d3, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3d3] ], [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_592_852,(0,0,2):C.UVGC_593_855,(0,0,1):C.UVGC_593_856})

V_538 = CTVertex(name = 'V_538',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.YF3d1, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3d1] ], [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_605_887,(0,0,2):C.UVGC_606_890,(0,0,1):C.UVGC_606_891})

V_539 = CTVertex(name = 'V_539',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.YF3d2, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3d2] ], [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_769_991,(0,0,2):C.UVGC_770_994,(0,0,1):C.UVGC_770_995})

V_540 = CTVertex(name = 'V_540',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.YF3d3, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3d3] ], [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_592_852,(0,0,2):C.UVGC_593_855,(0,0,1):C.UVGC_593_856})

V_541 = CTVertex(name = 'V_541',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.YF3u1, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3u1] ], [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_789_1036,(0,0,2):C.UVGC_790_1039,(0,0,1):C.UVGC_790_1040})

V_542 = CTVertex(name = 'V_542',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.YF3u2, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3u2] ], [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_601_876,(0,0,2):C.UVGC_602_879,(0,0,1):C.UVGC_602_880})

V_543 = CTVertex(name = 'V_543',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.YF3u3, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3u3] ], [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_782_1021,(0,0,2):C.UVGC_783_1024,(0,0,1):C.UVGC_783_1025})

V_544 = CTVertex(name = 'V_544',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.YF3u1, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3u1] ], [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_789_1036,(0,0,2):C.UVGC_790_1039,(0,0,1):C.UVGC_790_1040})

V_545 = CTVertex(name = 'V_545',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.YF3u2, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3u2] ], [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_601_876,(0,0,2):C.UVGC_602_879,(0,0,1):C.UVGC_602_880})

V_546 = CTVertex(name = 'V_546',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.YF3u3, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3u3] ], [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_782_1021,(0,0,2):C.UVGC_783_1024,(0,0,1):C.UVGC_783_1025})

V_547 = CTVertex(name = 'V_547',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.u, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_787_1033,(0,0,2):C.UVGC_788_1035,(0,0,1):C.UVGC_608_896})

V_548 = CTVertex(name = 'V_548',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.u, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_787_1033,(0,0,2):C.UVGC_788_1035,(0,0,1):C.UVGC_608_896})

V_549 = CTVertex(name = 'V_549',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.d, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_607_892,(0,0,2):C.UVGC_608_895,(0,0,1):C.UVGC_608_896})

V_550 = CTVertex(name = 'V_550',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.d, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_607_892,(0,0,2):C.UVGC_608_895,(0,0,1):C.UVGC_608_896})

V_551 = CTVertex(name = 'V_551',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.c, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_599_871,(0,0,2):C.UVGC_600_874,(0,0,1):C.UVGC_600_875})

V_552 = CTVertex(name = 'V_552',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.c, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_599_871,(0,0,2):C.UVGC_600_874,(0,0,1):C.UVGC_600_875})

V_553 = CTVertex(name = 'V_553',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.s, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3Qd2] ], [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_771_996,(0,0,2):C.UVGC_772_998,(0,0,1):C.UVGC_600_875})

V_554 = CTVertex(name = 'V_554',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.s, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3Qd2] ], [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_771_996,(0,0,2):C.UVGC_772_998,(0,0,1):C.UVGC_600_875})

V_555 = CTVertex(name = 'V_555',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.t, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_780_1018,(0,0,2):C.UVGC_781_1020,(0,0,1):C.UVGC_595_861})

V_556 = CTVertex(name = 'V_556',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.t, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_780_1018,(0,0,2):C.UVGC_781_1020,(0,0,1):C.UVGC_595_861})

V_557 = CTVertex(name = 'V_557',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.b, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_594_857,(0,0,2):C.UVGC_595_860,(0,0,1):C.UVGC_595_861})

V_558 = CTVertex(name = 'V_558',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.b, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_594_857,(0,0,2):C.UVGC_595_860,(0,0,1):C.UVGC_595_861})

V_559 = CTVertex(name = 'V_559',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.YF3Qd1, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3Qd1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_305_382,(0,3,0):C.UVGC_292_139,(0,3,1):C.UVGC_292_140,(0,3,2):C.UVGC_292_141,(0,3,3):C.UVGC_292_142,(0,3,4):C.UVGC_292_143,(0,3,6):C.UVGC_292_144,(0,3,7):C.UVGC_292_145,(0,3,8):C.UVGC_292_146,(0,3,9):C.UVGC_292_147,(0,3,10):C.UVGC_292_148,(0,3,11):C.UVGC_292_149,(0,3,12):C.UVGC_292_150,(0,3,13):C.UVGC_292_151,(0,3,14):C.UVGC_292_152,(0,3,15):C.UVGC_292_153,(0,3,16):C.UVGC_292_154,(0,3,17):C.UVGC_292_155,(0,3,18):C.UVGC_292_156,(0,3,19):C.UVGC_292_157,(0,3,20):C.UVGC_292_158,(0,3,21):C.UVGC_292_159,(0,3,22):C.UVGC_292_160,(0,3,23):C.UVGC_292_161,(0,3,24):C.UVGC_292_162,(0,3,25):C.UVGC_292_163,(0,3,26):C.UVGC_292_164,(0,3,27):C.UVGC_292_165,(0,3,28):C.UVGC_292_166,(0,3,29):C.UVGC_292_167,(0,3,30):C.UVGC_292_168,(0,3,31):C.UVGC_292_169,(0,3,32):C.UVGC_292_170,(0,1,5):C.UVGC_231_75,(0,2,5):C.UVGC_232_76})

V_560 = CTVertex(name = 'V_560',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.YF3Qd2, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3Qd2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_305_382,(0,3,0):C.UVGC_292_139,(0,3,1):C.UVGC_292_140,(0,3,2):C.UVGC_292_141,(0,3,3):C.UVGC_292_142,(0,3,4):C.UVGC_292_143,(0,3,6):C.UVGC_292_144,(0,3,7):C.UVGC_292_145,(0,3,8):C.UVGC_292_146,(0,3,9):C.UVGC_292_147,(0,3,10):C.UVGC_292_148,(0,3,11):C.UVGC_292_149,(0,3,12):C.UVGC_292_150,(0,3,13):C.UVGC_292_151,(0,3,14):C.UVGC_292_152,(0,3,15):C.UVGC_292_153,(0,3,16):C.UVGC_292_154,(0,3,17):C.UVGC_292_155,(0,3,18):C.UVGC_292_156,(0,3,19):C.UVGC_292_157,(0,3,20):C.UVGC_292_158,(0,3,21):C.UVGC_292_159,(0,3,22):C.UVGC_292_160,(0,3,23):C.UVGC_292_161,(0,3,24):C.UVGC_292_162,(0,3,25):C.UVGC_292_163,(0,3,26):C.UVGC_292_164,(0,3,27):C.UVGC_292_165,(0,3,28):C.UVGC_292_166,(0,3,29):C.UVGC_292_167,(0,3,30):C.UVGC_292_168,(0,3,31):C.UVGC_292_169,(0,3,32):C.UVGC_292_170,(0,1,5):C.UVGC_237_81,(0,2,5):C.UVGC_238_82})

V_561 = CTVertex(name = 'V_561',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.YF3Qd3, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3Qd3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_305_382,(0,3,0):C.UVGC_292_139,(0,3,1):C.UVGC_292_140,(0,3,2):C.UVGC_292_141,(0,3,3):C.UVGC_292_142,(0,3,4):C.UVGC_292_143,(0,3,6):C.UVGC_292_144,(0,3,7):C.UVGC_292_145,(0,3,8):C.UVGC_292_146,(0,3,9):C.UVGC_292_147,(0,3,10):C.UVGC_292_148,(0,3,11):C.UVGC_292_149,(0,3,12):C.UVGC_292_150,(0,3,13):C.UVGC_292_151,(0,3,14):C.UVGC_292_152,(0,3,15):C.UVGC_292_153,(0,3,16):C.UVGC_292_154,(0,3,17):C.UVGC_292_155,(0,3,18):C.UVGC_292_156,(0,3,19):C.UVGC_292_157,(0,3,20):C.UVGC_292_158,(0,3,21):C.UVGC_292_159,(0,3,22):C.UVGC_292_160,(0,3,23):C.UVGC_292_161,(0,3,24):C.UVGC_292_162,(0,3,25):C.UVGC_292_163,(0,3,26):C.UVGC_292_164,(0,3,27):C.UVGC_292_165,(0,3,28):C.UVGC_292_166,(0,3,29):C.UVGC_292_167,(0,3,30):C.UVGC_292_168,(0,3,31):C.UVGC_292_169,(0,3,32):C.UVGC_292_170,(0,1,5):C.UVGC_243_87,(0,2,5):C.UVGC_244_88})

V_562 = CTVertex(name = 'V_562',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.YF3Qu1, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3Qu1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_305_382,(0,3,0):C.UVGC_292_139,(0,3,1):C.UVGC_292_140,(0,3,2):C.UVGC_292_141,(0,3,3):C.UVGC_292_142,(0,3,4):C.UVGC_292_143,(0,3,6):C.UVGC_292_144,(0,3,7):C.UVGC_292_145,(0,3,8):C.UVGC_292_146,(0,3,9):C.UVGC_292_147,(0,3,10):C.UVGC_292_148,(0,3,11):C.UVGC_292_149,(0,3,12):C.UVGC_292_150,(0,3,13):C.UVGC_292_151,(0,3,14):C.UVGC_292_152,(0,3,15):C.UVGC_292_153,(0,3,16):C.UVGC_292_154,(0,3,17):C.UVGC_292_155,(0,3,18):C.UVGC_292_156,(0,3,19):C.UVGC_292_157,(0,3,20):C.UVGC_292_158,(0,3,21):C.UVGC_292_159,(0,3,22):C.UVGC_292_160,(0,3,23):C.UVGC_292_161,(0,3,24):C.UVGC_292_162,(0,3,25):C.UVGC_292_163,(0,3,26):C.UVGC_292_164,(0,3,27):C.UVGC_292_165,(0,3,28):C.UVGC_292_166,(0,3,29):C.UVGC_292_167,(0,3,30):C.UVGC_292_168,(0,3,31):C.UVGC_292_169,(0,3,32):C.UVGC_292_170,(0,1,5):C.UVGC_249_93,(0,2,5):C.UVGC_250_94})

V_563 = CTVertex(name = 'V_563',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.YF3Qu2, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3Qu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_305_382,(0,3,0):C.UVGC_292_139,(0,3,1):C.UVGC_292_140,(0,3,2):C.UVGC_292_141,(0,3,3):C.UVGC_292_142,(0,3,4):C.UVGC_292_143,(0,3,6):C.UVGC_292_144,(0,3,7):C.UVGC_292_145,(0,3,8):C.UVGC_292_146,(0,3,9):C.UVGC_292_147,(0,3,10):C.UVGC_292_148,(0,3,11):C.UVGC_292_149,(0,3,12):C.UVGC_292_150,(0,3,13):C.UVGC_292_151,(0,3,14):C.UVGC_292_152,(0,3,15):C.UVGC_292_153,(0,3,16):C.UVGC_292_154,(0,3,17):C.UVGC_292_155,(0,3,18):C.UVGC_292_156,(0,3,19):C.UVGC_292_157,(0,3,20):C.UVGC_292_158,(0,3,21):C.UVGC_292_159,(0,3,22):C.UVGC_292_160,(0,3,23):C.UVGC_292_161,(0,3,24):C.UVGC_292_162,(0,3,25):C.UVGC_292_163,(0,3,26):C.UVGC_292_164,(0,3,27):C.UVGC_292_165,(0,3,28):C.UVGC_292_166,(0,3,29):C.UVGC_292_167,(0,3,30):C.UVGC_292_168,(0,3,31):C.UVGC_292_169,(0,3,32):C.UVGC_292_170,(0,1,5):C.UVGC_255_99,(0,2,5):C.UVGC_256_100})

V_564 = CTVertex(name = 'V_564',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.YF3Qu3, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3Qu3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_305_382,(0,3,0):C.UVGC_292_139,(0,3,1):C.UVGC_292_140,(0,3,2):C.UVGC_292_141,(0,3,3):C.UVGC_292_142,(0,3,4):C.UVGC_292_143,(0,3,6):C.UVGC_292_144,(0,3,7):C.UVGC_292_145,(0,3,8):C.UVGC_292_146,(0,3,9):C.UVGC_292_147,(0,3,10):C.UVGC_292_148,(0,3,11):C.UVGC_292_149,(0,3,12):C.UVGC_292_150,(0,3,13):C.UVGC_292_151,(0,3,14):C.UVGC_292_152,(0,3,15):C.UVGC_292_153,(0,3,16):C.UVGC_292_154,(0,3,17):C.UVGC_292_155,(0,3,18):C.UVGC_292_156,(0,3,19):C.UVGC_292_157,(0,3,20):C.UVGC_292_158,(0,3,21):C.UVGC_292_159,(0,3,22):C.UVGC_292_160,(0,3,23):C.UVGC_292_161,(0,3,24):C.UVGC_292_162,(0,3,25):C.UVGC_292_163,(0,3,26):C.UVGC_292_164,(0,3,27):C.UVGC_292_165,(0,3,28):C.UVGC_292_166,(0,3,29):C.UVGC_292_167,(0,3,30):C.UVGC_292_168,(0,3,31):C.UVGC_292_169,(0,3,32):C.UVGC_292_170,(0,1,5):C.UVGC_261_105,(0,2,5):C.UVGC_262_106})

V_565 = CTVertex(name = 'V_565',
                 type = 'UV',
                 particles = [ P.YF3u1__tilde__, P.YF3u1, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3u1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_305_382,(0,3,0):C.UVGC_292_139,(0,3,1):C.UVGC_292_140,(0,3,2):C.UVGC_292_141,(0,3,3):C.UVGC_292_142,(0,3,4):C.UVGC_292_143,(0,3,6):C.UVGC_292_144,(0,3,7):C.UVGC_292_145,(0,3,8):C.UVGC_292_146,(0,3,9):C.UVGC_292_147,(0,3,10):C.UVGC_292_148,(0,3,11):C.UVGC_292_149,(0,3,12):C.UVGC_292_150,(0,3,13):C.UVGC_292_151,(0,3,14):C.UVGC_292_152,(0,3,15):C.UVGC_292_153,(0,3,16):C.UVGC_292_154,(0,3,17):C.UVGC_292_155,(0,3,18):C.UVGC_292_156,(0,3,19):C.UVGC_292_157,(0,3,20):C.UVGC_292_158,(0,3,21):C.UVGC_292_159,(0,3,22):C.UVGC_292_160,(0,3,23):C.UVGC_292_161,(0,3,24):C.UVGC_292_162,(0,3,25):C.UVGC_292_163,(0,3,26):C.UVGC_292_164,(0,3,27):C.UVGC_292_165,(0,3,28):C.UVGC_292_166,(0,3,29):C.UVGC_292_167,(0,3,30):C.UVGC_292_168,(0,3,31):C.UVGC_292_169,(0,3,32):C.UVGC_292_170,(0,1,5):C.UVGC_267_111,(0,2,5):C.UVGC_268_112})

V_566 = CTVertex(name = 'V_566',
                 type = 'UV',
                 particles = [ P.YF3u2__tilde__, P.YF3u2, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3u2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_305_382,(0,3,0):C.UVGC_292_139,(0,3,1):C.UVGC_292_140,(0,3,2):C.UVGC_292_141,(0,3,3):C.UVGC_292_142,(0,3,4):C.UVGC_292_143,(0,3,6):C.UVGC_292_144,(0,3,7):C.UVGC_292_145,(0,3,8):C.UVGC_292_146,(0,3,9):C.UVGC_292_147,(0,3,10):C.UVGC_292_148,(0,3,11):C.UVGC_292_149,(0,3,12):C.UVGC_292_150,(0,3,13):C.UVGC_292_151,(0,3,14):C.UVGC_292_152,(0,3,15):C.UVGC_292_153,(0,3,16):C.UVGC_292_154,(0,3,17):C.UVGC_292_155,(0,3,18):C.UVGC_292_156,(0,3,19):C.UVGC_292_157,(0,3,20):C.UVGC_292_158,(0,3,21):C.UVGC_292_159,(0,3,22):C.UVGC_292_160,(0,3,23):C.UVGC_292_161,(0,3,24):C.UVGC_292_162,(0,3,25):C.UVGC_292_163,(0,3,26):C.UVGC_292_164,(0,3,27):C.UVGC_292_165,(0,3,28):C.UVGC_292_166,(0,3,29):C.UVGC_292_167,(0,3,30):C.UVGC_292_168,(0,3,31):C.UVGC_292_169,(0,3,32):C.UVGC_292_170,(0,1,5):C.UVGC_275_119,(0,2,5):C.UVGC_276_120})

V_567 = CTVertex(name = 'V_567',
                 type = 'UV',
                 particles = [ P.YF3u3__tilde__, P.YF3u3, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3u3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_305_382,(0,3,0):C.UVGC_292_139,(0,3,1):C.UVGC_292_140,(0,3,2):C.UVGC_292_141,(0,3,3):C.UVGC_292_142,(0,3,4):C.UVGC_292_143,(0,3,6):C.UVGC_292_144,(0,3,7):C.UVGC_292_145,(0,3,8):C.UVGC_292_146,(0,3,9):C.UVGC_292_147,(0,3,10):C.UVGC_292_148,(0,3,11):C.UVGC_292_149,(0,3,12):C.UVGC_292_150,(0,3,13):C.UVGC_292_151,(0,3,14):C.UVGC_292_152,(0,3,15):C.UVGC_292_153,(0,3,16):C.UVGC_292_154,(0,3,17):C.UVGC_292_155,(0,3,18):C.UVGC_292_156,(0,3,19):C.UVGC_292_157,(0,3,20):C.UVGC_292_158,(0,3,21):C.UVGC_292_159,(0,3,22):C.UVGC_292_160,(0,3,23):C.UVGC_292_161,(0,3,24):C.UVGC_292_162,(0,3,25):C.UVGC_292_163,(0,3,26):C.UVGC_292_164,(0,3,27):C.UVGC_292_165,(0,3,28):C.UVGC_292_166,(0,3,29):C.UVGC_292_167,(0,3,30):C.UVGC_292_168,(0,3,31):C.UVGC_292_169,(0,3,32):C.UVGC_292_170,(0,1,5):C.UVGC_283_127,(0,2,5):C.UVGC_284_128})

V_568 = CTVertex(name = 'V_568',
                 type = 'UV',
                 particles = [ P.YF3d1__tilde__, P.YF3d1, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3d1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_305_382,(0,3,0):C.UVGC_292_139,(0,3,1):C.UVGC_292_140,(0,3,2):C.UVGC_292_141,(0,3,3):C.UVGC_292_142,(0,3,4):C.UVGC_292_143,(0,3,6):C.UVGC_292_144,(0,3,7):C.UVGC_292_145,(0,3,8):C.UVGC_292_146,(0,3,9):C.UVGC_292_147,(0,3,10):C.UVGC_292_148,(0,3,11):C.UVGC_292_149,(0,3,12):C.UVGC_292_150,(0,3,13):C.UVGC_292_151,(0,3,14):C.UVGC_292_152,(0,3,15):C.UVGC_292_153,(0,3,16):C.UVGC_292_154,(0,3,17):C.UVGC_292_155,(0,3,18):C.UVGC_292_156,(0,3,19):C.UVGC_292_157,(0,3,20):C.UVGC_292_158,(0,3,21):C.UVGC_292_159,(0,3,22):C.UVGC_292_160,(0,3,23):C.UVGC_292_161,(0,3,24):C.UVGC_292_162,(0,3,25):C.UVGC_292_163,(0,3,26):C.UVGC_292_164,(0,3,27):C.UVGC_292_165,(0,3,28):C.UVGC_292_166,(0,3,29):C.UVGC_292_167,(0,3,30):C.UVGC_292_168,(0,3,31):C.UVGC_292_169,(0,3,32):C.UVGC_292_170,(0,1,5):C.UVGC_207_51,(0,2,5):C.UVGC_208_52})

V_569 = CTVertex(name = 'V_569',
                 type = 'UV',
                 particles = [ P.YF3d2__tilde__, P.YF3d2, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3d2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_305_382,(0,3,0):C.UVGC_292_139,(0,3,1):C.UVGC_292_140,(0,3,2):C.UVGC_292_141,(0,3,3):C.UVGC_292_142,(0,3,4):C.UVGC_292_143,(0,3,6):C.UVGC_292_144,(0,3,7):C.UVGC_292_145,(0,3,8):C.UVGC_292_146,(0,3,9):C.UVGC_292_147,(0,3,10):C.UVGC_292_148,(0,3,11):C.UVGC_292_149,(0,3,12):C.UVGC_292_150,(0,3,13):C.UVGC_292_151,(0,3,14):C.UVGC_292_152,(0,3,15):C.UVGC_292_153,(0,3,16):C.UVGC_292_154,(0,3,17):C.UVGC_292_155,(0,3,18):C.UVGC_292_156,(0,3,19):C.UVGC_292_157,(0,3,20):C.UVGC_292_158,(0,3,21):C.UVGC_292_159,(0,3,22):C.UVGC_292_160,(0,3,23):C.UVGC_292_161,(0,3,24):C.UVGC_292_162,(0,3,25):C.UVGC_292_163,(0,3,26):C.UVGC_292_164,(0,3,27):C.UVGC_292_165,(0,3,28):C.UVGC_292_166,(0,3,29):C.UVGC_292_167,(0,3,30):C.UVGC_292_168,(0,3,31):C.UVGC_292_169,(0,3,32):C.UVGC_292_170,(0,1,5):C.UVGC_215_59,(0,2,5):C.UVGC_216_60})

V_570 = CTVertex(name = 'V_570',
                 type = 'UV',
                 particles = [ P.YF3d3__tilde__, P.YF3d3, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3d3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_305_382,(0,3,0):C.UVGC_292_139,(0,3,1):C.UVGC_292_140,(0,3,2):C.UVGC_292_141,(0,3,3):C.UVGC_292_142,(0,3,4):C.UVGC_292_143,(0,3,6):C.UVGC_292_144,(0,3,7):C.UVGC_292_145,(0,3,8):C.UVGC_292_146,(0,3,9):C.UVGC_292_147,(0,3,10):C.UVGC_292_148,(0,3,11):C.UVGC_292_149,(0,3,12):C.UVGC_292_150,(0,3,13):C.UVGC_292_151,(0,3,14):C.UVGC_292_152,(0,3,15):C.UVGC_292_153,(0,3,16):C.UVGC_292_154,(0,3,17):C.UVGC_292_155,(0,3,18):C.UVGC_292_156,(0,3,19):C.UVGC_292_157,(0,3,20):C.UVGC_292_158,(0,3,21):C.UVGC_292_159,(0,3,22):C.UVGC_292_160,(0,3,23):C.UVGC_292_161,(0,3,24):C.UVGC_292_162,(0,3,25):C.UVGC_292_163,(0,3,26):C.UVGC_292_164,(0,3,27):C.UVGC_292_165,(0,3,28):C.UVGC_292_166,(0,3,29):C.UVGC_292_167,(0,3,30):C.UVGC_292_168,(0,3,31):C.UVGC_292_169,(0,3,32):C.UVGC_292_170,(0,1,5):C.UVGC_223_67,(0,2,5):C.UVGC_224_68})

V_571 = CTVertex(name = 'V_571',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.YF3Qu1, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,1):C.UVGC_598_870,(0,1,0):C.UVGC_552_821,(0,1,2):C.UVGC_552_822,(0,2,0):C.UVGC_553_823,(0,2,2):C.UVGC_553_824})

V_572 = CTVertex(name = 'V_572',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.YF3Qu2, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd2] ], [ [P.g, P.YF3Qd2, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,1):C.UVGC_598_870,(0,1,0):C.UVGC_561_829,(0,1,2):C.UVGC_561_830,(0,2,0):C.UVGC_562_831,(0,2,2):C.UVGC_562_832})

V_573 = CTVertex(name = 'V_573',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.YF3Qu3, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,1):C.UVGC_598_870,(0,1,0):C.UVGC_570_836,(0,1,2):C.UVGC_570_837,(0,2,0):C.UVGC_571_838,(0,2,2):C.UVGC_571_839})

V_574 = CTVertex(name = 'V_574',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.YF3Qd1, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,1):C.UVGC_598_870,(0,1,0):C.UVGC_552_821,(0,1,2):C.UVGC_552_822,(0,2,0):C.UVGC_553_823,(0,2,2):C.UVGC_553_824})

V_575 = CTVertex(name = 'V_575',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.YF3Qd2, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd2] ], [ [P.g, P.YF3Qd2, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,1):C.UVGC_598_870,(0,1,0):C.UVGC_561_829,(0,1,2):C.UVGC_561_830,(0,2,0):C.UVGC_562_831,(0,2,2):C.UVGC_562_832})

V_576 = CTVertex(name = 'V_576',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.YF3Qd3, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,1):C.UVGC_598_870,(0,1,0):C.UVGC_570_836,(0,1,2):C.UVGC_570_837,(0,2,0):C.UVGC_571_838,(0,2,2):C.UVGC_571_839})

V_577 = CTVertex(name = 'V_577',
                 type = 'UV',
                 particles = [ P.a, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_322_392})

V_578 = CTVertex(name = 'V_578',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.d, P.YS3d1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YS3d1] ], [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_603_881,(0,0,2):C.UVGC_603_882,(0,0,1):C.UVGC_603_883})

V_579 = CTVertex(name = 'V_579',
                 type = 'UV',
                 particles = [ P.Xm, P.d, P.YS3d1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YS3d1] ], [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_603_881,(0,0,2):C.UVGC_603_882,(0,0,1):C.UVGC_603_883})

V_580 = CTVertex(name = 'V_580',
                 type = 'UV',
                 particles = [ P.g, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_324_394,(0,0,1):C.UVGC_324_395,(0,0,2):C.UVGC_324_396,(0,0,3):C.UVGC_324_397,(0,0,4):C.UVGC_324_398,(0,0,6):C.UVGC_324_399,(0,0,7):C.UVGC_324_400,(0,0,8):C.UVGC_324_401,(0,0,9):C.UVGC_324_402,(0,0,10):C.UVGC_324_403,(0,0,11):C.UVGC_324_404,(0,0,12):C.UVGC_324_405,(0,0,13):C.UVGC_324_406,(0,0,14):C.UVGC_324_407,(0,0,15):C.UVGC_324_408,(0,0,16):C.UVGC_324_409,(0,0,17):C.UVGC_324_410,(0,0,18):C.UVGC_324_411,(0,0,19):C.UVGC_324_412,(0,0,20):C.UVGC_324_413,(0,0,21):C.UVGC_324_414,(0,0,22):C.UVGC_324_415,(0,0,23):C.UVGC_324_416,(0,0,24):C.UVGC_324_417,(0,0,25):C.UVGC_324_418,(0,0,26):C.UVGC_324_419,(0,0,27):C.UVGC_324_420,(0,0,28):C.UVGC_324_421,(0,0,29):C.UVGC_324_422,(0,0,30):C.UVGC_324_423,(0,0,31):C.UVGC_324_424,(0,0,32):C.UVGC_324_425,(0,0,5):C.UVGC_324_426})

V_581 = CTVertex(name = 'V_581',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.Xd, P.YS3d1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YS3d1] ], [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_603_881,(0,0,2):C.UVGC_603_882,(0,0,1):C.UVGC_603_883})

V_582 = CTVertex(name = 'V_582',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.Xm, P.YS3d1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YS3d1] ], [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_603_881,(0,0,2):C.UVGC_603_882,(0,0,1):C.UVGC_603_883})

V_583 = CTVertex(name = 'V_583',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_323_393})

V_584 = CTVertex(name = 'V_584',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_325_427,(0,0,1):C.UVGC_325_428,(0,0,2):C.UVGC_325_429,(0,0,3):C.UVGC_325_430,(0,0,4):C.UVGC_325_431,(0,0,6):C.UVGC_325_432,(0,0,7):C.UVGC_325_433,(0,0,8):C.UVGC_325_434,(0,0,9):C.UVGC_325_435,(0,0,10):C.UVGC_325_436,(0,0,11):C.UVGC_325_437,(0,0,12):C.UVGC_325_438,(0,0,13):C.UVGC_325_439,(0,0,14):C.UVGC_325_440,(0,0,15):C.UVGC_325_441,(0,0,16):C.UVGC_325_442,(0,0,17):C.UVGC_325_443,(0,0,18):C.UVGC_325_444,(0,0,19):C.UVGC_325_445,(0,0,20):C.UVGC_325_446,(0,0,21):C.UVGC_325_447,(0,0,22):C.UVGC_325_448,(0,0,23):C.UVGC_325_449,(0,0,24):C.UVGC_325_450,(0,0,25):C.UVGC_325_451,(0,0,26):C.UVGC_325_452,(0,0,27):C.UVGC_325_453,(0,0,28):C.UVGC_325_454,(0,0,29):C.UVGC_325_455,(0,0,30):C.UVGC_325_456,(0,0,31):C.UVGC_325_457,(0,0,32):C.UVGC_325_458,(0,0,5):C.UVGC_325_459})

V_585 = CTVertex(name = 'V_585',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_328_464,(2,0,1):C.UVGC_328_465,(2,0,2):C.UVGC_328_466,(2,0,3):C.UVGC_328_467,(2,0,4):C.UVGC_328_468,(2,0,6):C.UVGC_328_469,(2,0,7):C.UVGC_328_470,(2,0,8):C.UVGC_328_471,(2,0,9):C.UVGC_328_472,(2,0,10):C.UVGC_328_473,(2,0,11):C.UVGC_328_474,(2,0,12):C.UVGC_328_475,(2,0,13):C.UVGC_328_476,(2,0,14):C.UVGC_328_477,(2,0,15):C.UVGC_328_478,(2,0,16):C.UVGC_328_479,(2,0,17):C.UVGC_328_480,(2,0,18):C.UVGC_328_481,(2,0,19):C.UVGC_328_482,(2,0,20):C.UVGC_328_483,(2,0,21):C.UVGC_328_484,(2,0,22):C.UVGC_328_485,(2,0,23):C.UVGC_328_486,(2,0,24):C.UVGC_328_487,(2,0,25):C.UVGC_328_488,(2,0,26):C.UVGC_328_489,(2,0,27):C.UVGC_328_490,(2,0,28):C.UVGC_328_491,(2,0,29):C.UVGC_328_492,(2,0,30):C.UVGC_328_493,(2,0,31):C.UVGC_328_494,(2,0,32):C.UVGC_328_495,(2,0,5):C.UVGC_328_496,(1,0,0):C.UVGC_328_464,(1,0,1):C.UVGC_328_465,(1,0,2):C.UVGC_328_466,(1,0,3):C.UVGC_328_467,(1,0,4):C.UVGC_328_468,(1,0,6):C.UVGC_328_469,(1,0,7):C.UVGC_328_470,(1,0,8):C.UVGC_328_471,(1,0,9):C.UVGC_328_472,(1,0,10):C.UVGC_328_473,(1,0,11):C.UVGC_328_474,(1,0,12):C.UVGC_328_475,(1,0,13):C.UVGC_328_476,(1,0,14):C.UVGC_328_477,(1,0,15):C.UVGC_328_478,(1,0,16):C.UVGC_328_479,(1,0,17):C.UVGC_328_480,(1,0,18):C.UVGC_328_481,(1,0,19):C.UVGC_328_482,(1,0,20):C.UVGC_328_483,(1,0,21):C.UVGC_328_484,(1,0,22):C.UVGC_328_485,(1,0,23):C.UVGC_328_486,(1,0,24):C.UVGC_328_487,(1,0,25):C.UVGC_328_488,(1,0,26):C.UVGC_328_489,(1,0,27):C.UVGC_328_490,(1,0,28):C.UVGC_328_491,(1,0,29):C.UVGC_328_492,(1,0,30):C.UVGC_328_493,(1,0,31):C.UVGC_328_494,(1,0,32):C.UVGC_328_495,(1,0,5):C.UVGC_328_496,(0,0,3):C.UVGC_327_462,(0,0,5):C.UVGC_327_463})

V_586 = CTVertex(name = 'V_586',
                 type = 'UV',
                 particles = [ P.a, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_335_535})

V_587 = CTVertex(name = 'V_587',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.s, P.YS3d2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YS3d2] ], [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_767_986,(0,0,2):C.UVGC_767_987,(0,0,1):C.UVGC_767_988})

V_588 = CTVertex(name = 'V_588',
                 type = 'UV',
                 particles = [ P.Xm, P.s, P.YS3d2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YS3d2] ], [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_767_986,(0,0,2):C.UVGC_767_987,(0,0,1):C.UVGC_767_988})

V_589 = CTVertex(name = 'V_589',
                 type = 'UV',
                 particles = [ P.g, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_324_394,(0,0,1):C.UVGC_324_395,(0,0,2):C.UVGC_324_396,(0,0,3):C.UVGC_324_397,(0,0,4):C.UVGC_324_398,(0,0,6):C.UVGC_324_399,(0,0,7):C.UVGC_324_400,(0,0,8):C.UVGC_324_401,(0,0,9):C.UVGC_324_402,(0,0,10):C.UVGC_324_403,(0,0,11):C.UVGC_324_404,(0,0,12):C.UVGC_324_405,(0,0,13):C.UVGC_324_406,(0,0,14):C.UVGC_324_407,(0,0,15):C.UVGC_324_408,(0,0,16):C.UVGC_324_409,(0,0,17):C.UVGC_324_410,(0,0,18):C.UVGC_324_411,(0,0,19):C.UVGC_324_412,(0,0,20):C.UVGC_324_413,(0,0,21):C.UVGC_324_414,(0,0,22):C.UVGC_324_415,(0,0,23):C.UVGC_324_416,(0,0,24):C.UVGC_324_417,(0,0,25):C.UVGC_324_418,(0,0,26):C.UVGC_324_419,(0,0,27):C.UVGC_324_420,(0,0,28):C.UVGC_324_421,(0,0,29):C.UVGC_324_422,(0,0,30):C.UVGC_324_423,(0,0,31):C.UVGC_324_424,(0,0,32):C.UVGC_324_425,(0,0,5):C.UVGC_337_537})

V_590 = CTVertex(name = 'V_590',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.Xd, P.YS3d2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YS3d2] ], [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_767_986,(0,0,2):C.UVGC_767_987,(0,0,1):C.UVGC_767_988})

V_591 = CTVertex(name = 'V_591',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.Xm, P.YS3d2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YS3d2] ], [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_767_986,(0,0,2):C.UVGC_767_987,(0,0,1):C.UVGC_767_988})

V_592 = CTVertex(name = 'V_592',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_336_536})

V_593 = CTVertex(name = 'V_593',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_325_427,(0,0,1):C.UVGC_325_428,(0,0,2):C.UVGC_325_429,(0,0,3):C.UVGC_325_430,(0,0,4):C.UVGC_325_431,(0,0,6):C.UVGC_325_432,(0,0,7):C.UVGC_325_433,(0,0,8):C.UVGC_325_434,(0,0,9):C.UVGC_325_435,(0,0,10):C.UVGC_325_436,(0,0,11):C.UVGC_325_437,(0,0,12):C.UVGC_325_438,(0,0,13):C.UVGC_325_439,(0,0,14):C.UVGC_325_440,(0,0,15):C.UVGC_325_441,(0,0,16):C.UVGC_325_442,(0,0,17):C.UVGC_325_443,(0,0,18):C.UVGC_325_444,(0,0,19):C.UVGC_325_445,(0,0,20):C.UVGC_325_446,(0,0,21):C.UVGC_325_447,(0,0,22):C.UVGC_325_448,(0,0,23):C.UVGC_325_449,(0,0,24):C.UVGC_325_450,(0,0,25):C.UVGC_325_451,(0,0,26):C.UVGC_325_452,(0,0,27):C.UVGC_325_453,(0,0,28):C.UVGC_325_454,(0,0,29):C.UVGC_325_455,(0,0,30):C.UVGC_325_456,(0,0,31):C.UVGC_325_457,(0,0,32):C.UVGC_325_458,(0,0,5):C.UVGC_338_538})

V_594 = CTVertex(name = 'V_594',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_328_464,(2,0,1):C.UVGC_328_465,(2,0,2):C.UVGC_328_466,(2,0,3):C.UVGC_328_467,(2,0,4):C.UVGC_328_468,(2,0,6):C.UVGC_328_469,(2,0,7):C.UVGC_328_470,(2,0,8):C.UVGC_328_471,(2,0,9):C.UVGC_328_472,(2,0,10):C.UVGC_328_473,(2,0,11):C.UVGC_328_474,(2,0,12):C.UVGC_328_475,(2,0,13):C.UVGC_328_476,(2,0,14):C.UVGC_328_477,(2,0,15):C.UVGC_328_478,(2,0,16):C.UVGC_328_479,(2,0,17):C.UVGC_328_480,(2,0,18):C.UVGC_328_481,(2,0,19):C.UVGC_328_482,(2,0,20):C.UVGC_328_483,(2,0,21):C.UVGC_328_484,(2,0,22):C.UVGC_328_485,(2,0,23):C.UVGC_328_486,(2,0,24):C.UVGC_328_487,(2,0,25):C.UVGC_328_488,(2,0,26):C.UVGC_328_489,(2,0,27):C.UVGC_328_490,(2,0,28):C.UVGC_328_491,(2,0,29):C.UVGC_328_492,(2,0,30):C.UVGC_328_493,(2,0,31):C.UVGC_328_494,(2,0,32):C.UVGC_328_495,(2,0,5):C.UVGC_341_539,(1,0,0):C.UVGC_328_464,(1,0,1):C.UVGC_328_465,(1,0,2):C.UVGC_328_466,(1,0,3):C.UVGC_328_467,(1,0,4):C.UVGC_328_468,(1,0,6):C.UVGC_328_469,(1,0,7):C.UVGC_328_470,(1,0,8):C.UVGC_328_471,(1,0,9):C.UVGC_328_472,(1,0,10):C.UVGC_328_473,(1,0,11):C.UVGC_328_474,(1,0,12):C.UVGC_328_475,(1,0,13):C.UVGC_328_476,(1,0,14):C.UVGC_328_477,(1,0,15):C.UVGC_328_478,(1,0,16):C.UVGC_328_479,(1,0,17):C.UVGC_328_480,(1,0,18):C.UVGC_328_481,(1,0,19):C.UVGC_328_482,(1,0,20):C.UVGC_328_483,(1,0,21):C.UVGC_328_484,(1,0,22):C.UVGC_328_485,(1,0,23):C.UVGC_328_486,(1,0,24):C.UVGC_328_487,(1,0,25):C.UVGC_328_488,(1,0,26):C.UVGC_328_489,(1,0,27):C.UVGC_328_490,(1,0,28):C.UVGC_328_491,(1,0,29):C.UVGC_328_492,(1,0,30):C.UVGC_328_493,(1,0,31):C.UVGC_328_494,(1,0,32):C.UVGC_328_495,(1,0,5):C.UVGC_341_539,(0,0,3):C.UVGC_327_462,(0,0,5):C.UVGC_327_463})

V_595 = CTVertex(name = 'V_595',
                 type = 'UV',
                 particles = [ P.a, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_348_546})

V_596 = CTVertex(name = 'V_596',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.b, P.YS3d3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YS3d3] ], [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_590_846,(0,0,2):C.UVGC_590_847,(0,0,1):C.UVGC_590_848})

V_597 = CTVertex(name = 'V_597',
                 type = 'UV',
                 particles = [ P.Xm, P.b, P.YS3d3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YS3d3] ], [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_590_846,(0,0,2):C.UVGC_590_847,(0,0,1):C.UVGC_590_848})

V_598 = CTVertex(name = 'V_598',
                 type = 'UV',
                 particles = [ P.g, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_324_394,(0,0,1):C.UVGC_324_395,(0,0,2):C.UVGC_324_396,(0,0,3):C.UVGC_324_397,(0,0,4):C.UVGC_324_398,(0,0,6):C.UVGC_324_399,(0,0,7):C.UVGC_324_400,(0,0,8):C.UVGC_324_401,(0,0,9):C.UVGC_324_402,(0,0,10):C.UVGC_324_403,(0,0,11):C.UVGC_324_404,(0,0,12):C.UVGC_324_405,(0,0,13):C.UVGC_324_406,(0,0,14):C.UVGC_324_407,(0,0,15):C.UVGC_324_408,(0,0,16):C.UVGC_324_409,(0,0,17):C.UVGC_324_410,(0,0,18):C.UVGC_324_411,(0,0,19):C.UVGC_324_412,(0,0,20):C.UVGC_324_413,(0,0,21):C.UVGC_324_414,(0,0,22):C.UVGC_324_415,(0,0,23):C.UVGC_324_416,(0,0,24):C.UVGC_324_417,(0,0,25):C.UVGC_324_418,(0,0,26):C.UVGC_324_419,(0,0,27):C.UVGC_324_420,(0,0,28):C.UVGC_324_421,(0,0,29):C.UVGC_324_422,(0,0,30):C.UVGC_324_423,(0,0,31):C.UVGC_324_424,(0,0,32):C.UVGC_324_425,(0,0,5):C.UVGC_350_548})

V_599 = CTVertex(name = 'V_599',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.Xd, P.YS3d3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YS3d3] ], [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_590_846,(0,0,2):C.UVGC_590_847,(0,0,1):C.UVGC_590_848})

V_600 = CTVertex(name = 'V_600',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.Xm, P.YS3d3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YS3d3] ], [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_590_846,(0,0,2):C.UVGC_590_847,(0,0,1):C.UVGC_590_848})

V_601 = CTVertex(name = 'V_601',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_349_547})

V_602 = CTVertex(name = 'V_602',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_325_427,(0,0,1):C.UVGC_325_428,(0,0,2):C.UVGC_325_429,(0,0,3):C.UVGC_325_430,(0,0,4):C.UVGC_325_431,(0,0,6):C.UVGC_325_432,(0,0,7):C.UVGC_325_433,(0,0,8):C.UVGC_325_434,(0,0,9):C.UVGC_325_435,(0,0,10):C.UVGC_325_436,(0,0,11):C.UVGC_325_437,(0,0,12):C.UVGC_325_438,(0,0,13):C.UVGC_325_439,(0,0,14):C.UVGC_325_440,(0,0,15):C.UVGC_325_441,(0,0,16):C.UVGC_325_442,(0,0,17):C.UVGC_325_443,(0,0,18):C.UVGC_325_444,(0,0,19):C.UVGC_325_445,(0,0,20):C.UVGC_325_446,(0,0,21):C.UVGC_325_447,(0,0,22):C.UVGC_325_448,(0,0,23):C.UVGC_325_449,(0,0,24):C.UVGC_325_450,(0,0,25):C.UVGC_325_451,(0,0,26):C.UVGC_325_452,(0,0,27):C.UVGC_325_453,(0,0,28):C.UVGC_325_454,(0,0,29):C.UVGC_325_455,(0,0,30):C.UVGC_325_456,(0,0,31):C.UVGC_325_457,(0,0,32):C.UVGC_325_458,(0,0,5):C.UVGC_351_549})

V_603 = CTVertex(name = 'V_603',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_328_464,(2,0,1):C.UVGC_328_465,(2,0,2):C.UVGC_328_466,(2,0,3):C.UVGC_328_467,(2,0,4):C.UVGC_328_468,(2,0,6):C.UVGC_328_469,(2,0,7):C.UVGC_328_470,(2,0,8):C.UVGC_328_471,(2,0,9):C.UVGC_328_472,(2,0,10):C.UVGC_328_473,(2,0,11):C.UVGC_328_474,(2,0,12):C.UVGC_328_475,(2,0,13):C.UVGC_328_476,(2,0,14):C.UVGC_328_477,(2,0,15):C.UVGC_328_478,(2,0,16):C.UVGC_328_479,(2,0,17):C.UVGC_328_480,(2,0,18):C.UVGC_328_481,(2,0,19):C.UVGC_328_482,(2,0,20):C.UVGC_328_483,(2,0,21):C.UVGC_328_484,(2,0,22):C.UVGC_328_485,(2,0,23):C.UVGC_328_486,(2,0,24):C.UVGC_328_487,(2,0,25):C.UVGC_328_488,(2,0,26):C.UVGC_328_489,(2,0,27):C.UVGC_328_490,(2,0,28):C.UVGC_328_491,(2,0,29):C.UVGC_328_492,(2,0,30):C.UVGC_328_493,(2,0,31):C.UVGC_328_494,(2,0,32):C.UVGC_328_495,(2,0,5):C.UVGC_354_550,(1,0,0):C.UVGC_328_464,(1,0,1):C.UVGC_328_465,(1,0,2):C.UVGC_328_466,(1,0,3):C.UVGC_328_467,(1,0,4):C.UVGC_328_468,(1,0,6):C.UVGC_328_469,(1,0,7):C.UVGC_328_470,(1,0,8):C.UVGC_328_471,(1,0,9):C.UVGC_328_472,(1,0,10):C.UVGC_328_473,(1,0,11):C.UVGC_328_474,(1,0,12):C.UVGC_328_475,(1,0,13):C.UVGC_328_476,(1,0,14):C.UVGC_328_477,(1,0,15):C.UVGC_328_478,(1,0,16):C.UVGC_328_479,(1,0,17):C.UVGC_328_480,(1,0,18):C.UVGC_328_481,(1,0,19):C.UVGC_328_482,(1,0,20):C.UVGC_328_483,(1,0,21):C.UVGC_328_484,(1,0,22):C.UVGC_328_485,(1,0,23):C.UVGC_328_486,(1,0,24):C.UVGC_328_487,(1,0,25):C.UVGC_328_488,(1,0,26):C.UVGC_328_489,(1,0,27):C.UVGC_328_490,(1,0,28):C.UVGC_328_491,(1,0,29):C.UVGC_328_492,(1,0,30):C.UVGC_328_493,(1,0,31):C.UVGC_328_494,(1,0,32):C.UVGC_328_495,(1,0,5):C.UVGC_354_550,(0,0,3):C.UVGC_327_462,(0,0,5):C.UVGC_327_463})

V_604 = CTVertex(name = 'V_604',
                 type = 'UV',
                 particles = [ P.a, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_361_557})

V_605 = CTVertex(name = 'V_605',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.d, P.YS3Qd1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_604_884,(0,0,2):C.UVGC_604_885,(0,0,1):C.UVGC_604_886})

V_606 = CTVertex(name = 'V_606',
                 type = 'UV',
                 particles = [ P.Xm, P.d, P.YS3Qd1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_604_884,(0,0,2):C.UVGC_604_885,(0,0,1):C.UVGC_604_886})

V_607 = CTVertex(name = 'V_607',
                 type = 'UV',
                 particles = [ P.W__minus__, P.YS3Qd1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,1,0):C.UVGC_669_912,(0,1,2):C.UVGC_669_913,(0,1,1):C.UVGC_669_914,(0,0,0):C.UVGC_180_24,(0,2,2):C.UVGC_181_25})

V_608 = CTVertex(name = 'V_608',
                 type = 'UV',
                 particles = [ P.g, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_324_394,(0,0,1):C.UVGC_324_395,(0,0,2):C.UVGC_324_396,(0,0,3):C.UVGC_324_397,(0,0,4):C.UVGC_324_398,(0,0,6):C.UVGC_324_399,(0,0,7):C.UVGC_324_400,(0,0,8):C.UVGC_324_401,(0,0,9):C.UVGC_324_402,(0,0,10):C.UVGC_324_403,(0,0,11):C.UVGC_324_404,(0,0,12):C.UVGC_324_405,(0,0,13):C.UVGC_324_406,(0,0,14):C.UVGC_324_407,(0,0,15):C.UVGC_324_408,(0,0,16):C.UVGC_324_409,(0,0,17):C.UVGC_324_410,(0,0,18):C.UVGC_324_411,(0,0,19):C.UVGC_324_412,(0,0,20):C.UVGC_324_413,(0,0,21):C.UVGC_324_414,(0,0,22):C.UVGC_324_415,(0,0,23):C.UVGC_324_416,(0,0,24):C.UVGC_324_417,(0,0,25):C.UVGC_324_418,(0,0,26):C.UVGC_324_419,(0,0,27):C.UVGC_324_420,(0,0,28):C.UVGC_324_421,(0,0,29):C.UVGC_324_422,(0,0,30):C.UVGC_324_423,(0,0,31):C.UVGC_324_424,(0,0,32):C.UVGC_324_425,(0,0,5):C.UVGC_364_560,(0,1,0):C.UVGC_292_139,(0,1,1):C.UVGC_292_140,(0,1,2):C.UVGC_292_141,(0,1,3):C.UVGC_292_142,(0,1,4):C.UVGC_292_143,(0,1,6):C.UVGC_292_144,(0,1,7):C.UVGC_292_145,(0,1,8):C.UVGC_292_146,(0,1,9):C.UVGC_292_147,(0,1,10):C.UVGC_292_148,(0,1,11):C.UVGC_292_149,(0,1,12):C.UVGC_292_150,(0,1,13):C.UVGC_292_151,(0,1,14):C.UVGC_292_152,(0,1,15):C.UVGC_292_153,(0,1,16):C.UVGC_292_154,(0,1,17):C.UVGC_292_155,(0,1,18):C.UVGC_292_156,(0,1,19):C.UVGC_292_157,(0,1,20):C.UVGC_292_158,(0,1,21):C.UVGC_292_159,(0,1,22):C.UVGC_292_160,(0,1,23):C.UVGC_292_161,(0,1,24):C.UVGC_292_162,(0,1,25):C.UVGC_292_163,(0,1,26):C.UVGC_292_164,(0,1,27):C.UVGC_292_165,(0,1,28):C.UVGC_292_166,(0,1,29):C.UVGC_292_167,(0,1,30):C.UVGC_292_168,(0,1,31):C.UVGC_292_169,(0,1,32):C.UVGC_292_170,(0,1,5):C.UVGC_363_559})

V_609 = CTVertex(name = 'V_609',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.Xd, P.YS3Qd1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_604_884,(0,0,2):C.UVGC_604_885,(0,0,1):C.UVGC_604_886})

V_610 = CTVertex(name = 'V_610',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.Xm, P.YS3Qd1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_604_884,(0,0,2):C.UVGC_604_885,(0,0,1):C.UVGC_604_886})

V_611 = CTVertex(name = 'V_611',
                 type = 'UV',
                 particles = [ P.W__plus__, P.YS3Qd1, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_668_910,(0,0,2):C.UVGC_668_911,(0,0,1):C.UVGC_598_870,(0,1,0):C.UVGC_669_912,(0,1,2):C.UVGC_670_915,(0,1,1):C.UVGC_669_914})

V_612 = CTVertex(name = 'V_612',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_362_558})

V_613 = CTVertex(name = 'V_613',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_667_909,(0,0,2):C.UVGC_666_906,(0,0,1):C.UVGC_666_908})

V_614 = CTVertex(name = 'V_614',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_325_427,(0,0,1):C.UVGC_325_428,(0,0,2):C.UVGC_325_429,(0,0,3):C.UVGC_325_430,(0,0,4):C.UVGC_325_431,(0,0,6):C.UVGC_325_432,(0,0,7):C.UVGC_325_433,(0,0,8):C.UVGC_325_434,(0,0,9):C.UVGC_325_435,(0,0,10):C.UVGC_325_436,(0,0,11):C.UVGC_325_437,(0,0,12):C.UVGC_325_438,(0,0,13):C.UVGC_325_439,(0,0,14):C.UVGC_325_440,(0,0,15):C.UVGC_325_441,(0,0,16):C.UVGC_325_442,(0,0,17):C.UVGC_325_443,(0,0,18):C.UVGC_325_444,(0,0,19):C.UVGC_325_445,(0,0,20):C.UVGC_325_446,(0,0,21):C.UVGC_325_447,(0,0,22):C.UVGC_325_448,(0,0,23):C.UVGC_325_449,(0,0,24):C.UVGC_325_450,(0,0,25):C.UVGC_325_451,(0,0,26):C.UVGC_325_452,(0,0,27):C.UVGC_325_453,(0,0,28):C.UVGC_325_454,(0,0,29):C.UVGC_325_455,(0,0,30):C.UVGC_325_456,(0,0,31):C.UVGC_325_457,(0,0,32):C.UVGC_325_458,(0,0,5):C.UVGC_365_561})

V_615 = CTVertex(name = 'V_615',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_328_464,(2,0,1):C.UVGC_328_465,(2,0,2):C.UVGC_328_466,(2,0,3):C.UVGC_328_467,(2,0,4):C.UVGC_328_468,(2,0,6):C.UVGC_328_469,(2,0,7):C.UVGC_328_470,(2,0,8):C.UVGC_328_471,(2,0,9):C.UVGC_328_472,(2,0,10):C.UVGC_328_473,(2,0,11):C.UVGC_328_474,(2,0,12):C.UVGC_328_475,(2,0,13):C.UVGC_328_476,(2,0,14):C.UVGC_328_477,(2,0,15):C.UVGC_328_478,(2,0,16):C.UVGC_328_479,(2,0,17):C.UVGC_328_480,(2,0,18):C.UVGC_328_481,(2,0,19):C.UVGC_328_482,(2,0,20):C.UVGC_328_483,(2,0,21):C.UVGC_328_484,(2,0,22):C.UVGC_328_485,(2,0,23):C.UVGC_328_486,(2,0,24):C.UVGC_328_487,(2,0,25):C.UVGC_328_488,(2,0,26):C.UVGC_328_489,(2,0,27):C.UVGC_328_490,(2,0,28):C.UVGC_328_491,(2,0,29):C.UVGC_328_492,(2,0,30):C.UVGC_328_493,(2,0,31):C.UVGC_328_494,(2,0,32):C.UVGC_328_495,(2,0,5):C.UVGC_368_562,(1,0,0):C.UVGC_328_464,(1,0,1):C.UVGC_328_465,(1,0,2):C.UVGC_328_466,(1,0,3):C.UVGC_328_467,(1,0,4):C.UVGC_328_468,(1,0,6):C.UVGC_328_469,(1,0,7):C.UVGC_328_470,(1,0,8):C.UVGC_328_471,(1,0,9):C.UVGC_328_472,(1,0,10):C.UVGC_328_473,(1,0,11):C.UVGC_328_474,(1,0,12):C.UVGC_328_475,(1,0,13):C.UVGC_328_476,(1,0,14):C.UVGC_328_477,(1,0,15):C.UVGC_328_478,(1,0,16):C.UVGC_328_479,(1,0,17):C.UVGC_328_480,(1,0,18):C.UVGC_328_481,(1,0,19):C.UVGC_328_482,(1,0,20):C.UVGC_328_483,(1,0,21):C.UVGC_328_484,(1,0,22):C.UVGC_328_485,(1,0,23):C.UVGC_328_486,(1,0,24):C.UVGC_328_487,(1,0,25):C.UVGC_328_488,(1,0,26):C.UVGC_328_489,(1,0,27):C.UVGC_328_490,(1,0,28):C.UVGC_328_491,(1,0,29):C.UVGC_328_492,(1,0,30):C.UVGC_328_493,(1,0,31):C.UVGC_328_494,(1,0,32):C.UVGC_328_495,(1,0,5):C.UVGC_368_562,(0,0,3):C.UVGC_327_462,(0,0,5):C.UVGC_327_463})

V_616 = CTVertex(name = 'V_616',
                 type = 'UV',
                 particles = [ P.a, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_376_602,(0,1,0):C.UVGC_375_601})

V_617 = CTVertex(name = 'V_617',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.s, P.YS3Qd2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YS3Qd2] ], [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_768_989,(0,0,2):C.UVGC_768_990,(0,0,1):C.UVGC_596_864})

V_618 = CTVertex(name = 'V_618',
                 type = 'UV',
                 particles = [ P.Xm, P.s, P.YS3Qd2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YS3Qd2] ], [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_768_989,(0,0,2):C.UVGC_768_990,(0,0,1):C.UVGC_596_864})

V_619 = CTVertex(name = 'V_619',
                 type = 'UV',
                 particles = [ P.W__minus__, P.YS3Qd2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_702_962,(0,0,2):C.UVGC_702_963,(0,0,1):C.UVGC_669_914,(0,1,0):C.UVGC_701_960,(0,1,2):C.UVGC_701_961,(0,1,1):C.UVGC_598_870})

V_620 = CTVertex(name = 'V_620',
                 type = 'UV',
                 particles = [ P.g, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_324_394,(0,0,1):C.UVGC_324_395,(0,0,2):C.UVGC_324_396,(0,0,3):C.UVGC_324_397,(0,0,4):C.UVGC_324_398,(0,0,6):C.UVGC_324_399,(0,0,7):C.UVGC_324_400,(0,0,8):C.UVGC_324_401,(0,0,9):C.UVGC_324_402,(0,0,10):C.UVGC_324_403,(0,0,11):C.UVGC_324_404,(0,0,12):C.UVGC_324_405,(0,0,13):C.UVGC_324_406,(0,0,14):C.UVGC_324_407,(0,0,15):C.UVGC_324_408,(0,0,16):C.UVGC_324_409,(0,0,17):C.UVGC_324_410,(0,0,18):C.UVGC_324_411,(0,0,19):C.UVGC_324_412,(0,0,20):C.UVGC_324_413,(0,0,21):C.UVGC_324_414,(0,0,22):C.UVGC_324_415,(0,0,23):C.UVGC_324_416,(0,0,24):C.UVGC_324_417,(0,0,25):C.UVGC_324_418,(0,0,26):C.UVGC_324_419,(0,0,27):C.UVGC_324_420,(0,0,28):C.UVGC_324_421,(0,0,29):C.UVGC_324_422,(0,0,30):C.UVGC_324_423,(0,0,31):C.UVGC_324_424,(0,0,32):C.UVGC_324_425,(0,0,5):C.UVGC_379_605,(0,1,0):C.UVGC_292_139,(0,1,1):C.UVGC_292_140,(0,1,2):C.UVGC_292_141,(0,1,3):C.UVGC_292_142,(0,1,4):C.UVGC_292_143,(0,1,6):C.UVGC_292_144,(0,1,7):C.UVGC_292_145,(0,1,8):C.UVGC_292_146,(0,1,9):C.UVGC_292_147,(0,1,10):C.UVGC_292_148,(0,1,11):C.UVGC_292_149,(0,1,12):C.UVGC_292_150,(0,1,13):C.UVGC_292_151,(0,1,14):C.UVGC_292_152,(0,1,15):C.UVGC_292_153,(0,1,16):C.UVGC_292_154,(0,1,17):C.UVGC_292_155,(0,1,18):C.UVGC_292_156,(0,1,19):C.UVGC_292_157,(0,1,20):C.UVGC_292_158,(0,1,21):C.UVGC_292_159,(0,1,22):C.UVGC_292_160,(0,1,23):C.UVGC_292_161,(0,1,24):C.UVGC_292_162,(0,1,25):C.UVGC_292_163,(0,1,26):C.UVGC_292_164,(0,1,27):C.UVGC_292_165,(0,1,28):C.UVGC_292_166,(0,1,29):C.UVGC_292_167,(0,1,30):C.UVGC_292_168,(0,1,31):C.UVGC_292_169,(0,1,32):C.UVGC_292_170,(0,1,5):C.UVGC_378_604})

V_621 = CTVertex(name = 'V_621',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.Xd, P.YS3Qd2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YS3Qd2] ], [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_768_989,(0,0,2):C.UVGC_768_990,(0,0,1):C.UVGC_596_864})

V_622 = CTVertex(name = 'V_622',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.Xm, P.YS3Qd2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YS3Qd2] ], [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_768_989,(0,0,2):C.UVGC_768_990,(0,0,1):C.UVGC_596_864})

V_623 = CTVertex(name = 'V_623',
                 type = 'UV',
                 particles = [ P.W__plus__, P.YS3Qd2, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_700_958,(0,0,2):C.UVGC_700_959,(0,0,1):C.UVGC_598_870,(0,1,0):C.UVGC_703_964,(0,1,2):C.UVGC_703_965,(0,1,1):C.UVGC_669_914})

V_624 = CTVertex(name = 'V_624',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_377_603})

V_625 = CTVertex(name = 'V_625',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_699_957,(0,0,2):C.UVGC_666_906,(0,0,1):C.UVGC_666_908})

V_626 = CTVertex(name = 'V_626',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_325_427,(0,0,1):C.UVGC_325_428,(0,0,2):C.UVGC_325_429,(0,0,3):C.UVGC_325_430,(0,0,4):C.UVGC_325_431,(0,0,6):C.UVGC_325_432,(0,0,7):C.UVGC_325_433,(0,0,8):C.UVGC_325_434,(0,0,9):C.UVGC_325_435,(0,0,10):C.UVGC_325_436,(0,0,11):C.UVGC_325_437,(0,0,12):C.UVGC_325_438,(0,0,13):C.UVGC_325_439,(0,0,14):C.UVGC_325_440,(0,0,15):C.UVGC_325_441,(0,0,16):C.UVGC_325_442,(0,0,17):C.UVGC_325_443,(0,0,18):C.UVGC_325_444,(0,0,19):C.UVGC_325_445,(0,0,20):C.UVGC_325_446,(0,0,21):C.UVGC_325_447,(0,0,22):C.UVGC_325_448,(0,0,23):C.UVGC_325_449,(0,0,24):C.UVGC_325_450,(0,0,25):C.UVGC_325_451,(0,0,26):C.UVGC_325_452,(0,0,27):C.UVGC_325_453,(0,0,28):C.UVGC_325_454,(0,0,29):C.UVGC_325_455,(0,0,30):C.UVGC_325_456,(0,0,31):C.UVGC_325_457,(0,0,32):C.UVGC_325_458,(0,0,5):C.UVGC_380_606})

V_627 = CTVertex(name = 'V_627',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_328_464,(2,0,1):C.UVGC_328_465,(2,0,2):C.UVGC_328_466,(2,0,3):C.UVGC_328_467,(2,0,4):C.UVGC_328_468,(2,0,6):C.UVGC_328_469,(2,0,7):C.UVGC_328_470,(2,0,8):C.UVGC_328_471,(2,0,9):C.UVGC_328_472,(2,0,10):C.UVGC_328_473,(2,0,11):C.UVGC_328_474,(2,0,12):C.UVGC_328_475,(2,0,13):C.UVGC_328_476,(2,0,14):C.UVGC_328_477,(2,0,15):C.UVGC_328_478,(2,0,16):C.UVGC_328_479,(2,0,17):C.UVGC_328_480,(2,0,18):C.UVGC_328_481,(2,0,19):C.UVGC_328_482,(2,0,20):C.UVGC_328_483,(2,0,21):C.UVGC_328_484,(2,0,22):C.UVGC_328_485,(2,0,23):C.UVGC_328_486,(2,0,24):C.UVGC_328_487,(2,0,25):C.UVGC_328_488,(2,0,26):C.UVGC_328_489,(2,0,27):C.UVGC_328_490,(2,0,28):C.UVGC_328_491,(2,0,29):C.UVGC_328_492,(2,0,30):C.UVGC_328_493,(2,0,31):C.UVGC_328_494,(2,0,32):C.UVGC_328_495,(2,0,5):C.UVGC_383_607,(1,0,0):C.UVGC_328_464,(1,0,1):C.UVGC_328_465,(1,0,2):C.UVGC_328_466,(1,0,3):C.UVGC_328_467,(1,0,4):C.UVGC_328_468,(1,0,6):C.UVGC_328_469,(1,0,7):C.UVGC_328_470,(1,0,8):C.UVGC_328_471,(1,0,9):C.UVGC_328_472,(1,0,10):C.UVGC_328_473,(1,0,11):C.UVGC_328_474,(1,0,12):C.UVGC_328_475,(1,0,13):C.UVGC_328_476,(1,0,14):C.UVGC_328_477,(1,0,15):C.UVGC_328_478,(1,0,16):C.UVGC_328_479,(1,0,17):C.UVGC_328_480,(1,0,18):C.UVGC_328_481,(1,0,19):C.UVGC_328_482,(1,0,20):C.UVGC_328_483,(1,0,21):C.UVGC_328_484,(1,0,22):C.UVGC_328_485,(1,0,23):C.UVGC_328_486,(1,0,24):C.UVGC_328_487,(1,0,25):C.UVGC_328_488,(1,0,26):C.UVGC_328_489,(1,0,27):C.UVGC_328_490,(1,0,28):C.UVGC_328_491,(1,0,29):C.UVGC_328_492,(1,0,30):C.UVGC_328_493,(1,0,31):C.UVGC_328_494,(1,0,32):C.UVGC_328_495,(1,0,5):C.UVGC_383_607,(0,0,3):C.UVGC_327_462,(0,0,5):C.UVGC_327_463})

V_628 = CTVertex(name = 'V_628',
                 type = 'UV',
                 particles = [ P.a, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_391_615,(0,1,0):C.UVGC_390_614})

V_629 = CTVertex(name = 'V_629',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.b, P.YS3Qd3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_591_849,(0,0,2):C.UVGC_591_850,(0,0,1):C.UVGC_591_851})

V_630 = CTVertex(name = 'V_630',
                 type = 'UV',
                 particles = [ P.Xm, P.b, P.YS3Qd3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_591_849,(0,0,2):C.UVGC_591_850,(0,0,1):C.UVGC_591_851})

V_631 = CTVertex(name = 'V_631',
                 type = 'UV',
                 particles = [ P.W__minus__, P.YS3Qd3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_733_978,(0,0,2):C.UVGC_733_979,(0,0,1):C.UVGC_669_914,(0,1,0):C.UVGC_732_976,(0,1,2):C.UVGC_732_977,(0,1,1):C.UVGC_598_870})

V_632 = CTVertex(name = 'V_632',
                 type = 'UV',
                 particles = [ P.g, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_324_394,(0,0,1):C.UVGC_324_395,(0,0,2):C.UVGC_324_396,(0,0,3):C.UVGC_324_397,(0,0,4):C.UVGC_324_398,(0,0,6):C.UVGC_324_399,(0,0,7):C.UVGC_324_400,(0,0,8):C.UVGC_324_401,(0,0,9):C.UVGC_324_402,(0,0,10):C.UVGC_324_403,(0,0,11):C.UVGC_324_404,(0,0,12):C.UVGC_324_405,(0,0,13):C.UVGC_324_406,(0,0,14):C.UVGC_324_407,(0,0,15):C.UVGC_324_408,(0,0,16):C.UVGC_324_409,(0,0,17):C.UVGC_324_410,(0,0,18):C.UVGC_324_411,(0,0,19):C.UVGC_324_412,(0,0,20):C.UVGC_324_413,(0,0,21):C.UVGC_324_414,(0,0,22):C.UVGC_324_415,(0,0,23):C.UVGC_324_416,(0,0,24):C.UVGC_324_417,(0,0,25):C.UVGC_324_418,(0,0,26):C.UVGC_324_419,(0,0,27):C.UVGC_324_420,(0,0,28):C.UVGC_324_421,(0,0,29):C.UVGC_324_422,(0,0,30):C.UVGC_324_423,(0,0,31):C.UVGC_324_424,(0,0,32):C.UVGC_324_425,(0,0,5):C.UVGC_394_618,(0,1,0):C.UVGC_292_139,(0,1,1):C.UVGC_292_140,(0,1,2):C.UVGC_292_141,(0,1,3):C.UVGC_292_142,(0,1,4):C.UVGC_292_143,(0,1,6):C.UVGC_292_144,(0,1,7):C.UVGC_292_145,(0,1,8):C.UVGC_292_146,(0,1,9):C.UVGC_292_147,(0,1,10):C.UVGC_292_148,(0,1,11):C.UVGC_292_149,(0,1,12):C.UVGC_292_150,(0,1,13):C.UVGC_292_151,(0,1,14):C.UVGC_292_152,(0,1,15):C.UVGC_292_153,(0,1,16):C.UVGC_292_154,(0,1,17):C.UVGC_292_155,(0,1,18):C.UVGC_292_156,(0,1,19):C.UVGC_292_157,(0,1,20):C.UVGC_292_158,(0,1,21):C.UVGC_292_159,(0,1,22):C.UVGC_292_160,(0,1,23):C.UVGC_292_161,(0,1,24):C.UVGC_292_162,(0,1,25):C.UVGC_292_163,(0,1,26):C.UVGC_292_164,(0,1,27):C.UVGC_292_165,(0,1,28):C.UVGC_292_166,(0,1,29):C.UVGC_292_167,(0,1,30):C.UVGC_292_168,(0,1,31):C.UVGC_292_169,(0,1,32):C.UVGC_292_170,(0,1,5):C.UVGC_393_617})

V_633 = CTVertex(name = 'V_633',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.Xd, P.YS3Qd3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_591_849,(0,0,2):C.UVGC_591_850,(0,0,1):C.UVGC_591_851})

V_634 = CTVertex(name = 'V_634',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.Xm, P.YS3Qd3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_591_849,(0,0,2):C.UVGC_591_850,(0,0,1):C.UVGC_591_851})

V_635 = CTVertex(name = 'V_635',
                 type = 'UV',
                 particles = [ P.W__plus__, P.YS3Qd3, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_731_974,(0,0,2):C.UVGC_731_975,(0,0,1):C.UVGC_598_870,(0,1,0):C.UVGC_734_980,(0,1,2):C.UVGC_734_981,(0,1,1):C.UVGC_669_914})

V_636 = CTVertex(name = 'V_636',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_392_616})

V_637 = CTVertex(name = 'V_637',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_730_973,(0,0,2):C.UVGC_666_906,(0,0,1):C.UVGC_666_908})

V_638 = CTVertex(name = 'V_638',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_325_427,(0,0,1):C.UVGC_325_428,(0,0,2):C.UVGC_325_429,(0,0,3):C.UVGC_325_430,(0,0,4):C.UVGC_325_431,(0,0,6):C.UVGC_325_432,(0,0,7):C.UVGC_325_433,(0,0,8):C.UVGC_325_434,(0,0,9):C.UVGC_325_435,(0,0,10):C.UVGC_325_436,(0,0,11):C.UVGC_325_437,(0,0,12):C.UVGC_325_438,(0,0,13):C.UVGC_325_439,(0,0,14):C.UVGC_325_440,(0,0,15):C.UVGC_325_441,(0,0,16):C.UVGC_325_442,(0,0,17):C.UVGC_325_443,(0,0,18):C.UVGC_325_444,(0,0,19):C.UVGC_325_445,(0,0,20):C.UVGC_325_446,(0,0,21):C.UVGC_325_447,(0,0,22):C.UVGC_325_448,(0,0,23):C.UVGC_325_449,(0,0,24):C.UVGC_325_450,(0,0,25):C.UVGC_325_451,(0,0,26):C.UVGC_325_452,(0,0,27):C.UVGC_325_453,(0,0,28):C.UVGC_325_454,(0,0,29):C.UVGC_325_455,(0,0,30):C.UVGC_325_456,(0,0,31):C.UVGC_325_457,(0,0,32):C.UVGC_325_458,(0,0,5):C.UVGC_395_619})

V_639 = CTVertex(name = 'V_639',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_328_464,(2,0,1):C.UVGC_328_465,(2,0,2):C.UVGC_328_466,(2,0,3):C.UVGC_328_467,(2,0,4):C.UVGC_328_468,(2,0,6):C.UVGC_328_469,(2,0,7):C.UVGC_328_470,(2,0,8):C.UVGC_328_471,(2,0,9):C.UVGC_328_472,(2,0,10):C.UVGC_328_473,(2,0,11):C.UVGC_328_474,(2,0,12):C.UVGC_328_475,(2,0,13):C.UVGC_328_476,(2,0,14):C.UVGC_328_477,(2,0,15):C.UVGC_328_478,(2,0,16):C.UVGC_328_479,(2,0,17):C.UVGC_328_480,(2,0,18):C.UVGC_328_481,(2,0,19):C.UVGC_328_482,(2,0,20):C.UVGC_328_483,(2,0,21):C.UVGC_328_484,(2,0,22):C.UVGC_328_485,(2,0,23):C.UVGC_328_486,(2,0,24):C.UVGC_328_487,(2,0,25):C.UVGC_328_488,(2,0,26):C.UVGC_328_489,(2,0,27):C.UVGC_328_490,(2,0,28):C.UVGC_328_491,(2,0,29):C.UVGC_328_492,(2,0,30):C.UVGC_328_493,(2,0,31):C.UVGC_328_494,(2,0,32):C.UVGC_328_495,(2,0,5):C.UVGC_398_620,(1,0,0):C.UVGC_328_464,(1,0,1):C.UVGC_328_465,(1,0,2):C.UVGC_328_466,(1,0,3):C.UVGC_328_467,(1,0,4):C.UVGC_328_468,(1,0,6):C.UVGC_328_469,(1,0,7):C.UVGC_328_470,(1,0,8):C.UVGC_328_471,(1,0,9):C.UVGC_328_472,(1,0,10):C.UVGC_328_473,(1,0,11):C.UVGC_328_474,(1,0,12):C.UVGC_328_475,(1,0,13):C.UVGC_328_476,(1,0,14):C.UVGC_328_477,(1,0,15):C.UVGC_328_478,(1,0,16):C.UVGC_328_479,(1,0,17):C.UVGC_328_480,(1,0,18):C.UVGC_328_481,(1,0,19):C.UVGC_328_482,(1,0,20):C.UVGC_328_483,(1,0,21):C.UVGC_328_484,(1,0,22):C.UVGC_328_485,(1,0,23):C.UVGC_328_486,(1,0,24):C.UVGC_328_487,(1,0,25):C.UVGC_328_488,(1,0,26):C.UVGC_328_489,(1,0,27):C.UVGC_328_490,(1,0,28):C.UVGC_328_491,(1,0,29):C.UVGC_328_492,(1,0,30):C.UVGC_328_493,(1,0,31):C.UVGC_328_494,(1,0,32):C.UVGC_328_495,(1,0,5):C.UVGC_398_620,(0,0,3):C.UVGC_327_462,(0,0,5):C.UVGC_327_463})

V_640 = CTVertex(name = 'V_640',
                 type = 'UV',
                 particles = [ P.a, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_405_627,(0,1,0):C.UVGC_406_628})

V_641 = CTVertex(name = 'V_641',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.u, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_785_1028,(0,0,2):C.UVGC_785_1029,(0,0,1):C.UVGC_604_886})

V_642 = CTVertex(name = 'V_642',
                 type = 'UV',
                 particles = [ P.Xm, P.u, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_785_1028,(0,0,2):C.UVGC_785_1029,(0,0,1):C.UVGC_604_886})

V_643 = CTVertex(name = 'V_643',
                 type = 'UV',
                 particles = [ P.a, P.W__plus__, P.YS3Qd1, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_671_916,(0,0,2):C.UVGC_671_917,(0,0,1):C.UVGC_671_918})

V_644 = CTVertex(name = 'V_644',
                 type = 'UV',
                 particles = [ P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu1__tilde__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_672_919,(0,0,1):C.UVGC_672_920,(0,0,2):C.UVGC_672_921,(0,0,3):C.UVGC_672_922,(0,0,4):C.UVGC_672_923,(0,0,8):C.UVGC_672_924,(0,0,9):C.UVGC_672_925,(0,0,10):C.UVGC_672_926,(0,0,11):C.UVGC_672_927,(0,0,12):C.UVGC_672_928,(0,0,13):C.UVGC_672_929,(0,0,14):C.UVGC_672_930,(0,0,15):C.UVGC_672_931,(0,0,16):C.UVGC_672_932,(0,0,17):C.UVGC_672_933,(0,0,18):C.UVGC_672_934,(0,0,19):C.UVGC_672_935,(0,0,20):C.UVGC_672_936,(0,0,21):C.UVGC_672_937,(0,0,22):C.UVGC_672_938,(0,0,23):C.UVGC_672_939,(0,0,24):C.UVGC_672_940,(0,0,25):C.UVGC_672_941,(0,0,26):C.UVGC_672_942,(0,0,27):C.UVGC_672_943,(0,0,28):C.UVGC_672_944,(0,0,29):C.UVGC_672_945,(0,0,30):C.UVGC_672_946,(0,0,31):C.UVGC_672_947,(0,0,32):C.UVGC_672_948,(0,0,33):C.UVGC_672_949,(0,0,34):C.UVGC_672_950,(0,0,5):C.UVGC_672_951,(0,0,7):C.UVGC_672_952,(0,0,6):C.UVGC_672_953})

V_645 = CTVertex(name = 'V_645',
                 type = 'UV',
                 particles = [ P.g, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_324_394,(0,0,1):C.UVGC_324_395,(0,0,2):C.UVGC_324_396,(0,0,3):C.UVGC_324_397,(0,0,4):C.UVGC_324_398,(0,0,6):C.UVGC_324_399,(0,0,7):C.UVGC_324_400,(0,0,8):C.UVGC_324_401,(0,0,9):C.UVGC_324_402,(0,0,10):C.UVGC_324_403,(0,0,11):C.UVGC_324_404,(0,0,12):C.UVGC_324_405,(0,0,13):C.UVGC_324_406,(0,0,14):C.UVGC_324_407,(0,0,15):C.UVGC_324_408,(0,0,16):C.UVGC_324_409,(0,0,17):C.UVGC_324_410,(0,0,18):C.UVGC_324_411,(0,0,19):C.UVGC_324_412,(0,0,20):C.UVGC_324_413,(0,0,21):C.UVGC_324_414,(0,0,22):C.UVGC_324_415,(0,0,23):C.UVGC_324_416,(0,0,24):C.UVGC_324_417,(0,0,25):C.UVGC_324_418,(0,0,26):C.UVGC_324_419,(0,0,27):C.UVGC_324_420,(0,0,28):C.UVGC_324_421,(0,0,29):C.UVGC_324_422,(0,0,30):C.UVGC_324_423,(0,0,31):C.UVGC_324_424,(0,0,32):C.UVGC_324_425,(0,0,5):C.UVGC_409_631,(0,1,0):C.UVGC_292_139,(0,1,1):C.UVGC_292_140,(0,1,2):C.UVGC_292_141,(0,1,3):C.UVGC_292_142,(0,1,4):C.UVGC_292_143,(0,1,6):C.UVGC_292_144,(0,1,7):C.UVGC_292_145,(0,1,8):C.UVGC_292_146,(0,1,9):C.UVGC_292_147,(0,1,10):C.UVGC_292_148,(0,1,11):C.UVGC_292_149,(0,1,12):C.UVGC_292_150,(0,1,13):C.UVGC_292_151,(0,1,14):C.UVGC_292_152,(0,1,15):C.UVGC_292_153,(0,1,16):C.UVGC_292_154,(0,1,17):C.UVGC_292_155,(0,1,18):C.UVGC_292_156,(0,1,19):C.UVGC_292_157,(0,1,20):C.UVGC_292_158,(0,1,21):C.UVGC_292_159,(0,1,22):C.UVGC_292_160,(0,1,23):C.UVGC_292_161,(0,1,24):C.UVGC_292_162,(0,1,25):C.UVGC_292_163,(0,1,26):C.UVGC_292_164,(0,1,27):C.UVGC_292_165,(0,1,28):C.UVGC_292_166,(0,1,29):C.UVGC_292_167,(0,1,30):C.UVGC_292_168,(0,1,31):C.UVGC_292_169,(0,1,32):C.UVGC_292_170,(0,1,5):C.UVGC_408_630})

V_646 = CTVertex(name = 'V_646',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.Xd, P.YS3Qu1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_785_1028,(0,0,2):C.UVGC_785_1029,(0,0,1):C.UVGC_604_886})

V_647 = CTVertex(name = 'V_647',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.Xm, P.YS3Qu1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_785_1028,(0,0,2):C.UVGC_785_1029,(0,0,1):C.UVGC_604_886})

V_648 = CTVertex(name = 'V_648',
                 type = 'UV',
                 particles = [ P.a, P.W__minus__, P.YS3Qd1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_671_916,(0,0,2):C.UVGC_671_917,(0,0,1):C.UVGC_671_918})

V_649 = CTVertex(name = 'V_649',
                 type = 'UV',
                 particles = [ P.g, P.W__minus__, P.YS3Qd1__tilde__, P.YS3Qu1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_672_919,(0,0,1):C.UVGC_672_920,(0,0,2):C.UVGC_672_921,(0,0,3):C.UVGC_672_922,(0,0,4):C.UVGC_672_923,(0,0,8):C.UVGC_672_924,(0,0,9):C.UVGC_672_925,(0,0,10):C.UVGC_672_926,(0,0,11):C.UVGC_672_927,(0,0,12):C.UVGC_672_928,(0,0,13):C.UVGC_672_929,(0,0,14):C.UVGC_672_930,(0,0,15):C.UVGC_672_931,(0,0,16):C.UVGC_672_932,(0,0,17):C.UVGC_672_933,(0,0,18):C.UVGC_672_934,(0,0,19):C.UVGC_672_935,(0,0,20):C.UVGC_672_936,(0,0,21):C.UVGC_672_937,(0,0,22):C.UVGC_672_938,(0,0,23):C.UVGC_672_939,(0,0,24):C.UVGC_672_940,(0,0,25):C.UVGC_672_941,(0,0,26):C.UVGC_672_942,(0,0,27):C.UVGC_672_943,(0,0,28):C.UVGC_672_944,(0,0,29):C.UVGC_672_945,(0,0,30):C.UVGC_672_946,(0,0,31):C.UVGC_672_947,(0,0,32):C.UVGC_672_948,(0,0,33):C.UVGC_672_949,(0,0,34):C.UVGC_672_950,(0,0,5):C.UVGC_672_951,(0,0,7):C.UVGC_672_952,(0,0,6):C.UVGC_672_953})

V_650 = CTVertex(name = 'V_650',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_407_629})

V_651 = CTVertex(name = 'V_651',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_666_906,(0,0,2):C.UVGC_666_907,(0,0,1):C.UVGC_666_908})

V_652 = CTVertex(name = 'V_652',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_410_632,(0,0,1):C.UVGC_410_633,(0,0,2):C.UVGC_410_634,(0,0,3):C.UVGC_410_635,(0,0,4):C.UVGC_410_636,(0,0,6):C.UVGC_410_637,(0,0,7):C.UVGC_410_638,(0,0,8):C.UVGC_410_639,(0,0,9):C.UVGC_410_640,(0,0,10):C.UVGC_410_641,(0,0,11):C.UVGC_410_642,(0,0,12):C.UVGC_410_643,(0,0,13):C.UVGC_410_644,(0,0,14):C.UVGC_410_645,(0,0,15):C.UVGC_410_646,(0,0,16):C.UVGC_410_647,(0,0,17):C.UVGC_410_648,(0,0,18):C.UVGC_410_649,(0,0,19):C.UVGC_410_650,(0,0,20):C.UVGC_410_651,(0,0,21):C.UVGC_410_652,(0,0,22):C.UVGC_410_653,(0,0,23):C.UVGC_410_654,(0,0,24):C.UVGC_410_655,(0,0,25):C.UVGC_410_656,(0,0,26):C.UVGC_410_657,(0,0,27):C.UVGC_410_658,(0,0,28):C.UVGC_410_659,(0,0,29):C.UVGC_410_660,(0,0,30):C.UVGC_410_661,(0,0,31):C.UVGC_410_662,(0,0,32):C.UVGC_410_663,(0,0,5):C.UVGC_410_664})

V_653 = CTVertex(name = 'V_653',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_328_464,(2,0,1):C.UVGC_328_465,(2,0,2):C.UVGC_328_466,(2,0,3):C.UVGC_328_467,(2,0,4):C.UVGC_328_468,(2,0,6):C.UVGC_328_469,(2,0,7):C.UVGC_328_470,(2,0,8):C.UVGC_328_471,(2,0,9):C.UVGC_328_472,(2,0,10):C.UVGC_328_473,(2,0,11):C.UVGC_328_474,(2,0,12):C.UVGC_328_475,(2,0,13):C.UVGC_328_476,(2,0,14):C.UVGC_328_477,(2,0,15):C.UVGC_328_478,(2,0,16):C.UVGC_328_479,(2,0,17):C.UVGC_328_480,(2,0,18):C.UVGC_328_481,(2,0,19):C.UVGC_328_482,(2,0,20):C.UVGC_328_483,(2,0,21):C.UVGC_328_484,(2,0,22):C.UVGC_328_485,(2,0,23):C.UVGC_328_486,(2,0,24):C.UVGC_328_487,(2,0,25):C.UVGC_328_488,(2,0,26):C.UVGC_328_489,(2,0,27):C.UVGC_328_490,(2,0,28):C.UVGC_328_491,(2,0,29):C.UVGC_328_492,(2,0,30):C.UVGC_328_493,(2,0,31):C.UVGC_328_494,(2,0,32):C.UVGC_328_495,(2,0,5):C.UVGC_413_665,(1,0,0):C.UVGC_328_464,(1,0,1):C.UVGC_328_465,(1,0,2):C.UVGC_328_466,(1,0,3):C.UVGC_328_467,(1,0,4):C.UVGC_328_468,(1,0,6):C.UVGC_328_469,(1,0,7):C.UVGC_328_470,(1,0,8):C.UVGC_328_471,(1,0,9):C.UVGC_328_472,(1,0,10):C.UVGC_328_473,(1,0,11):C.UVGC_328_474,(1,0,12):C.UVGC_328_475,(1,0,13):C.UVGC_328_476,(1,0,14):C.UVGC_328_477,(1,0,15):C.UVGC_328_478,(1,0,16):C.UVGC_328_479,(1,0,17):C.UVGC_328_480,(1,0,18):C.UVGC_328_481,(1,0,19):C.UVGC_328_482,(1,0,20):C.UVGC_328_483,(1,0,21):C.UVGC_328_484,(1,0,22):C.UVGC_328_485,(1,0,23):C.UVGC_328_486,(1,0,24):C.UVGC_328_487,(1,0,25):C.UVGC_328_488,(1,0,26):C.UVGC_328_489,(1,0,27):C.UVGC_328_490,(1,0,28):C.UVGC_328_491,(1,0,29):C.UVGC_328_492,(1,0,30):C.UVGC_328_493,(1,0,31):C.UVGC_328_494,(1,0,32):C.UVGC_328_495,(1,0,5):C.UVGC_413_665,(0,0,3):C.UVGC_327_462,(0,0,5):C.UVGC_327_463})

V_654 = CTVertex(name = 'V_654',
                 type = 'UV',
                 particles = [ P.a, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_420_704,(0,1,0):C.UVGC_421_705})

V_655 = CTVertex(name = 'V_655',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.c, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_596_862,(0,0,2):C.UVGC_596_863,(0,0,1):C.UVGC_596_864})

V_656 = CTVertex(name = 'V_656',
                 type = 'UV',
                 particles = [ P.Xm, P.c, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_596_862,(0,0,2):C.UVGC_596_863,(0,0,1):C.UVGC_596_864})

V_657 = CTVertex(name = 'V_657',
                 type = 'UV',
                 particles = [ P.a, P.W__plus__, P.YS3Qd2, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_704_966,(0,0,2):C.UVGC_704_967,(0,0,1):C.UVGC_671_918})

V_658 = CTVertex(name = 'V_658',
                 type = 'UV',
                 particles = [ P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu2__tilde__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_672_919,(0,0,1):C.UVGC_672_920,(0,0,2):C.UVGC_672_921,(0,0,3):C.UVGC_672_922,(0,0,4):C.UVGC_672_923,(0,0,8):C.UVGC_672_924,(0,0,9):C.UVGC_672_925,(0,0,10):C.UVGC_672_926,(0,0,11):C.UVGC_672_927,(0,0,12):C.UVGC_672_928,(0,0,13):C.UVGC_672_929,(0,0,14):C.UVGC_672_930,(0,0,15):C.UVGC_672_931,(0,0,16):C.UVGC_672_932,(0,0,17):C.UVGC_672_933,(0,0,18):C.UVGC_672_934,(0,0,19):C.UVGC_672_935,(0,0,20):C.UVGC_672_936,(0,0,21):C.UVGC_672_937,(0,0,22):C.UVGC_672_938,(0,0,23):C.UVGC_672_939,(0,0,24):C.UVGC_672_940,(0,0,25):C.UVGC_672_941,(0,0,26):C.UVGC_672_942,(0,0,27):C.UVGC_672_943,(0,0,28):C.UVGC_672_944,(0,0,29):C.UVGC_672_945,(0,0,30):C.UVGC_672_946,(0,0,31):C.UVGC_672_947,(0,0,32):C.UVGC_672_948,(0,0,33):C.UVGC_672_949,(0,0,34):C.UVGC_672_950,(0,0,5):C.UVGC_705_968,(0,0,7):C.UVGC_705_969,(0,0,6):C.UVGC_672_953})

V_659 = CTVertex(name = 'V_659',
                 type = 'UV',
                 particles = [ P.g, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_324_394,(0,0,1):C.UVGC_324_395,(0,0,2):C.UVGC_324_396,(0,0,3):C.UVGC_324_397,(0,0,4):C.UVGC_324_398,(0,0,6):C.UVGC_324_399,(0,0,7):C.UVGC_324_400,(0,0,8):C.UVGC_324_401,(0,0,9):C.UVGC_324_402,(0,0,10):C.UVGC_324_403,(0,0,11):C.UVGC_324_404,(0,0,12):C.UVGC_324_405,(0,0,13):C.UVGC_324_406,(0,0,14):C.UVGC_324_407,(0,0,15):C.UVGC_324_408,(0,0,16):C.UVGC_324_409,(0,0,17):C.UVGC_324_410,(0,0,18):C.UVGC_324_411,(0,0,19):C.UVGC_324_412,(0,0,20):C.UVGC_324_413,(0,0,21):C.UVGC_324_414,(0,0,22):C.UVGC_324_415,(0,0,23):C.UVGC_324_416,(0,0,24):C.UVGC_324_417,(0,0,25):C.UVGC_324_418,(0,0,26):C.UVGC_324_419,(0,0,27):C.UVGC_324_420,(0,0,28):C.UVGC_324_421,(0,0,29):C.UVGC_324_422,(0,0,30):C.UVGC_324_423,(0,0,31):C.UVGC_324_424,(0,0,32):C.UVGC_324_425,(0,0,5):C.UVGC_424_708,(0,1,0):C.UVGC_292_139,(0,1,1):C.UVGC_292_140,(0,1,2):C.UVGC_292_141,(0,1,3):C.UVGC_292_142,(0,1,4):C.UVGC_292_143,(0,1,6):C.UVGC_292_144,(0,1,7):C.UVGC_292_145,(0,1,8):C.UVGC_292_146,(0,1,9):C.UVGC_292_147,(0,1,10):C.UVGC_292_148,(0,1,11):C.UVGC_292_149,(0,1,12):C.UVGC_292_150,(0,1,13):C.UVGC_292_151,(0,1,14):C.UVGC_292_152,(0,1,15):C.UVGC_292_153,(0,1,16):C.UVGC_292_154,(0,1,17):C.UVGC_292_155,(0,1,18):C.UVGC_292_156,(0,1,19):C.UVGC_292_157,(0,1,20):C.UVGC_292_158,(0,1,21):C.UVGC_292_159,(0,1,22):C.UVGC_292_160,(0,1,23):C.UVGC_292_161,(0,1,24):C.UVGC_292_162,(0,1,25):C.UVGC_292_163,(0,1,26):C.UVGC_292_164,(0,1,27):C.UVGC_292_165,(0,1,28):C.UVGC_292_166,(0,1,29):C.UVGC_292_167,(0,1,30):C.UVGC_292_168,(0,1,31):C.UVGC_292_169,(0,1,32):C.UVGC_292_170,(0,1,5):C.UVGC_423_707})

V_660 = CTVertex(name = 'V_660',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.Xd, P.YS3Qu2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_596_862,(0,0,2):C.UVGC_596_863,(0,0,1):C.UVGC_596_864})

V_661 = CTVertex(name = 'V_661',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.Xm, P.YS3Qu2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_596_862,(0,0,2):C.UVGC_596_863,(0,0,1):C.UVGC_596_864})

V_662 = CTVertex(name = 'V_662',
                 type = 'UV',
                 particles = [ P.a, P.W__minus__, P.YS3Qd2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_704_966,(0,0,2):C.UVGC_704_967,(0,0,1):C.UVGC_671_918})

V_663 = CTVertex(name = 'V_663',
                 type = 'UV',
                 particles = [ P.g, P.W__minus__, P.YS3Qd2__tilde__, P.YS3Qu2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_672_919,(0,0,1):C.UVGC_672_920,(0,0,2):C.UVGC_672_921,(0,0,3):C.UVGC_672_922,(0,0,4):C.UVGC_672_923,(0,0,8):C.UVGC_672_924,(0,0,9):C.UVGC_672_925,(0,0,10):C.UVGC_672_926,(0,0,11):C.UVGC_672_927,(0,0,12):C.UVGC_672_928,(0,0,13):C.UVGC_672_929,(0,0,14):C.UVGC_672_930,(0,0,15):C.UVGC_672_931,(0,0,16):C.UVGC_672_932,(0,0,17):C.UVGC_672_933,(0,0,18):C.UVGC_672_934,(0,0,19):C.UVGC_672_935,(0,0,20):C.UVGC_672_936,(0,0,21):C.UVGC_672_937,(0,0,22):C.UVGC_672_938,(0,0,23):C.UVGC_672_939,(0,0,24):C.UVGC_672_940,(0,0,25):C.UVGC_672_941,(0,0,26):C.UVGC_672_942,(0,0,27):C.UVGC_672_943,(0,0,28):C.UVGC_672_944,(0,0,29):C.UVGC_672_945,(0,0,30):C.UVGC_672_946,(0,0,31):C.UVGC_672_947,(0,0,32):C.UVGC_672_948,(0,0,33):C.UVGC_672_949,(0,0,34):C.UVGC_672_950,(0,0,5):C.UVGC_705_968,(0,0,7):C.UVGC_705_969,(0,0,6):C.UVGC_672_953})

V_664 = CTVertex(name = 'V_664',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_422_706})

V_665 = CTVertex(name = 'V_665',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_666_906,(0,0,2):C.UVGC_698_956,(0,0,1):C.UVGC_666_908})

V_666 = CTVertex(name = 'V_666',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_410_632,(0,0,1):C.UVGC_410_633,(0,0,2):C.UVGC_410_634,(0,0,3):C.UVGC_410_635,(0,0,4):C.UVGC_410_636,(0,0,6):C.UVGC_410_637,(0,0,7):C.UVGC_410_638,(0,0,8):C.UVGC_410_639,(0,0,9):C.UVGC_410_640,(0,0,10):C.UVGC_410_641,(0,0,11):C.UVGC_410_642,(0,0,12):C.UVGC_410_643,(0,0,13):C.UVGC_410_644,(0,0,14):C.UVGC_410_645,(0,0,15):C.UVGC_410_646,(0,0,16):C.UVGC_410_647,(0,0,17):C.UVGC_410_648,(0,0,18):C.UVGC_410_649,(0,0,19):C.UVGC_410_650,(0,0,20):C.UVGC_410_651,(0,0,21):C.UVGC_410_652,(0,0,22):C.UVGC_410_653,(0,0,23):C.UVGC_410_654,(0,0,24):C.UVGC_410_655,(0,0,25):C.UVGC_410_656,(0,0,26):C.UVGC_410_657,(0,0,27):C.UVGC_410_658,(0,0,28):C.UVGC_410_659,(0,0,29):C.UVGC_410_660,(0,0,30):C.UVGC_410_661,(0,0,31):C.UVGC_410_662,(0,0,32):C.UVGC_410_663,(0,0,5):C.UVGC_425_709})

V_667 = CTVertex(name = 'V_667',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_328_464,(2,0,1):C.UVGC_328_465,(2,0,2):C.UVGC_328_466,(2,0,3):C.UVGC_328_467,(2,0,4):C.UVGC_328_468,(2,0,6):C.UVGC_328_469,(2,0,7):C.UVGC_328_470,(2,0,8):C.UVGC_328_471,(2,0,9):C.UVGC_328_472,(2,0,10):C.UVGC_328_473,(2,0,11):C.UVGC_328_474,(2,0,12):C.UVGC_328_475,(2,0,13):C.UVGC_328_476,(2,0,14):C.UVGC_328_477,(2,0,15):C.UVGC_328_478,(2,0,16):C.UVGC_328_479,(2,0,17):C.UVGC_328_480,(2,0,18):C.UVGC_328_481,(2,0,19):C.UVGC_328_482,(2,0,20):C.UVGC_328_483,(2,0,21):C.UVGC_328_484,(2,0,22):C.UVGC_328_485,(2,0,23):C.UVGC_328_486,(2,0,24):C.UVGC_328_487,(2,0,25):C.UVGC_328_488,(2,0,26):C.UVGC_328_489,(2,0,27):C.UVGC_328_490,(2,0,28):C.UVGC_328_491,(2,0,29):C.UVGC_328_492,(2,0,30):C.UVGC_328_493,(2,0,31):C.UVGC_328_494,(2,0,32):C.UVGC_328_495,(2,0,5):C.UVGC_428_710,(1,0,0):C.UVGC_328_464,(1,0,1):C.UVGC_328_465,(1,0,2):C.UVGC_328_466,(1,0,3):C.UVGC_328_467,(1,0,4):C.UVGC_328_468,(1,0,6):C.UVGC_328_469,(1,0,7):C.UVGC_328_470,(1,0,8):C.UVGC_328_471,(1,0,9):C.UVGC_328_472,(1,0,10):C.UVGC_328_473,(1,0,11):C.UVGC_328_474,(1,0,12):C.UVGC_328_475,(1,0,13):C.UVGC_328_476,(1,0,14):C.UVGC_328_477,(1,0,15):C.UVGC_328_478,(1,0,16):C.UVGC_328_479,(1,0,17):C.UVGC_328_480,(1,0,18):C.UVGC_328_481,(1,0,19):C.UVGC_328_482,(1,0,20):C.UVGC_328_483,(1,0,21):C.UVGC_328_484,(1,0,22):C.UVGC_328_485,(1,0,23):C.UVGC_328_486,(1,0,24):C.UVGC_328_487,(1,0,25):C.UVGC_328_488,(1,0,26):C.UVGC_328_489,(1,0,27):C.UVGC_328_490,(1,0,28):C.UVGC_328_491,(1,0,29):C.UVGC_328_492,(1,0,30):C.UVGC_328_493,(1,0,31):C.UVGC_328_494,(1,0,32):C.UVGC_328_495,(1,0,5):C.UVGC_428_710,(0,0,3):C.UVGC_327_462,(0,0,5):C.UVGC_327_463})

V_668 = CTVertex(name = 'V_668',
                 type = 'UV',
                 particles = [ P.a, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_435_717,(0,1,0):C.UVGC_436_718})

V_669 = CTVertex(name = 'V_669',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.t, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_778_1013,(0,0,2):C.UVGC_778_1014,(0,0,1):C.UVGC_591_851})

V_670 = CTVertex(name = 'V_670',
                 type = 'UV',
                 particles = [ P.Xm, P.t, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_778_1013,(0,0,2):C.UVGC_778_1014,(0,0,1):C.UVGC_591_851})

V_671 = CTVertex(name = 'V_671',
                 type = 'UV',
                 particles = [ P.a, P.W__plus__, P.YS3Qd3, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_735_982,(0,0,2):C.UVGC_735_983,(0,0,1):C.UVGC_671_918})

V_672 = CTVertex(name = 'V_672',
                 type = 'UV',
                 particles = [ P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu3__tilde__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_672_919,(0,0,1):C.UVGC_672_920,(0,0,2):C.UVGC_672_921,(0,0,3):C.UVGC_672_922,(0,0,4):C.UVGC_672_923,(0,0,8):C.UVGC_672_924,(0,0,9):C.UVGC_672_925,(0,0,10):C.UVGC_672_926,(0,0,11):C.UVGC_672_927,(0,0,12):C.UVGC_672_928,(0,0,13):C.UVGC_672_929,(0,0,14):C.UVGC_672_930,(0,0,15):C.UVGC_672_931,(0,0,16):C.UVGC_672_932,(0,0,17):C.UVGC_672_933,(0,0,18):C.UVGC_672_934,(0,0,19):C.UVGC_672_935,(0,0,20):C.UVGC_672_936,(0,0,21):C.UVGC_672_937,(0,0,22):C.UVGC_672_938,(0,0,23):C.UVGC_672_939,(0,0,24):C.UVGC_672_940,(0,0,25):C.UVGC_672_941,(0,0,26):C.UVGC_672_942,(0,0,27):C.UVGC_672_943,(0,0,28):C.UVGC_672_944,(0,0,29):C.UVGC_672_945,(0,0,30):C.UVGC_672_946,(0,0,31):C.UVGC_672_947,(0,0,32):C.UVGC_672_948,(0,0,33):C.UVGC_672_949,(0,0,34):C.UVGC_672_950,(0,0,5):C.UVGC_736_984,(0,0,7):C.UVGC_736_985,(0,0,6):C.UVGC_672_953})

V_673 = CTVertex(name = 'V_673',
                 type = 'UV',
                 particles = [ P.g, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_324_394,(0,0,1):C.UVGC_324_395,(0,0,2):C.UVGC_324_396,(0,0,3):C.UVGC_324_397,(0,0,4):C.UVGC_324_398,(0,0,6):C.UVGC_324_399,(0,0,7):C.UVGC_324_400,(0,0,8):C.UVGC_324_401,(0,0,9):C.UVGC_324_402,(0,0,10):C.UVGC_324_403,(0,0,11):C.UVGC_324_404,(0,0,12):C.UVGC_324_405,(0,0,13):C.UVGC_324_406,(0,0,14):C.UVGC_324_407,(0,0,15):C.UVGC_324_408,(0,0,16):C.UVGC_324_409,(0,0,17):C.UVGC_324_410,(0,0,18):C.UVGC_324_411,(0,0,19):C.UVGC_324_412,(0,0,20):C.UVGC_324_413,(0,0,21):C.UVGC_324_414,(0,0,22):C.UVGC_324_415,(0,0,23):C.UVGC_324_416,(0,0,24):C.UVGC_324_417,(0,0,25):C.UVGC_324_418,(0,0,26):C.UVGC_324_419,(0,0,27):C.UVGC_324_420,(0,0,28):C.UVGC_324_421,(0,0,29):C.UVGC_324_422,(0,0,30):C.UVGC_324_423,(0,0,31):C.UVGC_324_424,(0,0,32):C.UVGC_324_425,(0,0,5):C.UVGC_439_721,(0,1,0):C.UVGC_292_139,(0,1,1):C.UVGC_292_140,(0,1,2):C.UVGC_292_141,(0,1,3):C.UVGC_292_142,(0,1,4):C.UVGC_292_143,(0,1,6):C.UVGC_292_144,(0,1,7):C.UVGC_292_145,(0,1,8):C.UVGC_292_146,(0,1,9):C.UVGC_292_147,(0,1,10):C.UVGC_292_148,(0,1,11):C.UVGC_292_149,(0,1,12):C.UVGC_292_150,(0,1,13):C.UVGC_292_151,(0,1,14):C.UVGC_292_152,(0,1,15):C.UVGC_292_153,(0,1,16):C.UVGC_292_154,(0,1,17):C.UVGC_292_155,(0,1,18):C.UVGC_292_156,(0,1,19):C.UVGC_292_157,(0,1,20):C.UVGC_292_158,(0,1,21):C.UVGC_292_159,(0,1,22):C.UVGC_292_160,(0,1,23):C.UVGC_292_161,(0,1,24):C.UVGC_292_162,(0,1,25):C.UVGC_292_163,(0,1,26):C.UVGC_292_164,(0,1,27):C.UVGC_292_165,(0,1,28):C.UVGC_292_166,(0,1,29):C.UVGC_292_167,(0,1,30):C.UVGC_292_168,(0,1,31):C.UVGC_292_169,(0,1,32):C.UVGC_292_170,(0,1,5):C.UVGC_438_720})

V_674 = CTVertex(name = 'V_674',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.Xd, P.YS3Qu3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_778_1013,(0,0,2):C.UVGC_778_1014,(0,0,1):C.UVGC_591_851})

V_675 = CTVertex(name = 'V_675',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.Xm, P.YS3Qu3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_778_1013,(0,0,2):C.UVGC_778_1014,(0,0,1):C.UVGC_591_851})

V_676 = CTVertex(name = 'V_676',
                 type = 'UV',
                 particles = [ P.a, P.W__minus__, P.YS3Qd3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_735_982,(0,0,2):C.UVGC_735_983,(0,0,1):C.UVGC_671_918})

V_677 = CTVertex(name = 'V_677',
                 type = 'UV',
                 particles = [ P.g, P.W__minus__, P.YS3Qd3__tilde__, P.YS3Qu3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_672_919,(0,0,1):C.UVGC_672_920,(0,0,2):C.UVGC_672_921,(0,0,3):C.UVGC_672_922,(0,0,4):C.UVGC_672_923,(0,0,8):C.UVGC_672_924,(0,0,9):C.UVGC_672_925,(0,0,10):C.UVGC_672_926,(0,0,11):C.UVGC_672_927,(0,0,12):C.UVGC_672_928,(0,0,13):C.UVGC_672_929,(0,0,14):C.UVGC_672_930,(0,0,15):C.UVGC_672_931,(0,0,16):C.UVGC_672_932,(0,0,17):C.UVGC_672_933,(0,0,18):C.UVGC_672_934,(0,0,19):C.UVGC_672_935,(0,0,20):C.UVGC_672_936,(0,0,21):C.UVGC_672_937,(0,0,22):C.UVGC_672_938,(0,0,23):C.UVGC_672_939,(0,0,24):C.UVGC_672_940,(0,0,25):C.UVGC_672_941,(0,0,26):C.UVGC_672_942,(0,0,27):C.UVGC_672_943,(0,0,28):C.UVGC_672_944,(0,0,29):C.UVGC_672_945,(0,0,30):C.UVGC_672_946,(0,0,31):C.UVGC_672_947,(0,0,32):C.UVGC_672_948,(0,0,33):C.UVGC_672_949,(0,0,34):C.UVGC_672_950,(0,0,5):C.UVGC_736_984,(0,0,7):C.UVGC_736_985,(0,0,6):C.UVGC_672_953})

V_678 = CTVertex(name = 'V_678',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_437_719})

V_679 = CTVertex(name = 'V_679',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_666_906,(0,0,2):C.UVGC_729_972,(0,0,1):C.UVGC_666_908})

V_680 = CTVertex(name = 'V_680',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_410_632,(0,0,1):C.UVGC_410_633,(0,0,2):C.UVGC_410_634,(0,0,3):C.UVGC_410_635,(0,0,4):C.UVGC_410_636,(0,0,6):C.UVGC_410_637,(0,0,7):C.UVGC_410_638,(0,0,8):C.UVGC_410_639,(0,0,9):C.UVGC_410_640,(0,0,10):C.UVGC_410_641,(0,0,11):C.UVGC_410_642,(0,0,12):C.UVGC_410_643,(0,0,13):C.UVGC_410_644,(0,0,14):C.UVGC_410_645,(0,0,15):C.UVGC_410_646,(0,0,16):C.UVGC_410_647,(0,0,17):C.UVGC_410_648,(0,0,18):C.UVGC_410_649,(0,0,19):C.UVGC_410_650,(0,0,20):C.UVGC_410_651,(0,0,21):C.UVGC_410_652,(0,0,22):C.UVGC_410_653,(0,0,23):C.UVGC_410_654,(0,0,24):C.UVGC_410_655,(0,0,25):C.UVGC_410_656,(0,0,26):C.UVGC_410_657,(0,0,27):C.UVGC_410_658,(0,0,28):C.UVGC_410_659,(0,0,29):C.UVGC_410_660,(0,0,30):C.UVGC_410_661,(0,0,31):C.UVGC_410_662,(0,0,32):C.UVGC_410_663,(0,0,5):C.UVGC_440_722})

V_681 = CTVertex(name = 'V_681',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_328_464,(2,0,1):C.UVGC_328_465,(2,0,2):C.UVGC_328_466,(2,0,3):C.UVGC_328_467,(2,0,4):C.UVGC_328_468,(2,0,6):C.UVGC_328_469,(2,0,7):C.UVGC_328_470,(2,0,8):C.UVGC_328_471,(2,0,9):C.UVGC_328_472,(2,0,10):C.UVGC_328_473,(2,0,11):C.UVGC_328_474,(2,0,12):C.UVGC_328_475,(2,0,13):C.UVGC_328_476,(2,0,14):C.UVGC_328_477,(2,0,15):C.UVGC_328_478,(2,0,16):C.UVGC_328_479,(2,0,17):C.UVGC_328_480,(2,0,18):C.UVGC_328_481,(2,0,19):C.UVGC_328_482,(2,0,20):C.UVGC_328_483,(2,0,21):C.UVGC_328_484,(2,0,22):C.UVGC_328_485,(2,0,23):C.UVGC_328_486,(2,0,24):C.UVGC_328_487,(2,0,25):C.UVGC_328_488,(2,0,26):C.UVGC_328_489,(2,0,27):C.UVGC_328_490,(2,0,28):C.UVGC_328_491,(2,0,29):C.UVGC_328_492,(2,0,30):C.UVGC_328_493,(2,0,31):C.UVGC_328_494,(2,0,32):C.UVGC_328_495,(2,0,5):C.UVGC_443_723,(1,0,0):C.UVGC_328_464,(1,0,1):C.UVGC_328_465,(1,0,2):C.UVGC_328_466,(1,0,3):C.UVGC_328_467,(1,0,4):C.UVGC_328_468,(1,0,6):C.UVGC_328_469,(1,0,7):C.UVGC_328_470,(1,0,8):C.UVGC_328_471,(1,0,9):C.UVGC_328_472,(1,0,10):C.UVGC_328_473,(1,0,11):C.UVGC_328_474,(1,0,12):C.UVGC_328_475,(1,0,13):C.UVGC_328_476,(1,0,14):C.UVGC_328_477,(1,0,15):C.UVGC_328_478,(1,0,16):C.UVGC_328_479,(1,0,17):C.UVGC_328_480,(1,0,18):C.UVGC_328_481,(1,0,19):C.UVGC_328_482,(1,0,20):C.UVGC_328_483,(1,0,21):C.UVGC_328_484,(1,0,22):C.UVGC_328_485,(1,0,23):C.UVGC_328_486,(1,0,24):C.UVGC_328_487,(1,0,25):C.UVGC_328_488,(1,0,26):C.UVGC_328_489,(1,0,27):C.UVGC_328_490,(1,0,28):C.UVGC_328_491,(1,0,29):C.UVGC_328_492,(1,0,30):C.UVGC_328_493,(1,0,31):C.UVGC_328_494,(1,0,32):C.UVGC_328_495,(1,0,5):C.UVGC_443_723,(0,0,3):C.UVGC_327_462,(0,0,5):C.UVGC_327_463})

V_682 = CTVertex(name = 'V_682',
                 type = 'UV',
                 particles = [ P.a, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_450_730,(0,1,0):C.UVGC_451_731})

V_683 = CTVertex(name = 'V_683',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.u, P.YS3u1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YS3u1] ], [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_786_1030,(0,0,2):C.UVGC_786_1031,(0,0,1):C.UVGC_786_1032})

V_684 = CTVertex(name = 'V_684',
                 type = 'UV',
                 particles = [ P.Xm, P.u, P.YS3u1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YS3u1] ], [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_786_1030,(0,0,2):C.UVGC_786_1031,(0,0,1):C.UVGC_786_1032})

V_685 = CTVertex(name = 'V_685',
                 type = 'UV',
                 particles = [ P.g, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_324_394,(0,0,1):C.UVGC_324_395,(0,0,2):C.UVGC_324_396,(0,0,3):C.UVGC_324_397,(0,0,4):C.UVGC_324_398,(0,0,6):C.UVGC_324_399,(0,0,7):C.UVGC_324_400,(0,0,8):C.UVGC_324_401,(0,0,9):C.UVGC_324_402,(0,0,10):C.UVGC_324_403,(0,0,11):C.UVGC_324_404,(0,0,12):C.UVGC_324_405,(0,0,13):C.UVGC_324_406,(0,0,14):C.UVGC_324_407,(0,0,15):C.UVGC_324_408,(0,0,16):C.UVGC_324_409,(0,0,17):C.UVGC_324_410,(0,0,18):C.UVGC_324_411,(0,0,19):C.UVGC_324_412,(0,0,20):C.UVGC_324_413,(0,0,21):C.UVGC_324_414,(0,0,22):C.UVGC_324_415,(0,0,23):C.UVGC_324_416,(0,0,24):C.UVGC_324_417,(0,0,25):C.UVGC_324_418,(0,0,26):C.UVGC_324_419,(0,0,27):C.UVGC_324_420,(0,0,28):C.UVGC_324_421,(0,0,29):C.UVGC_324_422,(0,0,30):C.UVGC_324_423,(0,0,31):C.UVGC_324_424,(0,0,32):C.UVGC_324_425,(0,0,5):C.UVGC_454_734,(0,1,0):C.UVGC_292_139,(0,1,1):C.UVGC_292_140,(0,1,2):C.UVGC_292_141,(0,1,3):C.UVGC_292_142,(0,1,4):C.UVGC_292_143,(0,1,6):C.UVGC_292_144,(0,1,7):C.UVGC_292_145,(0,1,8):C.UVGC_292_146,(0,1,9):C.UVGC_292_147,(0,1,10):C.UVGC_292_148,(0,1,11):C.UVGC_292_149,(0,1,12):C.UVGC_292_150,(0,1,13):C.UVGC_292_151,(0,1,14):C.UVGC_292_152,(0,1,15):C.UVGC_292_153,(0,1,16):C.UVGC_292_154,(0,1,17):C.UVGC_292_155,(0,1,18):C.UVGC_292_156,(0,1,19):C.UVGC_292_157,(0,1,20):C.UVGC_292_158,(0,1,21):C.UVGC_292_159,(0,1,22):C.UVGC_292_160,(0,1,23):C.UVGC_292_161,(0,1,24):C.UVGC_292_162,(0,1,25):C.UVGC_292_163,(0,1,26):C.UVGC_292_164,(0,1,27):C.UVGC_292_165,(0,1,28):C.UVGC_292_166,(0,1,29):C.UVGC_292_167,(0,1,30):C.UVGC_292_168,(0,1,31):C.UVGC_292_169,(0,1,32):C.UVGC_292_170,(0,1,5):C.UVGC_453_733})

V_686 = CTVertex(name = 'V_686',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.Xd, P.YS3u1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YS3u1] ], [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_786_1030,(0,0,2):C.UVGC_786_1031,(0,0,1):C.UVGC_786_1032})

V_687 = CTVertex(name = 'V_687',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.Xm, P.YS3u1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YS3u1] ], [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_786_1030,(0,0,2):C.UVGC_786_1031,(0,0,1):C.UVGC_786_1032})

V_688 = CTVertex(name = 'V_688',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_452_732})

V_689 = CTVertex(name = 'V_689',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_410_632,(0,0,1):C.UVGC_410_633,(0,0,2):C.UVGC_410_634,(0,0,3):C.UVGC_410_635,(0,0,4):C.UVGC_410_636,(0,0,6):C.UVGC_410_637,(0,0,7):C.UVGC_410_638,(0,0,8):C.UVGC_410_639,(0,0,9):C.UVGC_410_640,(0,0,10):C.UVGC_410_641,(0,0,11):C.UVGC_410_642,(0,0,12):C.UVGC_410_643,(0,0,13):C.UVGC_410_644,(0,0,14):C.UVGC_410_645,(0,0,15):C.UVGC_410_646,(0,0,16):C.UVGC_410_647,(0,0,17):C.UVGC_410_648,(0,0,18):C.UVGC_410_649,(0,0,19):C.UVGC_410_650,(0,0,20):C.UVGC_410_651,(0,0,21):C.UVGC_410_652,(0,0,22):C.UVGC_410_653,(0,0,23):C.UVGC_410_654,(0,0,24):C.UVGC_410_655,(0,0,25):C.UVGC_410_656,(0,0,26):C.UVGC_410_657,(0,0,27):C.UVGC_410_658,(0,0,28):C.UVGC_410_659,(0,0,29):C.UVGC_410_660,(0,0,30):C.UVGC_410_661,(0,0,31):C.UVGC_410_662,(0,0,32):C.UVGC_410_663,(0,0,5):C.UVGC_455_735})

V_690 = CTVertex(name = 'V_690',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_328_464,(2,0,1):C.UVGC_328_465,(2,0,2):C.UVGC_328_466,(2,0,3):C.UVGC_328_467,(2,0,4):C.UVGC_328_468,(2,0,6):C.UVGC_328_469,(2,0,7):C.UVGC_328_470,(2,0,8):C.UVGC_328_471,(2,0,9):C.UVGC_328_472,(2,0,10):C.UVGC_328_473,(2,0,11):C.UVGC_328_474,(2,0,12):C.UVGC_328_475,(2,0,13):C.UVGC_328_476,(2,0,14):C.UVGC_328_477,(2,0,15):C.UVGC_328_478,(2,0,16):C.UVGC_328_479,(2,0,17):C.UVGC_328_480,(2,0,18):C.UVGC_328_481,(2,0,19):C.UVGC_328_482,(2,0,20):C.UVGC_328_483,(2,0,21):C.UVGC_328_484,(2,0,22):C.UVGC_328_485,(2,0,23):C.UVGC_328_486,(2,0,24):C.UVGC_328_487,(2,0,25):C.UVGC_328_488,(2,0,26):C.UVGC_328_489,(2,0,27):C.UVGC_328_490,(2,0,28):C.UVGC_328_491,(2,0,29):C.UVGC_328_492,(2,0,30):C.UVGC_328_493,(2,0,31):C.UVGC_328_494,(2,0,32):C.UVGC_328_495,(2,0,5):C.UVGC_458_736,(1,0,0):C.UVGC_328_464,(1,0,1):C.UVGC_328_465,(1,0,2):C.UVGC_328_466,(1,0,3):C.UVGC_328_467,(1,0,4):C.UVGC_328_468,(1,0,6):C.UVGC_328_469,(1,0,7):C.UVGC_328_470,(1,0,8):C.UVGC_328_471,(1,0,9):C.UVGC_328_472,(1,0,10):C.UVGC_328_473,(1,0,11):C.UVGC_328_474,(1,0,12):C.UVGC_328_475,(1,0,13):C.UVGC_328_476,(1,0,14):C.UVGC_328_477,(1,0,15):C.UVGC_328_478,(1,0,16):C.UVGC_328_479,(1,0,17):C.UVGC_328_480,(1,0,18):C.UVGC_328_481,(1,0,19):C.UVGC_328_482,(1,0,20):C.UVGC_328_483,(1,0,21):C.UVGC_328_484,(1,0,22):C.UVGC_328_485,(1,0,23):C.UVGC_328_486,(1,0,24):C.UVGC_328_487,(1,0,25):C.UVGC_328_488,(1,0,26):C.UVGC_328_489,(1,0,27):C.UVGC_328_490,(1,0,28):C.UVGC_328_491,(1,0,29):C.UVGC_328_492,(1,0,30):C.UVGC_328_493,(1,0,31):C.UVGC_328_494,(1,0,32):C.UVGC_328_495,(1,0,5):C.UVGC_458_736,(0,0,3):C.UVGC_327_462,(0,0,5):C.UVGC_327_463})

V_691 = CTVertex(name = 'V_691',
                 type = 'UV',
                 particles = [ P.a, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_465_775,(0,1,0):C.UVGC_466_776})

V_692 = CTVertex(name = 'V_692',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.c, P.YS3u2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YS3u2] ], [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_597_865,(0,0,2):C.UVGC_597_866,(0,0,1):C.UVGC_597_867})

V_693 = CTVertex(name = 'V_693',
                 type = 'UV',
                 particles = [ P.Xm, P.c, P.YS3u2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YS3u2] ], [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_597_865,(0,0,2):C.UVGC_597_866,(0,0,1):C.UVGC_597_867})

V_694 = CTVertex(name = 'V_694',
                 type = 'UV',
                 particles = [ P.g, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_324_394,(0,0,1):C.UVGC_324_395,(0,0,2):C.UVGC_324_396,(0,0,3):C.UVGC_324_397,(0,0,4):C.UVGC_324_398,(0,0,6):C.UVGC_324_399,(0,0,7):C.UVGC_324_400,(0,0,8):C.UVGC_324_401,(0,0,9):C.UVGC_324_402,(0,0,10):C.UVGC_324_403,(0,0,11):C.UVGC_324_404,(0,0,12):C.UVGC_324_405,(0,0,13):C.UVGC_324_406,(0,0,14):C.UVGC_324_407,(0,0,15):C.UVGC_324_408,(0,0,16):C.UVGC_324_409,(0,0,17):C.UVGC_324_410,(0,0,18):C.UVGC_324_411,(0,0,19):C.UVGC_324_412,(0,0,20):C.UVGC_324_413,(0,0,21):C.UVGC_324_414,(0,0,22):C.UVGC_324_415,(0,0,23):C.UVGC_324_416,(0,0,24):C.UVGC_324_417,(0,0,25):C.UVGC_324_418,(0,0,26):C.UVGC_324_419,(0,0,27):C.UVGC_324_420,(0,0,28):C.UVGC_324_421,(0,0,29):C.UVGC_324_422,(0,0,30):C.UVGC_324_423,(0,0,31):C.UVGC_324_424,(0,0,32):C.UVGC_324_425,(0,0,5):C.UVGC_469_779,(0,1,0):C.UVGC_292_139,(0,1,1):C.UVGC_292_140,(0,1,2):C.UVGC_292_141,(0,1,3):C.UVGC_292_142,(0,1,4):C.UVGC_292_143,(0,1,6):C.UVGC_292_144,(0,1,7):C.UVGC_292_145,(0,1,8):C.UVGC_292_146,(0,1,9):C.UVGC_292_147,(0,1,10):C.UVGC_292_148,(0,1,11):C.UVGC_292_149,(0,1,12):C.UVGC_292_150,(0,1,13):C.UVGC_292_151,(0,1,14):C.UVGC_292_152,(0,1,15):C.UVGC_292_153,(0,1,16):C.UVGC_292_154,(0,1,17):C.UVGC_292_155,(0,1,18):C.UVGC_292_156,(0,1,19):C.UVGC_292_157,(0,1,20):C.UVGC_292_158,(0,1,21):C.UVGC_292_159,(0,1,22):C.UVGC_292_160,(0,1,23):C.UVGC_292_161,(0,1,24):C.UVGC_292_162,(0,1,25):C.UVGC_292_163,(0,1,26):C.UVGC_292_164,(0,1,27):C.UVGC_292_165,(0,1,28):C.UVGC_292_166,(0,1,29):C.UVGC_292_167,(0,1,30):C.UVGC_292_168,(0,1,31):C.UVGC_292_169,(0,1,32):C.UVGC_292_170,(0,1,5):C.UVGC_468_778})

V_695 = CTVertex(name = 'V_695',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.Xd, P.YS3u2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YS3u2] ], [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_597_865,(0,0,2):C.UVGC_597_866,(0,0,1):C.UVGC_597_867})

V_696 = CTVertex(name = 'V_696',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.Xm, P.YS3u2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YS3u2] ], [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_597_865,(0,0,2):C.UVGC_597_866,(0,0,1):C.UVGC_597_867})

V_697 = CTVertex(name = 'V_697',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_467_777})

V_698 = CTVertex(name = 'V_698',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_410_632,(0,0,1):C.UVGC_410_633,(0,0,2):C.UVGC_410_634,(0,0,3):C.UVGC_410_635,(0,0,4):C.UVGC_410_636,(0,0,6):C.UVGC_410_637,(0,0,7):C.UVGC_410_638,(0,0,8):C.UVGC_410_639,(0,0,9):C.UVGC_410_640,(0,0,10):C.UVGC_410_641,(0,0,11):C.UVGC_410_642,(0,0,12):C.UVGC_410_643,(0,0,13):C.UVGC_410_644,(0,0,14):C.UVGC_410_645,(0,0,15):C.UVGC_410_646,(0,0,16):C.UVGC_410_647,(0,0,17):C.UVGC_410_648,(0,0,18):C.UVGC_410_649,(0,0,19):C.UVGC_410_650,(0,0,20):C.UVGC_410_651,(0,0,21):C.UVGC_410_652,(0,0,22):C.UVGC_410_653,(0,0,23):C.UVGC_410_654,(0,0,24):C.UVGC_410_655,(0,0,25):C.UVGC_410_656,(0,0,26):C.UVGC_410_657,(0,0,27):C.UVGC_410_658,(0,0,28):C.UVGC_410_659,(0,0,29):C.UVGC_410_660,(0,0,30):C.UVGC_410_661,(0,0,31):C.UVGC_410_662,(0,0,32):C.UVGC_410_663,(0,0,5):C.UVGC_470_780})

V_699 = CTVertex(name = 'V_699',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_328_464,(2,0,1):C.UVGC_328_465,(2,0,2):C.UVGC_328_466,(2,0,3):C.UVGC_328_467,(2,0,4):C.UVGC_328_468,(2,0,6):C.UVGC_328_469,(2,0,7):C.UVGC_328_470,(2,0,8):C.UVGC_328_471,(2,0,9):C.UVGC_328_472,(2,0,10):C.UVGC_328_473,(2,0,11):C.UVGC_328_474,(2,0,12):C.UVGC_328_475,(2,0,13):C.UVGC_328_476,(2,0,14):C.UVGC_328_477,(2,0,15):C.UVGC_328_478,(2,0,16):C.UVGC_328_479,(2,0,17):C.UVGC_328_480,(2,0,18):C.UVGC_328_481,(2,0,19):C.UVGC_328_482,(2,0,20):C.UVGC_328_483,(2,0,21):C.UVGC_328_484,(2,0,22):C.UVGC_328_485,(2,0,23):C.UVGC_328_486,(2,0,24):C.UVGC_328_487,(2,0,25):C.UVGC_328_488,(2,0,26):C.UVGC_328_489,(2,0,27):C.UVGC_328_490,(2,0,28):C.UVGC_328_491,(2,0,29):C.UVGC_328_492,(2,0,30):C.UVGC_328_493,(2,0,31):C.UVGC_328_494,(2,0,32):C.UVGC_328_495,(2,0,5):C.UVGC_473_781,(1,0,0):C.UVGC_328_464,(1,0,1):C.UVGC_328_465,(1,0,2):C.UVGC_328_466,(1,0,3):C.UVGC_328_467,(1,0,4):C.UVGC_328_468,(1,0,6):C.UVGC_328_469,(1,0,7):C.UVGC_328_470,(1,0,8):C.UVGC_328_471,(1,0,9):C.UVGC_328_472,(1,0,10):C.UVGC_328_473,(1,0,11):C.UVGC_328_474,(1,0,12):C.UVGC_328_475,(1,0,13):C.UVGC_328_476,(1,0,14):C.UVGC_328_477,(1,0,15):C.UVGC_328_478,(1,0,16):C.UVGC_328_479,(1,0,17):C.UVGC_328_480,(1,0,18):C.UVGC_328_481,(1,0,19):C.UVGC_328_482,(1,0,20):C.UVGC_328_483,(1,0,21):C.UVGC_328_484,(1,0,22):C.UVGC_328_485,(1,0,23):C.UVGC_328_486,(1,0,24):C.UVGC_328_487,(1,0,25):C.UVGC_328_488,(1,0,26):C.UVGC_328_489,(1,0,27):C.UVGC_328_490,(1,0,28):C.UVGC_328_491,(1,0,29):C.UVGC_328_492,(1,0,30):C.UVGC_328_493,(1,0,31):C.UVGC_328_494,(1,0,32):C.UVGC_328_495,(1,0,5):C.UVGC_473_781,(0,0,3):C.UVGC_327_462,(0,0,5):C.UVGC_327_463})

V_700 = CTVertex(name = 'V_700',
                 type = 'UV',
                 particles = [ P.a, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_480_788,(0,1,0):C.UVGC_481_789})

V_701 = CTVertex(name = 'V_701',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.t, P.YS3u3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YS3u3] ], [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_779_1015,(0,0,2):C.UVGC_779_1016,(0,0,1):C.UVGC_779_1017})

V_702 = CTVertex(name = 'V_702',
                 type = 'UV',
                 particles = [ P.Xm, P.t, P.YS3u3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YS3u3] ], [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_779_1015,(0,0,2):C.UVGC_779_1016,(0,0,1):C.UVGC_779_1017})

V_703 = CTVertex(name = 'V_703',
                 type = 'UV',
                 particles = [ P.g, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_324_394,(0,0,1):C.UVGC_324_395,(0,0,2):C.UVGC_324_396,(0,0,3):C.UVGC_324_397,(0,0,4):C.UVGC_324_398,(0,0,6):C.UVGC_324_399,(0,0,7):C.UVGC_324_400,(0,0,8):C.UVGC_324_401,(0,0,9):C.UVGC_324_402,(0,0,10):C.UVGC_324_403,(0,0,11):C.UVGC_324_404,(0,0,12):C.UVGC_324_405,(0,0,13):C.UVGC_324_406,(0,0,14):C.UVGC_324_407,(0,0,15):C.UVGC_324_408,(0,0,16):C.UVGC_324_409,(0,0,17):C.UVGC_324_410,(0,0,18):C.UVGC_324_411,(0,0,19):C.UVGC_324_412,(0,0,20):C.UVGC_324_413,(0,0,21):C.UVGC_324_414,(0,0,22):C.UVGC_324_415,(0,0,23):C.UVGC_324_416,(0,0,24):C.UVGC_324_417,(0,0,25):C.UVGC_324_418,(0,0,26):C.UVGC_324_419,(0,0,27):C.UVGC_324_420,(0,0,28):C.UVGC_324_421,(0,0,29):C.UVGC_324_422,(0,0,30):C.UVGC_324_423,(0,0,31):C.UVGC_324_424,(0,0,32):C.UVGC_324_425,(0,0,5):C.UVGC_484_792,(0,1,0):C.UVGC_292_139,(0,1,1):C.UVGC_292_140,(0,1,2):C.UVGC_292_141,(0,1,3):C.UVGC_292_142,(0,1,4):C.UVGC_292_143,(0,1,6):C.UVGC_292_144,(0,1,7):C.UVGC_292_145,(0,1,8):C.UVGC_292_146,(0,1,9):C.UVGC_292_147,(0,1,10):C.UVGC_292_148,(0,1,11):C.UVGC_292_149,(0,1,12):C.UVGC_292_150,(0,1,13):C.UVGC_292_151,(0,1,14):C.UVGC_292_152,(0,1,15):C.UVGC_292_153,(0,1,16):C.UVGC_292_154,(0,1,17):C.UVGC_292_155,(0,1,18):C.UVGC_292_156,(0,1,19):C.UVGC_292_157,(0,1,20):C.UVGC_292_158,(0,1,21):C.UVGC_292_159,(0,1,22):C.UVGC_292_160,(0,1,23):C.UVGC_292_161,(0,1,24):C.UVGC_292_162,(0,1,25):C.UVGC_292_163,(0,1,26):C.UVGC_292_164,(0,1,27):C.UVGC_292_165,(0,1,28):C.UVGC_292_166,(0,1,29):C.UVGC_292_167,(0,1,30):C.UVGC_292_168,(0,1,31):C.UVGC_292_169,(0,1,32):C.UVGC_292_170,(0,1,5):C.UVGC_483_791})

V_704 = CTVertex(name = 'V_704',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.Xd, P.YS3u3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YS3u3] ], [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_779_1015,(0,0,2):C.UVGC_779_1016,(0,0,1):C.UVGC_779_1017})

V_705 = CTVertex(name = 'V_705',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.Xm, P.YS3u3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YS3u3] ], [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_779_1015,(0,0,2):C.UVGC_779_1016,(0,0,1):C.UVGC_779_1017})

V_706 = CTVertex(name = 'V_706',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_482_790})

V_707 = CTVertex(name = 'V_707',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_410_632,(0,0,1):C.UVGC_410_633,(0,0,2):C.UVGC_410_634,(0,0,3):C.UVGC_410_635,(0,0,4):C.UVGC_410_636,(0,0,6):C.UVGC_410_637,(0,0,7):C.UVGC_410_638,(0,0,8):C.UVGC_410_639,(0,0,9):C.UVGC_410_640,(0,0,10):C.UVGC_410_641,(0,0,11):C.UVGC_410_642,(0,0,12):C.UVGC_410_643,(0,0,13):C.UVGC_410_644,(0,0,14):C.UVGC_410_645,(0,0,15):C.UVGC_410_646,(0,0,16):C.UVGC_410_647,(0,0,17):C.UVGC_410_648,(0,0,18):C.UVGC_410_649,(0,0,19):C.UVGC_410_650,(0,0,20):C.UVGC_410_651,(0,0,21):C.UVGC_410_652,(0,0,22):C.UVGC_410_653,(0,0,23):C.UVGC_410_654,(0,0,24):C.UVGC_410_655,(0,0,25):C.UVGC_410_656,(0,0,26):C.UVGC_410_657,(0,0,27):C.UVGC_410_658,(0,0,28):C.UVGC_410_659,(0,0,29):C.UVGC_410_660,(0,0,30):C.UVGC_410_661,(0,0,31):C.UVGC_410_662,(0,0,32):C.UVGC_410_663,(0,0,5):C.UVGC_485_793})

V_708 = CTVertex(name = 'V_708',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_328_464,(2,0,1):C.UVGC_328_465,(2,0,2):C.UVGC_328_466,(2,0,3):C.UVGC_328_467,(2,0,4):C.UVGC_328_468,(2,0,6):C.UVGC_328_469,(2,0,7):C.UVGC_328_470,(2,0,8):C.UVGC_328_471,(2,0,9):C.UVGC_328_472,(2,0,10):C.UVGC_328_473,(2,0,11):C.UVGC_328_474,(2,0,12):C.UVGC_328_475,(2,0,13):C.UVGC_328_476,(2,0,14):C.UVGC_328_477,(2,0,15):C.UVGC_328_478,(2,0,16):C.UVGC_328_479,(2,0,17):C.UVGC_328_480,(2,0,18):C.UVGC_328_481,(2,0,19):C.UVGC_328_482,(2,0,20):C.UVGC_328_483,(2,0,21):C.UVGC_328_484,(2,0,22):C.UVGC_328_485,(2,0,23):C.UVGC_328_486,(2,0,24):C.UVGC_328_487,(2,0,25):C.UVGC_328_488,(2,0,26):C.UVGC_328_489,(2,0,27):C.UVGC_328_490,(2,0,28):C.UVGC_328_491,(2,0,29):C.UVGC_328_492,(2,0,30):C.UVGC_328_493,(2,0,31):C.UVGC_328_494,(2,0,32):C.UVGC_328_495,(2,0,5):C.UVGC_488_794,(1,0,0):C.UVGC_328_464,(1,0,1):C.UVGC_328_465,(1,0,2):C.UVGC_328_466,(1,0,3):C.UVGC_328_467,(1,0,4):C.UVGC_328_468,(1,0,6):C.UVGC_328_469,(1,0,7):C.UVGC_328_470,(1,0,8):C.UVGC_328_471,(1,0,9):C.UVGC_328_472,(1,0,10):C.UVGC_328_473,(1,0,11):C.UVGC_328_474,(1,0,12):C.UVGC_328_475,(1,0,13):C.UVGC_328_476,(1,0,14):C.UVGC_328_477,(1,0,15):C.UVGC_328_478,(1,0,16):C.UVGC_328_479,(1,0,17):C.UVGC_328_480,(1,0,18):C.UVGC_328_481,(1,0,19):C.UVGC_328_482,(1,0,20):C.UVGC_328_483,(1,0,21):C.UVGC_328_484,(1,0,22):C.UVGC_328_485,(1,0,23):C.UVGC_328_486,(1,0,24):C.UVGC_328_487,(1,0,25):C.UVGC_328_488,(1,0,26):C.UVGC_328_489,(1,0,27):C.UVGC_328_490,(1,0,28):C.UVGC_328_491,(1,0,29):C.UVGC_328_492,(1,0,30):C.UVGC_328_493,(1,0,31):C.UVGC_328_494,(1,0,32):C.UVGC_328_495,(1,0,5):C.UVGC_488_794,(0,0,3):C.UVGC_327_462,(0,0,5):C.UVGC_327_463})

V_709 = CTVertex(name = 'V_709',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.YF3Qd1, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_533_813,(0,1,0):C.UVGC_531_811,(0,2,0):C.UVGC_532_812})

V_710 = CTVertex(name = 'V_710',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.YF3Qd2, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_533_813,(0,1,0):C.UVGC_538_815,(0,2,0):C.UVGC_539_816})

V_711 = CTVertex(name = 'V_711',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.YF3Qd3, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_533_813,(0,1,0):C.UVGC_545_818,(0,2,0):C.UVGC_546_819})

V_712 = CTVertex(name = 'V_712',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.YF3Qu1, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_556_827,(0,1,0):C.UVGC_554_825,(0,2,0):C.UVGC_555_826})

V_713 = CTVertex(name = 'V_713',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.YF3Qu2, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_556_827,(0,1,0):C.UVGC_563_833,(0,2,0):C.UVGC_564_834})

V_714 = CTVertex(name = 'V_714',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.YF3Qu3, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_556_827,(0,1,0):C.UVGC_572_840,(0,2,0):C.UVGC_573_841})

V_715 = CTVertex(name = 'V_715',
                 type = 'UV',
                 particles = [ P.YF3d1__tilde__, P.YF3d1, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_516_807,(0,1,0):C.UVGC_209_53,(0,2,0):C.UVGC_210_54})

V_716 = CTVertex(name = 'V_716',
                 type = 'UV',
                 particles = [ P.YF3d2__tilde__, P.YF3d2, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_516_807,(0,1,0):C.UVGC_217_61,(0,2,0):C.UVGC_218_62})

V_717 = CTVertex(name = 'V_717',
                 type = 'UV',
                 particles = [ P.YF3d3__tilde__, P.YF3d3, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_516_807,(0,1,0):C.UVGC_225_69,(0,2,0):C.UVGC_226_70})

V_718 = CTVertex(name = 'V_718',
                 type = 'UV',
                 particles = [ P.YF3u1__tilde__, P.YF3u1, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_579_843,(0,1,0):C.UVGC_269_113,(0,2,0):C.UVGC_270_114})

V_719 = CTVertex(name = 'V_719',
                 type = 'UV',
                 particles = [ P.YF3u2__tilde__, P.YF3u2, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_579_843,(0,1,0):C.UVGC_277_121,(0,2,0):C.UVGC_278_122})

V_720 = CTVertex(name = 'V_720',
                 type = 'UV',
                 particles = [ P.YF3u3__tilde__, P.YF3u3, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_579_843,(0,1,0):C.UVGC_285_129,(0,2,0):C.UVGC_286_130})

V_721 = CTVertex(name = 'V_721',
                 type = 'UV',
                 particles = [ P.Z, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_330_498})

V_722 = CTVertex(name = 'V_722',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_331_499})

V_723 = CTVertex(name = 'V_723',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_332_500,(0,0,1):C.UVGC_332_501,(0,0,2):C.UVGC_332_502,(0,0,3):C.UVGC_332_503,(0,0,4):C.UVGC_332_504,(0,0,6):C.UVGC_332_505,(0,0,7):C.UVGC_332_506,(0,0,8):C.UVGC_332_507,(0,0,9):C.UVGC_332_508,(0,0,10):C.UVGC_332_509,(0,0,11):C.UVGC_332_510,(0,0,12):C.UVGC_332_511,(0,0,13):C.UVGC_332_512,(0,0,14):C.UVGC_332_513,(0,0,15):C.UVGC_332_514,(0,0,16):C.UVGC_332_515,(0,0,17):C.UVGC_332_516,(0,0,18):C.UVGC_332_517,(0,0,19):C.UVGC_332_518,(0,0,20):C.UVGC_332_519,(0,0,21):C.UVGC_332_520,(0,0,22):C.UVGC_332_521,(0,0,23):C.UVGC_332_522,(0,0,24):C.UVGC_332_523,(0,0,25):C.UVGC_332_524,(0,0,26):C.UVGC_332_525,(0,0,27):C.UVGC_332_526,(0,0,28):C.UVGC_332_527,(0,0,29):C.UVGC_332_528,(0,0,30):C.UVGC_332_529,(0,0,31):C.UVGC_332_530,(0,0,32):C.UVGC_332_531,(0,0,5):C.UVGC_332_532})

V_724 = CTVertex(name = 'V_724',
                 type = 'UV',
                 particles = [ P.Z, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_343_541})

V_725 = CTVertex(name = 'V_725',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_344_542})

V_726 = CTVertex(name = 'V_726',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_332_500,(0,0,1):C.UVGC_332_501,(0,0,2):C.UVGC_332_502,(0,0,3):C.UVGC_332_503,(0,0,4):C.UVGC_332_504,(0,0,6):C.UVGC_332_505,(0,0,7):C.UVGC_332_506,(0,0,8):C.UVGC_332_507,(0,0,9):C.UVGC_332_508,(0,0,10):C.UVGC_332_509,(0,0,11):C.UVGC_332_510,(0,0,12):C.UVGC_332_511,(0,0,13):C.UVGC_332_512,(0,0,14):C.UVGC_332_513,(0,0,15):C.UVGC_332_514,(0,0,16):C.UVGC_332_515,(0,0,17):C.UVGC_332_516,(0,0,18):C.UVGC_332_517,(0,0,19):C.UVGC_332_518,(0,0,20):C.UVGC_332_519,(0,0,21):C.UVGC_332_520,(0,0,22):C.UVGC_332_521,(0,0,23):C.UVGC_332_522,(0,0,24):C.UVGC_332_523,(0,0,25):C.UVGC_332_524,(0,0,26):C.UVGC_332_525,(0,0,27):C.UVGC_332_526,(0,0,28):C.UVGC_332_527,(0,0,29):C.UVGC_332_528,(0,0,30):C.UVGC_332_529,(0,0,31):C.UVGC_332_530,(0,0,32):C.UVGC_332_531,(0,0,5):C.UVGC_345_543})

V_727 = CTVertex(name = 'V_727',
                 type = 'UV',
                 particles = [ P.Z, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_356_552})

V_728 = CTVertex(name = 'V_728',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_357_553})

V_729 = CTVertex(name = 'V_729',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_332_500,(0,0,1):C.UVGC_332_501,(0,0,2):C.UVGC_332_502,(0,0,3):C.UVGC_332_503,(0,0,4):C.UVGC_332_504,(0,0,6):C.UVGC_332_505,(0,0,7):C.UVGC_332_506,(0,0,8):C.UVGC_332_507,(0,0,9):C.UVGC_332_508,(0,0,10):C.UVGC_332_509,(0,0,11):C.UVGC_332_510,(0,0,12):C.UVGC_332_511,(0,0,13):C.UVGC_332_512,(0,0,14):C.UVGC_332_513,(0,0,15):C.UVGC_332_514,(0,0,16):C.UVGC_332_515,(0,0,17):C.UVGC_332_516,(0,0,18):C.UVGC_332_517,(0,0,19):C.UVGC_332_518,(0,0,20):C.UVGC_332_519,(0,0,21):C.UVGC_332_520,(0,0,22):C.UVGC_332_521,(0,0,23):C.UVGC_332_522,(0,0,24):C.UVGC_332_523,(0,0,25):C.UVGC_332_524,(0,0,26):C.UVGC_332_525,(0,0,27):C.UVGC_332_526,(0,0,28):C.UVGC_332_527,(0,0,29):C.UVGC_332_528,(0,0,30):C.UVGC_332_529,(0,0,31):C.UVGC_332_530,(0,0,32):C.UVGC_332_531,(0,0,5):C.UVGC_358_554})

V_730 = CTVertex(name = 'V_730',
                 type = 'UV',
                 particles = [ P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_370_564})

V_731 = CTVertex(name = 'V_731',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_371_565})

V_732 = CTVertex(name = 'V_732',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_372_566,(0,0,1):C.UVGC_372_567,(0,0,2):C.UVGC_372_568,(0,0,3):C.UVGC_372_569,(0,0,4):C.UVGC_372_570,(0,0,6):C.UVGC_372_571,(0,0,7):C.UVGC_372_572,(0,0,8):C.UVGC_372_573,(0,0,9):C.UVGC_372_574,(0,0,10):C.UVGC_372_575,(0,0,11):C.UVGC_372_576,(0,0,12):C.UVGC_372_577,(0,0,13):C.UVGC_372_578,(0,0,14):C.UVGC_372_579,(0,0,15):C.UVGC_372_580,(0,0,16):C.UVGC_372_581,(0,0,17):C.UVGC_372_582,(0,0,18):C.UVGC_372_583,(0,0,19):C.UVGC_372_584,(0,0,20):C.UVGC_372_585,(0,0,21):C.UVGC_372_586,(0,0,22):C.UVGC_372_587,(0,0,23):C.UVGC_372_588,(0,0,24):C.UVGC_372_589,(0,0,25):C.UVGC_372_590,(0,0,26):C.UVGC_372_591,(0,0,27):C.UVGC_372_592,(0,0,28):C.UVGC_372_593,(0,0,29):C.UVGC_372_594,(0,0,30):C.UVGC_372_595,(0,0,31):C.UVGC_372_596,(0,0,32):C.UVGC_372_597,(0,0,5):C.UVGC_372_598})

V_733 = CTVertex(name = 'V_733',
                 type = 'UV',
                 particles = [ P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_385_609})

V_734 = CTVertex(name = 'V_734',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_386_610})

V_735 = CTVertex(name = 'V_735',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_372_566,(0,0,1):C.UVGC_372_567,(0,0,2):C.UVGC_372_568,(0,0,3):C.UVGC_372_569,(0,0,4):C.UVGC_372_570,(0,0,6):C.UVGC_372_571,(0,0,7):C.UVGC_372_572,(0,0,8):C.UVGC_372_573,(0,0,9):C.UVGC_372_574,(0,0,10):C.UVGC_372_575,(0,0,11):C.UVGC_372_576,(0,0,12):C.UVGC_372_577,(0,0,13):C.UVGC_372_578,(0,0,14):C.UVGC_372_579,(0,0,15):C.UVGC_372_580,(0,0,16):C.UVGC_372_581,(0,0,17):C.UVGC_372_582,(0,0,18):C.UVGC_372_583,(0,0,19):C.UVGC_372_584,(0,0,20):C.UVGC_372_585,(0,0,21):C.UVGC_372_586,(0,0,22):C.UVGC_372_587,(0,0,23):C.UVGC_372_588,(0,0,24):C.UVGC_372_589,(0,0,25):C.UVGC_372_590,(0,0,26):C.UVGC_372_591,(0,0,27):C.UVGC_372_592,(0,0,28):C.UVGC_372_593,(0,0,29):C.UVGC_372_594,(0,0,30):C.UVGC_372_595,(0,0,31):C.UVGC_372_596,(0,0,32):C.UVGC_372_597,(0,0,5):C.UVGC_387_611})

V_736 = CTVertex(name = 'V_736',
                 type = 'UV',
                 particles = [ P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_400_622})

V_737 = CTVertex(name = 'V_737',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_401_623})

V_738 = CTVertex(name = 'V_738',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_372_566,(0,0,1):C.UVGC_372_567,(0,0,2):C.UVGC_372_568,(0,0,3):C.UVGC_372_569,(0,0,4):C.UVGC_372_570,(0,0,6):C.UVGC_372_571,(0,0,7):C.UVGC_372_572,(0,0,8):C.UVGC_372_573,(0,0,9):C.UVGC_372_574,(0,0,10):C.UVGC_372_575,(0,0,11):C.UVGC_372_576,(0,0,12):C.UVGC_372_577,(0,0,13):C.UVGC_372_578,(0,0,14):C.UVGC_372_579,(0,0,15):C.UVGC_372_580,(0,0,16):C.UVGC_372_581,(0,0,17):C.UVGC_372_582,(0,0,18):C.UVGC_372_583,(0,0,19):C.UVGC_372_584,(0,0,20):C.UVGC_372_585,(0,0,21):C.UVGC_372_586,(0,0,22):C.UVGC_372_587,(0,0,23):C.UVGC_372_588,(0,0,24):C.UVGC_372_589,(0,0,25):C.UVGC_372_590,(0,0,26):C.UVGC_372_591,(0,0,27):C.UVGC_372_592,(0,0,28):C.UVGC_372_593,(0,0,29):C.UVGC_372_594,(0,0,30):C.UVGC_372_595,(0,0,31):C.UVGC_372_596,(0,0,32):C.UVGC_372_597,(0,0,5):C.UVGC_402_624})

V_739 = CTVertex(name = 'V_739',
                 type = 'UV',
                 particles = [ P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_415_667})

V_740 = CTVertex(name = 'V_740',
                 type = 'UV',
                 particles = [ P.W__plus__, P.Z, P.YS3Qd1, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_663_903,(0,0,2):C.UVGC_663_904,(0,0,1):C.UVGC_663_905})

V_741 = CTVertex(name = 'V_741',
                 type = 'UV',
                 particles = [ P.W__minus__, P.Z, P.YS3Qd1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_663_903,(0,0,2):C.UVGC_663_904,(0,0,1):C.UVGC_663_905})

V_742 = CTVertex(name = 'V_742',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_416_668})

V_743 = CTVertex(name = 'V_743',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_417_669,(0,0,1):C.UVGC_417_670,(0,0,2):C.UVGC_417_671,(0,0,3):C.UVGC_417_672,(0,0,4):C.UVGC_417_673,(0,0,6):C.UVGC_417_674,(0,0,7):C.UVGC_417_675,(0,0,8):C.UVGC_417_676,(0,0,9):C.UVGC_417_677,(0,0,10):C.UVGC_417_678,(0,0,11):C.UVGC_417_679,(0,0,12):C.UVGC_417_680,(0,0,13):C.UVGC_417_681,(0,0,14):C.UVGC_417_682,(0,0,15):C.UVGC_417_683,(0,0,16):C.UVGC_417_684,(0,0,17):C.UVGC_417_685,(0,0,18):C.UVGC_417_686,(0,0,19):C.UVGC_417_687,(0,0,20):C.UVGC_417_688,(0,0,21):C.UVGC_417_689,(0,0,22):C.UVGC_417_690,(0,0,23):C.UVGC_417_691,(0,0,24):C.UVGC_417_692,(0,0,25):C.UVGC_417_693,(0,0,26):C.UVGC_417_694,(0,0,27):C.UVGC_417_695,(0,0,28):C.UVGC_417_696,(0,0,29):C.UVGC_417_697,(0,0,30):C.UVGC_417_698,(0,0,31):C.UVGC_417_699,(0,0,32):C.UVGC_417_700,(0,0,5):C.UVGC_417_701})

V_744 = CTVertex(name = 'V_744',
                 type = 'UV',
                 particles = [ P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_430_712})

V_745 = CTVertex(name = 'V_745',
                 type = 'UV',
                 particles = [ P.W__plus__, P.Z, P.YS3Qd2, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_695_954,(0,0,2):C.UVGC_695_955,(0,0,1):C.UVGC_663_905})

V_746 = CTVertex(name = 'V_746',
                 type = 'UV',
                 particles = [ P.W__minus__, P.Z, P.YS3Qd2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_695_954,(0,0,2):C.UVGC_695_955,(0,0,1):C.UVGC_663_905})

V_747 = CTVertex(name = 'V_747',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_431_713})

V_748 = CTVertex(name = 'V_748',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_417_669,(0,0,1):C.UVGC_417_670,(0,0,2):C.UVGC_417_671,(0,0,3):C.UVGC_417_672,(0,0,4):C.UVGC_417_673,(0,0,6):C.UVGC_417_674,(0,0,7):C.UVGC_417_675,(0,0,8):C.UVGC_417_676,(0,0,9):C.UVGC_417_677,(0,0,10):C.UVGC_417_678,(0,0,11):C.UVGC_417_679,(0,0,12):C.UVGC_417_680,(0,0,13):C.UVGC_417_681,(0,0,14):C.UVGC_417_682,(0,0,15):C.UVGC_417_683,(0,0,16):C.UVGC_417_684,(0,0,17):C.UVGC_417_685,(0,0,18):C.UVGC_417_686,(0,0,19):C.UVGC_417_687,(0,0,20):C.UVGC_417_688,(0,0,21):C.UVGC_417_689,(0,0,22):C.UVGC_417_690,(0,0,23):C.UVGC_417_691,(0,0,24):C.UVGC_417_692,(0,0,25):C.UVGC_417_693,(0,0,26):C.UVGC_417_694,(0,0,27):C.UVGC_417_695,(0,0,28):C.UVGC_417_696,(0,0,29):C.UVGC_417_697,(0,0,30):C.UVGC_417_698,(0,0,31):C.UVGC_417_699,(0,0,32):C.UVGC_417_700,(0,0,5):C.UVGC_432_714})

V_749 = CTVertex(name = 'V_749',
                 type = 'UV',
                 particles = [ P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_445_725})

V_750 = CTVertex(name = 'V_750',
                 type = 'UV',
                 particles = [ P.W__plus__, P.Z, P.YS3Qd3, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_726_970,(0,0,2):C.UVGC_726_971,(0,0,1):C.UVGC_663_905})

V_751 = CTVertex(name = 'V_751',
                 type = 'UV',
                 particles = [ P.W__minus__, P.Z, P.YS3Qd3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_726_970,(0,0,2):C.UVGC_726_971,(0,0,1):C.UVGC_663_905})

V_752 = CTVertex(name = 'V_752',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_446_726})

V_753 = CTVertex(name = 'V_753',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_417_669,(0,0,1):C.UVGC_417_670,(0,0,2):C.UVGC_417_671,(0,0,3):C.UVGC_417_672,(0,0,4):C.UVGC_417_673,(0,0,6):C.UVGC_417_674,(0,0,7):C.UVGC_417_675,(0,0,8):C.UVGC_417_676,(0,0,9):C.UVGC_417_677,(0,0,10):C.UVGC_417_678,(0,0,11):C.UVGC_417_679,(0,0,12):C.UVGC_417_680,(0,0,13):C.UVGC_417_681,(0,0,14):C.UVGC_417_682,(0,0,15):C.UVGC_417_683,(0,0,16):C.UVGC_417_684,(0,0,17):C.UVGC_417_685,(0,0,18):C.UVGC_417_686,(0,0,19):C.UVGC_417_687,(0,0,20):C.UVGC_417_688,(0,0,21):C.UVGC_417_689,(0,0,22):C.UVGC_417_690,(0,0,23):C.UVGC_417_691,(0,0,24):C.UVGC_417_692,(0,0,25):C.UVGC_417_693,(0,0,26):C.UVGC_417_694,(0,0,27):C.UVGC_417_695,(0,0,28):C.UVGC_417_696,(0,0,29):C.UVGC_417_697,(0,0,30):C.UVGC_417_698,(0,0,31):C.UVGC_417_699,(0,0,32):C.UVGC_417_700,(0,0,5):C.UVGC_447_727})

V_754 = CTVertex(name = 'V_754',
                 type = 'UV',
                 particles = [ P.Z, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_460_738})

V_755 = CTVertex(name = 'V_755',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_461_739})

V_756 = CTVertex(name = 'V_756',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_462_740,(0,0,1):C.UVGC_462_741,(0,0,2):C.UVGC_462_742,(0,0,3):C.UVGC_462_743,(0,0,4):C.UVGC_462_744,(0,0,6):C.UVGC_462_745,(0,0,7):C.UVGC_462_746,(0,0,8):C.UVGC_462_747,(0,0,9):C.UVGC_462_748,(0,0,10):C.UVGC_462_749,(0,0,11):C.UVGC_462_750,(0,0,12):C.UVGC_462_751,(0,0,13):C.UVGC_462_752,(0,0,14):C.UVGC_462_753,(0,0,15):C.UVGC_462_754,(0,0,16):C.UVGC_462_755,(0,0,17):C.UVGC_462_756,(0,0,18):C.UVGC_462_757,(0,0,19):C.UVGC_462_758,(0,0,20):C.UVGC_462_759,(0,0,21):C.UVGC_462_760,(0,0,22):C.UVGC_462_761,(0,0,23):C.UVGC_462_762,(0,0,24):C.UVGC_462_763,(0,0,25):C.UVGC_462_764,(0,0,26):C.UVGC_462_765,(0,0,27):C.UVGC_462_766,(0,0,28):C.UVGC_462_767,(0,0,29):C.UVGC_462_768,(0,0,30):C.UVGC_462_769,(0,0,31):C.UVGC_462_770,(0,0,32):C.UVGC_462_771,(0,0,5):C.UVGC_462_772})

V_757 = CTVertex(name = 'V_757',
                 type = 'UV',
                 particles = [ P.Z, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_475_783})

V_758 = CTVertex(name = 'V_758',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_476_784})

V_759 = CTVertex(name = 'V_759',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_462_740,(0,0,1):C.UVGC_462_741,(0,0,2):C.UVGC_462_742,(0,0,3):C.UVGC_462_743,(0,0,4):C.UVGC_462_744,(0,0,6):C.UVGC_462_745,(0,0,7):C.UVGC_462_746,(0,0,8):C.UVGC_462_747,(0,0,9):C.UVGC_462_748,(0,0,10):C.UVGC_462_749,(0,0,11):C.UVGC_462_750,(0,0,12):C.UVGC_462_751,(0,0,13):C.UVGC_462_752,(0,0,14):C.UVGC_462_753,(0,0,15):C.UVGC_462_754,(0,0,16):C.UVGC_462_755,(0,0,17):C.UVGC_462_756,(0,0,18):C.UVGC_462_757,(0,0,19):C.UVGC_462_758,(0,0,20):C.UVGC_462_759,(0,0,21):C.UVGC_462_760,(0,0,22):C.UVGC_462_761,(0,0,23):C.UVGC_462_762,(0,0,24):C.UVGC_462_763,(0,0,25):C.UVGC_462_764,(0,0,26):C.UVGC_462_765,(0,0,27):C.UVGC_462_766,(0,0,28):C.UVGC_462_767,(0,0,29):C.UVGC_462_768,(0,0,30):C.UVGC_462_769,(0,0,31):C.UVGC_462_770,(0,0,32):C.UVGC_462_771,(0,0,5):C.UVGC_477_785})

V_760 = CTVertex(name = 'V_760',
                 type = 'UV',
                 particles = [ P.Z, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_490_796})

V_761 = CTVertex(name = 'V_761',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_491_797})

V_762 = CTVertex(name = 'V_762',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_462_740,(0,0,1):C.UVGC_462_741,(0,0,2):C.UVGC_462_742,(0,0,3):C.UVGC_462_743,(0,0,4):C.UVGC_462_744,(0,0,6):C.UVGC_462_745,(0,0,7):C.UVGC_462_746,(0,0,8):C.UVGC_462_747,(0,0,9):C.UVGC_462_748,(0,0,10):C.UVGC_462_749,(0,0,11):C.UVGC_462_750,(0,0,12):C.UVGC_462_751,(0,0,13):C.UVGC_462_752,(0,0,14):C.UVGC_462_753,(0,0,15):C.UVGC_462_754,(0,0,16):C.UVGC_462_755,(0,0,17):C.UVGC_462_756,(0,0,18):C.UVGC_462_757,(0,0,19):C.UVGC_462_758,(0,0,20):C.UVGC_462_759,(0,0,21):C.UVGC_462_760,(0,0,22):C.UVGC_462_761,(0,0,23):C.UVGC_462_762,(0,0,24):C.UVGC_462_763,(0,0,25):C.UVGC_462_764,(0,0,26):C.UVGC_462_765,(0,0,27):C.UVGC_462_766,(0,0,28):C.UVGC_462_767,(0,0,29):C.UVGC_462_768,(0,0,30):C.UVGC_462_769,(0,0,31):C.UVGC_462_770,(0,0,32):C.UVGC_462_771,(0,0,5):C.UVGC_492_798})

V_763 = CTVertex(name = 'V_763',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_333_533})

V_764 = CTVertex(name = 'V_764',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_346_544})

V_765 = CTVertex(name = 'V_765',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_359_555})

V_766 = CTVertex(name = 'V_766',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_373_599})

V_767 = CTVertex(name = 'V_767',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_388_612})

V_768 = CTVertex(name = 'V_768',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_403_625})

V_769 = CTVertex(name = 'V_769',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_418_702})

V_770 = CTVertex(name = 'V_770',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_433_715})

V_771 = CTVertex(name = 'V_771',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_448_728})

V_772 = CTVertex(name = 'V_772',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_463_773})

V_773 = CTVertex(name = 'V_773',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_478_786})

V_774 = CTVertex(name = 'V_774',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_493_799})

V_775 = CTVertex(name = 'V_775',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.YF3Qu1, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_787_1033,(0,0,2):C.UVGC_787_1034,(0,0,1):C.UVGC_607_894})

V_776 = CTVertex(name = 'V_776',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.YF3Qd1, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_607_892,(0,0,2):C.UVGC_607_893,(0,0,1):C.UVGC_607_894})

V_777 = CTVertex(name = 'V_777',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.YF3Qu2, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_599_871,(0,0,2):C.UVGC_599_872,(0,0,1):C.UVGC_599_873})

V_778 = CTVertex(name = 'V_778',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.YF3Qd2, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3Qd2] ], [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_771_996,(0,0,2):C.UVGC_771_997,(0,0,1):C.UVGC_599_873})

V_779 = CTVertex(name = 'V_779',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.YF3Qu3, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_780_1018,(0,0,2):C.UVGC_780_1019,(0,0,1):C.UVGC_594_859})

V_780 = CTVertex(name = 'V_780',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.YF3Qd3, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_594_857,(0,0,2):C.UVGC_594_858,(0,0,1):C.UVGC_594_859})

V_781 = CTVertex(name = 'V_781',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.YF3Qu1, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_787_1033,(0,0,2):C.UVGC_787_1034,(0,0,1):C.UVGC_607_894})

V_782 = CTVertex(name = 'V_782',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.YF3Qd1, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_607_892,(0,0,2):C.UVGC_607_893,(0,0,1):C.UVGC_607_894})

V_783 = CTVertex(name = 'V_783',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.YF3Qu2, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_599_871,(0,0,2):C.UVGC_599_872,(0,0,1):C.UVGC_599_873})

V_784 = CTVertex(name = 'V_784',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.YF3Qd2, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3Qd2] ], [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_771_996,(0,0,2):C.UVGC_771_997,(0,0,1):C.UVGC_599_873})

V_785 = CTVertex(name = 'V_785',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.YF3Qu3, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_780_1018,(0,0,2):C.UVGC_780_1019,(0,0,1):C.UVGC_594_859})

V_786 = CTVertex(name = 'V_786',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.YF3Qd3, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_594_857,(0,0,2):C.UVGC_594_858,(0,0,1):C.UVGC_594_859})

V_787 = CTVertex(name = 'V_787',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_312_388,(0,1,0):C.UVGC_197_41,(0,2,0):C.UVGC_199_43})

V_788 = CTVertex(name = 'V_788',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_312_388,(0,1,0):C.UVGC_167_11,(0,2,0):C.UVGC_169_13})

V_789 = CTVertex(name = 'V_789',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_312_388,(0,1,0):C.UVGC_190_34,(0,2,0):C.UVGC_192_36})

V_790 = CTVertex(name = 'V_790',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_304_381,(0,1,0):C.UVGC_174_18,(0,2,0):C.UVGC_176_20})

V_791 = CTVertex(name = 'V_791',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_304_381,(0,1,0):C.UVGC_183_27,(0,2,0):C.UVGC_185_29})

V_792 = CTVertex(name = 'V_792',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_304_381,(0,1,0):C.UVGC_160_4,(0,2,0):C.UVGC_162_6})

V_793 = CTVertex(name = 'V_793',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_305_382,(0,3,0):C.UVGC_292_139,(0,3,1):C.UVGC_292_140,(0,3,2):C.UVGC_292_141,(0,3,3):C.UVGC_292_142,(0,3,4):C.UVGC_292_143,(0,3,6):C.UVGC_292_144,(0,3,7):C.UVGC_292_145,(0,3,8):C.UVGC_292_146,(0,3,9):C.UVGC_292_147,(0,3,10):C.UVGC_292_148,(0,3,11):C.UVGC_292_149,(0,3,12):C.UVGC_292_150,(0,3,13):C.UVGC_292_151,(0,3,14):C.UVGC_292_152,(0,3,15):C.UVGC_292_153,(0,3,16):C.UVGC_292_154,(0,3,17):C.UVGC_292_155,(0,3,18):C.UVGC_292_156,(0,3,19):C.UVGC_292_157,(0,3,20):C.UVGC_292_158,(0,3,21):C.UVGC_292_159,(0,3,22):C.UVGC_292_160,(0,3,23):C.UVGC_292_161,(0,3,24):C.UVGC_292_162,(0,3,25):C.UVGC_292_163,(0,3,26):C.UVGC_292_164,(0,3,27):C.UVGC_292_165,(0,3,28):C.UVGC_292_166,(0,3,29):C.UVGC_292_167,(0,3,30):C.UVGC_292_168,(0,3,31):C.UVGC_292_169,(0,3,32):C.UVGC_292_170,(0,1,5):C.UVGC_200_44,(0,2,5):C.UVGC_201_45})

V_794 = CTVertex(name = 'V_794',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.c, P.g] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,2):C.UVGC_305_382,(0,3,0):C.UVGC_292_139,(0,3,1):C.UVGC_292_140,(0,3,3):C.UVGC_292_141,(0,3,4):C.UVGC_292_142,(0,3,5):C.UVGC_292_143,(0,3,6):C.UVGC_292_144,(0,3,7):C.UVGC_292_145,(0,3,8):C.UVGC_292_146,(0,3,9):C.UVGC_292_147,(0,3,10):C.UVGC_292_148,(0,3,11):C.UVGC_292_149,(0,3,12):C.UVGC_292_150,(0,3,13):C.UVGC_292_151,(0,3,14):C.UVGC_292_152,(0,3,15):C.UVGC_292_153,(0,3,16):C.UVGC_292_154,(0,3,17):C.UVGC_292_155,(0,3,18):C.UVGC_292_156,(0,3,19):C.UVGC_292_157,(0,3,20):C.UVGC_292_158,(0,3,21):C.UVGC_292_159,(0,3,22):C.UVGC_292_160,(0,3,23):C.UVGC_292_161,(0,3,24):C.UVGC_292_162,(0,3,25):C.UVGC_292_163,(0,3,26):C.UVGC_292_164,(0,3,27):C.UVGC_292_165,(0,3,28):C.UVGC_292_166,(0,3,29):C.UVGC_292_167,(0,3,30):C.UVGC_292_168,(0,3,31):C.UVGC_292_169,(0,3,32):C.UVGC_292_170,(0,1,2):C.UVGC_170_14,(0,2,2):C.UVGC_171_15})

V_795 = CTVertex(name = 'V_795',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_305_382,(0,3,0):C.UVGC_292_139,(0,3,1):C.UVGC_292_140,(0,3,2):C.UVGC_292_141,(0,3,3):C.UVGC_292_142,(0,3,4):C.UVGC_292_143,(0,3,6):C.UVGC_292_144,(0,3,7):C.UVGC_292_145,(0,3,8):C.UVGC_292_146,(0,3,9):C.UVGC_292_147,(0,3,10):C.UVGC_292_148,(0,3,11):C.UVGC_292_149,(0,3,12):C.UVGC_292_150,(0,3,13):C.UVGC_292_151,(0,3,14):C.UVGC_292_152,(0,3,15):C.UVGC_292_153,(0,3,16):C.UVGC_292_154,(0,3,17):C.UVGC_292_155,(0,3,18):C.UVGC_292_156,(0,3,19):C.UVGC_292_157,(0,3,20):C.UVGC_292_158,(0,3,21):C.UVGC_292_159,(0,3,22):C.UVGC_292_160,(0,3,23):C.UVGC_292_161,(0,3,24):C.UVGC_292_162,(0,3,25):C.UVGC_292_163,(0,3,26):C.UVGC_292_164,(0,3,27):C.UVGC_292_165,(0,3,28):C.UVGC_292_166,(0,3,29):C.UVGC_292_167,(0,3,30):C.UVGC_292_168,(0,3,31):C.UVGC_292_169,(0,3,32):C.UVGC_292_170,(0,1,5):C.UVGC_193_37,(0,2,5):C.UVGC_194_38})

V_796 = CTVertex(name = 'V_796',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,3):C.UVGC_305_382,(0,3,0):C.UVGC_292_139,(0,3,1):C.UVGC_292_140,(0,3,2):C.UVGC_292_141,(0,3,4):C.UVGC_292_142,(0,3,5):C.UVGC_292_143,(0,3,6):C.UVGC_292_144,(0,3,7):C.UVGC_292_145,(0,3,8):C.UVGC_292_146,(0,3,9):C.UVGC_292_147,(0,3,10):C.UVGC_292_148,(0,3,11):C.UVGC_292_149,(0,3,12):C.UVGC_292_150,(0,3,13):C.UVGC_292_151,(0,3,14):C.UVGC_292_152,(0,3,15):C.UVGC_292_153,(0,3,16):C.UVGC_292_154,(0,3,17):C.UVGC_292_155,(0,3,18):C.UVGC_292_156,(0,3,19):C.UVGC_292_157,(0,3,20):C.UVGC_292_158,(0,3,21):C.UVGC_292_159,(0,3,22):C.UVGC_292_160,(0,3,23):C.UVGC_292_161,(0,3,24):C.UVGC_292_162,(0,3,25):C.UVGC_292_163,(0,3,26):C.UVGC_292_164,(0,3,27):C.UVGC_292_165,(0,3,28):C.UVGC_292_166,(0,3,29):C.UVGC_292_167,(0,3,30):C.UVGC_292_168,(0,3,31):C.UVGC_292_169,(0,3,32):C.UVGC_292_170,(0,1,3):C.UVGC_177_21,(0,2,3):C.UVGC_178_22})

V_797 = CTVertex(name = 'V_797',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_305_382,(0,3,0):C.UVGC_292_139,(0,3,1):C.UVGC_292_140,(0,3,2):C.UVGC_292_141,(0,3,3):C.UVGC_292_142,(0,3,4):C.UVGC_292_143,(0,3,6):C.UVGC_292_144,(0,3,7):C.UVGC_292_145,(0,3,8):C.UVGC_292_146,(0,3,9):C.UVGC_292_147,(0,3,10):C.UVGC_292_148,(0,3,11):C.UVGC_292_149,(0,3,12):C.UVGC_292_150,(0,3,13):C.UVGC_292_151,(0,3,14):C.UVGC_292_152,(0,3,15):C.UVGC_292_153,(0,3,16):C.UVGC_292_154,(0,3,17):C.UVGC_292_155,(0,3,18):C.UVGC_292_156,(0,3,19):C.UVGC_292_157,(0,3,20):C.UVGC_292_158,(0,3,21):C.UVGC_292_159,(0,3,22):C.UVGC_292_160,(0,3,23):C.UVGC_292_161,(0,3,24):C.UVGC_292_162,(0,3,25):C.UVGC_292_163,(0,3,26):C.UVGC_292_164,(0,3,27):C.UVGC_292_165,(0,3,28):C.UVGC_292_166,(0,3,29):C.UVGC_292_167,(0,3,30):C.UVGC_292_168,(0,3,31):C.UVGC_292_169,(0,3,32):C.UVGC_292_170,(0,1,5):C.UVGC_186_30,(0,2,5):C.UVGC_187_31})

V_798 = CTVertex(name = 'V_798',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.b, P.g] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,1):C.UVGC_305_382,(0,3,0):C.UVGC_292_139,(0,3,2):C.UVGC_292_140,(0,3,3):C.UVGC_292_141,(0,3,4):C.UVGC_292_142,(0,3,5):C.UVGC_292_143,(0,3,6):C.UVGC_292_144,(0,3,7):C.UVGC_292_145,(0,3,8):C.UVGC_292_146,(0,3,9):C.UVGC_292_147,(0,3,10):C.UVGC_292_148,(0,3,11):C.UVGC_292_149,(0,3,12):C.UVGC_292_150,(0,3,13):C.UVGC_292_151,(0,3,14):C.UVGC_292_152,(0,3,15):C.UVGC_292_153,(0,3,16):C.UVGC_292_154,(0,3,17):C.UVGC_292_155,(0,3,18):C.UVGC_292_156,(0,3,19):C.UVGC_292_157,(0,3,20):C.UVGC_292_158,(0,3,21):C.UVGC_292_159,(0,3,22):C.UVGC_292_160,(0,3,23):C.UVGC_292_161,(0,3,24):C.UVGC_292_162,(0,3,25):C.UVGC_292_163,(0,3,26):C.UVGC_292_164,(0,3,27):C.UVGC_292_165,(0,3,28):C.UVGC_292_166,(0,3,29):C.UVGC_292_167,(0,3,30):C.UVGC_292_168,(0,3,31):C.UVGC_292_169,(0,3,32):C.UVGC_292_170,(0,1,1):C.UVGC_163_7,(0,2,1):C.UVGC_164_8})

V_799 = CTVertex(name = 'V_799',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_784_1026,(0,0,2):C.UVGC_784_1027,(0,0,1):C.UVGC_598_870})

V_800 = CTVertex(name = 'V_800',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_598_868,(0,0,2):C.UVGC_598_869,(0,0,1):C.UVGC_598_870})

V_801 = CTVertex(name = 'V_801',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_773_999,(0,0,2):C.UVGC_773_1000,(0,0,1):C.UVGC_598_870})

V_802 = CTVertex(name = 'V_802',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_784_1026,(0,0,2):C.UVGC_784_1027,(0,0,1):C.UVGC_598_870})

V_803 = CTVertex(name = 'V_803',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_598_868,(0,0,2):C.UVGC_598_869,(0,0,1):C.UVGC_598_870})

V_804 = CTVertex(name = 'V_804',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_773_999,(0,0,2):C.UVGC_773_1000,(0,0,1):C.UVGC_598_870})

V_805 = CTVertex(name = 'V_805',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3, L.FFV7 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_510_805,(0,2,0):C.UVGC_308_385,(0,1,0):C.UVGC_202_46})

V_806 = CTVertex(name = 'V_806',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3, L.FFV7 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_314_389,(0,2,0):C.UVGC_308_385,(0,1,0):C.UVGC_172_16})

V_807 = CTVertex(name = 'V_807',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3, L.FFV7 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_503_802,(0,2,0):C.UVGC_308_385,(0,1,0):C.UVGC_195_39})

V_808 = CTVertex(name = 'V_808',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_319_390,(0,2,0):C.UVGC_308_385,(0,1,0):C.UVGC_179_23})

V_809 = CTVertex(name = 'V_809',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_497_800,(0,2,0):C.UVGC_308_385,(0,1,0):C.UVGC_188_32})

V_810 = CTVertex(name = 'V_810',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_307_384,(0,2,0):C.UVGC_308_385,(0,1,0):C.UVGC_165_9})

V_811 = CTVertex(name = 'V_811',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.u, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_787_1033,(0,0,2):C.UVGC_787_1034,(0,0,1):C.UVGC_607_894})

V_812 = CTVertex(name = 'V_812',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.d, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_607_892,(0,0,2):C.UVGC_607_893,(0,0,1):C.UVGC_607_894})

V_813 = CTVertex(name = 'V_813',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.c, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_599_871,(0,0,2):C.UVGC_599_872,(0,0,1):C.UVGC_599_873})

V_814 = CTVertex(name = 'V_814',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.s, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3Qd2] ], [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_771_996,(0,0,2):C.UVGC_771_997,(0,0,1):C.UVGC_599_873})

V_815 = CTVertex(name = 'V_815',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.t, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_780_1018,(0,0,2):C.UVGC_780_1019,(0,0,1):C.UVGC_594_859})

V_816 = CTVertex(name = 'V_816',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.b, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_594_857,(0,0,2):C.UVGC_594_858,(0,0,1):C.UVGC_594_859})

V_817 = CTVertex(name = 'V_817',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.u, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_787_1033,(0,0,2):C.UVGC_787_1034,(0,0,1):C.UVGC_607_894})

V_818 = CTVertex(name = 'V_818',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.d, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_607_892,(0,0,2):C.UVGC_607_893,(0,0,1):C.UVGC_607_894})

V_819 = CTVertex(name = 'V_819',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.c, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_599_871,(0,0,2):C.UVGC_599_872,(0,0,1):C.UVGC_599_873})

V_820 = CTVertex(name = 'V_820',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.s, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3Qd2] ], [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_771_996,(0,0,2):C.UVGC_771_997,(0,0,1):C.UVGC_599_873})

V_821 = CTVertex(name = 'V_821',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.t, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_780_1018,(0,0,2):C.UVGC_780_1019,(0,0,1):C.UVGC_594_859})

V_822 = CTVertex(name = 'V_822',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.b, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_594_857,(0,0,2):C.UVGC_594_858,(0,0,1):C.UVGC_594_859})

V_823 = CTVertex(name = 'V_823',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.YF3d1, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3d1] ], [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_605_887,(0,0,2):C.UVGC_605_888,(0,0,1):C.UVGC_605_889})

V_824 = CTVertex(name = 'V_824',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.YF3d2, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3d2] ], [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_769_991,(0,0,2):C.UVGC_769_992,(0,0,1):C.UVGC_769_993})

V_825 = CTVertex(name = 'V_825',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.YF3d3, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3d3] ], [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_592_852,(0,0,2):C.UVGC_592_853,(0,0,1):C.UVGC_592_854})

V_826 = CTVertex(name = 'V_826',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.YF3u1, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3u1] ], [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_789_1036,(0,0,2):C.UVGC_789_1037,(0,0,1):C.UVGC_789_1038})

V_827 = CTVertex(name = 'V_827',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.YF3u2, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3u2] ], [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_601_876,(0,0,2):C.UVGC_601_877,(0,0,1):C.UVGC_601_878})

V_828 = CTVertex(name = 'V_828',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.YF3u3, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3u3] ], [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_782_1021,(0,0,2):C.UVGC_782_1022,(0,0,1):C.UVGC_782_1023})

V_829 = CTVertex(name = 'V_829',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.YF3d1, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3d1] ], [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_605_887,(0,0,2):C.UVGC_605_888,(0,0,1):C.UVGC_605_889})

V_830 = CTVertex(name = 'V_830',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.YF3d2, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3d2] ], [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_769_991,(0,0,2):C.UVGC_769_992,(0,0,1):C.UVGC_769_993})

V_831 = CTVertex(name = 'V_831',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.YF3d3, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3d3] ], [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_592_852,(0,0,2):C.UVGC_592_853,(0,0,1):C.UVGC_592_854})

V_832 = CTVertex(name = 'V_832',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.YF3u1, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3u1] ], [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_789_1036,(0,0,2):C.UVGC_789_1037,(0,0,1):C.UVGC_789_1038})

V_833 = CTVertex(name = 'V_833',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.YF3u2, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3u2] ], [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_601_876,(0,0,2):C.UVGC_601_877,(0,0,1):C.UVGC_601_878})

V_834 = CTVertex(name = 'V_834',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.YF3u3, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3u3] ], [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_782_1021,(0,0,2):C.UVGC_782_1022,(0,0,1):C.UVGC_782_1023})

V_835 = CTVertex(name = 'V_835',
                 type = 'UV',
                 particles = [ P.YF3d1__tilde__, P.d, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3d1] ], [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_605_887,(0,0,2):C.UVGC_605_888,(0,0,1):C.UVGC_605_889})

V_836 = CTVertex(name = 'V_836',
                 type = 'UV',
                 particles = [ P.YF3d2__tilde__, P.s, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3d2] ], [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_769_991,(0,0,2):C.UVGC_769_992,(0,0,1):C.UVGC_769_993})

V_837 = CTVertex(name = 'V_837',
                 type = 'UV',
                 particles = [ P.YF3d3__tilde__, P.b, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3d3] ], [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_592_852,(0,0,2):C.UVGC_592_853,(0,0,1):C.UVGC_592_854})

V_838 = CTVertex(name = 'V_838',
                 type = 'UV',
                 particles = [ P.YF3u1__tilde__, P.u, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3u1] ], [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_789_1036,(0,0,2):C.UVGC_789_1037,(0,0,1):C.UVGC_789_1038})

V_839 = CTVertex(name = 'V_839',
                 type = 'UV',
                 particles = [ P.YF3u2__tilde__, P.c, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3u2] ], [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_601_876,(0,0,2):C.UVGC_601_877,(0,0,1):C.UVGC_601_878})

V_840 = CTVertex(name = 'V_840',
                 type = 'UV',
                 particles = [ P.YF3u3__tilde__, P.t, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3u3] ], [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_782_1021,(0,0,2):C.UVGC_782_1022,(0,0,1):C.UVGC_782_1023})

V_841 = CTVertex(name = 'V_841',
                 type = 'UV',
                 particles = [ P.YF3d1__tilde__, P.d, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3d1] ], [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_605_887,(0,0,2):C.UVGC_605_888,(0,0,1):C.UVGC_605_889})

V_842 = CTVertex(name = 'V_842',
                 type = 'UV',
                 particles = [ P.YF3d2__tilde__, P.s, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3d2] ], [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_769_991,(0,0,2):C.UVGC_769_992,(0,0,1):C.UVGC_769_993})

V_843 = CTVertex(name = 'V_843',
                 type = 'UV',
                 particles = [ P.YF3d3__tilde__, P.b, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3d3] ], [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_592_852,(0,0,2):C.UVGC_592_853,(0,0,1):C.UVGC_592_854})

V_844 = CTVertex(name = 'V_844',
                 type = 'UV',
                 particles = [ P.YF3u1__tilde__, P.u, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3u1] ], [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_789_1036,(0,0,2):C.UVGC_789_1037,(0,0,1):C.UVGC_789_1038})

V_845 = CTVertex(name = 'V_845',
                 type = 'UV',
                 particles = [ P.YF3u2__tilde__, P.c, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3u2] ], [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_601_876,(0,0,2):C.UVGC_601_877,(0,0,1):C.UVGC_601_878})

V_846 = CTVertex(name = 'V_846',
                 type = 'UV',
                 particles = [ P.YF3u3__tilde__, P.t, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3u3] ], [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_782_1021,(0,0,2):C.UVGC_782_1022,(0,0,1):C.UVGC_782_1023})

V_847 = CTVertex(name = 'V_847',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF4 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_303_380,(0,1,0):C.UVGC_196_40,(0,2,0):C.UVGC_198_42})

V_848 = CTVertex(name = 'V_848',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF4 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_303_380,(0,1,0):C.UVGC_166_10,(0,2,0):C.UVGC_168_12})

V_849 = CTVertex(name = 'V_849',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,1,0):C.UVGC_502_801,(0,3,0):C.UVGC_303_380,(0,0,0):C.UVGC_189_33,(0,2,0):C.UVGC_191_35})

V_850 = CTVertex(name = 'V_850',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF4 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_303_380,(0,1,0):C.UVGC_173_17,(0,2,0):C.UVGC_175_19})

V_851 = CTVertex(name = 'V_851',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF4 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_303_380,(0,1,0):C.UVGC_182_26,(0,2,0):C.UVGC_184_28})

V_852 = CTVertex(name = 'V_852',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,1,0):C.UVGC_306_383,(0,3,0):C.UVGC_303_380,(0,0,0):C.UVGC_159_3,(0,2,0):C.UVGC_161_5})

V_853 = CTVertex(name = 'V_853',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.YF3Qu1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,1,0):C.UVGC_551_820,(0,3,0):C.UVGC_303_380,(0,0,0):C.UVGC_245_89,(0,2,0):C.UVGC_247_91})

V_854 = CTVertex(name = 'V_854',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.YF3Qu2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,1,0):C.UVGC_560_828,(0,3,0):C.UVGC_303_380,(0,0,0):C.UVGC_251_95,(0,2,0):C.UVGC_253_97})

V_855 = CTVertex(name = 'V_855',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.YF3Qu3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,1,0):C.UVGC_569_835,(0,3,0):C.UVGC_303_380,(0,0,0):C.UVGC_257_101,(0,2,0):C.UVGC_259_103})

V_856 = CTVertex(name = 'V_856',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.YF3Qd1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,1,0):C.UVGC_530_810,(0,3,0):C.UVGC_303_380,(0,0,0):C.UVGC_227_71,(0,2,0):C.UVGC_229_73})

V_857 = CTVertex(name = 'V_857',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.YF3Qd2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,1,0):C.UVGC_537_814,(0,3,0):C.UVGC_303_380,(0,0,0):C.UVGC_233_77,(0,2,0):C.UVGC_235_79})

V_858 = CTVertex(name = 'V_858',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.YF3Qd3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,1,0):C.UVGC_544_817,(0,3,0):C.UVGC_303_380,(0,0,0):C.UVGC_239_83,(0,2,0):C.UVGC_241_85})

V_859 = CTVertex(name = 'V_859',
                 type = 'UV',
                 particles = [ P.YF3u1__tilde__, P.YF3u1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,1,0):C.UVGC_578_842,(0,3,0):C.UVGC_303_380,(0,0,0):C.UVGC_263_107,(0,2,0):C.UVGC_265_109})

V_860 = CTVertex(name = 'V_860',
                 type = 'UV',
                 particles = [ P.YF3u2__tilde__, P.YF3u2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,1,0):C.UVGC_583_844,(0,3,0):C.UVGC_303_380,(0,0,0):C.UVGC_271_115,(0,2,0):C.UVGC_273_117})

V_861 = CTVertex(name = 'V_861',
                 type = 'UV',
                 particles = [ P.YF3u3__tilde__, P.YF3u3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,1,0):C.UVGC_588_845,(0,3,0):C.UVGC_303_380,(0,0,0):C.UVGC_279_123,(0,2,0):C.UVGC_281_125})

V_862 = CTVertex(name = 'V_862',
                 type = 'UV',
                 particles = [ P.YF3d1__tilde__, P.YF3d1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,1,0):C.UVGC_515_806,(0,3,0):C.UVGC_303_380,(0,0,0):C.UVGC_203_47,(0,2,0):C.UVGC_205_49})

V_863 = CTVertex(name = 'V_863',
                 type = 'UV',
                 particles = [ P.YF3d2__tilde__, P.YF3d2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,1,0):C.UVGC_520_808,(0,3,0):C.UVGC_303_380,(0,0,0):C.UVGC_211_55,(0,2,0):C.UVGC_213_57})

V_864 = CTVertex(name = 'V_864',
                 type = 'UV',
                 particles = [ P.YF3d3__tilde__, P.YF3d3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,1,0):C.UVGC_525_809,(0,3,0):C.UVGC_303_380,(0,0,0):C.UVGC_219_63,(0,2,0):C.UVGC_221_65})

V_865 = CTVertex(name = 'V_865',
                 type = 'UV',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV4, L.VV5, L.VV6 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_293_171,(0,0,1):C.UVGC_293_172,(0,0,2):C.UVGC_293_173,(0,0,3):C.UVGC_293_174,(0,0,4):C.UVGC_293_175,(0,0,5):C.UVGC_293_176,(0,0,6):C.UVGC_293_177,(0,0,7):C.UVGC_293_178,(0,0,8):C.UVGC_293_179,(0,0,9):C.UVGC_293_180,(0,0,10):C.UVGC_293_181,(0,0,11):C.UVGC_293_182,(0,0,12):C.UVGC_293_183,(0,0,13):C.UVGC_293_184,(0,0,14):C.UVGC_293_185,(0,0,15):C.UVGC_293_186,(0,0,16):C.UVGC_293_187,(0,0,17):C.UVGC_293_188,(0,0,18):C.UVGC_293_189,(0,0,19):C.UVGC_293_190,(0,0,20):C.UVGC_293_191,(0,0,21):C.UVGC_293_192,(0,0,22):C.UVGC_293_193,(0,0,23):C.UVGC_293_194,(0,0,24):C.UVGC_293_195,(0,0,25):C.UVGC_293_196,(0,0,26):C.UVGC_293_197,(0,0,27):C.UVGC_293_198,(0,0,28):C.UVGC_293_199,(0,0,29):C.UVGC_293_200,(0,0,30):C.UVGC_293_201,(0,0,31):C.UVGC_293_202,(0,1,3):C.UVGC_157_1,(0,2,4):C.UVGC_158_2})

V_866 = CTVertex(name = 'V_866',
                 type = 'UV',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_414_666,(0,1,0):C.UVGC_404_626})

V_867 = CTVertex(name = 'V_867',
                 type = 'UV',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_429_711,(0,1,0):C.UVGC_419_703})

V_868 = CTVertex(name = 'V_868',
                 type = 'UV',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_444_724,(0,1,0):C.UVGC_434_716})

V_869 = CTVertex(name = 'V_869',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_369_563,(0,1,0):C.UVGC_360_556})

V_870 = CTVertex(name = 'V_870',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_384_608,(0,1,0):C.UVGC_374_600})

V_871 = CTVertex(name = 'V_871',
                 type = 'UV',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_399_621,(0,1,0):C.UVGC_389_613})

V_872 = CTVertex(name = 'V_872',
                 type = 'UV',
                 particles = [ P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_459_737,(0,1,0):C.UVGC_449_729})

V_873 = CTVertex(name = 'V_873',
                 type = 'UV',
                 particles = [ P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_474_782,(0,1,0):C.UVGC_464_774})

V_874 = CTVertex(name = 'V_874',
                 type = 'UV',
                 particles = [ P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_489_795,(0,1,0):C.UVGC_479_787})

V_875 = CTVertex(name = 'V_875',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_329_497,(0,1,0):C.UVGC_321_391})

V_876 = CTVertex(name = 'V_876',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_342_540,(0,1,0):C.UVGC_334_534})

V_877 = CTVertex(name = 'V_877',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_355_551,(0,1,0):C.UVGC_347_545})

V_878 = CTVertex(name = 'V_878',
                 type = 'UV',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3Qu1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_326_460,(1,0,3):C.UVGC_326_461,(1,0,0):C.UVGC_800_1047,(1,0,5):C.UVGC_800_1048,(1,0,1):C.UVGC_800_1049,(1,0,4):C.UVGC_800_1050,(0,0,2):C.UVGC_326_460,(0,0,3):C.UVGC_326_461,(0,0,0):C.UVGC_800_1047,(0,0,5):C.UVGC_800_1048,(0,0,1):C.UVGC_800_1049,(0,0,4):C.UVGC_800_1050})

V_879 = CTVertex(name = 'V_879',
                 type = 'UV',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3Qu1, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qu1, P.YS3Qu2] ], [ [P.g, P.YS3Qu1, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_873_1113,(1,0,8):C.UVGC_873_1114,(1,0,1):C.UVGC_873_1115,(1,0,7):C.UVGC_873_1116,(1,0,2):C.UVGC_813_1065,(1,0,6):C.UVGC_873_1117,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_872_1108,(0,0,8):C.UVGC_872_1109,(0,0,1):C.UVGC_872_1110,(0,0,7):C.UVGC_872_1111,(0,0,2):C.UVGC_812_1059,(0,0,6):C.UVGC_872_1112})

V_880 = CTVertex(name = 'V_880',
                 type = 'UV',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3Qu2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_326_460,(1,0,3):C.UVGC_326_461,(1,0,0):C.UVGC_800_1047,(1,0,5):C.UVGC_800_1048,(1,0,1):C.UVGC_800_1049,(1,0,4):C.UVGC_800_1050,(0,0,2):C.UVGC_326_460,(0,0,3):C.UVGC_326_461,(0,0,0):C.UVGC_800_1047,(0,0,5):C.UVGC_800_1048,(0,0,1):C.UVGC_800_1049,(0,0,4):C.UVGC_800_1050})

V_881 = CTVertex(name = 'V_881',
                 type = 'UV',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qu1, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qu1, P.YS3Qu3] ], [ [P.g, P.YS3Qu1, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_873_1113,(1,0,8):C.UVGC_873_1114,(1,0,1):C.UVGC_873_1115,(1,0,7):C.UVGC_873_1116,(1,0,2):C.UVGC_813_1065,(1,0,6):C.UVGC_873_1117,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_872_1108,(0,0,8):C.UVGC_872_1109,(0,0,1):C.UVGC_872_1110,(0,0,7):C.UVGC_872_1111,(0,0,2):C.UVGC_812_1059,(0,0,6):C.UVGC_872_1112})

V_882 = CTVertex(name = 'V_882',
                 type = 'UV',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qu2, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qu2], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qu2, P.YS3Qu3] ], [ [P.g, P.YS3Qu2, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qu2, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_873_1113,(1,0,8):C.UVGC_873_1114,(1,0,1):C.UVGC_873_1115,(1,0,7):C.UVGC_873_1116,(1,0,2):C.UVGC_813_1065,(1,0,6):C.UVGC_873_1117,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_872_1108,(0,0,8):C.UVGC_872_1109,(0,0,1):C.UVGC_872_1110,(0,0,7):C.UVGC_872_1111,(0,0,2):C.UVGC_812_1059,(0,0,6):C.UVGC_872_1112})

V_883 = CTVertex(name = 'V_883',
                 type = 'UV',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3__tilde__, P.YS3Qu3, P.YS3Qu3 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_326_460,(1,0,3):C.UVGC_326_461,(1,0,0):C.UVGC_800_1047,(1,0,5):C.UVGC_800_1048,(1,0,1):C.UVGC_800_1049,(1,0,4):C.UVGC_800_1050,(0,0,2):C.UVGC_326_460,(0,0,3):C.UVGC_326_461,(0,0,0):C.UVGC_800_1047,(0,0,5):C.UVGC_800_1048,(0,0,1):C.UVGC_800_1049,(0,0,4):C.UVGC_800_1050})

V_884 = CTVertex(name = 'V_884',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qu1] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,7):C.UVGC_610_901,(1,0,8):C.UVGC_610_902,(1,0,0):C.UVGC_829_1087,(1,0,4):C.UVGC_806_1053,(1,0,11):C.UVGC_867_1104,(1,0,1):C.UVGC_829_1089,(1,0,5):C.UVGC_807_1058,(1,0,10):C.UVGC_867_1105,(1,0,2):C.UVGC_829_1091,(1,0,6):C.UVGC_867_1106,(1,0,9):C.UVGC_867_1107,(0,0,3):C.UVGC_609_897,(0,0,7):C.UVGC_609_898,(0,0,8):C.UVGC_609_899,(0,0,0):C.UVGC_794_1041,(0,0,4):C.UVGC_807_1056,(0,0,11):C.UVGC_866_1099,(0,0,1):C.UVGC_794_1043,(0,0,5):C.UVGC_866_1100,(0,0,10):C.UVGC_866_1101,(0,0,2):C.UVGC_828_1085,(0,0,6):C.UVGC_866_1102,(0,0,9):C.UVGC_866_1103})

V_885 = CTVertex(name = 'V_885',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qd1, P.YS3Qu2] ], [ [P.g, P.YS3Qd1, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_829_1087,(1,0,8):C.UVGC_867_1104,(1,0,1):C.UVGC_829_1089,(1,0,7):C.UVGC_867_1105,(1,0,2):C.UVGC_829_1091,(1,0,6):C.UVGC_867_1107,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_794_1041,(0,0,8):C.UVGC_866_1099,(0,0,1):C.UVGC_794_1043,(0,0,7):C.UVGC_866_1101,(0,0,2):C.UVGC_828_1085,(0,0,6):C.UVGC_866_1103})

V_886 = CTVertex(name = 'V_886',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qd1, P.YS3Qu3] ], [ [P.g, P.YS3Qd1, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_829_1087,(1,0,8):C.UVGC_867_1104,(1,0,1):C.UVGC_829_1089,(1,0,7):C.UVGC_867_1105,(1,0,2):C.UVGC_829_1091,(1,0,6):C.UVGC_867_1107,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_794_1041,(0,0,8):C.UVGC_866_1099,(0,0,1):C.UVGC_794_1043,(0,0,7):C.UVGC_866_1101,(0,0,2):C.UVGC_828_1085,(0,0,6):C.UVGC_866_1103})

V_887 = CTVertex(name = 'V_887',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qd1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1] ], [ [P.g] ], [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_326_460,(1,0,3):C.UVGC_326_461,(1,0,0):C.UVGC_794_1041,(1,0,5):C.UVGC_797_1045,(1,0,1):C.UVGC_794_1043,(1,0,4):C.UVGC_797_1046,(0,0,2):C.UVGC_326_460,(0,0,3):C.UVGC_326_461,(0,0,0):C.UVGC_794_1041,(0,0,5):C.UVGC_797_1045,(0,0,1):C.UVGC_794_1043,(0,0,4):C.UVGC_797_1046})

V_888 = CTVertex(name = 'V_888',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd2, P.YS3Qu1, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu2] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu1, P.YS3Qu2] ] ],
                 couplings = {(1,0,0):C.UVGC_806_1053,(1,0,1):C.UVGC_806_1054,(1,0,2):C.UVGC_806_1055,(0,0,0):C.UVGC_807_1056,(0,0,1):C.UVGC_807_1057,(0,0,2):C.UVGC_807_1058})

V_889 = CTVertex(name = 'V_889',
                 type = 'UV',
                 particles = [ P.YS3Qd1, P.YS3Qd2__tilde__, P.YS3Qu1__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu2] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu1, P.YS3Qu2] ] ],
                 couplings = {(1,0,0):C.UVGC_806_1053,(1,0,1):C.UVGC_806_1054,(1,0,2):C.UVGC_806_1055,(0,0,0):C.UVGC_807_1056,(0,0,1):C.UVGC_807_1057,(0,0,2):C.UVGC_807_1058})

V_890 = CTVertex(name = 'V_890',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3Qd2, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qd2, P.YS3Qu1] ], [ [P.g, P.YS3Qd2, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_829_1087,(1,0,8):C.UVGC_867_1104,(1,0,1):C.UVGC_829_1089,(1,0,7):C.UVGC_867_1105,(1,0,2):C.UVGC_829_1091,(1,0,6):C.UVGC_867_1107,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_794_1041,(0,0,8):C.UVGC_866_1099,(0,0,1):C.UVGC_794_1043,(0,0,7):C.UVGC_866_1101,(0,0,2):C.UVGC_828_1085,(0,0,6):C.UVGC_866_1103})

V_891 = CTVertex(name = 'V_891',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qu2] ], [ [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,7):C.UVGC_610_901,(1,0,8):C.UVGC_610_902,(1,0,0):C.UVGC_829_1087,(1,0,4):C.UVGC_806_1053,(1,0,11):C.UVGC_867_1104,(1,0,1):C.UVGC_829_1089,(1,0,5):C.UVGC_807_1058,(1,0,10):C.UVGC_867_1105,(1,0,2):C.UVGC_829_1091,(1,0,6):C.UVGC_867_1106,(1,0,9):C.UVGC_867_1107,(0,0,3):C.UVGC_609_897,(0,0,7):C.UVGC_609_898,(0,0,8):C.UVGC_609_899,(0,0,0):C.UVGC_794_1041,(0,0,4):C.UVGC_807_1056,(0,0,11):C.UVGC_866_1099,(0,0,1):C.UVGC_794_1043,(0,0,5):C.UVGC_866_1100,(0,0,10):C.UVGC_866_1101,(0,0,2):C.UVGC_828_1085,(0,0,6):C.UVGC_866_1102,(0,0,9):C.UVGC_866_1103})

V_892 = CTVertex(name = 'V_892',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qd2, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qd2, P.YS3Qu3] ], [ [P.g, P.YS3Qd2, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_829_1087,(1,0,8):C.UVGC_867_1104,(1,0,1):C.UVGC_829_1089,(1,0,7):C.UVGC_867_1105,(1,0,2):C.UVGC_829_1091,(1,0,6):C.UVGC_867_1107,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_794_1041,(0,0,8):C.UVGC_866_1099,(0,0,1):C.UVGC_794_1043,(0,0,7):C.UVGC_866_1101,(0,0,2):C.UVGC_828_1085,(0,0,6):C.UVGC_866_1103})

V_893 = CTVertex(name = 'V_893',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qd2] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd1, P.YS3Qd2] ], [ [P.g, P.YS3Qd1, P.YS3Qd2, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_813_1065,(1,0,8):C.UVGC_825_1080,(1,0,1):C.UVGC_813_1067,(1,0,7):C.UVGC_825_1081,(1,0,2):C.UVGC_813_1069,(1,0,6):C.UVGC_825_1082,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_812_1059,(0,0,8):C.UVGC_824_1077,(0,0,1):C.UVGC_812_1061,(0,0,7):C.UVGC_824_1078,(0,0,2):C.UVGC_812_1063,(0,0,6):C.UVGC_824_1079})

V_894 = CTVertex(name = 'V_894',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qd2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_326_460,(1,0,3):C.UVGC_326_461,(1,0,0):C.UVGC_794_1041,(1,0,5):C.UVGC_797_1045,(1,0,1):C.UVGC_794_1043,(1,0,4):C.UVGC_797_1046,(0,0,2):C.UVGC_326_460,(0,0,3):C.UVGC_326_461,(0,0,0):C.UVGC_794_1041,(0,0,5):C.UVGC_797_1045,(0,0,1):C.UVGC_794_1043,(0,0,4):C.UVGC_797_1046})

V_895 = CTVertex(name = 'V_895',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd3, P.YS3Qu1, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu3], [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu1, P.YS3Qu3] ] ],
                 couplings = {(1,0,0):C.UVGC_806_1053,(1,0,1):C.UVGC_806_1054,(1,0,2):C.UVGC_806_1055,(0,0,0):C.UVGC_807_1056,(0,0,1):C.UVGC_807_1057,(0,0,2):C.UVGC_807_1058})

V_896 = CTVertex(name = 'V_896',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd3, P.YS3Qu2, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu3], [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qu2, P.YS3Qu3] ] ],
                 couplings = {(1,0,0):C.UVGC_806_1053,(1,0,1):C.UVGC_806_1054,(1,0,2):C.UVGC_806_1055,(0,0,0):C.UVGC_807_1056,(0,0,1):C.UVGC_807_1057,(0,0,2):C.UVGC_807_1058})

V_897 = CTVertex(name = 'V_897',
                 type = 'UV',
                 particles = [ P.YS3Qd1, P.YS3Qd3__tilde__, P.YS3Qu1__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu3], [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu1, P.YS3Qu3] ] ],
                 couplings = {(1,0,0):C.UVGC_806_1053,(1,0,1):C.UVGC_806_1054,(1,0,2):C.UVGC_806_1055,(0,0,0):C.UVGC_807_1056,(0,0,1):C.UVGC_807_1057,(0,0,2):C.UVGC_807_1058})

V_898 = CTVertex(name = 'V_898',
                 type = 'UV',
                 particles = [ P.YS3Qd2, P.YS3Qd3__tilde__, P.YS3Qu2__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu3], [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qu2, P.YS3Qu3] ] ],
                 couplings = {(1,0,0):C.UVGC_806_1053,(1,0,1):C.UVGC_806_1054,(1,0,2):C.UVGC_806_1055,(0,0,0):C.UVGC_807_1056,(0,0,1):C.UVGC_807_1057,(0,0,2):C.UVGC_807_1058})

V_899 = CTVertex(name = 'V_899',
                 type = 'UV',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3Qd3, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qd3, P.YS3Qu1] ], [ [P.g, P.YS3Qd3, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_829_1087,(1,0,8):C.UVGC_867_1104,(1,0,1):C.UVGC_829_1089,(1,0,7):C.UVGC_867_1105,(1,0,2):C.UVGC_829_1091,(1,0,6):C.UVGC_867_1107,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_794_1041,(0,0,8):C.UVGC_866_1099,(0,0,1):C.UVGC_794_1043,(0,0,7):C.UVGC_866_1101,(0,0,2):C.UVGC_828_1085,(0,0,6):C.UVGC_866_1103})

V_900 = CTVertex(name = 'V_900',
                 type = 'UV',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3Qd3, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qd3, P.YS3Qu2] ], [ [P.g, P.YS3Qd3, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_829_1087,(1,0,8):C.UVGC_867_1104,(1,0,1):C.UVGC_829_1089,(1,0,7):C.UVGC_867_1105,(1,0,2):C.UVGC_829_1091,(1,0,6):C.UVGC_867_1107,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_794_1041,(0,0,8):C.UVGC_866_1099,(0,0,1):C.UVGC_794_1043,(0,0,7):C.UVGC_866_1101,(0,0,2):C.UVGC_828_1085,(0,0,6):C.UVGC_866_1103})

V_901 = CTVertex(name = 'V_901',
                 type = 'UV',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,7):C.UVGC_610_901,(1,0,8):C.UVGC_610_902,(1,0,0):C.UVGC_829_1087,(1,0,4):C.UVGC_806_1053,(1,0,11):C.UVGC_867_1104,(1,0,1):C.UVGC_829_1089,(1,0,5):C.UVGC_807_1058,(1,0,10):C.UVGC_867_1105,(1,0,2):C.UVGC_829_1091,(1,0,6):C.UVGC_867_1106,(1,0,9):C.UVGC_867_1107,(0,0,3):C.UVGC_609_897,(0,0,7):C.UVGC_609_898,(0,0,8):C.UVGC_609_899,(0,0,0):C.UVGC_794_1041,(0,0,4):C.UVGC_807_1056,(0,0,11):C.UVGC_866_1099,(0,0,1):C.UVGC_794_1043,(0,0,5):C.UVGC_866_1100,(0,0,10):C.UVGC_866_1101,(0,0,2):C.UVGC_828_1085,(0,0,6):C.UVGC_866_1102,(0,0,9):C.UVGC_866_1103})

V_902 = CTVertex(name = 'V_902',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd1, P.YS3Qd3] ], [ [P.g, P.YS3Qd1, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_813_1065,(1,0,8):C.UVGC_825_1080,(1,0,1):C.UVGC_813_1067,(1,0,7):C.UVGC_825_1081,(1,0,2):C.UVGC_813_1069,(1,0,6):C.UVGC_825_1082,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_812_1059,(0,0,8):C.UVGC_824_1077,(0,0,1):C.UVGC_812_1061,(0,0,7):C.UVGC_824_1078,(0,0,2):C.UVGC_812_1063,(0,0,6):C.UVGC_824_1079})

V_903 = CTVertex(name = 'V_903',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3Qd2, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd2, P.YS3Qd3] ], [ [P.g, P.YS3Qd2, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_813_1065,(1,0,8):C.UVGC_825_1080,(1,0,1):C.UVGC_813_1067,(1,0,7):C.UVGC_825_1081,(1,0,2):C.UVGC_813_1069,(1,0,6):C.UVGC_825_1082,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_812_1059,(0,0,8):C.UVGC_824_1077,(0,0,1):C.UVGC_812_1061,(0,0,7):C.UVGC_824_1078,(0,0,2):C.UVGC_812_1063,(0,0,6):C.UVGC_824_1079})

V_904 = CTVertex(name = 'V_904',
                 type = 'UV',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3Qd3 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_326_460,(1,0,3):C.UVGC_326_461,(1,0,0):C.UVGC_794_1041,(1,0,5):C.UVGC_797_1045,(1,0,1):C.UVGC_794_1043,(1,0,4):C.UVGC_797_1046,(0,0,2):C.UVGC_326_460,(0,0,3):C.UVGC_326_461,(0,0,0):C.UVGC_794_1041,(0,0,5):C.UVGC_797_1045,(0,0,1):C.UVGC_794_1043,(0,0,4):C.UVGC_797_1046})

V_905 = CTVertex(name = 'V_905',
                 type = 'UV',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qu1, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qu1, P.YS3u1] ], [ [P.g, P.YS3Qu1, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_873_1113,(1,0,8):C.UVGC_877_1121,(1,0,1):C.UVGC_873_1115,(1,0,7):C.UVGC_877_1122,(1,0,2):C.UVGC_813_1065,(1,0,6):C.UVGC_877_1123,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_872_1108,(0,0,8):C.UVGC_876_1118,(0,0,1):C.UVGC_872_1110,(0,0,7):C.UVGC_876_1119,(0,0,2):C.UVGC_812_1059,(0,0,6):C.UVGC_876_1120})

V_906 = CTVertex(name = 'V_906',
                 type = 'UV',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qu2, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qu2], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qu2, P.YS3u1] ], [ [P.g, P.YS3Qu2, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qu2, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_873_1113,(1,0,8):C.UVGC_877_1121,(1,0,1):C.UVGC_873_1115,(1,0,7):C.UVGC_877_1122,(1,0,2):C.UVGC_813_1065,(1,0,6):C.UVGC_877_1123,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_872_1108,(0,0,8):C.UVGC_876_1118,(0,0,1):C.UVGC_872_1110,(0,0,7):C.UVGC_876_1119,(0,0,2):C.UVGC_812_1059,(0,0,6):C.UVGC_876_1120})

V_907 = CTVertex(name = 'V_907',
                 type = 'UV',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu3], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qu3, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qu3], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qu3, P.YS3u1] ], [ [P.g, P.YS3Qu3, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qu3, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_873_1113,(1,0,8):C.UVGC_877_1121,(1,0,1):C.UVGC_873_1115,(1,0,7):C.UVGC_877_1122,(1,0,2):C.UVGC_813_1065,(1,0,6):C.UVGC_877_1123,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_872_1108,(0,0,8):C.UVGC_876_1118,(0,0,1):C.UVGC_872_1110,(0,0,7):C.UVGC_876_1119,(0,0,2):C.UVGC_812_1059,(0,0,6):C.UVGC_876_1120})

V_908 = CTVertex(name = 'V_908',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qd1, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qd1, P.YS3u1] ], [ [P.g, P.YS3Qd1, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_829_1087,(1,0,8):C.UVGC_829_1088,(1,0,1):C.UVGC_829_1089,(1,0,7):C.UVGC_829_1090,(1,0,2):C.UVGC_829_1091,(1,0,6):C.UVGC_829_1092,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_794_1041,(0,0,8):C.UVGC_828_1083,(0,0,1):C.UVGC_794_1043,(0,0,7):C.UVGC_828_1084,(0,0,2):C.UVGC_828_1085,(0,0,6):C.UVGC_828_1086})

V_909 = CTVertex(name = 'V_909',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qd2, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qd2, P.YS3u1] ], [ [P.g, P.YS3Qd2, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_829_1087,(1,0,8):C.UVGC_829_1088,(1,0,1):C.UVGC_829_1089,(1,0,7):C.UVGC_829_1090,(1,0,2):C.UVGC_829_1091,(1,0,6):C.UVGC_829_1092,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_794_1041,(0,0,8):C.UVGC_828_1083,(0,0,1):C.UVGC_794_1043,(0,0,7):C.UVGC_828_1084,(0,0,2):C.UVGC_828_1085,(0,0,6):C.UVGC_828_1086})

V_910 = CTVertex(name = 'V_910',
                 type = 'UV',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qd3, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qd3, P.YS3u1] ], [ [P.g, P.YS3Qd3, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_829_1087,(1,0,8):C.UVGC_829_1088,(1,0,1):C.UVGC_829_1089,(1,0,7):C.UVGC_829_1090,(1,0,2):C.UVGC_829_1091,(1,0,6):C.UVGC_829_1092,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_794_1041,(0,0,8):C.UVGC_828_1083,(0,0,1):C.UVGC_794_1043,(0,0,7):C.UVGC_828_1084,(0,0,2):C.UVGC_828_1085,(0,0,6):C.UVGC_828_1086})

V_911 = CTVertex(name = 'V_911',
                 type = 'UV',
                 particles = [ P.YS3u1__tilde__, P.YS3u1__tilde__, P.YS3u1, P.YS3u1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3u1] ], [ [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_326_460,(1,0,3):C.UVGC_326_461,(1,0,0):C.UVGC_800_1047,(1,0,5):C.UVGC_803_1051,(1,0,1):C.UVGC_800_1049,(1,0,4):C.UVGC_803_1052,(0,0,2):C.UVGC_326_460,(0,0,3):C.UVGC_326_461,(0,0,0):C.UVGC_800_1047,(0,0,5):C.UVGC_803_1051,(0,0,1):C.UVGC_800_1049,(0,0,4):C.UVGC_803_1052})

V_912 = CTVertex(name = 'V_912',
                 type = 'UV',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qu1, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qu1, P.YS3u2] ], [ [P.g, P.YS3Qu1, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_873_1113,(1,0,8):C.UVGC_877_1121,(1,0,1):C.UVGC_873_1115,(1,0,7):C.UVGC_877_1122,(1,0,2):C.UVGC_813_1065,(1,0,6):C.UVGC_877_1123,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_872_1108,(0,0,8):C.UVGC_876_1118,(0,0,1):C.UVGC_872_1110,(0,0,7):C.UVGC_876_1119,(0,0,2):C.UVGC_812_1059,(0,0,6):C.UVGC_876_1120})

V_913 = CTVertex(name = 'V_913',
                 type = 'UV',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qu2, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qu2], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qu2, P.YS3u2] ], [ [P.g, P.YS3Qu2, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qu2, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_873_1113,(1,0,8):C.UVGC_877_1121,(1,0,1):C.UVGC_873_1115,(1,0,7):C.UVGC_877_1122,(1,0,2):C.UVGC_813_1065,(1,0,6):C.UVGC_877_1123,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_872_1108,(0,0,8):C.UVGC_876_1118,(0,0,1):C.UVGC_872_1110,(0,0,7):C.UVGC_876_1119,(0,0,2):C.UVGC_812_1059,(0,0,6):C.UVGC_876_1120})

V_914 = CTVertex(name = 'V_914',
                 type = 'UV',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu3], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qu3, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qu3], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qu3, P.YS3u2] ], [ [P.g, P.YS3Qu3, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qu3, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_873_1113,(1,0,8):C.UVGC_877_1121,(1,0,1):C.UVGC_873_1115,(1,0,7):C.UVGC_877_1122,(1,0,2):C.UVGC_813_1065,(1,0,6):C.UVGC_877_1123,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_872_1108,(0,0,8):C.UVGC_876_1118,(0,0,1):C.UVGC_872_1110,(0,0,7):C.UVGC_876_1119,(0,0,2):C.UVGC_812_1059,(0,0,6):C.UVGC_876_1120})

V_915 = CTVertex(name = 'V_915',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qd1, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qd1, P.YS3u2] ], [ [P.g, P.YS3Qd1, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_829_1087,(1,0,8):C.UVGC_829_1088,(1,0,1):C.UVGC_829_1089,(1,0,7):C.UVGC_829_1090,(1,0,2):C.UVGC_829_1091,(1,0,6):C.UVGC_829_1092,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_794_1041,(0,0,8):C.UVGC_828_1083,(0,0,1):C.UVGC_794_1043,(0,0,7):C.UVGC_828_1084,(0,0,2):C.UVGC_828_1085,(0,0,6):C.UVGC_828_1086})

V_916 = CTVertex(name = 'V_916',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qd2, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qd2, P.YS3u2] ], [ [P.g, P.YS3Qd2, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_829_1087,(1,0,8):C.UVGC_829_1088,(1,0,1):C.UVGC_829_1089,(1,0,7):C.UVGC_829_1090,(1,0,2):C.UVGC_829_1091,(1,0,6):C.UVGC_829_1092,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_794_1041,(0,0,8):C.UVGC_828_1083,(0,0,1):C.UVGC_794_1043,(0,0,7):C.UVGC_828_1084,(0,0,2):C.UVGC_828_1085,(0,0,6):C.UVGC_828_1086})

V_917 = CTVertex(name = 'V_917',
                 type = 'UV',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qd3, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qd3, P.YS3u2] ], [ [P.g, P.YS3Qd3, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_829_1087,(1,0,8):C.UVGC_829_1088,(1,0,1):C.UVGC_829_1089,(1,0,7):C.UVGC_829_1090,(1,0,2):C.UVGC_829_1091,(1,0,6):C.UVGC_829_1092,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_794_1041,(0,0,8):C.UVGC_828_1083,(0,0,1):C.UVGC_794_1043,(0,0,7):C.UVGC_828_1084,(0,0,2):C.UVGC_828_1085,(0,0,6):C.UVGC_828_1086})

V_918 = CTVertex(name = 'V_918',
                 type = 'UV',
                 particles = [ P.YS3u1__tilde__, P.YS3u1, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u1], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3u1, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3u1], [P.g, P.YS3u2] ], [ [P.g, P.YS3u1, P.YS3u2] ], [ [P.g, P.YS3u1, P.YS3u2, P.Z] ], [ [P.g, P.YS3u1, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_873_1113,(1,0,8):C.UVGC_927_1130,(1,0,1):C.UVGC_873_1115,(1,0,7):C.UVGC_927_1131,(1,0,2):C.UVGC_813_1065,(1,0,6):C.UVGC_813_1066,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_872_1108,(0,0,8):C.UVGC_926_1128,(0,0,1):C.UVGC_872_1110,(0,0,7):C.UVGC_926_1129,(0,0,2):C.UVGC_812_1059,(0,0,6):C.UVGC_812_1060})

V_919 = CTVertex(name = 'V_919',
                 type = 'UV',
                 particles = [ P.YS3u2__tilde__, P.YS3u2__tilde__, P.YS3u2, P.YS3u2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3u2] ], [ [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_326_460,(1,0,3):C.UVGC_326_461,(1,0,0):C.UVGC_800_1047,(1,0,5):C.UVGC_803_1051,(1,0,1):C.UVGC_800_1049,(1,0,4):C.UVGC_803_1052,(0,0,2):C.UVGC_326_460,(0,0,3):C.UVGC_326_461,(0,0,0):C.UVGC_800_1047,(0,0,5):C.UVGC_803_1051,(0,0,1):C.UVGC_800_1049,(0,0,4):C.UVGC_803_1052})

V_920 = CTVertex(name = 'V_920',
                 type = 'UV',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qu1, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qu1, P.YS3u3] ], [ [P.g, P.YS3Qu1, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_873_1113,(1,0,8):C.UVGC_877_1121,(1,0,1):C.UVGC_873_1115,(1,0,7):C.UVGC_877_1122,(1,0,2):C.UVGC_813_1065,(1,0,6):C.UVGC_877_1123,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_872_1108,(0,0,8):C.UVGC_876_1118,(0,0,1):C.UVGC_872_1110,(0,0,7):C.UVGC_876_1119,(0,0,2):C.UVGC_812_1059,(0,0,6):C.UVGC_876_1120})

V_921 = CTVertex(name = 'V_921',
                 type = 'UV',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qu2, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qu2], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qu2, P.YS3u3] ], [ [P.g, P.YS3Qu2, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qu2, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_873_1113,(1,0,8):C.UVGC_877_1121,(1,0,1):C.UVGC_873_1115,(1,0,7):C.UVGC_877_1122,(1,0,2):C.UVGC_813_1065,(1,0,6):C.UVGC_877_1123,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_872_1108,(0,0,8):C.UVGC_876_1118,(0,0,1):C.UVGC_872_1110,(0,0,7):C.UVGC_876_1119,(0,0,2):C.UVGC_812_1059,(0,0,6):C.UVGC_876_1120})

V_922 = CTVertex(name = 'V_922',
                 type = 'UV',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu3], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qu3, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qu3], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qu3, P.YS3u3] ], [ [P.g, P.YS3Qu3, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qu3, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_873_1113,(1,0,8):C.UVGC_877_1121,(1,0,1):C.UVGC_873_1115,(1,0,7):C.UVGC_877_1122,(1,0,2):C.UVGC_813_1065,(1,0,6):C.UVGC_877_1123,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_872_1108,(0,0,8):C.UVGC_876_1118,(0,0,1):C.UVGC_872_1110,(0,0,7):C.UVGC_876_1119,(0,0,2):C.UVGC_812_1059,(0,0,6):C.UVGC_876_1120})

V_923 = CTVertex(name = 'V_923',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qd1, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qd1, P.YS3u3] ], [ [P.g, P.YS3Qd1, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_829_1087,(1,0,8):C.UVGC_829_1088,(1,0,1):C.UVGC_829_1089,(1,0,7):C.UVGC_829_1090,(1,0,2):C.UVGC_829_1091,(1,0,6):C.UVGC_829_1092,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_794_1041,(0,0,8):C.UVGC_828_1083,(0,0,1):C.UVGC_794_1043,(0,0,7):C.UVGC_828_1084,(0,0,2):C.UVGC_828_1085,(0,0,6):C.UVGC_828_1086})

V_924 = CTVertex(name = 'V_924',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qd2, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qd2, P.YS3u3] ], [ [P.g, P.YS3Qd2, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_829_1087,(1,0,8):C.UVGC_829_1088,(1,0,1):C.UVGC_829_1089,(1,0,7):C.UVGC_829_1090,(1,0,2):C.UVGC_829_1091,(1,0,6):C.UVGC_829_1092,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_794_1041,(0,0,8):C.UVGC_828_1083,(0,0,1):C.UVGC_794_1043,(0,0,7):C.UVGC_828_1084,(0,0,2):C.UVGC_828_1085,(0,0,6):C.UVGC_828_1086})

V_925 = CTVertex(name = 'V_925',
                 type = 'UV',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qd3, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qd3, P.YS3u3] ], [ [P.g, P.YS3Qd3, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_829_1087,(1,0,8):C.UVGC_829_1088,(1,0,1):C.UVGC_829_1089,(1,0,7):C.UVGC_829_1090,(1,0,2):C.UVGC_829_1091,(1,0,6):C.UVGC_829_1092,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_794_1041,(0,0,8):C.UVGC_828_1083,(0,0,1):C.UVGC_794_1043,(0,0,7):C.UVGC_828_1084,(0,0,2):C.UVGC_828_1085,(0,0,6):C.UVGC_828_1086})

V_926 = CTVertex(name = 'V_926',
                 type = 'UV',
                 particles = [ P.YS3u1__tilde__, P.YS3u1, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u1], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3u1, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3u1], [P.g, P.YS3u3] ], [ [P.g, P.YS3u1, P.YS3u3] ], [ [P.g, P.YS3u1, P.YS3u3, P.Z] ], [ [P.g, P.YS3u1, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_873_1113,(1,0,8):C.UVGC_927_1130,(1,0,1):C.UVGC_873_1115,(1,0,7):C.UVGC_927_1131,(1,0,2):C.UVGC_813_1065,(1,0,6):C.UVGC_813_1066,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_872_1108,(0,0,8):C.UVGC_926_1128,(0,0,1):C.UVGC_872_1110,(0,0,7):C.UVGC_926_1129,(0,0,2):C.UVGC_812_1059,(0,0,6):C.UVGC_812_1060})

V_927 = CTVertex(name = 'V_927',
                 type = 'UV',
                 particles = [ P.YS3u2__tilde__, P.YS3u2, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u2], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3u2, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3u2], [P.g, P.YS3u3] ], [ [P.g, P.YS3u2, P.YS3u3] ], [ [P.g, P.YS3u2, P.YS3u3, P.Z] ], [ [P.g, P.YS3u2, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_873_1113,(1,0,8):C.UVGC_927_1130,(1,0,1):C.UVGC_873_1115,(1,0,7):C.UVGC_927_1131,(1,0,2):C.UVGC_813_1065,(1,0,6):C.UVGC_813_1066,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_872_1108,(0,0,8):C.UVGC_926_1128,(0,0,1):C.UVGC_872_1110,(0,0,7):C.UVGC_926_1129,(0,0,2):C.UVGC_812_1059,(0,0,6):C.UVGC_812_1060})

V_928 = CTVertex(name = 'V_928',
                 type = 'UV',
                 particles = [ P.YS3u3__tilde__, P.YS3u3__tilde__, P.YS3u3, P.YS3u3 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3u3] ], [ [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_326_460,(1,0,3):C.UVGC_326_461,(1,0,0):C.UVGC_800_1047,(1,0,5):C.UVGC_803_1051,(1,0,1):C.UVGC_800_1049,(1,0,4):C.UVGC_803_1052,(0,0,2):C.UVGC_326_460,(0,0,3):C.UVGC_326_461,(0,0,0):C.UVGC_800_1047,(0,0,5):C.UVGC_803_1051,(0,0,1):C.UVGC_800_1049,(0,0,4):C.UVGC_803_1052})

V_929 = CTVertex(name = 'V_929',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3d1, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3d1, P.YS3Qu1] ], [ [P.g, P.YS3d1, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_829_1087,(1,0,8):C.UVGC_861_1096,(1,0,1):C.UVGC_829_1089,(1,0,7):C.UVGC_861_1097,(1,0,2):C.UVGC_829_1091,(1,0,6):C.UVGC_861_1098,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_794_1041,(0,0,8):C.UVGC_860_1093,(0,0,1):C.UVGC_794_1043,(0,0,7):C.UVGC_860_1094,(0,0,2):C.UVGC_828_1085,(0,0,6):C.UVGC_860_1095})

V_930 = CTVertex(name = 'V_930',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3d1, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3d1, P.YS3Qu2] ], [ [P.g, P.YS3d1, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_829_1087,(1,0,8):C.UVGC_861_1096,(1,0,1):C.UVGC_829_1089,(1,0,7):C.UVGC_861_1097,(1,0,2):C.UVGC_829_1091,(1,0,6):C.UVGC_861_1098,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_794_1041,(0,0,8):C.UVGC_860_1093,(0,0,1):C.UVGC_794_1043,(0,0,7):C.UVGC_860_1094,(0,0,2):C.UVGC_828_1085,(0,0,6):C.UVGC_860_1095})

V_931 = CTVertex(name = 'V_931',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3d1, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3d1, P.YS3Qu3] ], [ [P.g, P.YS3d1, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_829_1087,(1,0,8):C.UVGC_861_1096,(1,0,1):C.UVGC_829_1089,(1,0,7):C.UVGC_861_1097,(1,0,2):C.UVGC_829_1091,(1,0,6):C.UVGC_861_1098,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_794_1041,(0,0,8):C.UVGC_860_1093,(0,0,1):C.UVGC_794_1043,(0,0,7):C.UVGC_860_1094,(0,0,2):C.UVGC_828_1085,(0,0,6):C.UVGC_860_1095})

V_932 = CTVertex(name = 'V_932',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qd1] ], [ [P.a, P.g, P.YS3d1, P.YS3Qd1] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qd1] ], [ [P.g, P.YS3d1, P.YS3Qd1] ], [ [P.g, P.YS3d1, P.YS3Qd1, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qd1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_813_1065,(1,0,8):C.UVGC_819_1074,(1,0,1):C.UVGC_813_1067,(1,0,7):C.UVGC_819_1075,(1,0,2):C.UVGC_813_1069,(1,0,6):C.UVGC_819_1076,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_812_1059,(0,0,8):C.UVGC_818_1071,(0,0,1):C.UVGC_812_1061,(0,0,7):C.UVGC_818_1072,(0,0,2):C.UVGC_812_1063,(0,0,6):C.UVGC_818_1073})

V_933 = CTVertex(name = 'V_933',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qd2] ], [ [P.a, P.g, P.YS3d1, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qd2] ], [ [P.g, P.YS3d1, P.YS3Qd2] ], [ [P.g, P.YS3d1, P.YS3Qd2, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_813_1065,(1,0,8):C.UVGC_819_1074,(1,0,1):C.UVGC_813_1067,(1,0,7):C.UVGC_819_1075,(1,0,2):C.UVGC_813_1069,(1,0,6):C.UVGC_819_1076,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_812_1059,(0,0,8):C.UVGC_818_1071,(0,0,1):C.UVGC_812_1061,(0,0,7):C.UVGC_818_1072,(0,0,2):C.UVGC_812_1063,(0,0,6):C.UVGC_818_1073})

V_934 = CTVertex(name = 'V_934',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3d1, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3d1, P.YS3Qd3] ], [ [P.g, P.YS3d1, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_813_1065,(1,0,8):C.UVGC_819_1074,(1,0,1):C.UVGC_813_1067,(1,0,7):C.UVGC_819_1075,(1,0,2):C.UVGC_813_1069,(1,0,6):C.UVGC_819_1076,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_812_1059,(0,0,8):C.UVGC_818_1071,(0,0,1):C.UVGC_812_1061,(0,0,7):C.UVGC_818_1072,(0,0,2):C.UVGC_812_1063,(0,0,6):C.UVGC_818_1073})

V_935 = CTVertex(name = 'V_935',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3d1, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3u1] ], [ [P.g, P.YS3d1, P.YS3u1] ], [ [P.g, P.YS3d1, P.YS3u1, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_829_1087,(1,0,8):C.UVGC_921_1125,(1,0,1):C.UVGC_829_1089,(1,0,7):C.UVGC_921_1126,(1,0,2):C.UVGC_829_1091,(1,0,6):C.UVGC_921_1127,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_794_1041,(0,0,8):C.UVGC_794_1042,(0,0,1):C.UVGC_794_1043,(0,0,7):C.UVGC_794_1044,(0,0,2):C.UVGC_828_1085,(0,0,6):C.UVGC_920_1124})

V_936 = CTVertex(name = 'V_936',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3d1, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3u2] ], [ [P.g, P.YS3d1, P.YS3u2] ], [ [P.g, P.YS3d1, P.YS3u2, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_829_1087,(1,0,8):C.UVGC_921_1125,(1,0,1):C.UVGC_829_1089,(1,0,7):C.UVGC_921_1126,(1,0,2):C.UVGC_829_1091,(1,0,6):C.UVGC_921_1127,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_794_1041,(0,0,8):C.UVGC_794_1042,(0,0,1):C.UVGC_794_1043,(0,0,7):C.UVGC_794_1044,(0,0,2):C.UVGC_828_1085,(0,0,6):C.UVGC_920_1124})

V_937 = CTVertex(name = 'V_937',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3d1, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3u3] ], [ [P.g, P.YS3d1, P.YS3u3] ], [ [P.g, P.YS3d1, P.YS3u3, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_829_1087,(1,0,8):C.UVGC_921_1125,(1,0,1):C.UVGC_829_1089,(1,0,7):C.UVGC_921_1126,(1,0,2):C.UVGC_829_1091,(1,0,6):C.UVGC_921_1127,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_794_1041,(0,0,8):C.UVGC_794_1042,(0,0,1):C.UVGC_794_1043,(0,0,7):C.UVGC_794_1044,(0,0,2):C.UVGC_828_1085,(0,0,6):C.UVGC_920_1124})

V_938 = CTVertex(name = 'V_938',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1__tilde__, P.YS3d1, P.YS3d1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1] ], [ [P.g] ], [ [P.g, P.YS3d1] ], [ [P.g, P.YS3d1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_326_460,(1,0,3):C.UVGC_326_461,(1,0,0):C.UVGC_794_1041,(1,0,5):C.UVGC_794_1042,(1,0,1):C.UVGC_794_1043,(1,0,4):C.UVGC_794_1044,(0,0,2):C.UVGC_326_460,(0,0,3):C.UVGC_326_461,(0,0,0):C.UVGC_794_1041,(0,0,5):C.UVGC_794_1042,(0,0,1):C.UVGC_794_1043,(0,0,4):C.UVGC_794_1044})

V_939 = CTVertex(name = 'V_939',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3d2, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3d2, P.YS3Qu1] ], [ [P.g, P.YS3d2, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_829_1087,(1,0,8):C.UVGC_861_1096,(1,0,1):C.UVGC_829_1089,(1,0,7):C.UVGC_861_1097,(1,0,2):C.UVGC_829_1091,(1,0,6):C.UVGC_861_1098,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_794_1041,(0,0,8):C.UVGC_860_1093,(0,0,1):C.UVGC_794_1043,(0,0,7):C.UVGC_860_1094,(0,0,2):C.UVGC_828_1085,(0,0,6):C.UVGC_860_1095})

V_940 = CTVertex(name = 'V_940',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3d2, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3d2, P.YS3Qu2] ], [ [P.g, P.YS3d2, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_829_1087,(1,0,8):C.UVGC_861_1096,(1,0,1):C.UVGC_829_1089,(1,0,7):C.UVGC_861_1097,(1,0,2):C.UVGC_829_1091,(1,0,6):C.UVGC_861_1098,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_794_1041,(0,0,8):C.UVGC_860_1093,(0,0,1):C.UVGC_794_1043,(0,0,7):C.UVGC_860_1094,(0,0,2):C.UVGC_828_1085,(0,0,6):C.UVGC_860_1095})

V_941 = CTVertex(name = 'V_941',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3d2, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3d2, P.YS3Qu3] ], [ [P.g, P.YS3d2, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_829_1087,(1,0,8):C.UVGC_861_1096,(1,0,1):C.UVGC_829_1089,(1,0,7):C.UVGC_861_1097,(1,0,2):C.UVGC_829_1091,(1,0,6):C.UVGC_861_1098,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_794_1041,(0,0,8):C.UVGC_860_1093,(0,0,1):C.UVGC_794_1043,(0,0,7):C.UVGC_860_1094,(0,0,2):C.UVGC_828_1085,(0,0,6):C.UVGC_860_1095})

V_942 = CTVertex(name = 'V_942',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qd1] ], [ [P.a, P.g, P.YS3d2, P.YS3Qd1] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qd1] ], [ [P.g, P.YS3d2, P.YS3Qd1] ], [ [P.g, P.YS3d2, P.YS3Qd1, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qd1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_813_1065,(1,0,8):C.UVGC_819_1074,(1,0,1):C.UVGC_813_1067,(1,0,7):C.UVGC_819_1075,(1,0,2):C.UVGC_813_1069,(1,0,6):C.UVGC_819_1076,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_812_1059,(0,0,8):C.UVGC_818_1071,(0,0,1):C.UVGC_812_1061,(0,0,7):C.UVGC_818_1072,(0,0,2):C.UVGC_812_1063,(0,0,6):C.UVGC_818_1073})

V_943 = CTVertex(name = 'V_943',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qd2] ], [ [P.a, P.g, P.YS3d2, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qd2] ], [ [P.g, P.YS3d2, P.YS3Qd2] ], [ [P.g, P.YS3d2, P.YS3Qd2, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_813_1065,(1,0,8):C.UVGC_819_1074,(1,0,1):C.UVGC_813_1067,(1,0,7):C.UVGC_819_1075,(1,0,2):C.UVGC_813_1069,(1,0,6):C.UVGC_819_1076,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_812_1059,(0,0,8):C.UVGC_818_1071,(0,0,1):C.UVGC_812_1061,(0,0,7):C.UVGC_818_1072,(0,0,2):C.UVGC_812_1063,(0,0,6):C.UVGC_818_1073})

V_944 = CTVertex(name = 'V_944',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3d2, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3d2, P.YS3Qd3] ], [ [P.g, P.YS3d2, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_813_1065,(1,0,8):C.UVGC_819_1074,(1,0,1):C.UVGC_813_1067,(1,0,7):C.UVGC_819_1075,(1,0,2):C.UVGC_813_1069,(1,0,6):C.UVGC_819_1076,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_812_1059,(0,0,8):C.UVGC_818_1071,(0,0,1):C.UVGC_812_1061,(0,0,7):C.UVGC_818_1072,(0,0,2):C.UVGC_812_1063,(0,0,6):C.UVGC_818_1073})

V_945 = CTVertex(name = 'V_945',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3d2, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3u1] ], [ [P.g, P.YS3d2, P.YS3u1] ], [ [P.g, P.YS3d2, P.YS3u1, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_829_1087,(1,0,8):C.UVGC_921_1125,(1,0,1):C.UVGC_829_1089,(1,0,7):C.UVGC_921_1126,(1,0,2):C.UVGC_829_1091,(1,0,6):C.UVGC_921_1127,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_794_1041,(0,0,8):C.UVGC_794_1042,(0,0,1):C.UVGC_794_1043,(0,0,7):C.UVGC_794_1044,(0,0,2):C.UVGC_828_1085,(0,0,6):C.UVGC_920_1124})

V_946 = CTVertex(name = 'V_946',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3d2, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3u2] ], [ [P.g, P.YS3d2, P.YS3u2] ], [ [P.g, P.YS3d2, P.YS3u2, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_829_1087,(1,0,8):C.UVGC_921_1125,(1,0,1):C.UVGC_829_1089,(1,0,7):C.UVGC_921_1126,(1,0,2):C.UVGC_829_1091,(1,0,6):C.UVGC_921_1127,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_794_1041,(0,0,8):C.UVGC_794_1042,(0,0,1):C.UVGC_794_1043,(0,0,7):C.UVGC_794_1044,(0,0,2):C.UVGC_828_1085,(0,0,6):C.UVGC_920_1124})

V_947 = CTVertex(name = 'V_947',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3d2, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3u3] ], [ [P.g, P.YS3d2, P.YS3u3] ], [ [P.g, P.YS3d2, P.YS3u3, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_829_1087,(1,0,8):C.UVGC_921_1125,(1,0,1):C.UVGC_829_1089,(1,0,7):C.UVGC_921_1126,(1,0,2):C.UVGC_829_1091,(1,0,6):C.UVGC_921_1127,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_794_1041,(0,0,8):C.UVGC_794_1042,(0,0,1):C.UVGC_794_1043,(0,0,7):C.UVGC_794_1044,(0,0,2):C.UVGC_828_1085,(0,0,6):C.UVGC_920_1124})

V_948 = CTVertex(name = 'V_948',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3d2] ], [ [P.a, P.g, P.YS3d1, P.YS3d2] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3d2] ], [ [P.g, P.YS3d1, P.YS3d2] ], [ [P.g, P.YS3d1, P.YS3d2, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3d2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_813_1065,(1,0,8):C.UVGC_813_1066,(1,0,1):C.UVGC_813_1067,(1,0,7):C.UVGC_813_1068,(1,0,2):C.UVGC_813_1069,(1,0,6):C.UVGC_813_1070,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_812_1059,(0,0,8):C.UVGC_812_1060,(0,0,1):C.UVGC_812_1061,(0,0,7):C.UVGC_812_1062,(0,0,2):C.UVGC_812_1063,(0,0,6):C.UVGC_812_1064})

V_949 = CTVertex(name = 'V_949',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2__tilde__, P.YS3d2, P.YS3d2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2] ], [ [P.g] ], [ [P.g, P.YS3d2] ], [ [P.g, P.YS3d2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_326_460,(1,0,3):C.UVGC_326_461,(1,0,0):C.UVGC_794_1041,(1,0,5):C.UVGC_794_1042,(1,0,1):C.UVGC_794_1043,(1,0,4):C.UVGC_794_1044,(0,0,2):C.UVGC_326_460,(0,0,3):C.UVGC_326_461,(0,0,0):C.UVGC_794_1041,(0,0,5):C.UVGC_794_1042,(0,0,1):C.UVGC_794_1043,(0,0,4):C.UVGC_794_1044})

V_950 = CTVertex(name = 'V_950',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3d3, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3d3, P.YS3Qu1] ], [ [P.g, P.YS3d3, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_829_1087,(1,0,8):C.UVGC_861_1096,(1,0,1):C.UVGC_829_1089,(1,0,7):C.UVGC_861_1097,(1,0,2):C.UVGC_829_1091,(1,0,6):C.UVGC_861_1098,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_794_1041,(0,0,8):C.UVGC_860_1093,(0,0,1):C.UVGC_794_1043,(0,0,7):C.UVGC_860_1094,(0,0,2):C.UVGC_828_1085,(0,0,6):C.UVGC_860_1095})

V_951 = CTVertex(name = 'V_951',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3d3, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3d3, P.YS3Qu2] ], [ [P.g, P.YS3d3, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_829_1087,(1,0,8):C.UVGC_861_1096,(1,0,1):C.UVGC_829_1089,(1,0,7):C.UVGC_861_1097,(1,0,2):C.UVGC_829_1091,(1,0,6):C.UVGC_861_1098,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_794_1041,(0,0,8):C.UVGC_860_1093,(0,0,1):C.UVGC_794_1043,(0,0,7):C.UVGC_860_1094,(0,0,2):C.UVGC_828_1085,(0,0,6):C.UVGC_860_1095})

V_952 = CTVertex(name = 'V_952',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3d3, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3d3, P.YS3Qu3] ], [ [P.g, P.YS3d3, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_829_1087,(1,0,8):C.UVGC_861_1096,(1,0,1):C.UVGC_829_1089,(1,0,7):C.UVGC_861_1097,(1,0,2):C.UVGC_829_1091,(1,0,6):C.UVGC_861_1098,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_794_1041,(0,0,8):C.UVGC_860_1093,(0,0,1):C.UVGC_794_1043,(0,0,7):C.UVGC_860_1094,(0,0,2):C.UVGC_828_1085,(0,0,6):C.UVGC_860_1095})

V_953 = CTVertex(name = 'V_953',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qd1] ], [ [P.a, P.g, P.YS3d3, P.YS3Qd1] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qd1] ], [ [P.g, P.YS3d3, P.YS3Qd1] ], [ [P.g, P.YS3d3, P.YS3Qd1, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qd1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_813_1065,(1,0,8):C.UVGC_819_1074,(1,0,1):C.UVGC_813_1067,(1,0,7):C.UVGC_819_1075,(1,0,2):C.UVGC_813_1069,(1,0,6):C.UVGC_819_1076,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_812_1059,(0,0,8):C.UVGC_818_1071,(0,0,1):C.UVGC_812_1061,(0,0,7):C.UVGC_818_1072,(0,0,2):C.UVGC_812_1063,(0,0,6):C.UVGC_818_1073})

V_954 = CTVertex(name = 'V_954',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qd2] ], [ [P.a, P.g, P.YS3d3, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qd2] ], [ [P.g, P.YS3d3, P.YS3Qd2] ], [ [P.g, P.YS3d3, P.YS3Qd2, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_813_1065,(1,0,8):C.UVGC_819_1074,(1,0,1):C.UVGC_813_1067,(1,0,7):C.UVGC_819_1075,(1,0,2):C.UVGC_813_1069,(1,0,6):C.UVGC_819_1076,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_812_1059,(0,0,8):C.UVGC_818_1071,(0,0,1):C.UVGC_812_1061,(0,0,7):C.UVGC_818_1072,(0,0,2):C.UVGC_812_1063,(0,0,6):C.UVGC_818_1073})

V_955 = CTVertex(name = 'V_955',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3d3, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3d3, P.YS3Qd3] ], [ [P.g, P.YS3d3, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_813_1065,(1,0,8):C.UVGC_819_1074,(1,0,1):C.UVGC_813_1067,(1,0,7):C.UVGC_819_1075,(1,0,2):C.UVGC_813_1069,(1,0,6):C.UVGC_819_1076,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_812_1059,(0,0,8):C.UVGC_818_1071,(0,0,1):C.UVGC_812_1061,(0,0,7):C.UVGC_818_1072,(0,0,2):C.UVGC_812_1063,(0,0,6):C.UVGC_818_1073})

V_956 = CTVertex(name = 'V_956',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3d3, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3u1] ], [ [P.g, P.YS3d3, P.YS3u1] ], [ [P.g, P.YS3d3, P.YS3u1, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_829_1087,(1,0,8):C.UVGC_921_1125,(1,0,1):C.UVGC_829_1089,(1,0,7):C.UVGC_921_1126,(1,0,2):C.UVGC_829_1091,(1,0,6):C.UVGC_921_1127,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_794_1041,(0,0,8):C.UVGC_794_1042,(0,0,1):C.UVGC_794_1043,(0,0,7):C.UVGC_794_1044,(0,0,2):C.UVGC_828_1085,(0,0,6):C.UVGC_920_1124})

V_957 = CTVertex(name = 'V_957',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3d3, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3u2] ], [ [P.g, P.YS3d3, P.YS3u2] ], [ [P.g, P.YS3d3, P.YS3u2, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_829_1087,(1,0,8):C.UVGC_921_1125,(1,0,1):C.UVGC_829_1089,(1,0,7):C.UVGC_921_1126,(1,0,2):C.UVGC_829_1091,(1,0,6):C.UVGC_921_1127,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_794_1041,(0,0,8):C.UVGC_794_1042,(0,0,1):C.UVGC_794_1043,(0,0,7):C.UVGC_794_1044,(0,0,2):C.UVGC_828_1085,(0,0,6):C.UVGC_920_1124})

V_958 = CTVertex(name = 'V_958',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3d3, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3u3] ], [ [P.g, P.YS3d3, P.YS3u3] ], [ [P.g, P.YS3d3, P.YS3u3, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_829_1087,(1,0,8):C.UVGC_921_1125,(1,0,1):C.UVGC_829_1089,(1,0,7):C.UVGC_921_1126,(1,0,2):C.UVGC_829_1091,(1,0,6):C.UVGC_921_1127,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_794_1041,(0,0,8):C.UVGC_794_1042,(0,0,1):C.UVGC_794_1043,(0,0,7):C.UVGC_794_1044,(0,0,2):C.UVGC_828_1085,(0,0,6):C.UVGC_920_1124})

V_959 = CTVertex(name = 'V_959',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3d3] ], [ [P.a, P.g, P.YS3d1, P.YS3d3] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3d3] ], [ [P.g, P.YS3d1, P.YS3d3] ], [ [P.g, P.YS3d1, P.YS3d3, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3d3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_813_1065,(1,0,8):C.UVGC_813_1066,(1,0,1):C.UVGC_813_1067,(1,0,7):C.UVGC_813_1068,(1,0,2):C.UVGC_813_1069,(1,0,6):C.UVGC_813_1070,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_812_1059,(0,0,8):C.UVGC_812_1060,(0,0,1):C.UVGC_812_1061,(0,0,7):C.UVGC_812_1062,(0,0,2):C.UVGC_812_1063,(0,0,6):C.UVGC_812_1064})

V_960 = CTVertex(name = 'V_960',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3d3] ], [ [P.a, P.g, P.YS3d2, P.YS3d3] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3d3] ], [ [P.g, P.YS3d2, P.YS3d3] ], [ [P.g, P.YS3d2, P.YS3d3, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3d3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_610_900,(1,0,4):C.UVGC_610_901,(1,0,5):C.UVGC_610_902,(1,0,0):C.UVGC_813_1065,(1,0,8):C.UVGC_813_1066,(1,0,1):C.UVGC_813_1067,(1,0,7):C.UVGC_813_1068,(1,0,2):C.UVGC_813_1069,(1,0,6):C.UVGC_813_1070,(0,0,3):C.UVGC_609_897,(0,0,4):C.UVGC_609_898,(0,0,5):C.UVGC_609_899,(0,0,0):C.UVGC_812_1059,(0,0,8):C.UVGC_812_1060,(0,0,1):C.UVGC_812_1061,(0,0,7):C.UVGC_812_1062,(0,0,2):C.UVGC_812_1063,(0,0,6):C.UVGC_812_1064})

V_961 = CTVertex(name = 'V_961',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3__tilde__, P.YS3d3, P.YS3d3 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3] ], [ [P.g] ], [ [P.g, P.YS3d3] ], [ [P.g, P.YS3d3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_326_460,(1,0,3):C.UVGC_326_461,(1,0,0):C.UVGC_794_1041,(1,0,5):C.UVGC_794_1042,(1,0,1):C.UVGC_794_1043,(1,0,4):C.UVGC_794_1044,(0,0,2):C.UVGC_326_460,(0,0,3):C.UVGC_326_461,(0,0,0):C.UVGC_794_1041,(0,0,5):C.UVGC_794_1042,(0,0,1):C.UVGC_794_1043,(0,0,4):C.UVGC_794_1044})

