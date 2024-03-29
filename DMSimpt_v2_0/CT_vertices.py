# This file was automatically created by FeynRules 2.4.91
# Mathematica version: 13.1.0 for Mac OS X ARM (64-bit) (June 16, 2022)
# Date: Thu 28 Mar 2024 20:48:09


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
               couplings = {(0,0,0):C.R2GC_268_91,(0,0,1):C.R2GC_268_92})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV10, L.VVVV2, L.VVVV3, L.VVVV5 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u], [P.YF3d1], [P.YF3d2], [P.YF3d3], [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3], [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3], [P.YF3u1], [P.YF3u2], [P.YF3u3] ], [ [P.g] ] ],
               couplings = {(0,1,0):C.R2GC_263_86,(0,1,1):C.R2GC_263_87,(2,1,0):C.R2GC_263_86,(2,1,1):C.R2GC_263_87,(5,1,0):C.R2GC_261_82,(5,1,1):C.R2GC_261_83,(1,1,0):C.R2GC_261_82,(1,1,1):C.R2GC_261_83,(7,1,0):C.R2GC_271_97,(7,1,1):C.R2GC_271_98,(4,1,0):C.R2GC_261_82,(4,1,1):C.R2GC_261_83,(3,1,0):C.R2GC_261_82,(3,1,1):C.R2GC_261_83,(8,1,0):C.R2GC_262_84,(8,1,1):C.R2GC_262_85,(6,1,0):C.R2GC_270_95,(6,1,1):C.R2GC_270_96,(11,0,0):C.R2GC_265_89,(11,0,1):C.R2GC_265_90,(10,0,0):C.R2GC_265_89,(10,0,1):C.R2GC_265_90,(9,0,1):C.R2GC_264_88,(0,2,0):C.R2GC_263_86,(0,2,1):C.R2GC_263_87,(2,2,0):C.R2GC_263_86,(2,2,1):C.R2GC_263_87,(7,2,0):C.R2GC_271_97,(7,2,1):C.R2GC_262_85,(5,2,0):C.R2GC_261_82,(5,2,1):C.R2GC_261_83,(1,2,0):C.R2GC_261_82,(1,2,1):C.R2GC_261_83,(4,2,0):C.R2GC_261_82,(4,2,1):C.R2GC_261_83,(3,2,0):C.R2GC_261_82,(3,2,1):C.R2GC_261_83,(8,2,0):C.R2GC_262_84,(8,2,1):C.R2GC_271_98,(6,2,0):C.R2GC_276_99,(6,2,1):C.R2GC_276_100,(0,3,0):C.R2GC_263_86,(0,3,1):C.R2GC_263_87,(2,3,0):C.R2GC_263_86,(2,3,1):C.R2GC_263_87,(7,3,0):C.R2GC_269_93,(7,3,1):C.R2GC_269_94,(5,3,0):C.R2GC_261_82,(5,3,1):C.R2GC_261_83,(1,3,0):C.R2GC_261_82,(1,3,1):C.R2GC_261_83,(4,3,0):C.R2GC_261_82,(4,3,1):C.R2GC_261_83,(3,3,0):C.R2GC_261_82,(3,3,1):C.R2GC_261_83,(8,3,0):C.R2GC_262_84,(8,3,1):C.R2GC_269_94,(6,3,0):C.R2GC_270_95})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.YF3d1__tilde__, P.YF3d1, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.YF3d1] ] ],
               couplings = {(0,0,0):C.R2GC_280_102})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.YF3d2__tilde__, P.YF3d2, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.YF3d2] ] ],
               couplings = {(0,0,0):C.R2GC_280_102})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.YF3d3__tilde__, P.YF3d3, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.YF3d3] ] ],
               couplings = {(0,0,0):C.R2GC_280_102})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.YF3Qd1__tilde__, P.YF3Qd1, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.YF3Qd1] ] ],
               couplings = {(0,0,0):C.R2GC_280_102})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.YF3Qd2__tilde__, P.YF3Qd2, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.YF3Qd2] ] ],
               couplings = {(0,0,0):C.R2GC_280_102})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.YF3Qd3__tilde__, P.YF3Qd3, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.YF3Qd3] ] ],
               couplings = {(0,0,0):C.R2GC_280_102})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.YF3Qu1__tilde__, P.YF3Qu1, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.YF3Qu1] ] ],
               couplings = {(0,0,0):C.R2GC_287_106})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.YF3Qu2__tilde__, P.YF3Qu2, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qu2] ] ],
                couplings = {(0,0,0):C.R2GC_287_106})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.YF3Qu3__tilde__, P.YF3Qu3, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qu3] ] ],
                couplings = {(0,0,0):C.R2GC_287_106})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.YF3u1__tilde__, P.YF3u1, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3u1] ] ],
                couplings = {(0,0,0):C.R2GC_287_106})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.YF3u2__tilde__, P.YF3u2, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3u2] ] ],
                couplings = {(0,0,0):C.R2GC_287_106})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.YF3u3__tilde__, P.YF3u3, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3u3] ] ],
                couplings = {(0,0,0):C.R2GC_287_106})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.u__tilde__, P.YF3Qu1, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.u, P.YF3Qu1] ] ],
                couplings = {(0,0,0):C.R2GC_590_186})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.u__tilde__, P.YF3Qu1, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.u, P.YF3Qu1] ] ],
                couplings = {(0,0,0):C.R2GC_590_186})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.d__tilde__, P.YF3Qd1, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.YF3Qd1] ] ],
                couplings = {(0,0,0):C.R2GC_590_186})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.d__tilde__, P.YF3Qd1, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.YF3Qd1] ] ],
                couplings = {(0,0,0):C.R2GC_590_186})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.c__tilde__, P.YF3Qu2, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.c, P.g, P.YF3Qu2] ] ],
                couplings = {(0,0,0):C.R2GC_582_178})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.c__tilde__, P.YF3Qu2, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.c, P.g, P.YF3Qu2] ] ],
                couplings = {(0,0,0):C.R2GC_582_178})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.s__tilde__, P.YF3Qd2, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s, P.YF3Qd2] ] ],
                couplings = {(0,0,0):C.R2GC_582_178})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.s__tilde__, P.YF3Qd2, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s, P.YF3Qd2] ] ],
                couplings = {(0,0,0):C.R2GC_582_178})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.t__tilde__, P.YF3Qu3, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.t, P.YF3Qu3] ] ],
                couplings = {(0,0,0):C.R2GC_577_173})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.t__tilde__, P.YF3Qu3, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.t, P.YF3Qu3] ] ],
                couplings = {(0,0,0):C.R2GC_577_173})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.b__tilde__, P.YF3Qd3, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g, P.YF3Qd3] ] ],
                couplings = {(0,0,0):C.R2GC_577_173})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.b__tilde__, P.YF3Qd3, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g, P.YF3Qd3] ] ],
                couplings = {(0,0,0):C.R2GC_577_173})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.YF3d1__tilde__, P.d, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.YF3d1] ] ],
                couplings = {(0,0,0):C.R2GC_588_184})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.YF3d2__tilde__, P.s, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s, P.YF3d2] ] ],
                couplings = {(0,0,0):C.R2GC_752_203})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.YF3d3__tilde__, P.b, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g, P.YF3d3] ] ],
                couplings = {(0,0,0):C.R2GC_575_171})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.YF3d1__tilde__, P.d, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.YF3d1] ] ],
                couplings = {(0,0,0):C.R2GC_588_184})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.YF3d2__tilde__, P.s, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s, P.YF3d2] ] ],
                couplings = {(0,0,0):C.R2GC_752_203})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.YF3d3__tilde__, P.b, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g, P.YF3d3] ] ],
                couplings = {(0,0,0):C.R2GC_575_171})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.YF3u1__tilde__, P.u, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.u, P.YF3u1] ] ],
                couplings = {(0,0,0):C.R2GC_770_211})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.YF3u2__tilde__, P.c, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.c, P.g, P.YF3u2] ] ],
                couplings = {(0,0,0):C.R2GC_584_180})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.YF3u3__tilde__, P.t, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.t, P.YF3u3] ] ],
                couplings = {(0,0,0):C.R2GC_763_208})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.YF3u1__tilde__, P.u, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.u, P.YF3u1] ] ],
                couplings = {(0,0,0):C.R2GC_770_211})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.YF3u2__tilde__, P.c, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.c, P.g, P.YF3u2] ] ],
                couplings = {(0,0,0):C.R2GC_584_180})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.YF3u3__tilde__, P.t, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.t, P.YF3u3] ] ],
                couplings = {(0,0,0):C.R2GC_763_208})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_756_204})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_486_155})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_485_154})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.d__tilde__, P.YF3d1, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.d, P.g, P.YF3d1] ] ],
                couplings = {(0,0,0):C.R2GC_588_184})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.s__tilde__, P.YF3d2, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.s, P.YF3d2] ] ],
                couplings = {(0,0,0):C.R2GC_752_203})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.b__tilde__, P.YF3d3, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.b, P.g, P.YF3d3] ] ],
                couplings = {(0,0,0):C.R2GC_575_171})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.d__tilde__, P.YF3d1, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.d, P.g, P.YF3d1] ] ],
                couplings = {(0,0,0):C.R2GC_588_184})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.s__tilde__, P.YF3d2, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.s, P.YF3d2] ] ],
                couplings = {(0,0,0):C.R2GC_752_203})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.b__tilde__, P.YF3d3, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.b, P.g, P.YF3d3] ] ],
                couplings = {(0,0,0):C.R2GC_575_171})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.u__tilde__, P.YF3u1, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.u, P.YF3u1] ] ],
                couplings = {(0,0,0):C.R2GC_770_211})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.c__tilde__, P.YF3u2, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.c, P.g, P.YF3u2] ] ],
                couplings = {(0,0,0):C.R2GC_584_180})

V_50 = CTVertex(name = 'V_50',
                type = 'R2',
                particles = [ P.t__tilde__, P.YF3u3, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.t, P.YF3u3] ] ],
                couplings = {(0,0,0):C.R2GC_763_208})

V_51 = CTVertex(name = 'V_51',
                type = 'R2',
                particles = [ P.u__tilde__, P.YF3u1, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.u, P.YF3u1] ] ],
                couplings = {(0,0,0):C.R2GC_770_211})

V_52 = CTVertex(name = 'V_52',
                type = 'R2',
                particles = [ P.c__tilde__, P.YF3u2, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.c, P.g, P.YF3u2] ] ],
                couplings = {(0,0,0):C.R2GC_584_180})

V_53 = CTVertex(name = 'V_53',
                type = 'R2',
                particles = [ P.t__tilde__, P.YF3u3, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.t, P.YF3u3] ] ],
                couplings = {(0,0,0):C.R2GC_763_208})

V_54 = CTVertex(name = 'V_54',
                type = 'R2',
                particles = [ P.YF3Qu1__tilde__, P.u, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.u, P.YF3Qu1] ] ],
                couplings = {(0,0,0):C.R2GC_590_186})

V_55 = CTVertex(name = 'V_55',
                type = 'R2',
                particles = [ P.YF3Qu1__tilde__, P.u, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.u, P.YF3Qu1] ] ],
                couplings = {(0,0,0):C.R2GC_590_186})

V_56 = CTVertex(name = 'V_56',
                type = 'R2',
                particles = [ P.YF3Qd1__tilde__, P.d, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.d, P.g, P.YF3Qd1] ] ],
                couplings = {(0,0,0):C.R2GC_590_186})

V_57 = CTVertex(name = 'V_57',
                type = 'R2',
                particles = [ P.YF3Qd1__tilde__, P.d, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.d, P.g, P.YF3Qd1] ] ],
                couplings = {(0,0,0):C.R2GC_590_186})

V_58 = CTVertex(name = 'V_58',
                type = 'R2',
                particles = [ P.YF3Qu2__tilde__, P.c, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.c, P.g, P.YF3Qu2] ] ],
                couplings = {(0,0,0):C.R2GC_582_178})

V_59 = CTVertex(name = 'V_59',
                type = 'R2',
                particles = [ P.YF3Qu2__tilde__, P.c, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.c, P.g, P.YF3Qu2] ] ],
                couplings = {(0,0,0):C.R2GC_582_178})

V_60 = CTVertex(name = 'V_60',
                type = 'R2',
                particles = [ P.YF3Qd2__tilde__, P.s, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.s, P.YF3Qd2] ] ],
                couplings = {(0,0,0):C.R2GC_582_178})

V_61 = CTVertex(name = 'V_61',
                type = 'R2',
                particles = [ P.YF3Qd2__tilde__, P.s, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.s, P.YF3Qd2] ] ],
                couplings = {(0,0,0):C.R2GC_582_178})

V_62 = CTVertex(name = 'V_62',
                type = 'R2',
                particles = [ P.YF3Qu3__tilde__, P.t, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.t, P.YF3Qu3] ] ],
                couplings = {(0,0,0):C.R2GC_577_173})

V_63 = CTVertex(name = 'V_63',
                type = 'R2',
                particles = [ P.YF3Qu3__tilde__, P.t, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.t, P.YF3Qu3] ] ],
                couplings = {(0,0,0):C.R2GC_577_173})

V_64 = CTVertex(name = 'V_64',
                type = 'R2',
                particles = [ P.YF3Qd3__tilde__, P.b, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.b, P.g, P.YF3Qd3] ] ],
                couplings = {(0,0,0):C.R2GC_577_173})

V_65 = CTVertex(name = 'V_65',
                type = 'R2',
                particles = [ P.YF3Qd3__tilde__, P.b, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.b, P.g, P.YF3Qd3] ] ],
                couplings = {(0,0,0):C.R2GC_577_173})

V_66 = CTVertex(name = 'V_66',
                type = 'R2',
                particles = [ P.YF3Qd1__tilde__, P.YF3Qd1, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd1] ] ],
                couplings = {(0,0,0):C.R2GC_281_103})

V_67 = CTVertex(name = 'V_67',
                type = 'R2',
                particles = [ P.YF3Qd2__tilde__, P.YF3Qd2, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd2] ] ],
                couplings = {(0,0,0):C.R2GC_281_103})

V_68 = CTVertex(name = 'V_68',
                type = 'R2',
                particles = [ P.YF3Qd3__tilde__, P.YF3Qd3, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd3] ] ],
                couplings = {(0,0,0):C.R2GC_281_103})

V_69 = CTVertex(name = 'V_69',
                type = 'R2',
                particles = [ P.YF3Qu1__tilde__, P.YF3Qu1, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qu1] ] ],
                couplings = {(0,0,0):C.R2GC_281_103})

V_70 = CTVertex(name = 'V_70',
                type = 'R2',
                particles = [ P.YF3Qu2__tilde__, P.YF3Qu2, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qu2] ] ],
                couplings = {(0,0,0):C.R2GC_281_103})

V_71 = CTVertex(name = 'V_71',
                type = 'R2',
                particles = [ P.YF3Qu3__tilde__, P.YF3Qu3, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qu3] ] ],
                couplings = {(0,0,0):C.R2GC_281_103})

V_72 = CTVertex(name = 'V_72',
                type = 'R2',
                particles = [ P.YF3u1__tilde__, P.YF3u1, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3u1] ] ],
                couplings = {(0,0,0):C.R2GC_281_103})

V_73 = CTVertex(name = 'V_73',
                type = 'R2',
                particles = [ P.YF3u2__tilde__, P.YF3u2, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3u2] ] ],
                couplings = {(0,0,0):C.R2GC_281_103})

V_74 = CTVertex(name = 'V_74',
                type = 'R2',
                particles = [ P.YF3u3__tilde__, P.YF3u3, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3u3] ] ],
                couplings = {(0,0,0):C.R2GC_281_103})

V_75 = CTVertex(name = 'V_75',
                type = 'R2',
                particles = [ P.YF3d1__tilde__, P.YF3d1, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3d1] ] ],
                couplings = {(0,0,0):C.R2GC_281_103})

V_76 = CTVertex(name = 'V_76',
                type = 'R2',
                particles = [ P.YF3d2__tilde__, P.YF3d2, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3d2] ] ],
                couplings = {(0,0,0):C.R2GC_281_103})

V_77 = CTVertex(name = 'V_77',
                type = 'R2',
                particles = [ P.YF3d3__tilde__, P.YF3d3, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3d3] ] ],
                couplings = {(0,0,0):C.R2GC_281_103})

V_78 = CTVertex(name = 'V_78',
                type = 'R2',
                particles = [ P.YF3Qd1__tilde__, P.YF3Qu1, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd1, P.YF3Qu1] ] ],
                couplings = {(0,0,0):C.R2GC_580_176})

V_79 = CTVertex(name = 'V_79',
                type = 'R2',
                particles = [ P.YF3Qd2__tilde__, P.YF3Qu2, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd2, P.YF3Qu2] ] ],
                couplings = {(0,0,0):C.R2GC_580_176})

V_80 = CTVertex(name = 'V_80',
                type = 'R2',
                particles = [ P.YF3Qd3__tilde__, P.YF3Qu3, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd3, P.YF3Qu3] ] ],
                couplings = {(0,0,0):C.R2GC_580_176})

V_81 = CTVertex(name = 'V_81',
                type = 'R2',
                particles = [ P.YF3Qu1__tilde__, P.YF3Qd1, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd1, P.YF3Qu1] ] ],
                couplings = {(0,0,0):C.R2GC_580_176})

V_82 = CTVertex(name = 'V_82',
                type = 'R2',
                particles = [ P.YF3Qu2__tilde__, P.YF3Qd2, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd2, P.YF3Qu2] ] ],
                couplings = {(0,0,0):C.R2GC_580_176})

V_83 = CTVertex(name = 'V_83',
                type = 'R2',
                particles = [ P.YF3Qu3__tilde__, P.YF3Qd3, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd3, P.YF3Qu3] ] ],
                couplings = {(0,0,0):C.R2GC_580_176})

V_84 = CTVertex(name = 'V_84',
                type = 'R2',
                particles = [ P.a, P.YS3d1__tilde__, P.YS3d1 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.YS3d1] ] ],
                couplings = {(0,0,0):C.R2GC_299_110})

V_85 = CTVertex(name = 'V_85',
                type = 'R2',
                particles = [ P.Xd__tilde__, P.d, P.YS3d1__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.YS3d1] ] ],
                couplings = {(0,0,0):C.R2GC_585_181})

V_86 = CTVertex(name = 'V_86',
                type = 'R2',
                particles = [ P.Xm, P.d, P.YS3d1__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.YS3d1] ] ],
                couplings = {(0,0,0):C.R2GC_585_181})

V_87 = CTVertex(name = 'V_87',
                type = 'R2',
                particles = [ P.g, P.YS3d1__tilde__, P.YS3d1 ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.YS3d1] ] ],
                couplings = {(0,0,0):C.R2GC_301_112})

V_88 = CTVertex(name = 'V_88',
                type = 'R2',
                particles = [ P.d__tilde__, P.Xd, P.YS3d1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.d, P.g, P.YS3d1] ] ],
                couplings = {(0,0,0):C.R2GC_585_181})

V_89 = CTVertex(name = 'V_89',
                type = 'R2',
                particles = [ P.d__tilde__, P.Xm, P.YS3d1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.d, P.g, P.YS3d1] ] ],
                couplings = {(0,0,0):C.R2GC_585_181})

V_90 = CTVertex(name = 'V_90',
                type = 'R2',
                particles = [ P.a, P.a, P.YS3d1__tilde__, P.YS3d1 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.YS3d1] ] ],
                couplings = {(0,0,0):C.R2GC_300_111})

V_91 = CTVertex(name = 'V_91',
                type = 'R2',
                particles = [ P.a, P.g, P.YS3d1__tilde__, P.YS3d1 ],
                color = [ 'T(2,4,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.YS3d1] ] ],
                couplings = {(0,0,0):C.R2GC_302_113})

V_92 = CTVertex(name = 'V_92',
                type = 'R2',
                particles = [ P.g, P.g, P.YS3d1__tilde__, P.YS3d1 ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g] ], [ [P.g, P.YS3d1] ] ],
                couplings = {(2,0,0):C.R2GC_305_117,(2,0,1):C.R2GC_305_118,(1,0,0):C.R2GC_305_117,(1,0,1):C.R2GC_305_118,(0,0,0):C.R2GC_265_90,(0,0,1):C.R2GC_304_116})

V_93 = CTVertex(name = 'V_93',
                type = 'R2',
                particles = [ P.a, P.YS3d2__tilde__, P.YS3d2 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.YS3d2] ] ],
                couplings = {(0,0,0):C.R2GC_299_110})

V_94 = CTVertex(name = 'V_94',
                type = 'R2',
                particles = [ P.Xd__tilde__, P.s, P.YS3d2__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s, P.YS3d2] ] ],
                couplings = {(0,0,0):C.R2GC_749_201})

V_95 = CTVertex(name = 'V_95',
                type = 'R2',
                particles = [ P.Xm, P.s, P.YS3d2__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s, P.YS3d2] ] ],
                couplings = {(0,0,0):C.R2GC_749_201})

V_96 = CTVertex(name = 'V_96',
                type = 'R2',
                particles = [ P.g, P.YS3d2__tilde__, P.YS3d2 ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.YS3d2] ] ],
                couplings = {(0,0,0):C.R2GC_301_112})

V_97 = CTVertex(name = 'V_97',
                type = 'R2',
                particles = [ P.s__tilde__, P.Xd, P.YS3d2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.s, P.YS3d2] ] ],
                couplings = {(0,0,0):C.R2GC_749_201})

V_98 = CTVertex(name = 'V_98',
                type = 'R2',
                particles = [ P.s__tilde__, P.Xm, P.YS3d2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.s, P.YS3d2] ] ],
                couplings = {(0,0,0):C.R2GC_749_201})

V_99 = CTVertex(name = 'V_99',
                type = 'R2',
                particles = [ P.a, P.a, P.YS3d2__tilde__, P.YS3d2 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.YS3d2] ] ],
                couplings = {(0,0,0):C.R2GC_300_111})

V_100 = CTVertex(name = 'V_100',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_302_113})

V_101 = CTVertex(name = 'V_101',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3d2] ] ],
                 couplings = {(2,0,0):C.R2GC_305_117,(2,0,1):C.R2GC_305_118,(1,0,0):C.R2GC_305_117,(1,0,1):C.R2GC_305_118,(0,0,0):C.R2GC_265_90,(0,0,1):C.R2GC_304_116})

V_102 = CTVertex(name = 'V_102',
                 type = 'R2',
                 particles = [ P.a, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_299_110})

V_103 = CTVertex(name = 'V_103',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.b, P.YS3d3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_572_168})

V_104 = CTVertex(name = 'V_104',
                 type = 'R2',
                 particles = [ P.Xm, P.b, P.YS3d3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_572_168})

V_105 = CTVertex(name = 'V_105',
                 type = 'R2',
                 particles = [ P.g, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_301_112})

V_106 = CTVertex(name = 'V_106',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.Xd, P.YS3d3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_572_168})

V_107 = CTVertex(name = 'V_107',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.Xm, P.YS3d3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_572_168})

V_108 = CTVertex(name = 'V_108',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_300_111})

V_109 = CTVertex(name = 'V_109',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_302_113})

V_110 = CTVertex(name = 'V_110',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3d3] ] ],
                 couplings = {(2,0,0):C.R2GC_305_117,(2,0,1):C.R2GC_305_118,(1,0,0):C.R2GC_305_117,(1,0,1):C.R2GC_305_118,(0,0,0):C.R2GC_265_90,(0,0,1):C.R2GC_304_116})

V_111 = CTVertex(name = 'V_111',
                 type = 'R2',
                 particles = [ P.a, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_299_110})

V_112 = CTVertex(name = 'V_112',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.d, P.YS3Qd1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_586_182})

V_113 = CTVertex(name = 'V_113',
                 type = 'R2',
                 particles = [ P.Xm, P.d, P.YS3Qd1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_586_182})

V_114 = CTVertex(name = 'V_114',
                 type = 'R2',
                 particles = [ P.W__minus__, P.YS3Qd1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_651_197})

V_115 = CTVertex(name = 'V_115',
                 type = 'R2',
                 particles = [ P.g, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_301_112})

V_116 = CTVertex(name = 'V_116',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.Xd, P.YS3Qd1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_586_182})

V_117 = CTVertex(name = 'V_117',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.Xm, P.YS3Qd1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_586_182})

V_118 = CTVertex(name = 'V_118',
                 type = 'R2',
                 particles = [ P.W__plus__, P.YS3Qd1, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_650_196,(0,1,0):C.R2GC_651_197})

V_119 = CTVertex(name = 'V_119',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_300_111})

V_120 = CTVertex(name = 'V_120',
                 type = 'R2',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_648_194,(0,0,1):C.R2GC_648_195})

V_121 = CTVertex(name = 'V_121',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_302_113})

V_122 = CTVertex(name = 'V_122',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(2,0,0):C.R2GC_305_117,(2,0,1):C.R2GC_305_118,(1,0,0):C.R2GC_305_117,(1,0,1):C.R2GC_305_118,(0,0,0):C.R2GC_265_90,(0,0,1):C.R2GC_304_116})

V_123 = CTVertex(name = 'V_123',
                 type = 'R2',
                 particles = [ P.a, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_299_110,(0,1,0):C.R2GC_351_131})

V_124 = CTVertex(name = 'V_124',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.s, P.YS3Qd2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_578_174})

V_125 = CTVertex(name = 'V_125',
                 type = 'R2',
                 particles = [ P.Xm, P.s, P.YS3Qd2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_578_174})

V_126 = CTVertex(name = 'V_126',
                 type = 'R2',
                 particles = [ P.W__minus__, P.YS3Qd2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_651_197,(0,1,0):C.R2GC_650_196})

V_127 = CTVertex(name = 'V_127',
                 type = 'R2',
                 particles = [ P.g, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_301_112,(0,1,0):C.R2GC_354_132})

V_128 = CTVertex(name = 'V_128',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.Xd, P.YS3Qd2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_578_174})

V_129 = CTVertex(name = 'V_129',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.Xm, P.YS3Qd2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_578_174})

V_130 = CTVertex(name = 'V_130',
                 type = 'R2',
                 particles = [ P.W__plus__, P.YS3Qd2, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_650_196,(0,1,0):C.R2GC_651_197})

V_131 = CTVertex(name = 'V_131',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_300_111})

V_132 = CTVertex(name = 'V_132',
                 type = 'R2',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_648_194,(0,0,1):C.R2GC_648_195})

V_133 = CTVertex(name = 'V_133',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_302_113})

V_134 = CTVertex(name = 'V_134',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(2,0,0):C.R2GC_305_117,(2,0,1):C.R2GC_305_118,(1,0,0):C.R2GC_305_117,(1,0,1):C.R2GC_305_118,(0,0,0):C.R2GC_265_90,(0,0,1):C.R2GC_304_116})

V_135 = CTVertex(name = 'V_135',
                 type = 'R2',
                 particles = [ P.a, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_299_110,(0,1,0):C.R2GC_351_131})

V_136 = CTVertex(name = 'V_136',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.b, P.YS3Qd3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_573_169})

V_137 = CTVertex(name = 'V_137',
                 type = 'R2',
                 particles = [ P.Xm, P.b, P.YS3Qd3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_573_169})

V_138 = CTVertex(name = 'V_138',
                 type = 'R2',
                 particles = [ P.W__minus__, P.YS3Qd3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_651_197,(0,1,0):C.R2GC_650_196})

V_139 = CTVertex(name = 'V_139',
                 type = 'R2',
                 particles = [ P.g, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_301_112,(0,1,0):C.R2GC_354_132})

V_140 = CTVertex(name = 'V_140',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.Xd, P.YS3Qd3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_573_169})

V_141 = CTVertex(name = 'V_141',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.Xm, P.YS3Qd3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_573_169})

V_142 = CTVertex(name = 'V_142',
                 type = 'R2',
                 particles = [ P.W__plus__, P.YS3Qd3, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_650_196,(0,1,0):C.R2GC_651_197})

V_143 = CTVertex(name = 'V_143',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_300_111})

V_144 = CTVertex(name = 'V_144',
                 type = 'R2',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_648_194,(0,0,1):C.R2GC_648_195})

V_145 = CTVertex(name = 'V_145',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_302_113})

V_146 = CTVertex(name = 'V_146',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(2,0,0):C.R2GC_305_117,(2,0,1):C.R2GC_305_118,(1,0,0):C.R2GC_305_117,(1,0,1):C.R2GC_305_118,(0,0,0):C.R2GC_265_90,(0,0,1):C.R2GC_304_116})

V_147 = CTVertex(name = 'V_147',
                 type = 'R2',
                 particles = [ P.a, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_381_135,(0,1,0):C.R2GC_382_136})

V_148 = CTVertex(name = 'V_148',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.u, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_586_182})

V_149 = CTVertex(name = 'V_149',
                 type = 'R2',
                 particles = [ P.Xm, P.u, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_586_182})

V_150 = CTVertex(name = 'V_150',
                 type = 'R2',
                 particles = [ P.a, P.W__plus__, P.YS3Qd1, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_653_198})

V_151 = CTVertex(name = 'V_151',
                 type = 'R2',
                 particles = [ P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu1__tilde__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_654_199,(0,0,1):C.R2GC_654_200})

V_152 = CTVertex(name = 'V_152',
                 type = 'R2',
                 particles = [ P.g, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_301_112,(0,1,0):C.R2GC_354_132})

V_153 = CTVertex(name = 'V_153',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.Xd, P.YS3Qu1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_586_182})

V_154 = CTVertex(name = 'V_154',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.Xm, P.YS3Qu1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_586_182})

V_155 = CTVertex(name = 'V_155',
                 type = 'R2',
                 particles = [ P.a, P.W__minus__, P.YS3Qd1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_653_198})

V_156 = CTVertex(name = 'V_156',
                 type = 'R2',
                 particles = [ P.g, P.W__minus__, P.YS3Qd1__tilde__, P.YS3Qu1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_654_199,(0,0,1):C.R2GC_654_200})

V_157 = CTVertex(name = 'V_157',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_383_137})

V_158 = CTVertex(name = 'V_158',
                 type = 'R2',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,1):C.R2GC_648_194,(0,0,0):C.R2GC_648_195})

V_159 = CTVertex(name = 'V_159',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_386_138})

V_160 = CTVertex(name = 'V_160',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(2,0,0):C.R2GC_305_117,(2,0,1):C.R2GC_305_118,(1,0,0):C.R2GC_305_117,(1,0,1):C.R2GC_305_118,(0,0,0):C.R2GC_265_90,(0,0,1):C.R2GC_304_116})

V_161 = CTVertex(name = 'V_161',
                 type = 'R2',
                 particles = [ P.a, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_381_135,(0,1,0):C.R2GC_382_136})

V_162 = CTVertex(name = 'V_162',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.c, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_578_174})

V_163 = CTVertex(name = 'V_163',
                 type = 'R2',
                 particles = [ P.Xm, P.c, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_578_174})

V_164 = CTVertex(name = 'V_164',
                 type = 'R2',
                 particles = [ P.a, P.W__plus__, P.YS3Qd2, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_653_198})

V_165 = CTVertex(name = 'V_165',
                 type = 'R2',
                 particles = [ P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu2__tilde__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_654_199,(0,0,1):C.R2GC_654_200})

V_166 = CTVertex(name = 'V_166',
                 type = 'R2',
                 particles = [ P.g, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_301_112,(0,1,0):C.R2GC_354_132})

V_167 = CTVertex(name = 'V_167',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.Xd, P.YS3Qu2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_578_174})

V_168 = CTVertex(name = 'V_168',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.Xm, P.YS3Qu2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_578_174})

V_169 = CTVertex(name = 'V_169',
                 type = 'R2',
                 particles = [ P.a, P.W__minus__, P.YS3Qd2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_653_198})

V_170 = CTVertex(name = 'V_170',
                 type = 'R2',
                 particles = [ P.g, P.W__minus__, P.YS3Qd2__tilde__, P.YS3Qu2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_654_199,(0,0,1):C.R2GC_654_200})

V_171 = CTVertex(name = 'V_171',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_383_137})

V_172 = CTVertex(name = 'V_172',
                 type = 'R2',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,1):C.R2GC_648_194,(0,0,0):C.R2GC_648_195})

V_173 = CTVertex(name = 'V_173',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_386_138})

V_174 = CTVertex(name = 'V_174',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(2,0,0):C.R2GC_305_117,(2,0,1):C.R2GC_305_118,(1,0,0):C.R2GC_305_117,(1,0,1):C.R2GC_305_118,(0,0,0):C.R2GC_265_90,(0,0,1):C.R2GC_304_116})

V_175 = CTVertex(name = 'V_175',
                 type = 'R2',
                 particles = [ P.a, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_381_135,(0,1,0):C.R2GC_382_136})

V_176 = CTVertex(name = 'V_176',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.t, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_573_169})

V_177 = CTVertex(name = 'V_177',
                 type = 'R2',
                 particles = [ P.Xm, P.t, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_573_169})

V_178 = CTVertex(name = 'V_178',
                 type = 'R2',
                 particles = [ P.a, P.W__plus__, P.YS3Qd3, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_653_198})

V_179 = CTVertex(name = 'V_179',
                 type = 'R2',
                 particles = [ P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu3__tilde__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_654_199,(0,0,1):C.R2GC_654_200})

V_180 = CTVertex(name = 'V_180',
                 type = 'R2',
                 particles = [ P.g, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_301_112,(0,1,0):C.R2GC_354_132})

V_181 = CTVertex(name = 'V_181',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.Xd, P.YS3Qu3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_573_169})

V_182 = CTVertex(name = 'V_182',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.Xm, P.YS3Qu3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_573_169})

V_183 = CTVertex(name = 'V_183',
                 type = 'R2',
                 particles = [ P.a, P.W__minus__, P.YS3Qd3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_653_198})

V_184 = CTVertex(name = 'V_184',
                 type = 'R2',
                 particles = [ P.g, P.W__minus__, P.YS3Qd3__tilde__, P.YS3Qu3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_654_199,(0,0,1):C.R2GC_654_200})

V_185 = CTVertex(name = 'V_185',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_383_137})

V_186 = CTVertex(name = 'V_186',
                 type = 'R2',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,1):C.R2GC_648_194,(0,0,0):C.R2GC_648_195})

V_187 = CTVertex(name = 'V_187',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_386_138})

V_188 = CTVertex(name = 'V_188',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(2,0,0):C.R2GC_305_117,(2,0,1):C.R2GC_305_118,(1,0,0):C.R2GC_305_117,(1,0,1):C.R2GC_305_118,(0,0,0):C.R2GC_265_90,(0,0,1):C.R2GC_304_116})

V_189 = CTVertex(name = 'V_189',
                 type = 'R2',
                 particles = [ P.a, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_381_135,(0,1,0):C.R2GC_382_136})

V_190 = CTVertex(name = 'V_190',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.u, P.YS3u1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_766_209})

V_191 = CTVertex(name = 'V_191',
                 type = 'R2',
                 particles = [ P.Xm, P.u, P.YS3u1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_766_209})

V_192 = CTVertex(name = 'V_192',
                 type = 'R2',
                 particles = [ P.g, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_301_112,(0,1,0):C.R2GC_354_132})

V_193 = CTVertex(name = 'V_193',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.Xd, P.YS3u1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_766_209})

V_194 = CTVertex(name = 'V_194',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.Xm, P.YS3u1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_766_209})

V_195 = CTVertex(name = 'V_195',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_383_137})

V_196 = CTVertex(name = 'V_196',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_386_138})

V_197 = CTVertex(name = 'V_197',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3u1] ] ],
                 couplings = {(2,0,0):C.R2GC_305_117,(2,0,1):C.R2GC_305_118,(1,0,0):C.R2GC_305_117,(1,0,1):C.R2GC_305_118,(0,0,0):C.R2GC_265_90,(0,0,1):C.R2GC_304_116})

V_198 = CTVertex(name = 'V_198',
                 type = 'R2',
                 particles = [ P.a, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_381_135,(0,1,0):C.R2GC_382_136})

V_199 = CTVertex(name = 'V_199',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.c, P.YS3u2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_579_175})

V_200 = CTVertex(name = 'V_200',
                 type = 'R2',
                 particles = [ P.Xm, P.c, P.YS3u2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_579_175})

V_201 = CTVertex(name = 'V_201',
                 type = 'R2',
                 particles = [ P.g, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_301_112,(0,1,0):C.R2GC_354_132})

V_202 = CTVertex(name = 'V_202',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.Xd, P.YS3u2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_579_175})

V_203 = CTVertex(name = 'V_203',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.Xm, P.YS3u2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_579_175})

V_204 = CTVertex(name = 'V_204',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_383_137})

V_205 = CTVertex(name = 'V_205',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_386_138})

V_206 = CTVertex(name = 'V_206',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3u2] ] ],
                 couplings = {(2,0,0):C.R2GC_305_117,(2,0,1):C.R2GC_305_118,(1,0,0):C.R2GC_305_117,(1,0,1):C.R2GC_305_118,(0,0,0):C.R2GC_265_90,(0,0,1):C.R2GC_304_116})

V_207 = CTVertex(name = 'V_207',
                 type = 'R2',
                 particles = [ P.a, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_381_135,(0,1,0):C.R2GC_382_136})

V_208 = CTVertex(name = 'V_208',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.t, P.YS3u3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_759_206})

V_209 = CTVertex(name = 'V_209',
                 type = 'R2',
                 particles = [ P.Xm, P.t, P.YS3u3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_759_206})

V_210 = CTVertex(name = 'V_210',
                 type = 'R2',
                 particles = [ P.g, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_301_112,(0,1,0):C.R2GC_354_132})

V_211 = CTVertex(name = 'V_211',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.Xd, P.YS3u3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_759_206})

V_212 = CTVertex(name = 'V_212',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.Xm, P.YS3u3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_759_206})

V_213 = CTVertex(name = 'V_213',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_383_137})

V_214 = CTVertex(name = 'V_214',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_386_138})

V_215 = CTVertex(name = 'V_215',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3u3] ] ],
                 couplings = {(2,0,0):C.R2GC_305_117,(2,0,1):C.R2GC_305_118,(1,0,0):C.R2GC_305_117,(1,0,1):C.R2GC_305_118,(0,0,0):C.R2GC_265_90,(0,0,1):C.R2GC_304_116})

V_216 = CTVertex(name = 'V_216',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_757_205})

V_217 = CTVertex(name = 'V_217',
                 type = 'R2',
                 particles = [ P.YF3Qd1__tilde__, P.YF3Qd1, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_282_104})

V_218 = CTVertex(name = 'V_218',
                 type = 'R2',
                 particles = [ P.YF3Qd2__tilde__, P.YF3Qd2, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_282_104})

V_219 = CTVertex(name = 'V_219',
                 type = 'R2',
                 particles = [ P.YF3Qd3__tilde__, P.YF3Qd3, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_282_104})

V_220 = CTVertex(name = 'V_220',
                 type = 'R2',
                 particles = [ P.YF3Qu1__tilde__, P.YF3Qu1, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_289_107})

V_221 = CTVertex(name = 'V_221',
                 type = 'R2',
                 particles = [ P.YF3Qu2__tilde__, P.YF3Qu2, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_289_107})

V_222 = CTVertex(name = 'V_222',
                 type = 'R2',
                 particles = [ P.YF3Qu3__tilde__, P.YF3Qu3, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_289_107})

V_223 = CTVertex(name = 'V_223',
                 type = 'R2',
                 particles = [ P.YF3d1__tilde__, P.YF3d1, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_283_105})

V_224 = CTVertex(name = 'V_224',
                 type = 'R2',
                 particles = [ P.YF3d2__tilde__, P.YF3d2, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_283_105})

V_225 = CTVertex(name = 'V_225',
                 type = 'R2',
                 particles = [ P.YF3d3__tilde__, P.YF3d3, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_283_105})

V_226 = CTVertex(name = 'V_226',
                 type = 'R2',
                 particles = [ P.YF3u1__tilde__, P.YF3u1, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_290_108})

V_227 = CTVertex(name = 'V_227',
                 type = 'R2',
                 particles = [ P.YF3u2__tilde__, P.YF3u2, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_290_108})

V_228 = CTVertex(name = 'V_228',
                 type = 'R2',
                 particles = [ P.YF3u3__tilde__, P.YF3u3, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_290_108})

V_229 = CTVertex(name = 'V_229',
                 type = 'R2',
                 particles = [ P.Z, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_307_120})

V_230 = CTVertex(name = 'V_230',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_308_121})

V_231 = CTVertex(name = 'V_231',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_309_122})

V_232 = CTVertex(name = 'V_232',
                 type = 'R2',
                 particles = [ P.Z, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_307_120})

V_233 = CTVertex(name = 'V_233',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_308_121})

V_234 = CTVertex(name = 'V_234',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_309_122})

V_235 = CTVertex(name = 'V_235',
                 type = 'R2',
                 particles = [ P.Z, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_307_120})

V_236 = CTVertex(name = 'V_236',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_308_121})

V_237 = CTVertex(name = 'V_237',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_309_122})

V_238 = CTVertex(name = 'V_238',
                 type = 'R2',
                 particles = [ P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_346_127})

V_239 = CTVertex(name = 'V_239',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_347_128})

V_240 = CTVertex(name = 'V_240',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_348_129})

V_241 = CTVertex(name = 'V_241',
                 type = 'R2',
                 particles = [ P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_346_127})

V_242 = CTVertex(name = 'V_242',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_347_128})

V_243 = CTVertex(name = 'V_243',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_348_129})

V_244 = CTVertex(name = 'V_244',
                 type = 'R2',
                 particles = [ P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_346_127})

V_245 = CTVertex(name = 'V_245',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_347_128})

V_246 = CTVertex(name = 'V_246',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_348_129})

V_247 = CTVertex(name = 'V_247',
                 type = 'R2',
                 particles = [ P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_391_140})

V_248 = CTVertex(name = 'V_248',
                 type = 'R2',
                 particles = [ P.W__plus__, P.Z, P.YS3Qd1, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_645_193})

V_249 = CTVertex(name = 'V_249',
                 type = 'R2',
                 particles = [ P.W__minus__, P.Z, P.YS3Qd1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_645_193})

V_250 = CTVertex(name = 'V_250',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_392_141})

V_251 = CTVertex(name = 'V_251',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_393_142})

V_252 = CTVertex(name = 'V_252',
                 type = 'R2',
                 particles = [ P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_391_140})

V_253 = CTVertex(name = 'V_253',
                 type = 'R2',
                 particles = [ P.W__plus__, P.Z, P.YS3Qd2, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_645_193})

V_254 = CTVertex(name = 'V_254',
                 type = 'R2',
                 particles = [ P.W__minus__, P.Z, P.YS3Qd2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_645_193})

V_255 = CTVertex(name = 'V_255',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_392_141})

V_256 = CTVertex(name = 'V_256',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_393_142})

V_257 = CTVertex(name = 'V_257',
                 type = 'R2',
                 particles = [ P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_391_140})

V_258 = CTVertex(name = 'V_258',
                 type = 'R2',
                 particles = [ P.W__plus__, P.Z, P.YS3Qd3, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_645_193})

V_259 = CTVertex(name = 'V_259',
                 type = 'R2',
                 particles = [ P.W__minus__, P.Z, P.YS3Qd3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_645_193})

V_260 = CTVertex(name = 'V_260',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_392_141})

V_261 = CTVertex(name = 'V_261',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_393_142})

V_262 = CTVertex(name = 'V_262',
                 type = 'R2',
                 particles = [ P.Z, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_436_147})

V_263 = CTVertex(name = 'V_263',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_437_148})

V_264 = CTVertex(name = 'V_264',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_438_149})

V_265 = CTVertex(name = 'V_265',
                 type = 'R2',
                 particles = [ P.Z, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_436_147})

V_266 = CTVertex(name = 'V_266',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_437_148})

V_267 = CTVertex(name = 'V_267',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_438_149})

V_268 = CTVertex(name = 'V_268',
                 type = 'R2',
                 particles = [ P.Z, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_436_147})

V_269 = CTVertex(name = 'V_269',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_437_148})

V_270 = CTVertex(name = 'V_270',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_438_149})

V_271 = CTVertex(name = 'V_271',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_310_123})

V_272 = CTVertex(name = 'V_272',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_310_123})

V_273 = CTVertex(name = 'V_273',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_310_123})

V_274 = CTVertex(name = 'V_274',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_349_130})

V_275 = CTVertex(name = 'V_275',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_349_130})

V_276 = CTVertex(name = 'V_276',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_349_130})

V_277 = CTVertex(name = 'V_277',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_394_143})

V_278 = CTVertex(name = 'V_278',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_394_143})

V_279 = CTVertex(name = 'V_279',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_394_143})

V_280 = CTVertex(name = 'V_280',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_439_150})

V_281 = CTVertex(name = 'V_281',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_439_150})

V_282 = CTVertex(name = 'V_282',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_439_150})

V_283 = CTVertex(name = 'V_283',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.YF3Qu1, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.u, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_589_185})

V_284 = CTVertex(name = 'V_284',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.YF3Qd1, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_589_185})

V_285 = CTVertex(name = 'V_285',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.YF3Qu2, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_581_177})

V_286 = CTVertex(name = 'V_286',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.YF3Qd2, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_581_177})

V_287 = CTVertex(name = 'V_287',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.YF3Qu3, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.t, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_576_172})

V_288 = CTVertex(name = 'V_288',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.YF3Qd3, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_576_172})

V_289 = CTVertex(name = 'V_289',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.YF3Qu1, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.u, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_589_185})

V_290 = CTVertex(name = 'V_290',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.YF3Qd1, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_589_185})

V_291 = CTVertex(name = 'V_291',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.YF3Qu2, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_581_177})

V_292 = CTVertex(name = 'V_292',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.YF3Qd2, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_581_177})

V_293 = CTVertex(name = 'V_293',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.YF3Qu3, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.t, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_576_172})

V_294 = CTVertex(name = 'V_294',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.YF3Qd3, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_576_172})

V_295 = CTVertex(name = 'V_295',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_287_106})

V_296 = CTVertex(name = 'V_296',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_287_106})

V_297 = CTVertex(name = 'V_297',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_287_106})

V_298 = CTVertex(name = 'V_298',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_280_102})

V_299 = CTVertex(name = 'V_299',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_280_102})

V_300 = CTVertex(name = 'V_300',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_280_102})

V_301 = CTVertex(name = 'V_301',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_281_103})

V_302 = CTVertex(name = 'V_302',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_281_103})

V_303 = CTVertex(name = 'V_303',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_281_103})

V_304 = CTVertex(name = 'V_304',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_281_103})

V_305 = CTVertex(name = 'V_305',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_281_103})

V_306 = CTVertex(name = 'V_306',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_281_103})

V_307 = CTVertex(name = 'V_307',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_580_176})

V_308 = CTVertex(name = 'V_308',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_580_176})

V_309 = CTVertex(name = 'V_309',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_580_176})

V_310 = CTVertex(name = 'V_310',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_580_176})

V_311 = CTVertex(name = 'V_311',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_580_176})

V_312 = CTVertex(name = 'V_312',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_580_176})

V_313 = CTVertex(name = 'V_313',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_289_107,(0,1,0):C.R2GC_290_108})

V_314 = CTVertex(name = 'V_314',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_289_107,(0,1,0):C.R2GC_290_108})

V_315 = CTVertex(name = 'V_315',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_289_107,(0,1,0):C.R2GC_290_108})

V_316 = CTVertex(name = 'V_316',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_282_104,(0,1,0):C.R2GC_283_105})

V_317 = CTVertex(name = 'V_317',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_282_104,(0,1,0):C.R2GC_283_105})

V_318 = CTVertex(name = 'V_318',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_282_104,(0,1,0):C.R2GC_283_105})

V_319 = CTVertex(name = 'V_319',
                 type = 'R2',
                 particles = [ P.YF3Qu1__tilde__, P.u, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.u, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_589_185})

V_320 = CTVertex(name = 'V_320',
                 type = 'R2',
                 particles = [ P.YF3Qd1__tilde__, P.d, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_589_185})

V_321 = CTVertex(name = 'V_321',
                 type = 'R2',
                 particles = [ P.YF3Qu2__tilde__, P.c, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_581_177})

V_322 = CTVertex(name = 'V_322',
                 type = 'R2',
                 particles = [ P.YF3Qd2__tilde__, P.s, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_581_177})

V_323 = CTVertex(name = 'V_323',
                 type = 'R2',
                 particles = [ P.YF3Qu3__tilde__, P.t, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.t, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_576_172})

V_324 = CTVertex(name = 'V_324',
                 type = 'R2',
                 particles = [ P.YF3Qd3__tilde__, P.b, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_576_172})

V_325 = CTVertex(name = 'V_325',
                 type = 'R2',
                 particles = [ P.YF3Qu1__tilde__, P.u, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.u, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_589_185})

V_326 = CTVertex(name = 'V_326',
                 type = 'R2',
                 particles = [ P.YF3Qd1__tilde__, P.d, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_589_185})

V_327 = CTVertex(name = 'V_327',
                 type = 'R2',
                 particles = [ P.YF3Qu2__tilde__, P.c, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_581_177})

V_328 = CTVertex(name = 'V_328',
                 type = 'R2',
                 particles = [ P.YF3Qd2__tilde__, P.s, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_581_177})

V_329 = CTVertex(name = 'V_329',
                 type = 'R2',
                 particles = [ P.YF3Qu3__tilde__, P.t, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.t, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_576_172})

V_330 = CTVertex(name = 'V_330',
                 type = 'R2',
                 particles = [ P.YF3Qd3__tilde__, P.b, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_576_172})

V_331 = CTVertex(name = 'V_331',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.YF3d1, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_587_183})

V_332 = CTVertex(name = 'V_332',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.YF3d2, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_751_202})

V_333 = CTVertex(name = 'V_333',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.YF3d3, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_574_170})

V_334 = CTVertex(name = 'V_334',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.YF3u1, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_769_210})

V_335 = CTVertex(name = 'V_335',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.YF3u2, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_583_179})

V_336 = CTVertex(name = 'V_336',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.YF3u3, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_762_207})

V_337 = CTVertex(name = 'V_337',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.YF3d1, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_587_183})

V_338 = CTVertex(name = 'V_338',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.YF3d2, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_751_202})

V_339 = CTVertex(name = 'V_339',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.YF3d3, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_574_170})

V_340 = CTVertex(name = 'V_340',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.YF3u1, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_769_210})

V_341 = CTVertex(name = 'V_341',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.YF3u2, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_583_179})

V_342 = CTVertex(name = 'V_342',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.YF3u3, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_762_207})

V_343 = CTVertex(name = 'V_343',
                 type = 'R2',
                 particles = [ P.YF3d1__tilde__, P.d, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_587_183})

V_344 = CTVertex(name = 'V_344',
                 type = 'R2',
                 particles = [ P.YF3d2__tilde__, P.s, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_751_202})

V_345 = CTVertex(name = 'V_345',
                 type = 'R2',
                 particles = [ P.YF3d3__tilde__, P.b, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_574_170})

V_346 = CTVertex(name = 'V_346',
                 type = 'R2',
                 particles = [ P.YF3u1__tilde__, P.u, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_769_210})

V_347 = CTVertex(name = 'V_347',
                 type = 'R2',
                 particles = [ P.YF3u2__tilde__, P.c, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_583_179})

V_348 = CTVertex(name = 'V_348',
                 type = 'R2',
                 particles = [ P.YF3u3__tilde__, P.t, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_762_207})

V_349 = CTVertex(name = 'V_349',
                 type = 'R2',
                 particles = [ P.YF3d1__tilde__, P.d, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_587_183})

V_350 = CTVertex(name = 'V_350',
                 type = 'R2',
                 particles = [ P.YF3d2__tilde__, P.s, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_751_202})

V_351 = CTVertex(name = 'V_351',
                 type = 'R2',
                 particles = [ P.YF3d3__tilde__, P.b, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_574_170})

V_352 = CTVertex(name = 'V_352',
                 type = 'R2',
                 particles = [ P.YF3u1__tilde__, P.u, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_769_210})

V_353 = CTVertex(name = 'V_353',
                 type = 'R2',
                 particles = [ P.YF3u2__tilde__, P.c, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_583_179})

V_354 = CTVertex(name = 'V_354',
                 type = 'R2',
                 particles = [ P.YF3u3__tilde__, P.t, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_762_207})

V_355 = CTVertex(name = 'V_355',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_279_101})

V_356 = CTVertex(name = 'V_356',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_279_101})

V_357 = CTVertex(name = 'V_357',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_482_153,(0,1,0):C.R2GC_279_101})

V_358 = CTVertex(name = 'V_358',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_279_101})

V_359 = CTVertex(name = 'V_359',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_279_101})

V_360 = CTVertex(name = 'V_360',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_279_101})

V_361 = CTVertex(name = 'V_361',
                 type = 'R2',
                 particles = [ P.YF3Qu1__tilde__, P.YF3Qu1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_533_162,(0,1,0):C.R2GC_279_101})

V_362 = CTVertex(name = 'V_362',
                 type = 'R2',
                 particles = [ P.YF3Qu2__tilde__, P.YF3Qu2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_542_163,(0,1,0):C.R2GC_279_101})

V_363 = CTVertex(name = 'V_363',
                 type = 'R2',
                 particles = [ P.YF3Qu3__tilde__, P.YF3Qu3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_551_164,(0,1,0):C.R2GC_279_101})

V_364 = CTVertex(name = 'V_364',
                 type = 'R2',
                 particles = [ P.YF3Qd1__tilde__, P.YF3Qd1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_512_159,(0,1,0):C.R2GC_279_101})

V_365 = CTVertex(name = 'V_365',
                 type = 'R2',
                 particles = [ P.YF3Qd2__tilde__, P.YF3Qd2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_519_160,(0,1,0):C.R2GC_279_101})

V_366 = CTVertex(name = 'V_366',
                 type = 'R2',
                 particles = [ P.YF3Qd3__tilde__, P.YF3Qd3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_526_161,(0,1,0):C.R2GC_279_101})

V_367 = CTVertex(name = 'V_367',
                 type = 'R2',
                 particles = [ P.YF3u1__tilde__, P.YF3u1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_560_165,(0,1,0):C.R2GC_279_101})

V_368 = CTVertex(name = 'V_368',
                 type = 'R2',
                 particles = [ P.YF3u2__tilde__, P.YF3u2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_565_166,(0,1,0):C.R2GC_279_101})

V_369 = CTVertex(name = 'V_369',
                 type = 'R2',
                 particles = [ P.YF3u3__tilde__, P.YF3u3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_570_167,(0,1,0):C.R2GC_279_101})

V_370 = CTVertex(name = 'V_370',
                 type = 'R2',
                 particles = [ P.YF3d1__tilde__, P.YF3d1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_497_156,(0,1,0):C.R2GC_279_101})

V_371 = CTVertex(name = 'V_371',
                 type = 'R2',
                 particles = [ P.YF3d2__tilde__, P.YF3d2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_502_157,(0,1,0):C.R2GC_279_101})

V_372 = CTVertex(name = 'V_372',
                 type = 'R2',
                 particles = [ P.YF3d3__tilde__, P.YF3d3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_507_158,(0,1,0):C.R2GC_279_101})

V_373 = CTVertex(name = 'V_373',
                 type = 'R2',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV1, L.VV2, L.VV3 ],
                 loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u], [P.YF3d1], [P.YF3d2], [P.YF3d3], [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3], [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3], [P.YF3u1], [P.YF3u2], [P.YF3u3] ], [ [P.g] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ] ],
                 couplings = {(0,2,1):C.R2GC_131_1,(0,0,2):C.R2GC_140_13,(0,0,3):C.R2GC_140_14,(0,0,4):C.R2GC_140_15,(0,0,5):C.R2GC_140_16,(0,0,6):C.R2GC_140_17,(0,0,7):C.R2GC_140_18,(0,0,8):C.R2GC_140_19,(0,0,9):C.R2GC_140_20,(0,0,10):C.R2GC_140_21,(0,0,11):C.R2GC_140_22,(0,0,12):C.R2GC_140_23,(0,0,13):C.R2GC_140_24,(0,0,14):C.R2GC_140_25,(0,1,0):C.R2GC_137_8})

V_374 = CTVertex(name = 'V_374',
                 type = 'R2',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_390_139,(0,1,0):C.R2GC_298_109})

V_375 = CTVertex(name = 'V_375',
                 type = 'R2',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_405_144,(0,1,0):C.R2GC_298_109})

V_376 = CTVertex(name = 'V_376',
                 type = 'R2',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_420_145,(0,1,0):C.R2GC_298_109})

V_377 = CTVertex(name = 'V_377',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_345_126,(0,1,0):C.R2GC_298_109})

V_378 = CTVertex(name = 'V_378',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_360_133,(0,1,0):C.R2GC_298_109})

V_379 = CTVertex(name = 'V_379',
                 type = 'R2',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_375_134,(0,1,0):C.R2GC_298_109})

V_380 = CTVertex(name = 'V_380',
                 type = 'R2',
                 particles = [ P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_435_146,(0,1,0):C.R2GC_298_109})

V_381 = CTVertex(name = 'V_381',
                 type = 'R2',
                 particles = [ P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_450_151,(0,1,0):C.R2GC_298_109})

V_382 = CTVertex(name = 'V_382',
                 type = 'R2',
                 particles = [ P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_465_152,(0,1,0):C.R2GC_298_109})

V_383 = CTVertex(name = 'V_383',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_306_119,(0,1,0):C.R2GC_298_109})

V_384 = CTVertex(name = 'V_384',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_319_124,(0,1,0):C.R2GC_298_109})

V_385 = CTVertex(name = 'V_385',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_332_125,(0,1,0):C.R2GC_298_109})

V_386 = CTVertex(name = 'V_386',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVV1 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_135_4,(0,0,1):C.R2GC_135_5})

V_387 = CTVertex(name = 'V_387',
                 type = 'R2',
                 particles = [ P.g, P.g, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVS1 ],
                 loop_particles = [ [ [P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_132_2})

V_388 = CTVertex(name = 'V_388',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Xv, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV10 ],
                 loop_particles = [ [ [P.b, P.YF3d3] ], [ [P.b, P.YF3Qd3], [P.t, P.YF3Qu3] ], [ [P.c, P.YF3Qu2], [P.s, P.YF3Qd2] ], [ [P.c, P.YF3u2] ], [ [P.d, P.YF3d1] ], [ [P.d, P.YF3Qd1], [P.u, P.YF3Qu1] ], [ [P.s, P.YF3d2] ], [ [P.t, P.YF3u3] ], [ [P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_145_53,(0,0,1):C.R2GC_145_54,(0,0,2):C.R2GC_145_55,(0,0,3):C.R2GC_145_56,(0,0,4):C.R2GC_145_57,(0,0,5):C.R2GC_145_58,(0,0,6):C.R2GC_145_59,(0,0,7):C.R2GC_145_60,(0,0,8):C.R2GC_145_61})

V_389 = CTVertex(name = 'V_389',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Xv, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV10 ],
                 loop_particles = [ [ [P.b, P.YF3d3] ], [ [P.b, P.YF3Qd3], [P.t, P.YF3Qu3] ], [ [P.c, P.YF3Qu2], [P.s, P.YF3Qd2] ], [ [P.c, P.YF3u2] ], [ [P.d, P.YF3d1] ], [ [P.d, P.YF3Qd1], [P.u, P.YF3Qu1] ], [ [P.s, P.YF3d2] ], [ [P.t, P.YF3u3] ], [ [P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_144_44,(0,0,1):C.R2GC_144_45,(0,0,2):C.R2GC_144_46,(0,0,3):C.R2GC_144_47,(0,0,4):C.R2GC_144_48,(0,0,5):C.R2GC_144_49,(0,0,6):C.R2GC_144_50,(0,0,7):C.R2GC_144_51,(0,0,8):C.R2GC_144_52})

V_390 = CTVertex(name = 'V_390',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Xv, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV10 ],
                 loop_particles = [ [ [P.b, P.YF3d3] ], [ [P.b, P.YF3Qd3], [P.t, P.YF3Qu3] ], [ [P.c, P.YF3Qu2], [P.s, P.YF3Qd2] ], [ [P.c, P.YF3u2] ], [ [P.d, P.YF3d1] ], [ [P.d, P.YF3Qd1], [P.u, P.YF3Qu1] ], [ [P.s, P.YF3d2] ], [ [P.t, P.YF3u3] ], [ [P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_144_44,(0,0,1):C.R2GC_144_45,(0,0,2):C.R2GC_144_46,(0,0,3):C.R2GC_144_47,(0,0,4):C.R2GC_144_48,(0,0,5):C.R2GC_144_49,(0,0,6):C.R2GC_144_50,(0,0,7):C.R2GC_144_51,(0,0,8):C.R2GC_144_52})

V_391 = CTVertex(name = 'V_391',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Xw__tilde__, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV10 ],
                 loop_particles = [ [ [P.b, P.YF3d3] ], [ [P.b, P.YF3Qd3], [P.t, P.YF3Qu3] ], [ [P.c, P.YF3Qu2], [P.s, P.YF3Qd2] ], [ [P.c, P.YF3u2] ], [ [P.d, P.YF3d1] ], [ [P.d, P.YF3Qd1], [P.u, P.YF3Qu1] ], [ [P.s, P.YF3d2] ], [ [P.t, P.YF3u3] ], [ [P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_144_44,(0,0,1):C.R2GC_144_45,(0,0,2):C.R2GC_144_46,(0,0,3):C.R2GC_144_47,(0,0,4):C.R2GC_144_48,(0,0,5):C.R2GC_144_49,(0,0,6):C.R2GC_144_50,(0,0,7):C.R2GC_144_51,(0,0,8):C.R2GC_144_52})

V_392 = CTVertex(name = 'V_392',
                 type = 'R2',
                 particles = [ P.a, P.a, P.g, P.g ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVVV10 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s], [P.YF3d1], [P.YF3d2], [P.YF3d3], [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3] ], [ [P.c], [P.t], [P.u], [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3], [P.YF3u1], [P.YF3u2], [P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_138_9,(0,0,1):C.R2GC_138_10})

V_393 = CTVertex(name = 'V_393',
                 type = 'R2',
                 particles = [ P.a, P.g, P.g, P.Z ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VVVV10 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ], [ [P.YF3d1], [P.YF3d2], [P.YF3d3] ], [ [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3] ], [ [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3] ], [ [P.YF3u1], [P.YF3u2], [P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_141_26,(0,0,1):C.R2GC_141_27,(0,0,2):C.R2GC_141_28,(0,0,3):C.R2GC_141_29,(0,0,4):C.R2GC_141_30,(0,0,5):C.R2GC_141_31})

V_394 = CTVertex(name = 'V_394',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Z, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV10 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ], [ [P.YF3d1], [P.YF3d2], [P.YF3d3] ], [ [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3] ], [ [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3] ], [ [P.YF3u1], [P.YF3u2], [P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_143_38,(0,0,1):C.R2GC_143_39,(0,0,2):C.R2GC_143_40,(0,0,3):C.R2GC_143_41,(0,0,4):C.R2GC_143_42,(0,0,5):C.R2GC_143_43})

V_395 = CTVertex(name = 'V_395',
                 type = 'R2',
                 particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV10 ],
                 loop_particles = [ [ [P.b, P.t], [P.c, P.s], [P.d, P.u] ], [ [P.YF3Qd1, P.YF3Qu1], [P.YF3Qd2, P.YF3Qu2], [P.YF3Qd3, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_148_80,(0,0,1):C.R2GC_148_81})

V_396 = CTVertex(name = 'V_396',
                 type = 'R2',
                 particles = [ P.a, P.g, P.g, P.g ],
                 color = [ 'd(2,3,4)' ],
                 lorentz = [ L.VVVV10 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s], [P.YF3d1], [P.YF3d2], [P.YF3d3], [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3] ], [ [P.c], [P.t], [P.u], [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3], [P.YF3u1], [P.YF3u2], [P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_139_11,(0,0,1):C.R2GC_139_12})

V_397 = CTVertex(name = 'V_397',
                 type = 'R2',
                 particles = [ P.g, P.g, P.g, P.Z ],
                 color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                 lorentz = [ L.VVVV1, L.VVVV10 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ], [ [P.YF3d1], [P.YF3d2], [P.YF3d3] ], [ [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3] ], [ [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3] ], [ [P.YF3u1], [P.YF3u2], [P.YF3u3] ] ],
                 couplings = {(1,0,0):C.R2GC_136_6,(1,0,1):C.R2GC_136_7,(0,1,0):C.R2GC_142_32,(0,1,1):C.R2GC_142_33,(0,1,2):C.R2GC_142_34,(0,1,3):C.R2GC_142_35,(0,1,4):C.R2GC_142_36,(0,1,5):C.R2GC_142_37})

V_398 = CTVertex(name = 'V_398',
                 type = 'R2',
                 particles = [ P.g, P.g, P.H, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_133_3})

V_399 = CTVertex(name = 'V_399',
                 type = 'R2',
                 particles = [ P.g, P.g, P.G0, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_133_3})

V_400 = CTVertex(name = 'V_400',
                 type = 'R2',
                 particles = [ P.g, P.g, P.G__minus__, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_133_3})

V_401 = CTVertex(name = 'V_401',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Xs, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.YF3d3] ], [ [P.b, P.YF3Qd3], [P.t, P.YF3Qu3] ], [ [P.c, P.YF3Qu2], [P.s, P.YF3Qd2] ], [ [P.c, P.YF3u2] ], [ [P.d, P.YF3d1] ], [ [P.d, P.YF3Qd1], [P.u, P.YF3Qu1] ], [ [P.s, P.YF3d2] ], [ [P.t, P.YF3u3] ], [ [P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_147_71,(0,0,1):C.R2GC_147_72,(0,0,2):C.R2GC_147_73,(0,0,3):C.R2GC_147_74,(0,0,4):C.R2GC_147_75,(0,0,5):C.R2GC_147_76,(0,0,6):C.R2GC_147_77,(0,0,7):C.R2GC_147_78,(0,0,8):C.R2GC_147_79})

V_402 = CTVertex(name = 'V_402',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Xc, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.YF3d3] ], [ [P.b, P.YF3Qd3], [P.t, P.YF3Qu3] ], [ [P.c, P.YF3Qu2], [P.s, P.YF3Qd2] ], [ [P.c, P.YF3u2] ], [ [P.d, P.YF3d1] ], [ [P.d, P.YF3Qd1], [P.u, P.YF3Qu1] ], [ [P.s, P.YF3d2] ], [ [P.t, P.YF3u3] ], [ [P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_146_62,(0,0,1):C.R2GC_146_63,(0,0,2):C.R2GC_146_64,(0,0,3):C.R2GC_146_65,(0,0,4):C.R2GC_146_66,(0,0,5):C.R2GC_146_67,(0,0,6):C.R2GC_146_68,(0,0,7):C.R2GC_146_69,(0,0,8):C.R2GC_146_70})

V_403 = CTVertex(name = 'V_403',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Xc__tilde__, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.YF3d3] ], [ [P.b, P.YF3Qd3], [P.t, P.YF3Qu3] ], [ [P.c, P.YF3Qu2], [P.s, P.YF3Qd2] ], [ [P.c, P.YF3u2] ], [ [P.d, P.YF3d1] ], [ [P.d, P.YF3Qd1], [P.u, P.YF3Qu1] ], [ [P.s, P.YF3d2] ], [ [P.t, P.YF3u3] ], [ [P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_146_62,(0,0,1):C.R2GC_146_63,(0,0,2):C.R2GC_146_64,(0,0,3):C.R2GC_146_65,(0,0,4):C.R2GC_146_66,(0,0,5):C.R2GC_146_67,(0,0,6):C.R2GC_146_68,(0,0,7):C.R2GC_146_69,(0,0,8):C.R2GC_146_70})

V_404 = CTVertex(name = 'V_404',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Xc__tilde__, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.YF3d3] ], [ [P.b, P.YF3Qd3], [P.t, P.YF3Qu3] ], [ [P.c, P.YF3Qu2], [P.s, P.YF3Qd2] ], [ [P.c, P.YF3u2] ], [ [P.d, P.YF3d1] ], [ [P.d, P.YF3Qd1], [P.u, P.YF3Qu1] ], [ [P.s, P.YF3d2] ], [ [P.t, P.YF3u3] ], [ [P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_146_62,(0,0,1):C.R2GC_146_63,(0,0,2):C.R2GC_146_64,(0,0,3):C.R2GC_146_65,(0,0,4):C.R2GC_146_66,(0,0,5):C.R2GC_146_67,(0,0,6):C.R2GC_146_68,(0,0,7):C.R2GC_146_69,(0,0,8):C.R2GC_146_70})

V_405 = CTVertex(name = 'V_405',
                 type = 'R2',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3Qu1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_303_114,(1,0,3):C.R2GC_303_115,(1,0,0):C.R2GC_780_218,(1,0,5):C.R2GC_780_219,(1,0,1):C.R2GC_780_220,(1,0,4):C.R2GC_780_221,(0,0,2):C.R2GC_303_114,(0,0,3):C.R2GC_303_115,(0,0,0):C.R2GC_780_218,(0,0,5):C.R2GC_780_219,(0,0,1):C.R2GC_780_220,(0,0,4):C.R2GC_780_221})

V_406 = CTVertex(name = 'V_406',
                 type = 'R2',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3Qu1, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qu1, P.YS3Qu2] ], [ [P.g, P.YS3Qu1, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_853_286,(1,0,8):C.R2GC_853_287,(1,0,1):C.R2GC_853_288,(1,0,7):C.R2GC_853_289,(1,0,2):C.R2GC_853_290,(1,0,6):C.R2GC_853_291,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_852_280,(0,0,8):C.R2GC_852_281,(0,0,1):C.R2GC_852_282,(0,0,7):C.R2GC_852_283,(0,0,2):C.R2GC_852_284,(0,0,6):C.R2GC_852_285})

V_407 = CTVertex(name = 'V_407',
                 type = 'R2',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3Qu2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_303_114,(1,0,3):C.R2GC_303_115,(1,0,0):C.R2GC_780_218,(1,0,5):C.R2GC_780_219,(1,0,1):C.R2GC_780_220,(1,0,4):C.R2GC_780_221,(0,0,2):C.R2GC_303_114,(0,0,3):C.R2GC_303_115,(0,0,0):C.R2GC_780_218,(0,0,5):C.R2GC_780_219,(0,0,1):C.R2GC_780_220,(0,0,4):C.R2GC_780_221})

V_408 = CTVertex(name = 'V_408',
                 type = 'R2',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qu1, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qu1, P.YS3Qu3] ], [ [P.g, P.YS3Qu1, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_853_286,(1,0,8):C.R2GC_853_287,(1,0,1):C.R2GC_853_288,(1,0,7):C.R2GC_853_289,(1,0,2):C.R2GC_853_290,(1,0,6):C.R2GC_853_291,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_852_280,(0,0,8):C.R2GC_852_281,(0,0,1):C.R2GC_852_282,(0,0,7):C.R2GC_852_283,(0,0,2):C.R2GC_852_284,(0,0,6):C.R2GC_852_285})

V_409 = CTVertex(name = 'V_409',
                 type = 'R2',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qu2, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qu2], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qu2, P.YS3Qu3] ], [ [P.g, P.YS3Qu2, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qu2, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_853_286,(1,0,8):C.R2GC_853_287,(1,0,1):C.R2GC_853_288,(1,0,7):C.R2GC_853_289,(1,0,2):C.R2GC_853_290,(1,0,6):C.R2GC_853_291,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_852_280,(0,0,8):C.R2GC_852_281,(0,0,1):C.R2GC_852_282,(0,0,7):C.R2GC_852_283,(0,0,2):C.R2GC_852_284,(0,0,6):C.R2GC_852_285})

V_410 = CTVertex(name = 'V_410',
                 type = 'R2',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3__tilde__, P.YS3Qu3, P.YS3Qu3 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_303_114,(1,0,3):C.R2GC_303_115,(1,0,0):C.R2GC_780_218,(1,0,5):C.R2GC_780_219,(1,0,1):C.R2GC_780_220,(1,0,4):C.R2GC_780_221,(0,0,2):C.R2GC_303_114,(0,0,3):C.R2GC_303_115,(0,0,0):C.R2GC_780_218,(0,0,5):C.R2GC_780_219,(0,0,1):C.R2GC_780_220,(0,0,4):C.R2GC_780_221})

V_411 = CTVertex(name = 'V_411',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qu1] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,7):C.R2GC_592_191,(1,0,8):C.R2GC_592_192,(1,0,0):C.R2GC_809_258,(1,0,4):C.R2GC_786_224,(1,0,11):C.R2GC_847_275,(1,0,1):C.R2GC_809_260,(1,0,5):C.R2GC_847_276,(1,0,10):C.R2GC_847_277,(1,0,2):C.R2GC_809_262,(1,0,6):C.R2GC_847_278,(1,0,9):C.R2GC_847_279,(0,0,3):C.R2GC_591_187,(0,0,7):C.R2GC_591_188,(0,0,8):C.R2GC_591_189,(0,0,0):C.R2GC_774_212,(0,0,4):C.R2GC_787_227,(0,0,11):C.R2GC_846_270,(0,0,1):C.R2GC_138_9,(0,0,5):C.R2GC_846_271,(0,0,10):C.R2GC_846_272,(0,0,2):C.R2GC_808_256,(0,0,6):C.R2GC_846_273,(0,0,9):C.R2GC_846_274})

V_412 = CTVertex(name = 'V_412',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qd1, P.YS3Qu2] ], [ [P.g, P.YS3Qd1, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_809_258,(1,0,8):C.R2GC_847_275,(1,0,1):C.R2GC_809_260,(1,0,7):C.R2GC_847_277,(1,0,2):C.R2GC_809_262,(1,0,6):C.R2GC_847_279,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_774_212,(0,0,8):C.R2GC_846_270,(0,0,1):C.R2GC_138_9,(0,0,7):C.R2GC_846_272,(0,0,2):C.R2GC_808_256,(0,0,6):C.R2GC_846_274})

V_413 = CTVertex(name = 'V_413',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qd1, P.YS3Qu3] ], [ [P.g, P.YS3Qd1, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_809_258,(1,0,8):C.R2GC_847_275,(1,0,1):C.R2GC_809_260,(1,0,7):C.R2GC_847_277,(1,0,2):C.R2GC_809_262,(1,0,6):C.R2GC_847_279,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_774_212,(0,0,8):C.R2GC_846_270,(0,0,1):C.R2GC_138_9,(0,0,7):C.R2GC_846_272,(0,0,2):C.R2GC_808_256,(0,0,6):C.R2GC_846_274})

V_414 = CTVertex(name = 'V_414',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qd1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1] ], [ [P.g] ], [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_303_114,(1,0,3):C.R2GC_303_115,(1,0,0):C.R2GC_774_212,(1,0,5):C.R2GC_777_216,(1,0,1):C.R2GC_774_214,(1,0,4):C.R2GC_777_217,(0,0,2):C.R2GC_303_114,(0,0,3):C.R2GC_303_115,(0,0,0):C.R2GC_774_212,(0,0,5):C.R2GC_777_216,(0,0,1):C.R2GC_774_214,(0,0,4):C.R2GC_777_217})

V_415 = CTVertex(name = 'V_415',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd2, P.YS3Qu1, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu2] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu1, P.YS3Qu2] ] ],
                 couplings = {(1,0,0):C.R2GC_786_224,(1,0,1):C.R2GC_786_225,(1,0,2):C.R2GC_786_226,(0,0,0):C.R2GC_787_227,(0,0,1):C.R2GC_787_228,(0,0,2):C.R2GC_787_229})

V_416 = CTVertex(name = 'V_416',
                 type = 'R2',
                 particles = [ P.YS3Qd1, P.YS3Qd2__tilde__, P.YS3Qu1__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu2] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu1, P.YS3Qu2] ] ],
                 couplings = {(1,0,0):C.R2GC_786_224,(1,0,1):C.R2GC_786_225,(1,0,2):C.R2GC_786_226,(0,0,0):C.R2GC_787_227,(0,0,1):C.R2GC_787_228,(0,0,2):C.R2GC_787_229})

V_417 = CTVertex(name = 'V_417',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3Qd2, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qd2, P.YS3Qu1] ], [ [P.g, P.YS3Qd2, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_809_258,(1,0,8):C.R2GC_847_275,(1,0,1):C.R2GC_809_260,(1,0,7):C.R2GC_847_277,(1,0,2):C.R2GC_809_262,(1,0,6):C.R2GC_847_279,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_774_212,(0,0,8):C.R2GC_846_270,(0,0,1):C.R2GC_138_9,(0,0,7):C.R2GC_846_272,(0,0,2):C.R2GC_808_256,(0,0,6):C.R2GC_846_274})

V_418 = CTVertex(name = 'V_418',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qu2] ], [ [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,7):C.R2GC_592_191,(1,0,8):C.R2GC_592_192,(1,0,0):C.R2GC_809_258,(1,0,4):C.R2GC_786_224,(1,0,11):C.R2GC_847_275,(1,0,1):C.R2GC_809_260,(1,0,5):C.R2GC_847_276,(1,0,10):C.R2GC_847_277,(1,0,2):C.R2GC_809_262,(1,0,6):C.R2GC_847_278,(1,0,9):C.R2GC_847_279,(0,0,3):C.R2GC_591_187,(0,0,7):C.R2GC_591_188,(0,0,8):C.R2GC_591_189,(0,0,0):C.R2GC_774_212,(0,0,4):C.R2GC_787_227,(0,0,11):C.R2GC_846_270,(0,0,1):C.R2GC_138_9,(0,0,5):C.R2GC_846_271,(0,0,10):C.R2GC_846_272,(0,0,2):C.R2GC_808_256,(0,0,6):C.R2GC_846_273,(0,0,9):C.R2GC_846_274})

V_419 = CTVertex(name = 'V_419',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qd2, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qd2, P.YS3Qu3] ], [ [P.g, P.YS3Qd2, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_809_258,(1,0,8):C.R2GC_847_275,(1,0,1):C.R2GC_809_260,(1,0,7):C.R2GC_847_277,(1,0,2):C.R2GC_809_262,(1,0,6):C.R2GC_847_279,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_774_212,(0,0,8):C.R2GC_846_270,(0,0,1):C.R2GC_138_9,(0,0,7):C.R2GC_846_272,(0,0,2):C.R2GC_808_256,(0,0,6):C.R2GC_846_274})

V_420 = CTVertex(name = 'V_420',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qd2] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd1, P.YS3Qd2] ], [ [P.g, P.YS3Qd1, P.YS3Qd2, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_793_236,(1,0,8):C.R2GC_805_251,(1,0,1):C.R2GC_793_238,(1,0,7):C.R2GC_805_252,(1,0,2):C.R2GC_793_240,(1,0,6):C.R2GC_805_253,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_792_230,(0,0,8):C.R2GC_804_248,(0,0,1):C.R2GC_792_232,(0,0,7):C.R2GC_804_249,(0,0,2):C.R2GC_792_234,(0,0,6):C.R2GC_804_250})

V_421 = CTVertex(name = 'V_421',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qd2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_303_114,(1,0,3):C.R2GC_303_115,(1,0,0):C.R2GC_774_212,(1,0,5):C.R2GC_777_216,(1,0,1):C.R2GC_774_214,(1,0,4):C.R2GC_777_217,(0,0,2):C.R2GC_303_114,(0,0,3):C.R2GC_303_115,(0,0,0):C.R2GC_774_212,(0,0,5):C.R2GC_777_216,(0,0,1):C.R2GC_774_214,(0,0,4):C.R2GC_777_217})

V_422 = CTVertex(name = 'V_422',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd3, P.YS3Qu1, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu3], [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu1, P.YS3Qu3] ] ],
                 couplings = {(1,0,0):C.R2GC_786_224,(1,0,1):C.R2GC_786_225,(1,0,2):C.R2GC_786_226,(0,0,0):C.R2GC_787_227,(0,0,1):C.R2GC_787_228,(0,0,2):C.R2GC_787_229})

V_423 = CTVertex(name = 'V_423',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd3, P.YS3Qu2, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu3], [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qu2, P.YS3Qu3] ] ],
                 couplings = {(1,0,0):C.R2GC_786_224,(1,0,1):C.R2GC_786_225,(1,0,2):C.R2GC_786_226,(0,0,0):C.R2GC_787_227,(0,0,1):C.R2GC_787_228,(0,0,2):C.R2GC_787_229})

V_424 = CTVertex(name = 'V_424',
                 type = 'R2',
                 particles = [ P.YS3Qd1, P.YS3Qd3__tilde__, P.YS3Qu1__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu3], [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu1, P.YS3Qu3] ] ],
                 couplings = {(1,0,0):C.R2GC_786_224,(1,0,1):C.R2GC_786_225,(1,0,2):C.R2GC_786_226,(0,0,0):C.R2GC_787_227,(0,0,1):C.R2GC_787_228,(0,0,2):C.R2GC_787_229})

V_425 = CTVertex(name = 'V_425',
                 type = 'R2',
                 particles = [ P.YS3Qd2, P.YS3Qd3__tilde__, P.YS3Qu2__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu3], [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qu2, P.YS3Qu3] ] ],
                 couplings = {(1,0,0):C.R2GC_786_224,(1,0,1):C.R2GC_786_225,(1,0,2):C.R2GC_786_226,(0,0,0):C.R2GC_787_227,(0,0,1):C.R2GC_787_228,(0,0,2):C.R2GC_787_229})

V_426 = CTVertex(name = 'V_426',
                 type = 'R2',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3Qd3, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qd3, P.YS3Qu1] ], [ [P.g, P.YS3Qd3, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_809_258,(1,0,8):C.R2GC_847_275,(1,0,1):C.R2GC_809_260,(1,0,7):C.R2GC_847_277,(1,0,2):C.R2GC_809_262,(1,0,6):C.R2GC_847_279,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_774_212,(0,0,8):C.R2GC_846_270,(0,0,1):C.R2GC_138_9,(0,0,7):C.R2GC_846_272,(0,0,2):C.R2GC_808_256,(0,0,6):C.R2GC_846_274})

V_427 = CTVertex(name = 'V_427',
                 type = 'R2',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3Qd3, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qd3, P.YS3Qu2] ], [ [P.g, P.YS3Qd3, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_809_258,(1,0,8):C.R2GC_847_275,(1,0,1):C.R2GC_809_260,(1,0,7):C.R2GC_847_277,(1,0,2):C.R2GC_809_262,(1,0,6):C.R2GC_847_279,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_774_212,(0,0,8):C.R2GC_846_270,(0,0,1):C.R2GC_138_9,(0,0,7):C.R2GC_846_272,(0,0,2):C.R2GC_808_256,(0,0,6):C.R2GC_846_274})

V_428 = CTVertex(name = 'V_428',
                 type = 'R2',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,7):C.R2GC_592_191,(1,0,8):C.R2GC_592_192,(1,0,0):C.R2GC_809_258,(1,0,4):C.R2GC_786_224,(1,0,11):C.R2GC_847_275,(1,0,1):C.R2GC_809_260,(1,0,5):C.R2GC_847_276,(1,0,10):C.R2GC_847_277,(1,0,2):C.R2GC_809_262,(1,0,6):C.R2GC_847_278,(1,0,9):C.R2GC_847_279,(0,0,3):C.R2GC_591_187,(0,0,7):C.R2GC_591_188,(0,0,8):C.R2GC_591_189,(0,0,0):C.R2GC_774_212,(0,0,4):C.R2GC_787_227,(0,0,11):C.R2GC_846_270,(0,0,1):C.R2GC_138_9,(0,0,5):C.R2GC_846_271,(0,0,10):C.R2GC_846_272,(0,0,2):C.R2GC_808_256,(0,0,6):C.R2GC_846_273,(0,0,9):C.R2GC_846_274})

V_429 = CTVertex(name = 'V_429',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd1, P.YS3Qd3] ], [ [P.g, P.YS3Qd1, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_793_236,(1,0,8):C.R2GC_805_251,(1,0,1):C.R2GC_793_238,(1,0,7):C.R2GC_805_252,(1,0,2):C.R2GC_793_240,(1,0,6):C.R2GC_805_253,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_792_230,(0,0,8):C.R2GC_804_248,(0,0,1):C.R2GC_792_232,(0,0,7):C.R2GC_804_249,(0,0,2):C.R2GC_792_234,(0,0,6):C.R2GC_804_250})

V_430 = CTVertex(name = 'V_430',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3Qd2, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd2, P.YS3Qd3] ], [ [P.g, P.YS3Qd2, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_793_236,(1,0,8):C.R2GC_805_251,(1,0,1):C.R2GC_793_238,(1,0,7):C.R2GC_805_252,(1,0,2):C.R2GC_793_240,(1,0,6):C.R2GC_805_253,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_792_230,(0,0,8):C.R2GC_804_248,(0,0,1):C.R2GC_792_232,(0,0,7):C.R2GC_804_249,(0,0,2):C.R2GC_792_234,(0,0,6):C.R2GC_804_250})

V_431 = CTVertex(name = 'V_431',
                 type = 'R2',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3Qd3 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_303_114,(1,0,3):C.R2GC_303_115,(1,0,0):C.R2GC_774_212,(1,0,5):C.R2GC_777_216,(1,0,1):C.R2GC_774_214,(1,0,4):C.R2GC_777_217,(0,0,2):C.R2GC_303_114,(0,0,3):C.R2GC_303_115,(0,0,0):C.R2GC_774_212,(0,0,5):C.R2GC_777_216,(0,0,1):C.R2GC_774_214,(0,0,4):C.R2GC_777_217})

V_432 = CTVertex(name = 'V_432',
                 type = 'R2',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qu1, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qu1, P.YS3u1] ], [ [P.g, P.YS3Qu1, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_853_286,(1,0,8):C.R2GC_857_295,(1,0,1):C.R2GC_853_288,(1,0,7):C.R2GC_857_296,(1,0,2):C.R2GC_853_290,(1,0,6):C.R2GC_857_297,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_852_280,(0,0,8):C.R2GC_856_292,(0,0,1):C.R2GC_852_282,(0,0,7):C.R2GC_856_293,(0,0,2):C.R2GC_852_284,(0,0,6):C.R2GC_856_294})

V_433 = CTVertex(name = 'V_433',
                 type = 'R2',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qu2, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qu2], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qu2, P.YS3u1] ], [ [P.g, P.YS3Qu2, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qu2, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_853_286,(1,0,8):C.R2GC_857_295,(1,0,1):C.R2GC_853_288,(1,0,7):C.R2GC_857_296,(1,0,2):C.R2GC_853_290,(1,0,6):C.R2GC_857_297,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_852_280,(0,0,8):C.R2GC_856_292,(0,0,1):C.R2GC_852_282,(0,0,7):C.R2GC_856_293,(0,0,2):C.R2GC_852_284,(0,0,6):C.R2GC_856_294})

V_434 = CTVertex(name = 'V_434',
                 type = 'R2',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu3], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qu3, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qu3], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qu3, P.YS3u1] ], [ [P.g, P.YS3Qu3, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qu3, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_853_286,(1,0,8):C.R2GC_857_295,(1,0,1):C.R2GC_853_288,(1,0,7):C.R2GC_857_296,(1,0,2):C.R2GC_853_290,(1,0,6):C.R2GC_857_297,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_852_280,(0,0,8):C.R2GC_856_292,(0,0,1):C.R2GC_852_282,(0,0,7):C.R2GC_856_293,(0,0,2):C.R2GC_852_284,(0,0,6):C.R2GC_856_294})

V_435 = CTVertex(name = 'V_435',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qd1, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qd1, P.YS3u1] ], [ [P.g, P.YS3Qd1, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_809_258,(1,0,8):C.R2GC_809_259,(1,0,1):C.R2GC_809_260,(1,0,7):C.R2GC_809_261,(1,0,2):C.R2GC_809_262,(1,0,6):C.R2GC_809_263,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_774_212,(0,0,8):C.R2GC_808_254,(0,0,1):C.R2GC_138_9,(0,0,7):C.R2GC_808_255,(0,0,2):C.R2GC_808_256,(0,0,6):C.R2GC_808_257})

V_436 = CTVertex(name = 'V_436',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qd2, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qd2, P.YS3u1] ], [ [P.g, P.YS3Qd2, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_809_258,(1,0,8):C.R2GC_809_259,(1,0,1):C.R2GC_809_260,(1,0,7):C.R2GC_809_261,(1,0,2):C.R2GC_809_262,(1,0,6):C.R2GC_809_263,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_774_212,(0,0,8):C.R2GC_808_254,(0,0,1):C.R2GC_138_9,(0,0,7):C.R2GC_808_255,(0,0,2):C.R2GC_808_256,(0,0,6):C.R2GC_808_257})

V_437 = CTVertex(name = 'V_437',
                 type = 'R2',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qd3, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qd3, P.YS3u1] ], [ [P.g, P.YS3Qd3, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_809_258,(1,0,8):C.R2GC_809_259,(1,0,1):C.R2GC_809_260,(1,0,7):C.R2GC_809_261,(1,0,2):C.R2GC_809_262,(1,0,6):C.R2GC_809_263,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_774_212,(0,0,8):C.R2GC_808_254,(0,0,1):C.R2GC_138_9,(0,0,7):C.R2GC_808_255,(0,0,2):C.R2GC_808_256,(0,0,6):C.R2GC_808_257})

V_438 = CTVertex(name = 'V_438',
                 type = 'R2',
                 particles = [ P.YS3u1__tilde__, P.YS3u1__tilde__, P.YS3u1, P.YS3u1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3u1] ], [ [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_303_114,(1,0,3):C.R2GC_303_115,(1,0,0):C.R2GC_780_218,(1,0,5):C.R2GC_783_222,(1,0,1):C.R2GC_780_220,(1,0,4):C.R2GC_783_223,(0,0,2):C.R2GC_303_114,(0,0,3):C.R2GC_303_115,(0,0,0):C.R2GC_780_218,(0,0,5):C.R2GC_783_222,(0,0,1):C.R2GC_780_220,(0,0,4):C.R2GC_783_223})

V_439 = CTVertex(name = 'V_439',
                 type = 'R2',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qu1, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qu1, P.YS3u2] ], [ [P.g, P.YS3Qu1, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_853_286,(1,0,8):C.R2GC_857_295,(1,0,1):C.R2GC_853_288,(1,0,7):C.R2GC_857_296,(1,0,2):C.R2GC_853_290,(1,0,6):C.R2GC_857_297,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_852_280,(0,0,8):C.R2GC_856_292,(0,0,1):C.R2GC_852_282,(0,0,7):C.R2GC_856_293,(0,0,2):C.R2GC_852_284,(0,0,6):C.R2GC_856_294})

V_440 = CTVertex(name = 'V_440',
                 type = 'R2',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qu2, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qu2], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qu2, P.YS3u2] ], [ [P.g, P.YS3Qu2, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qu2, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_853_286,(1,0,8):C.R2GC_857_295,(1,0,1):C.R2GC_853_288,(1,0,7):C.R2GC_857_296,(1,0,2):C.R2GC_853_290,(1,0,6):C.R2GC_857_297,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_852_280,(0,0,8):C.R2GC_856_292,(0,0,1):C.R2GC_852_282,(0,0,7):C.R2GC_856_293,(0,0,2):C.R2GC_852_284,(0,0,6):C.R2GC_856_294})

V_441 = CTVertex(name = 'V_441',
                 type = 'R2',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu3], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qu3, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qu3], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qu3, P.YS3u2] ], [ [P.g, P.YS3Qu3, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qu3, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_853_286,(1,0,8):C.R2GC_857_295,(1,0,1):C.R2GC_853_288,(1,0,7):C.R2GC_857_296,(1,0,2):C.R2GC_853_290,(1,0,6):C.R2GC_857_297,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_852_280,(0,0,8):C.R2GC_856_292,(0,0,1):C.R2GC_852_282,(0,0,7):C.R2GC_856_293,(0,0,2):C.R2GC_852_284,(0,0,6):C.R2GC_856_294})

V_442 = CTVertex(name = 'V_442',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qd1, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qd1, P.YS3u2] ], [ [P.g, P.YS3Qd1, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_809_258,(1,0,8):C.R2GC_809_259,(1,0,1):C.R2GC_809_260,(1,0,7):C.R2GC_809_261,(1,0,2):C.R2GC_809_262,(1,0,6):C.R2GC_809_263,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_774_212,(0,0,8):C.R2GC_808_254,(0,0,1):C.R2GC_138_9,(0,0,7):C.R2GC_808_255,(0,0,2):C.R2GC_808_256,(0,0,6):C.R2GC_808_257})

V_443 = CTVertex(name = 'V_443',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qd2, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qd2, P.YS3u2] ], [ [P.g, P.YS3Qd2, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_809_258,(1,0,8):C.R2GC_809_259,(1,0,1):C.R2GC_809_260,(1,0,7):C.R2GC_809_261,(1,0,2):C.R2GC_809_262,(1,0,6):C.R2GC_809_263,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_774_212,(0,0,8):C.R2GC_808_254,(0,0,1):C.R2GC_138_9,(0,0,7):C.R2GC_808_255,(0,0,2):C.R2GC_808_256,(0,0,6):C.R2GC_808_257})

V_444 = CTVertex(name = 'V_444',
                 type = 'R2',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qd3, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qd3, P.YS3u2] ], [ [P.g, P.YS3Qd3, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_809_258,(1,0,8):C.R2GC_809_259,(1,0,1):C.R2GC_809_260,(1,0,7):C.R2GC_809_261,(1,0,2):C.R2GC_809_262,(1,0,6):C.R2GC_809_263,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_774_212,(0,0,8):C.R2GC_808_254,(0,0,1):C.R2GC_138_9,(0,0,7):C.R2GC_808_255,(0,0,2):C.R2GC_808_256,(0,0,6):C.R2GC_808_257})

V_445 = CTVertex(name = 'V_445',
                 type = 'R2',
                 particles = [ P.YS3u1__tilde__, P.YS3u1, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u1], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3u1, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3u1], [P.g, P.YS3u2] ], [ [P.g, P.YS3u1, P.YS3u2] ], [ [P.g, P.YS3u1, P.YS3u2, P.Z] ], [ [P.g, P.YS3u1, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_853_286,(1,0,8):C.R2GC_907_305,(1,0,1):C.R2GC_853_288,(1,0,7):C.R2GC_907_306,(1,0,2):C.R2GC_853_290,(1,0,6):C.R2GC_907_307,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_852_280,(0,0,8):C.R2GC_906_302,(0,0,1):C.R2GC_852_282,(0,0,7):C.R2GC_906_303,(0,0,2):C.R2GC_852_284,(0,0,6):C.R2GC_906_304})

V_446 = CTVertex(name = 'V_446',
                 type = 'R2',
                 particles = [ P.YS3u2__tilde__, P.YS3u2__tilde__, P.YS3u2, P.YS3u2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3u2] ], [ [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_303_114,(1,0,3):C.R2GC_303_115,(1,0,0):C.R2GC_780_218,(1,0,5):C.R2GC_783_222,(1,0,1):C.R2GC_780_220,(1,0,4):C.R2GC_783_223,(0,0,2):C.R2GC_303_114,(0,0,3):C.R2GC_303_115,(0,0,0):C.R2GC_780_218,(0,0,5):C.R2GC_783_222,(0,0,1):C.R2GC_780_220,(0,0,4):C.R2GC_783_223})

V_447 = CTVertex(name = 'V_447',
                 type = 'R2',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qu1, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qu1, P.YS3u3] ], [ [P.g, P.YS3Qu1, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_853_286,(1,0,8):C.R2GC_857_295,(1,0,1):C.R2GC_853_288,(1,0,7):C.R2GC_857_296,(1,0,2):C.R2GC_853_290,(1,0,6):C.R2GC_857_297,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_852_280,(0,0,8):C.R2GC_856_292,(0,0,1):C.R2GC_852_282,(0,0,7):C.R2GC_856_293,(0,0,2):C.R2GC_852_284,(0,0,6):C.R2GC_856_294})

V_448 = CTVertex(name = 'V_448',
                 type = 'R2',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qu2, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qu2], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qu2, P.YS3u3] ], [ [P.g, P.YS3Qu2, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qu2, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_853_286,(1,0,8):C.R2GC_857_295,(1,0,1):C.R2GC_853_288,(1,0,7):C.R2GC_857_296,(1,0,2):C.R2GC_853_290,(1,0,6):C.R2GC_857_297,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_852_280,(0,0,8):C.R2GC_856_292,(0,0,1):C.R2GC_852_282,(0,0,7):C.R2GC_856_293,(0,0,2):C.R2GC_852_284,(0,0,6):C.R2GC_856_294})

V_449 = CTVertex(name = 'V_449',
                 type = 'R2',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu3], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qu3, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qu3], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qu3, P.YS3u3] ], [ [P.g, P.YS3Qu3, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qu3, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_853_286,(1,0,8):C.R2GC_857_295,(1,0,1):C.R2GC_853_288,(1,0,7):C.R2GC_857_296,(1,0,2):C.R2GC_853_290,(1,0,6):C.R2GC_857_297,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_852_280,(0,0,8):C.R2GC_856_292,(0,0,1):C.R2GC_852_282,(0,0,7):C.R2GC_856_293,(0,0,2):C.R2GC_852_284,(0,0,6):C.R2GC_856_294})

V_450 = CTVertex(name = 'V_450',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qd1, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qd1, P.YS3u3] ], [ [P.g, P.YS3Qd1, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_809_258,(1,0,8):C.R2GC_809_259,(1,0,1):C.R2GC_809_260,(1,0,7):C.R2GC_809_261,(1,0,2):C.R2GC_809_262,(1,0,6):C.R2GC_809_263,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_774_212,(0,0,8):C.R2GC_808_254,(0,0,1):C.R2GC_138_9,(0,0,7):C.R2GC_808_255,(0,0,2):C.R2GC_808_256,(0,0,6):C.R2GC_808_257})

V_451 = CTVertex(name = 'V_451',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qd2, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qd2, P.YS3u3] ], [ [P.g, P.YS3Qd2, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_809_258,(1,0,8):C.R2GC_809_259,(1,0,1):C.R2GC_809_260,(1,0,7):C.R2GC_809_261,(1,0,2):C.R2GC_809_262,(1,0,6):C.R2GC_809_263,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_774_212,(0,0,8):C.R2GC_808_254,(0,0,1):C.R2GC_138_9,(0,0,7):C.R2GC_808_255,(0,0,2):C.R2GC_808_256,(0,0,6):C.R2GC_808_257})

V_452 = CTVertex(name = 'V_452',
                 type = 'R2',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qd3, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qd3, P.YS3u3] ], [ [P.g, P.YS3Qd3, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_809_258,(1,0,8):C.R2GC_809_259,(1,0,1):C.R2GC_809_260,(1,0,7):C.R2GC_809_261,(1,0,2):C.R2GC_809_262,(1,0,6):C.R2GC_809_263,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_774_212,(0,0,8):C.R2GC_808_254,(0,0,1):C.R2GC_138_9,(0,0,7):C.R2GC_808_255,(0,0,2):C.R2GC_808_256,(0,0,6):C.R2GC_808_257})

V_453 = CTVertex(name = 'V_453',
                 type = 'R2',
                 particles = [ P.YS3u1__tilde__, P.YS3u1, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u1], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3u1, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3u1], [P.g, P.YS3u3] ], [ [P.g, P.YS3u1, P.YS3u3] ], [ [P.g, P.YS3u1, P.YS3u3, P.Z] ], [ [P.g, P.YS3u1, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_853_286,(1,0,8):C.R2GC_907_305,(1,0,1):C.R2GC_853_288,(1,0,7):C.R2GC_907_306,(1,0,2):C.R2GC_853_290,(1,0,6):C.R2GC_907_307,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_852_280,(0,0,8):C.R2GC_906_302,(0,0,1):C.R2GC_852_282,(0,0,7):C.R2GC_906_303,(0,0,2):C.R2GC_852_284,(0,0,6):C.R2GC_906_304})

V_454 = CTVertex(name = 'V_454',
                 type = 'R2',
                 particles = [ P.YS3u2__tilde__, P.YS3u2, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u2], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3u2, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3u2], [P.g, P.YS3u3] ], [ [P.g, P.YS3u2, P.YS3u3] ], [ [P.g, P.YS3u2, P.YS3u3, P.Z] ], [ [P.g, P.YS3u2, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_853_286,(1,0,8):C.R2GC_907_305,(1,0,1):C.R2GC_853_288,(1,0,7):C.R2GC_907_306,(1,0,2):C.R2GC_853_290,(1,0,6):C.R2GC_907_307,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_852_280,(0,0,8):C.R2GC_906_302,(0,0,1):C.R2GC_852_282,(0,0,7):C.R2GC_906_303,(0,0,2):C.R2GC_852_284,(0,0,6):C.R2GC_906_304})

V_455 = CTVertex(name = 'V_455',
                 type = 'R2',
                 particles = [ P.YS3u3__tilde__, P.YS3u3__tilde__, P.YS3u3, P.YS3u3 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3u3] ], [ [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_303_114,(1,0,3):C.R2GC_303_115,(1,0,0):C.R2GC_780_218,(1,0,5):C.R2GC_783_222,(1,0,1):C.R2GC_780_220,(1,0,4):C.R2GC_783_223,(0,0,2):C.R2GC_303_114,(0,0,3):C.R2GC_303_115,(0,0,0):C.R2GC_780_218,(0,0,5):C.R2GC_783_222,(0,0,1):C.R2GC_780_220,(0,0,4):C.R2GC_783_223})

V_456 = CTVertex(name = 'V_456',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3d1, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3d1, P.YS3Qu1] ], [ [P.g, P.YS3d1, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_809_258,(1,0,8):C.R2GC_841_267,(1,0,1):C.R2GC_809_260,(1,0,7):C.R2GC_841_268,(1,0,2):C.R2GC_809_262,(1,0,6):C.R2GC_841_269,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_774_212,(0,0,8):C.R2GC_840_264,(0,0,1):C.R2GC_138_9,(0,0,7):C.R2GC_840_265,(0,0,2):C.R2GC_808_256,(0,0,6):C.R2GC_840_266})

V_457 = CTVertex(name = 'V_457',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3d1, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3d1, P.YS3Qu2] ], [ [P.g, P.YS3d1, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_809_258,(1,0,8):C.R2GC_841_267,(1,0,1):C.R2GC_809_260,(1,0,7):C.R2GC_841_268,(1,0,2):C.R2GC_809_262,(1,0,6):C.R2GC_841_269,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_774_212,(0,0,8):C.R2GC_840_264,(0,0,1):C.R2GC_138_9,(0,0,7):C.R2GC_840_265,(0,0,2):C.R2GC_808_256,(0,0,6):C.R2GC_840_266})

V_458 = CTVertex(name = 'V_458',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3d1, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3d1, P.YS3Qu3] ], [ [P.g, P.YS3d1, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_809_258,(1,0,8):C.R2GC_841_267,(1,0,1):C.R2GC_809_260,(1,0,7):C.R2GC_841_268,(1,0,2):C.R2GC_809_262,(1,0,6):C.R2GC_841_269,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_774_212,(0,0,8):C.R2GC_840_264,(0,0,1):C.R2GC_138_9,(0,0,7):C.R2GC_840_265,(0,0,2):C.R2GC_808_256,(0,0,6):C.R2GC_840_266})

V_459 = CTVertex(name = 'V_459',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qd1] ], [ [P.a, P.g, P.YS3d1, P.YS3Qd1] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qd1] ], [ [P.g, P.YS3d1, P.YS3Qd1] ], [ [P.g, P.YS3d1, P.YS3Qd1, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qd1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_793_236,(1,0,8):C.R2GC_799_245,(1,0,1):C.R2GC_793_238,(1,0,7):C.R2GC_799_246,(1,0,2):C.R2GC_793_240,(1,0,6):C.R2GC_799_247,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_792_230,(0,0,8):C.R2GC_798_242,(0,0,1):C.R2GC_792_232,(0,0,7):C.R2GC_798_243,(0,0,2):C.R2GC_792_234,(0,0,6):C.R2GC_798_244})

V_460 = CTVertex(name = 'V_460',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qd2] ], [ [P.a, P.g, P.YS3d1, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qd2] ], [ [P.g, P.YS3d1, P.YS3Qd2] ], [ [P.g, P.YS3d1, P.YS3Qd2, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_793_236,(1,0,8):C.R2GC_799_245,(1,0,1):C.R2GC_793_238,(1,0,7):C.R2GC_799_246,(1,0,2):C.R2GC_793_240,(1,0,6):C.R2GC_799_247,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_792_230,(0,0,8):C.R2GC_798_242,(0,0,1):C.R2GC_792_232,(0,0,7):C.R2GC_798_243,(0,0,2):C.R2GC_792_234,(0,0,6):C.R2GC_798_244})

V_461 = CTVertex(name = 'V_461',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3d1, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3d1, P.YS3Qd3] ], [ [P.g, P.YS3d1, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_793_236,(1,0,8):C.R2GC_799_245,(1,0,1):C.R2GC_793_238,(1,0,7):C.R2GC_799_246,(1,0,2):C.R2GC_793_240,(1,0,6):C.R2GC_799_247,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_792_230,(0,0,8):C.R2GC_798_242,(0,0,1):C.R2GC_792_232,(0,0,7):C.R2GC_798_243,(0,0,2):C.R2GC_792_234,(0,0,6):C.R2GC_798_244})

V_462 = CTVertex(name = 'V_462',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3d1, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3u1] ], [ [P.g, P.YS3d1, P.YS3u1] ], [ [P.g, P.YS3d1, P.YS3u1, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_809_258,(1,0,8):C.R2GC_901_299,(1,0,1):C.R2GC_809_260,(1,0,7):C.R2GC_901_300,(1,0,2):C.R2GC_809_262,(1,0,6):C.R2GC_901_301,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_774_212,(0,0,8):C.R2GC_774_213,(0,0,1):C.R2GC_138_9,(0,0,7):C.R2GC_143_40,(0,0,2):C.R2GC_808_256,(0,0,6):C.R2GC_900_298})

V_463 = CTVertex(name = 'V_463',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3d1, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3u2] ], [ [P.g, P.YS3d1, P.YS3u2] ], [ [P.g, P.YS3d1, P.YS3u2, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_809_258,(1,0,8):C.R2GC_901_299,(1,0,1):C.R2GC_809_260,(1,0,7):C.R2GC_901_300,(1,0,2):C.R2GC_809_262,(1,0,6):C.R2GC_901_301,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_774_212,(0,0,8):C.R2GC_774_213,(0,0,1):C.R2GC_138_9,(0,0,7):C.R2GC_143_40,(0,0,2):C.R2GC_808_256,(0,0,6):C.R2GC_900_298})

V_464 = CTVertex(name = 'V_464',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3d1, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3u3] ], [ [P.g, P.YS3d1, P.YS3u3] ], [ [P.g, P.YS3d1, P.YS3u3, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_809_258,(1,0,8):C.R2GC_901_299,(1,0,1):C.R2GC_809_260,(1,0,7):C.R2GC_901_300,(1,0,2):C.R2GC_809_262,(1,0,6):C.R2GC_901_301,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_774_212,(0,0,8):C.R2GC_774_213,(0,0,1):C.R2GC_138_9,(0,0,7):C.R2GC_143_40,(0,0,2):C.R2GC_808_256,(0,0,6):C.R2GC_900_298})

V_465 = CTVertex(name = 'V_465',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1__tilde__, P.YS3d1, P.YS3d1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1] ], [ [P.g] ], [ [P.g, P.YS3d1] ], [ [P.g, P.YS3d1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_303_114,(1,0,3):C.R2GC_303_115,(1,0,0):C.R2GC_774_212,(1,0,5):C.R2GC_774_213,(1,0,1):C.R2GC_774_214,(1,0,4):C.R2GC_774_215,(0,0,2):C.R2GC_303_114,(0,0,3):C.R2GC_303_115,(0,0,0):C.R2GC_774_212,(0,0,5):C.R2GC_774_213,(0,0,1):C.R2GC_774_214,(0,0,4):C.R2GC_774_215})

V_466 = CTVertex(name = 'V_466',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3d2, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3d2, P.YS3Qu1] ], [ [P.g, P.YS3d2, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_809_258,(1,0,8):C.R2GC_841_267,(1,0,1):C.R2GC_809_260,(1,0,7):C.R2GC_841_268,(1,0,2):C.R2GC_809_262,(1,0,6):C.R2GC_841_269,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_774_212,(0,0,8):C.R2GC_840_264,(0,0,1):C.R2GC_138_9,(0,0,7):C.R2GC_840_265,(0,0,2):C.R2GC_808_256,(0,0,6):C.R2GC_840_266})

V_467 = CTVertex(name = 'V_467',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3d2, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3d2, P.YS3Qu2] ], [ [P.g, P.YS3d2, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_809_258,(1,0,8):C.R2GC_841_267,(1,0,1):C.R2GC_809_260,(1,0,7):C.R2GC_841_268,(1,0,2):C.R2GC_809_262,(1,0,6):C.R2GC_841_269,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_774_212,(0,0,8):C.R2GC_840_264,(0,0,1):C.R2GC_138_9,(0,0,7):C.R2GC_840_265,(0,0,2):C.R2GC_808_256,(0,0,6):C.R2GC_840_266})

V_468 = CTVertex(name = 'V_468',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3d2, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3d2, P.YS3Qu3] ], [ [P.g, P.YS3d2, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_809_258,(1,0,8):C.R2GC_841_267,(1,0,1):C.R2GC_809_260,(1,0,7):C.R2GC_841_268,(1,0,2):C.R2GC_809_262,(1,0,6):C.R2GC_841_269,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_774_212,(0,0,8):C.R2GC_840_264,(0,0,1):C.R2GC_138_9,(0,0,7):C.R2GC_840_265,(0,0,2):C.R2GC_808_256,(0,0,6):C.R2GC_840_266})

V_469 = CTVertex(name = 'V_469',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qd1] ], [ [P.a, P.g, P.YS3d2, P.YS3Qd1] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qd1] ], [ [P.g, P.YS3d2, P.YS3Qd1] ], [ [P.g, P.YS3d2, P.YS3Qd1, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qd1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_793_236,(1,0,8):C.R2GC_799_245,(1,0,1):C.R2GC_793_238,(1,0,7):C.R2GC_799_246,(1,0,2):C.R2GC_793_240,(1,0,6):C.R2GC_799_247,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_792_230,(0,0,8):C.R2GC_798_242,(0,0,1):C.R2GC_792_232,(0,0,7):C.R2GC_798_243,(0,0,2):C.R2GC_792_234,(0,0,6):C.R2GC_798_244})

V_470 = CTVertex(name = 'V_470',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qd2] ], [ [P.a, P.g, P.YS3d2, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qd2] ], [ [P.g, P.YS3d2, P.YS3Qd2] ], [ [P.g, P.YS3d2, P.YS3Qd2, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_793_236,(1,0,8):C.R2GC_799_245,(1,0,1):C.R2GC_793_238,(1,0,7):C.R2GC_799_246,(1,0,2):C.R2GC_793_240,(1,0,6):C.R2GC_799_247,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_792_230,(0,0,8):C.R2GC_798_242,(0,0,1):C.R2GC_792_232,(0,0,7):C.R2GC_798_243,(0,0,2):C.R2GC_792_234,(0,0,6):C.R2GC_798_244})

V_471 = CTVertex(name = 'V_471',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3d2, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3d2, P.YS3Qd3] ], [ [P.g, P.YS3d2, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_793_236,(1,0,8):C.R2GC_799_245,(1,0,1):C.R2GC_793_238,(1,0,7):C.R2GC_799_246,(1,0,2):C.R2GC_793_240,(1,0,6):C.R2GC_799_247,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_792_230,(0,0,8):C.R2GC_798_242,(0,0,1):C.R2GC_792_232,(0,0,7):C.R2GC_798_243,(0,0,2):C.R2GC_792_234,(0,0,6):C.R2GC_798_244})

V_472 = CTVertex(name = 'V_472',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3d2, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3u1] ], [ [P.g, P.YS3d2, P.YS3u1] ], [ [P.g, P.YS3d2, P.YS3u1, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_809_258,(1,0,8):C.R2GC_901_299,(1,0,1):C.R2GC_809_260,(1,0,7):C.R2GC_901_300,(1,0,2):C.R2GC_809_262,(1,0,6):C.R2GC_901_301,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_774_212,(0,0,8):C.R2GC_774_213,(0,0,1):C.R2GC_138_9,(0,0,7):C.R2GC_143_40,(0,0,2):C.R2GC_808_256,(0,0,6):C.R2GC_900_298})

V_473 = CTVertex(name = 'V_473',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3d2, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3u2] ], [ [P.g, P.YS3d2, P.YS3u2] ], [ [P.g, P.YS3d2, P.YS3u2, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_809_258,(1,0,8):C.R2GC_901_299,(1,0,1):C.R2GC_809_260,(1,0,7):C.R2GC_901_300,(1,0,2):C.R2GC_809_262,(1,0,6):C.R2GC_901_301,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_774_212,(0,0,8):C.R2GC_774_213,(0,0,1):C.R2GC_138_9,(0,0,7):C.R2GC_143_40,(0,0,2):C.R2GC_808_256,(0,0,6):C.R2GC_900_298})

V_474 = CTVertex(name = 'V_474',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3d2, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3u3] ], [ [P.g, P.YS3d2, P.YS3u3] ], [ [P.g, P.YS3d2, P.YS3u3, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_809_258,(1,0,8):C.R2GC_901_299,(1,0,1):C.R2GC_809_260,(1,0,7):C.R2GC_901_300,(1,0,2):C.R2GC_809_262,(1,0,6):C.R2GC_901_301,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_774_212,(0,0,8):C.R2GC_774_213,(0,0,1):C.R2GC_138_9,(0,0,7):C.R2GC_143_40,(0,0,2):C.R2GC_808_256,(0,0,6):C.R2GC_900_298})

V_475 = CTVertex(name = 'V_475',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3d2] ], [ [P.a, P.g, P.YS3d1, P.YS3d2] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3d2] ], [ [P.g, P.YS3d1, P.YS3d2] ], [ [P.g, P.YS3d1, P.YS3d2, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3d2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_793_236,(1,0,8):C.R2GC_793_237,(1,0,1):C.R2GC_793_238,(1,0,7):C.R2GC_793_239,(1,0,2):C.R2GC_793_240,(1,0,6):C.R2GC_793_241,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_792_230,(0,0,8):C.R2GC_792_231,(0,0,1):C.R2GC_792_232,(0,0,7):C.R2GC_792_233,(0,0,2):C.R2GC_792_234,(0,0,6):C.R2GC_792_235})

V_476 = CTVertex(name = 'V_476',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2__tilde__, P.YS3d2, P.YS3d2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2] ], [ [P.g] ], [ [P.g, P.YS3d2] ], [ [P.g, P.YS3d2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_303_114,(1,0,3):C.R2GC_303_115,(1,0,0):C.R2GC_774_212,(1,0,5):C.R2GC_774_213,(1,0,1):C.R2GC_774_214,(1,0,4):C.R2GC_774_215,(0,0,2):C.R2GC_303_114,(0,0,3):C.R2GC_303_115,(0,0,0):C.R2GC_774_212,(0,0,5):C.R2GC_774_213,(0,0,1):C.R2GC_774_214,(0,0,4):C.R2GC_774_215})

V_477 = CTVertex(name = 'V_477',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3d3, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3d3, P.YS3Qu1] ], [ [P.g, P.YS3d3, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_809_258,(1,0,8):C.R2GC_841_267,(1,0,1):C.R2GC_809_260,(1,0,7):C.R2GC_841_268,(1,0,2):C.R2GC_809_262,(1,0,6):C.R2GC_841_269,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_774_212,(0,0,8):C.R2GC_840_264,(0,0,1):C.R2GC_138_9,(0,0,7):C.R2GC_840_265,(0,0,2):C.R2GC_808_256,(0,0,6):C.R2GC_840_266})

V_478 = CTVertex(name = 'V_478',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3d3, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3d3, P.YS3Qu2] ], [ [P.g, P.YS3d3, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_809_258,(1,0,8):C.R2GC_841_267,(1,0,1):C.R2GC_809_260,(1,0,7):C.R2GC_841_268,(1,0,2):C.R2GC_809_262,(1,0,6):C.R2GC_841_269,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_774_212,(0,0,8):C.R2GC_840_264,(0,0,1):C.R2GC_138_9,(0,0,7):C.R2GC_840_265,(0,0,2):C.R2GC_808_256,(0,0,6):C.R2GC_840_266})

V_479 = CTVertex(name = 'V_479',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3d3, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3d3, P.YS3Qu3] ], [ [P.g, P.YS3d3, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_809_258,(1,0,8):C.R2GC_841_267,(1,0,1):C.R2GC_809_260,(1,0,7):C.R2GC_841_268,(1,0,2):C.R2GC_809_262,(1,0,6):C.R2GC_841_269,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_774_212,(0,0,8):C.R2GC_840_264,(0,0,1):C.R2GC_138_9,(0,0,7):C.R2GC_840_265,(0,0,2):C.R2GC_808_256,(0,0,6):C.R2GC_840_266})

V_480 = CTVertex(name = 'V_480',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qd1] ], [ [P.a, P.g, P.YS3d3, P.YS3Qd1] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qd1] ], [ [P.g, P.YS3d3, P.YS3Qd1] ], [ [P.g, P.YS3d3, P.YS3Qd1, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qd1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_793_236,(1,0,8):C.R2GC_799_245,(1,0,1):C.R2GC_793_238,(1,0,7):C.R2GC_799_246,(1,0,2):C.R2GC_793_240,(1,0,6):C.R2GC_799_247,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_792_230,(0,0,8):C.R2GC_798_242,(0,0,1):C.R2GC_792_232,(0,0,7):C.R2GC_798_243,(0,0,2):C.R2GC_792_234,(0,0,6):C.R2GC_798_244})

V_481 = CTVertex(name = 'V_481',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qd2] ], [ [P.a, P.g, P.YS3d3, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qd2] ], [ [P.g, P.YS3d3, P.YS3Qd2] ], [ [P.g, P.YS3d3, P.YS3Qd2, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_793_236,(1,0,8):C.R2GC_799_245,(1,0,1):C.R2GC_793_238,(1,0,7):C.R2GC_799_246,(1,0,2):C.R2GC_793_240,(1,0,6):C.R2GC_799_247,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_792_230,(0,0,8):C.R2GC_798_242,(0,0,1):C.R2GC_792_232,(0,0,7):C.R2GC_798_243,(0,0,2):C.R2GC_792_234,(0,0,6):C.R2GC_798_244})

V_482 = CTVertex(name = 'V_482',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3d3, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3d3, P.YS3Qd3] ], [ [P.g, P.YS3d3, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_793_236,(1,0,8):C.R2GC_799_245,(1,0,1):C.R2GC_793_238,(1,0,7):C.R2GC_799_246,(1,0,2):C.R2GC_793_240,(1,0,6):C.R2GC_799_247,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_792_230,(0,0,8):C.R2GC_798_242,(0,0,1):C.R2GC_792_232,(0,0,7):C.R2GC_798_243,(0,0,2):C.R2GC_792_234,(0,0,6):C.R2GC_798_244})

V_483 = CTVertex(name = 'V_483',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3d3, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3u1] ], [ [P.g, P.YS3d3, P.YS3u1] ], [ [P.g, P.YS3d3, P.YS3u1, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_809_258,(1,0,8):C.R2GC_901_299,(1,0,1):C.R2GC_809_260,(1,0,7):C.R2GC_901_300,(1,0,2):C.R2GC_809_262,(1,0,6):C.R2GC_901_301,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_774_212,(0,0,8):C.R2GC_774_213,(0,0,1):C.R2GC_138_9,(0,0,7):C.R2GC_143_40,(0,0,2):C.R2GC_808_256,(0,0,6):C.R2GC_900_298})

V_484 = CTVertex(name = 'V_484',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3d3, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3u2] ], [ [P.g, P.YS3d3, P.YS3u2] ], [ [P.g, P.YS3d3, P.YS3u2, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_809_258,(1,0,8):C.R2GC_901_299,(1,0,1):C.R2GC_809_260,(1,0,7):C.R2GC_901_300,(1,0,2):C.R2GC_809_262,(1,0,6):C.R2GC_901_301,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_774_212,(0,0,8):C.R2GC_774_213,(0,0,1):C.R2GC_138_9,(0,0,7):C.R2GC_143_40,(0,0,2):C.R2GC_808_256,(0,0,6):C.R2GC_900_298})

V_485 = CTVertex(name = 'V_485',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3d3, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3u3] ], [ [P.g, P.YS3d3, P.YS3u3] ], [ [P.g, P.YS3d3, P.YS3u3, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_809_258,(1,0,8):C.R2GC_901_299,(1,0,1):C.R2GC_809_260,(1,0,7):C.R2GC_901_300,(1,0,2):C.R2GC_809_262,(1,0,6):C.R2GC_901_301,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_774_212,(0,0,8):C.R2GC_774_213,(0,0,1):C.R2GC_138_9,(0,0,7):C.R2GC_143_40,(0,0,2):C.R2GC_808_256,(0,0,6):C.R2GC_900_298})

V_486 = CTVertex(name = 'V_486',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3d3] ], [ [P.a, P.g, P.YS3d1, P.YS3d3] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3d3] ], [ [P.g, P.YS3d1, P.YS3d3] ], [ [P.g, P.YS3d1, P.YS3d3, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3d3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_793_236,(1,0,8):C.R2GC_793_237,(1,0,1):C.R2GC_793_238,(1,0,7):C.R2GC_793_239,(1,0,2):C.R2GC_793_240,(1,0,6):C.R2GC_793_241,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_792_230,(0,0,8):C.R2GC_792_231,(0,0,1):C.R2GC_792_232,(0,0,7):C.R2GC_792_233,(0,0,2):C.R2GC_792_234,(0,0,6):C.R2GC_792_235})

V_487 = CTVertex(name = 'V_487',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3d3] ], [ [P.a, P.g, P.YS3d2, P.YS3d3] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3d3] ], [ [P.g, P.YS3d2, P.YS3d3] ], [ [P.g, P.YS3d2, P.YS3d3, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3d3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_592_190,(1,0,4):C.R2GC_592_191,(1,0,5):C.R2GC_592_192,(1,0,0):C.R2GC_793_236,(1,0,8):C.R2GC_793_237,(1,0,1):C.R2GC_793_238,(1,0,7):C.R2GC_793_239,(1,0,2):C.R2GC_793_240,(1,0,6):C.R2GC_793_241,(0,0,3):C.R2GC_591_187,(0,0,4):C.R2GC_591_188,(0,0,5):C.R2GC_591_189,(0,0,0):C.R2GC_792_230,(0,0,8):C.R2GC_792_231,(0,0,1):C.R2GC_792_232,(0,0,7):C.R2GC_792_233,(0,0,2):C.R2GC_792_234,(0,0,6):C.R2GC_792_235})

V_488 = CTVertex(name = 'V_488',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3__tilde__, P.YS3d3, P.YS3d3 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3] ], [ [P.g] ], [ [P.g, P.YS3d3] ], [ [P.g, P.YS3d3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_303_114,(1,0,3):C.R2GC_303_115,(1,0,0):C.R2GC_774_212,(1,0,5):C.R2GC_774_213,(1,0,1):C.R2GC_774_214,(1,0,4):C.R2GC_774_215,(0,0,2):C.R2GC_303_114,(0,0,3):C.R2GC_303_115,(0,0,0):C.R2GC_774_212,(0,0,5):C.R2GC_774_213,(0,0,1):C.R2GC_774_214,(0,0,4):C.R2GC_774_215})

V_489 = CTVertex(name = 'V_489',
                 type = 'UV',
                 particles = [ P.g, P.g, P.g ],
                 color = [ 'f(1,2,3)' ],
                 lorentz = [ L.VVV2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_268_185,(0,0,1):C.UVGC_268_186,(0,0,2):C.UVGC_268_187,(0,0,3):C.UVGC_268_188,(0,0,4):C.UVGC_268_189,(0,0,5):C.UVGC_268_190,(0,0,6):C.UVGC_268_191,(0,0,7):C.UVGC_268_192,(0,0,8):C.UVGC_268_193,(0,0,9):C.UVGC_268_194,(0,0,10):C.UVGC_268_195,(0,0,11):C.UVGC_268_196,(0,0,12):C.UVGC_268_197,(0,0,13):C.UVGC_268_198,(0,0,14):C.UVGC_268_199,(0,0,15):C.UVGC_268_200,(0,0,16):C.UVGC_268_201,(0,0,17):C.UVGC_268_202,(0,0,18):C.UVGC_268_203,(0,0,19):C.UVGC_268_204,(0,0,20):C.UVGC_268_205,(0,0,21):C.UVGC_268_206,(0,0,22):C.UVGC_268_207,(0,0,23):C.UVGC_268_208,(0,0,24):C.UVGC_268_209,(0,0,25):C.UVGC_268_210,(0,0,26):C.UVGC_268_211,(0,0,27):C.UVGC_268_212,(0,0,28):C.UVGC_268_213,(0,0,29):C.UVGC_268_214,(0,0,30):C.UVGC_268_215,(0,0,31):C.UVGC_268_216})

V_490 = CTVertex(name = 'V_490',
                 type = 'UV',
                 particles = [ P.g, P.g, P.g, P.g ],
                 color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.VVVV10, L.VVVV2, L.VVVV3, L.VVVV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u], [P.YF3d1], [P.YF3d2], [P.YF3d3], [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3], [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3], [P.YF3u1], [P.YF3u2], [P.YF3u3] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u], [P.YF3d1], [P.YF3d2], [P.YF3d3], [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3], [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3], [P.YF3u1], [P.YF3u2], [P.YF3u3], [P.YS3d1], [P.YS3d2], [P.YS3d3], [P.YS3Qd1], [P.YS3Qd2], [P.YS3Qd3], [P.YS3Qu1], [P.YS3Qu2], [P.YS3Qu3], [P.YS3u1], [P.YS3u2], [P.YS3u3] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d1], [P.YS3d2], [P.YS3d3], [P.YS3Qd1], [P.YS3Qd2], [P.YS3Qd3], [P.YS3Qu1], [P.YS3Qu2], [P.YS3Qu3], [P.YS3u1], [P.YS3u2], [P.YS3u3] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,1,5):C.UVGC_262_116,(0,1,6):C.UVGC_262_115,(2,1,5):C.UVGC_262_116,(2,1,6):C.UVGC_262_115,(5,1,5):C.UVGC_261_113,(5,1,6):C.UVGC_261_114,(1,1,5):C.UVGC_261_113,(1,1,6):C.UVGC_261_114,(7,1,0):C.UVGC_270_249,(7,1,3):C.UVGC_270_250,(7,1,4):C.UVGC_270_251,(7,1,5):C.UVGC_271_281,(7,1,6):C.UVGC_271_282,(7,1,7):C.UVGC_270_254,(7,1,8):C.UVGC_270_255,(7,1,9):C.UVGC_270_256,(7,1,10):C.UVGC_270_257,(7,1,11):C.UVGC_270_258,(7,1,12):C.UVGC_270_259,(7,1,13):C.UVGC_270_260,(7,1,14):C.UVGC_270_261,(7,1,15):C.UVGC_270_262,(7,1,16):C.UVGC_270_263,(7,1,17):C.UVGC_270_264,(7,1,18):C.UVGC_270_265,(7,1,19):C.UVGC_270_266,(7,1,20):C.UVGC_270_267,(7,1,21):C.UVGC_270_268,(7,1,22):C.UVGC_270_269,(7,1,24):C.UVGC_270_270,(7,1,25):C.UVGC_270_271,(7,1,26):C.UVGC_270_272,(7,1,27):C.UVGC_270_273,(7,1,28):C.UVGC_270_274,(7,1,29):C.UVGC_270_275,(7,1,30):C.UVGC_270_276,(7,1,31):C.UVGC_270_277,(7,1,32):C.UVGC_270_278,(7,1,33):C.UVGC_270_279,(7,1,34):C.UVGC_270_280,(4,1,5):C.UVGC_261_113,(4,1,6):C.UVGC_261_114,(3,1,5):C.UVGC_261_113,(3,1,6):C.UVGC_261_114,(8,1,5):C.UVGC_262_115,(8,1,6):C.UVGC_262_116,(6,1,0):C.UVGC_270_249,(6,1,3):C.UVGC_270_250,(6,1,4):C.UVGC_270_251,(6,1,5):C.UVGC_270_252,(6,1,6):C.UVGC_270_253,(6,1,7):C.UVGC_270_254,(6,1,8):C.UVGC_270_255,(6,1,9):C.UVGC_270_256,(6,1,10):C.UVGC_270_257,(6,1,11):C.UVGC_270_258,(6,1,12):C.UVGC_270_259,(6,1,13):C.UVGC_270_260,(6,1,14):C.UVGC_270_261,(6,1,15):C.UVGC_270_262,(6,1,16):C.UVGC_270_263,(6,1,17):C.UVGC_270_264,(6,1,18):C.UVGC_270_265,(6,1,19):C.UVGC_270_266,(6,1,20):C.UVGC_270_267,(6,1,21):C.UVGC_270_268,(6,1,22):C.UVGC_270_269,(6,1,24):C.UVGC_270_270,(6,1,25):C.UVGC_270_271,(6,1,26):C.UVGC_270_272,(6,1,27):C.UVGC_270_273,(6,1,28):C.UVGC_270_274,(6,1,29):C.UVGC_270_275,(6,1,30):C.UVGC_270_276,(6,1,31):C.UVGC_270_277,(6,1,32):C.UVGC_270_278,(6,1,33):C.UVGC_270_279,(6,1,34):C.UVGC_270_280,(11,0,5):C.UVGC_265_119,(11,0,6):C.UVGC_265_120,(10,0,5):C.UVGC_265_119,(10,0,6):C.UVGC_265_120,(9,0,5):C.UVGC_264_117,(9,0,6):C.UVGC_264_118,(0,2,5):C.UVGC_262_116,(0,2,6):C.UVGC_262_115,(2,2,5):C.UVGC_262_116,(2,2,6):C.UVGC_262_115,(7,2,2):C.UVGC_272_283,(7,2,5):C.UVGC_262_115,(7,2,6):C.UVGC_275_347,(5,2,5):C.UVGC_261_113,(5,2,6):C.UVGC_261_114,(1,2,5):C.UVGC_261_113,(1,2,6):C.UVGC_261_114,(4,2,5):C.UVGC_261_113,(4,2,6):C.UVGC_261_114,(3,2,5):C.UVGC_261_113,(3,2,6):C.UVGC_261_114,(8,2,0):C.UVGC_274_316,(8,2,3):C.UVGC_274_317,(8,2,4):C.UVGC_274_318,(8,2,5):C.UVGC_271_281,(8,2,6):C.UVGC_274_319,(8,2,7):C.UVGC_274_320,(8,2,8):C.UVGC_274_321,(8,2,9):C.UVGC_274_322,(8,2,10):C.UVGC_274_323,(8,2,11):C.UVGC_274_324,(8,2,12):C.UVGC_274_325,(8,2,13):C.UVGC_274_326,(8,2,14):C.UVGC_274_327,(8,2,15):C.UVGC_274_328,(8,2,16):C.UVGC_274_329,(8,2,17):C.UVGC_274_330,(8,2,18):C.UVGC_274_331,(8,2,19):C.UVGC_274_332,(8,2,20):C.UVGC_274_333,(8,2,21):C.UVGC_274_334,(8,2,22):C.UVGC_274_335,(8,2,24):C.UVGC_274_336,(8,2,25):C.UVGC_274_337,(8,2,26):C.UVGC_274_338,(8,2,27):C.UVGC_274_339,(8,2,28):C.UVGC_274_340,(8,2,29):C.UVGC_274_341,(8,2,30):C.UVGC_274_342,(8,2,31):C.UVGC_274_343,(8,2,32):C.UVGC_274_344,(8,2,33):C.UVGC_274_345,(8,2,34):C.UVGC_274_346,(6,2,0):C.UVGC_269_217,(6,2,3):C.UVGC_269_218,(6,2,4):C.UVGC_269_219,(6,2,5):C.UVGC_276_348,(6,2,6):C.UVGC_276_349,(6,2,7):C.UVGC_269_222,(6,2,8):C.UVGC_269_223,(6,2,9):C.UVGC_269_224,(6,2,10):C.UVGC_269_225,(6,2,11):C.UVGC_269_226,(6,2,12):C.UVGC_269_227,(6,2,13):C.UVGC_269_228,(6,2,14):C.UVGC_269_229,(6,2,15):C.UVGC_269_230,(6,2,16):C.UVGC_269_231,(6,2,17):C.UVGC_269_232,(6,2,18):C.UVGC_269_233,(6,2,19):C.UVGC_269_234,(6,2,20):C.UVGC_269_235,(6,2,21):C.UVGC_269_236,(6,2,22):C.UVGC_276_350,(6,2,24):C.UVGC_276_351,(6,2,25):C.UVGC_276_352,(6,2,26):C.UVGC_276_353,(6,2,27):C.UVGC_276_354,(6,2,28):C.UVGC_276_355,(6,2,29):C.UVGC_276_356,(6,2,30):C.UVGC_276_357,(6,2,31):C.UVGC_276_358,(6,2,32):C.UVGC_276_359,(6,2,33):C.UVGC_276_360,(6,2,34):C.UVGC_276_361,(0,3,5):C.UVGC_262_116,(0,3,6):C.UVGC_262_115,(2,3,5):C.UVGC_262_116,(2,3,6):C.UVGC_262_115,(7,3,0):C.UVGC_269_217,(7,3,3):C.UVGC_269_218,(7,3,4):C.UVGC_269_219,(7,3,5):C.UVGC_269_220,(7,3,6):C.UVGC_269_221,(7,3,7):C.UVGC_269_222,(7,3,8):C.UVGC_269_223,(7,3,9):C.UVGC_269_224,(7,3,10):C.UVGC_269_225,(7,3,11):C.UVGC_269_226,(7,3,12):C.UVGC_269_227,(7,3,13):C.UVGC_269_228,(7,3,14):C.UVGC_269_229,(7,3,15):C.UVGC_269_230,(7,3,16):C.UVGC_269_231,(7,3,17):C.UVGC_269_232,(7,3,18):C.UVGC_269_233,(7,3,19):C.UVGC_269_234,(7,3,20):C.UVGC_269_235,(7,3,21):C.UVGC_269_236,(7,3,22):C.UVGC_269_237,(7,3,24):C.UVGC_269_238,(7,3,25):C.UVGC_269_239,(7,3,26):C.UVGC_269_240,(7,3,27):C.UVGC_269_241,(7,3,28):C.UVGC_269_242,(7,3,29):C.UVGC_269_243,(7,3,30):C.UVGC_269_244,(7,3,31):C.UVGC_269_245,(7,3,32):C.UVGC_269_246,(7,3,33):C.UVGC_269_247,(7,3,34):C.UVGC_269_248,(5,3,5):C.UVGC_261_113,(5,3,6):C.UVGC_261_114,(1,3,5):C.UVGC_261_113,(1,3,6):C.UVGC_261_114,(4,3,5):C.UVGC_261_113,(4,3,6):C.UVGC_261_114,(3,3,5):C.UVGC_261_113,(3,3,6):C.UVGC_261_114,(8,3,0):C.UVGC_273_285,(8,3,3):C.UVGC_273_286,(8,3,4):C.UVGC_273_287,(8,3,5):C.UVGC_269_220,(8,3,6):C.UVGC_273_288,(8,3,7):C.UVGC_273_289,(8,3,8):C.UVGC_273_290,(8,3,9):C.UVGC_273_291,(8,3,10):C.UVGC_273_292,(8,3,11):C.UVGC_273_293,(8,3,12):C.UVGC_273_294,(8,3,13):C.UVGC_273_295,(8,3,14):C.UVGC_273_296,(8,3,15):C.UVGC_273_297,(8,3,16):C.UVGC_273_298,(8,3,17):C.UVGC_273_299,(8,3,18):C.UVGC_273_300,(8,3,19):C.UVGC_273_301,(8,3,20):C.UVGC_273_302,(8,3,21):C.UVGC_273_303,(8,3,22):C.UVGC_273_304,(8,3,24):C.UVGC_273_305,(8,3,25):C.UVGC_273_306,(8,3,26):C.UVGC_273_307,(8,3,27):C.UVGC_273_308,(8,3,28):C.UVGC_273_309,(8,3,29):C.UVGC_273_310,(8,3,30):C.UVGC_273_311,(8,3,31):C.UVGC_273_312,(8,3,32):C.UVGC_273_313,(8,3,33):C.UVGC_273_314,(8,3,34):C.UVGC_273_315,(6,3,1):C.UVGC_272_283,(6,3,6):C.UVGC_264_117,(6,3,23):C.UVGC_272_284})

V_491 = CTVertex(name = 'V_491',
                 type = 'UV',
                 particles = [ P.YF3d1__tilde__, P.YF3d1, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_280_365,(0,1,0):C.UVGC_178_30,(0,2,0):C.UVGC_180_32})

V_492 = CTVertex(name = 'V_492',
                 type = 'UV',
                 particles = [ P.YF3d2__tilde__, P.YF3d2, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_280_365,(0,1,0):C.UVGC_186_38,(0,2,0):C.UVGC_188_40})

V_493 = CTVertex(name = 'V_493',
                 type = 'UV',
                 particles = [ P.YF3d3__tilde__, P.YF3d3, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_280_365,(0,1,0):C.UVGC_194_46,(0,2,0):C.UVGC_196_48})

V_494 = CTVertex(name = 'V_494',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.YF3Qd1, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_280_365,(0,1,0):C.UVGC_202_54,(0,2,0):C.UVGC_204_56})

V_495 = CTVertex(name = 'V_495',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.YF3Qd2, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_280_365,(0,1,0):C.UVGC_208_60,(0,2,0):C.UVGC_210_62})

V_496 = CTVertex(name = 'V_496',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.YF3Qd3, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_280_365,(0,1,0):C.UVGC_214_66,(0,2,0):C.UVGC_216_68})

V_497 = CTVertex(name = 'V_497',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.YF3Qu1, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_287_371,(0,1,0):C.UVGC_220_72,(0,2,0):C.UVGC_222_74})

V_498 = CTVertex(name = 'V_498',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.YF3Qu2, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_287_371,(0,1,0):C.UVGC_226_78,(0,2,0):C.UVGC_228_80})

V_499 = CTVertex(name = 'V_499',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.YF3Qu3, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_287_371,(0,1,0):C.UVGC_232_84,(0,2,0):C.UVGC_234_86})

V_500 = CTVertex(name = 'V_500',
                 type = 'UV',
                 particles = [ P.YF3u1__tilde__, P.YF3u1, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_287_371,(0,1,0):C.UVGC_238_90,(0,2,0):C.UVGC_240_92})

V_501 = CTVertex(name = 'V_501',
                 type = 'UV',
                 particles = [ P.YF3u2__tilde__, P.YF3u2, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_287_371,(0,1,0):C.UVGC_246_98,(0,2,0):C.UVGC_248_100})

V_502 = CTVertex(name = 'V_502',
                 type = 'UV',
                 particles = [ P.YF3u3__tilde__, P.YF3u3, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_287_371,(0,1,0):C.UVGC_254_106,(0,2,0):C.UVGC_256_108})

V_503 = CTVertex(name = 'V_503',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.YF3Qu1, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_767_1022,(0,0,2):C.UVGC_768_1024,(0,0,1):C.UVGC_590_891})

V_504 = CTVertex(name = 'V_504',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.YF3Qu1, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_767_1022,(0,0,2):C.UVGC_768_1024,(0,0,1):C.UVGC_590_891})

V_505 = CTVertex(name = 'V_505',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.YF3Qd1, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_589_887,(0,0,2):C.UVGC_590_890,(0,0,1):C.UVGC_590_891})

V_506 = CTVertex(name = 'V_506',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.YF3Qd1, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_589_887,(0,0,2):C.UVGC_590_890,(0,0,1):C.UVGC_590_891})

V_507 = CTVertex(name = 'V_507',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.YF3Qu2, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_581_866,(0,0,2):C.UVGC_582_869,(0,0,1):C.UVGC_582_870})

V_508 = CTVertex(name = 'V_508',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.YF3Qu2, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_581_866,(0,0,2):C.UVGC_582_869,(0,0,1):C.UVGC_582_870})

V_509 = CTVertex(name = 'V_509',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.YF3Qd2, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3Qd2] ], [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_753_991,(0,0,2):C.UVGC_754_993,(0,0,1):C.UVGC_582_870})

V_510 = CTVertex(name = 'V_510',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.YF3Qd2, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3Qd2] ], [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_753_991,(0,0,2):C.UVGC_754_993,(0,0,1):C.UVGC_582_870})

V_511 = CTVertex(name = 'V_511',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.YF3Qu3, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_760_1007,(0,0,2):C.UVGC_761_1009,(0,0,1):C.UVGC_577_856})

V_512 = CTVertex(name = 'V_512',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.YF3Qu3, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_760_1007,(0,0,2):C.UVGC_761_1009,(0,0,1):C.UVGC_577_856})

V_513 = CTVertex(name = 'V_513',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.YF3Qd3, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_576_852,(0,0,2):C.UVGC_577_855,(0,0,1):C.UVGC_577_856})

V_514 = CTVertex(name = 'V_514',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.YF3Qd3, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_576_852,(0,0,2):C.UVGC_577_855,(0,0,1):C.UVGC_577_856})

V_515 = CTVertex(name = 'V_515',
                 type = 'UV',
                 particles = [ P.YF3d1__tilde__, P.d, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3d1] ], [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_587_882,(0,0,2):C.UVGC_588_885,(0,0,1):C.UVGC_588_886})

V_516 = CTVertex(name = 'V_516',
                 type = 'UV',
                 particles = [ P.YF3d2__tilde__, P.s, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3d2] ], [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_751_986,(0,0,2):C.UVGC_752_989,(0,0,1):C.UVGC_752_990})

V_517 = CTVertex(name = 'V_517',
                 type = 'UV',
                 particles = [ P.YF3d3__tilde__, P.b, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3d3] ], [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_574_847,(0,0,2):C.UVGC_575_850,(0,0,1):C.UVGC_575_851})

V_518 = CTVertex(name = 'V_518',
                 type = 'UV',
                 particles = [ P.YF3d1__tilde__, P.d, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3d1] ], [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_587_882,(0,0,2):C.UVGC_588_885,(0,0,1):C.UVGC_588_886})

V_519 = CTVertex(name = 'V_519',
                 type = 'UV',
                 particles = [ P.YF3d2__tilde__, P.s, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3d2] ], [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_751_986,(0,0,2):C.UVGC_752_989,(0,0,1):C.UVGC_752_990})

V_520 = CTVertex(name = 'V_520',
                 type = 'UV',
                 particles = [ P.YF3d3__tilde__, P.b, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3d3] ], [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_574_847,(0,0,2):C.UVGC_575_850,(0,0,1):C.UVGC_575_851})

V_521 = CTVertex(name = 'V_521',
                 type = 'UV',
                 particles = [ P.YF3u1__tilde__, P.u, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3u1] ], [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_769_1025,(0,0,2):C.UVGC_770_1028,(0,0,1):C.UVGC_770_1029})

V_522 = CTVertex(name = 'V_522',
                 type = 'UV',
                 particles = [ P.YF3u2__tilde__, P.c, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3u2] ], [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_583_871,(0,0,2):C.UVGC_584_874,(0,0,1):C.UVGC_584_875})

V_523 = CTVertex(name = 'V_523',
                 type = 'UV',
                 particles = [ P.YF3u3__tilde__, P.t, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3u3] ], [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_762_1010,(0,0,2):C.UVGC_763_1013,(0,0,1):C.UVGC_763_1014})

V_524 = CTVertex(name = 'V_524',
                 type = 'UV',
                 particles = [ P.YF3u1__tilde__, P.u, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3u1] ], [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_769_1025,(0,0,2):C.UVGC_770_1028,(0,0,1):C.UVGC_770_1029})

V_525 = CTVertex(name = 'V_525',
                 type = 'UV',
                 particles = [ P.YF3u2__tilde__, P.c, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3u2] ], [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_583_871,(0,0,2):C.UVGC_584_874,(0,0,1):C.UVGC_584_875})

V_526 = CTVertex(name = 'V_526',
                 type = 'UV',
                 particles = [ P.YF3u3__tilde__, P.t, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3u3] ], [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_762_1010,(0,0,2):C.UVGC_763_1013,(0,0,1):C.UVGC_763_1014})

V_527 = CTVertex(name = 'V_527',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_756_996,(0,0,2):C.UVGC_756_997,(0,0,1):C.UVGC_756_998})

V_528 = CTVertex(name = 'V_528',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_486_796})

V_529 = CTVertex(name = 'V_529',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_485_795})

V_530 = CTVertex(name = 'V_530',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.YF3d1, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3d1] ], [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_587_882,(0,0,2):C.UVGC_588_885,(0,0,1):C.UVGC_588_886})

V_531 = CTVertex(name = 'V_531',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.YF3d2, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3d2] ], [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_751_986,(0,0,2):C.UVGC_752_989,(0,0,1):C.UVGC_752_990})

V_532 = CTVertex(name = 'V_532',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.YF3d3, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3d3] ], [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_574_847,(0,0,2):C.UVGC_575_850,(0,0,1):C.UVGC_575_851})

V_533 = CTVertex(name = 'V_533',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.YF3d1, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3d1] ], [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_587_882,(0,0,2):C.UVGC_588_885,(0,0,1):C.UVGC_588_886})

V_534 = CTVertex(name = 'V_534',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.YF3d2, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3d2] ], [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_751_986,(0,0,2):C.UVGC_752_989,(0,0,1):C.UVGC_752_990})

V_535 = CTVertex(name = 'V_535',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.YF3d3, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3d3] ], [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_574_847,(0,0,2):C.UVGC_575_850,(0,0,1):C.UVGC_575_851})

V_536 = CTVertex(name = 'V_536',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.YF3u1, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3u1] ], [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_769_1025,(0,0,2):C.UVGC_770_1028,(0,0,1):C.UVGC_770_1029})

V_537 = CTVertex(name = 'V_537',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.YF3u2, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3u2] ], [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_583_871,(0,0,2):C.UVGC_584_874,(0,0,1):C.UVGC_584_875})

V_538 = CTVertex(name = 'V_538',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.YF3u3, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3u3] ], [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_762_1010,(0,0,2):C.UVGC_763_1013,(0,0,1):C.UVGC_763_1014})

V_539 = CTVertex(name = 'V_539',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.YF3u1, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3u1] ], [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_769_1025,(0,0,2):C.UVGC_770_1028,(0,0,1):C.UVGC_770_1029})

V_540 = CTVertex(name = 'V_540',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.YF3u2, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3u2] ], [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_583_871,(0,0,2):C.UVGC_584_874,(0,0,1):C.UVGC_584_875})

V_541 = CTVertex(name = 'V_541',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.YF3u3, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3u3] ], [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_762_1010,(0,0,2):C.UVGC_763_1013,(0,0,1):C.UVGC_763_1014})

V_542 = CTVertex(name = 'V_542',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.u, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_767_1022,(0,0,2):C.UVGC_768_1024,(0,0,1):C.UVGC_590_891})

V_543 = CTVertex(name = 'V_543',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.u, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_767_1022,(0,0,2):C.UVGC_768_1024,(0,0,1):C.UVGC_590_891})

V_544 = CTVertex(name = 'V_544',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.d, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_589_887,(0,0,2):C.UVGC_590_890,(0,0,1):C.UVGC_590_891})

V_545 = CTVertex(name = 'V_545',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.d, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_589_887,(0,0,2):C.UVGC_590_890,(0,0,1):C.UVGC_590_891})

V_546 = CTVertex(name = 'V_546',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.c, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_581_866,(0,0,2):C.UVGC_582_869,(0,0,1):C.UVGC_582_870})

V_547 = CTVertex(name = 'V_547',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.c, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_581_866,(0,0,2):C.UVGC_582_869,(0,0,1):C.UVGC_582_870})

V_548 = CTVertex(name = 'V_548',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.s, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3Qd2] ], [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_753_991,(0,0,2):C.UVGC_754_993,(0,0,1):C.UVGC_582_870})

V_549 = CTVertex(name = 'V_549',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.s, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3Qd2] ], [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_753_991,(0,0,2):C.UVGC_754_993,(0,0,1):C.UVGC_582_870})

V_550 = CTVertex(name = 'V_550',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.t, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_760_1007,(0,0,2):C.UVGC_761_1009,(0,0,1):C.UVGC_577_856})

V_551 = CTVertex(name = 'V_551',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.t, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_760_1007,(0,0,2):C.UVGC_761_1009,(0,0,1):C.UVGC_577_856})

V_552 = CTVertex(name = 'V_552',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.b, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_576_852,(0,0,2):C.UVGC_577_855,(0,0,1):C.UVGC_577_856})

V_553 = CTVertex(name = 'V_553',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.b, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_576_852,(0,0,2):C.UVGC_577_855,(0,0,1):C.UVGC_577_856})

V_554 = CTVertex(name = 'V_554',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.YF3Qd1, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3Qd1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_281_366,(0,3,0):C.UVGC_266_121,(0,3,1):C.UVGC_266_122,(0,3,2):C.UVGC_266_123,(0,3,3):C.UVGC_266_124,(0,3,4):C.UVGC_266_125,(0,3,6):C.UVGC_266_126,(0,3,7):C.UVGC_266_127,(0,3,8):C.UVGC_266_128,(0,3,9):C.UVGC_266_129,(0,3,10):C.UVGC_266_130,(0,3,11):C.UVGC_266_131,(0,3,12):C.UVGC_266_132,(0,3,13):C.UVGC_266_133,(0,3,14):C.UVGC_266_134,(0,3,15):C.UVGC_266_135,(0,3,16):C.UVGC_266_136,(0,3,17):C.UVGC_266_137,(0,3,18):C.UVGC_266_138,(0,3,19):C.UVGC_266_139,(0,3,20):C.UVGC_266_140,(0,3,21):C.UVGC_266_141,(0,3,22):C.UVGC_266_142,(0,3,23):C.UVGC_266_143,(0,3,24):C.UVGC_266_144,(0,3,25):C.UVGC_266_145,(0,3,26):C.UVGC_266_146,(0,3,27):C.UVGC_266_147,(0,3,28):C.UVGC_266_148,(0,3,29):C.UVGC_266_149,(0,3,30):C.UVGC_266_150,(0,3,31):C.UVGC_266_151,(0,3,32):C.UVGC_266_152,(0,1,5):C.UVGC_205_57,(0,2,5):C.UVGC_206_58})

V_555 = CTVertex(name = 'V_555',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.YF3Qd2, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3Qd2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_281_366,(0,3,0):C.UVGC_266_121,(0,3,1):C.UVGC_266_122,(0,3,2):C.UVGC_266_123,(0,3,3):C.UVGC_266_124,(0,3,4):C.UVGC_266_125,(0,3,6):C.UVGC_266_126,(0,3,7):C.UVGC_266_127,(0,3,8):C.UVGC_266_128,(0,3,9):C.UVGC_266_129,(0,3,10):C.UVGC_266_130,(0,3,11):C.UVGC_266_131,(0,3,12):C.UVGC_266_132,(0,3,13):C.UVGC_266_133,(0,3,14):C.UVGC_266_134,(0,3,15):C.UVGC_266_135,(0,3,16):C.UVGC_266_136,(0,3,17):C.UVGC_266_137,(0,3,18):C.UVGC_266_138,(0,3,19):C.UVGC_266_139,(0,3,20):C.UVGC_266_140,(0,3,21):C.UVGC_266_141,(0,3,22):C.UVGC_266_142,(0,3,23):C.UVGC_266_143,(0,3,24):C.UVGC_266_144,(0,3,25):C.UVGC_266_145,(0,3,26):C.UVGC_266_146,(0,3,27):C.UVGC_266_147,(0,3,28):C.UVGC_266_148,(0,3,29):C.UVGC_266_149,(0,3,30):C.UVGC_266_150,(0,3,31):C.UVGC_266_151,(0,3,32):C.UVGC_266_152,(0,1,5):C.UVGC_211_63,(0,2,5):C.UVGC_212_64})

V_556 = CTVertex(name = 'V_556',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.YF3Qd3, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3Qd3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_281_366,(0,3,0):C.UVGC_266_121,(0,3,1):C.UVGC_266_122,(0,3,2):C.UVGC_266_123,(0,3,3):C.UVGC_266_124,(0,3,4):C.UVGC_266_125,(0,3,6):C.UVGC_266_126,(0,3,7):C.UVGC_266_127,(0,3,8):C.UVGC_266_128,(0,3,9):C.UVGC_266_129,(0,3,10):C.UVGC_266_130,(0,3,11):C.UVGC_266_131,(0,3,12):C.UVGC_266_132,(0,3,13):C.UVGC_266_133,(0,3,14):C.UVGC_266_134,(0,3,15):C.UVGC_266_135,(0,3,16):C.UVGC_266_136,(0,3,17):C.UVGC_266_137,(0,3,18):C.UVGC_266_138,(0,3,19):C.UVGC_266_139,(0,3,20):C.UVGC_266_140,(0,3,21):C.UVGC_266_141,(0,3,22):C.UVGC_266_142,(0,3,23):C.UVGC_266_143,(0,3,24):C.UVGC_266_144,(0,3,25):C.UVGC_266_145,(0,3,26):C.UVGC_266_146,(0,3,27):C.UVGC_266_147,(0,3,28):C.UVGC_266_148,(0,3,29):C.UVGC_266_149,(0,3,30):C.UVGC_266_150,(0,3,31):C.UVGC_266_151,(0,3,32):C.UVGC_266_152,(0,1,5):C.UVGC_217_69,(0,2,5):C.UVGC_218_70})

V_557 = CTVertex(name = 'V_557',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.YF3Qu1, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3Qu1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_281_366,(0,3,0):C.UVGC_266_121,(0,3,1):C.UVGC_266_122,(0,3,2):C.UVGC_266_123,(0,3,3):C.UVGC_266_124,(0,3,4):C.UVGC_266_125,(0,3,6):C.UVGC_266_126,(0,3,7):C.UVGC_266_127,(0,3,8):C.UVGC_266_128,(0,3,9):C.UVGC_266_129,(0,3,10):C.UVGC_266_130,(0,3,11):C.UVGC_266_131,(0,3,12):C.UVGC_266_132,(0,3,13):C.UVGC_266_133,(0,3,14):C.UVGC_266_134,(0,3,15):C.UVGC_266_135,(0,3,16):C.UVGC_266_136,(0,3,17):C.UVGC_266_137,(0,3,18):C.UVGC_266_138,(0,3,19):C.UVGC_266_139,(0,3,20):C.UVGC_266_140,(0,3,21):C.UVGC_266_141,(0,3,22):C.UVGC_266_142,(0,3,23):C.UVGC_266_143,(0,3,24):C.UVGC_266_144,(0,3,25):C.UVGC_266_145,(0,3,26):C.UVGC_266_146,(0,3,27):C.UVGC_266_147,(0,3,28):C.UVGC_266_148,(0,3,29):C.UVGC_266_149,(0,3,30):C.UVGC_266_150,(0,3,31):C.UVGC_266_151,(0,3,32):C.UVGC_266_152,(0,1,5):C.UVGC_223_75,(0,2,5):C.UVGC_224_76})

V_558 = CTVertex(name = 'V_558',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.YF3Qu2, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3Qu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_281_366,(0,3,0):C.UVGC_266_121,(0,3,1):C.UVGC_266_122,(0,3,2):C.UVGC_266_123,(0,3,3):C.UVGC_266_124,(0,3,4):C.UVGC_266_125,(0,3,6):C.UVGC_266_126,(0,3,7):C.UVGC_266_127,(0,3,8):C.UVGC_266_128,(0,3,9):C.UVGC_266_129,(0,3,10):C.UVGC_266_130,(0,3,11):C.UVGC_266_131,(0,3,12):C.UVGC_266_132,(0,3,13):C.UVGC_266_133,(0,3,14):C.UVGC_266_134,(0,3,15):C.UVGC_266_135,(0,3,16):C.UVGC_266_136,(0,3,17):C.UVGC_266_137,(0,3,18):C.UVGC_266_138,(0,3,19):C.UVGC_266_139,(0,3,20):C.UVGC_266_140,(0,3,21):C.UVGC_266_141,(0,3,22):C.UVGC_266_142,(0,3,23):C.UVGC_266_143,(0,3,24):C.UVGC_266_144,(0,3,25):C.UVGC_266_145,(0,3,26):C.UVGC_266_146,(0,3,27):C.UVGC_266_147,(0,3,28):C.UVGC_266_148,(0,3,29):C.UVGC_266_149,(0,3,30):C.UVGC_266_150,(0,3,31):C.UVGC_266_151,(0,3,32):C.UVGC_266_152,(0,1,5):C.UVGC_229_81,(0,2,5):C.UVGC_230_82})

V_559 = CTVertex(name = 'V_559',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.YF3Qu3, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3Qu3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_281_366,(0,3,0):C.UVGC_266_121,(0,3,1):C.UVGC_266_122,(0,3,2):C.UVGC_266_123,(0,3,3):C.UVGC_266_124,(0,3,4):C.UVGC_266_125,(0,3,6):C.UVGC_266_126,(0,3,7):C.UVGC_266_127,(0,3,8):C.UVGC_266_128,(0,3,9):C.UVGC_266_129,(0,3,10):C.UVGC_266_130,(0,3,11):C.UVGC_266_131,(0,3,12):C.UVGC_266_132,(0,3,13):C.UVGC_266_133,(0,3,14):C.UVGC_266_134,(0,3,15):C.UVGC_266_135,(0,3,16):C.UVGC_266_136,(0,3,17):C.UVGC_266_137,(0,3,18):C.UVGC_266_138,(0,3,19):C.UVGC_266_139,(0,3,20):C.UVGC_266_140,(0,3,21):C.UVGC_266_141,(0,3,22):C.UVGC_266_142,(0,3,23):C.UVGC_266_143,(0,3,24):C.UVGC_266_144,(0,3,25):C.UVGC_266_145,(0,3,26):C.UVGC_266_146,(0,3,27):C.UVGC_266_147,(0,3,28):C.UVGC_266_148,(0,3,29):C.UVGC_266_149,(0,3,30):C.UVGC_266_150,(0,3,31):C.UVGC_266_151,(0,3,32):C.UVGC_266_152,(0,1,5):C.UVGC_235_87,(0,2,5):C.UVGC_236_88})

V_560 = CTVertex(name = 'V_560',
                 type = 'UV',
                 particles = [ P.YF3u1__tilde__, P.YF3u1, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3u1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_281_366,(0,3,0):C.UVGC_266_121,(0,3,1):C.UVGC_266_122,(0,3,2):C.UVGC_266_123,(0,3,3):C.UVGC_266_124,(0,3,4):C.UVGC_266_125,(0,3,6):C.UVGC_266_126,(0,3,7):C.UVGC_266_127,(0,3,8):C.UVGC_266_128,(0,3,9):C.UVGC_266_129,(0,3,10):C.UVGC_266_130,(0,3,11):C.UVGC_266_131,(0,3,12):C.UVGC_266_132,(0,3,13):C.UVGC_266_133,(0,3,14):C.UVGC_266_134,(0,3,15):C.UVGC_266_135,(0,3,16):C.UVGC_266_136,(0,3,17):C.UVGC_266_137,(0,3,18):C.UVGC_266_138,(0,3,19):C.UVGC_266_139,(0,3,20):C.UVGC_266_140,(0,3,21):C.UVGC_266_141,(0,3,22):C.UVGC_266_142,(0,3,23):C.UVGC_266_143,(0,3,24):C.UVGC_266_144,(0,3,25):C.UVGC_266_145,(0,3,26):C.UVGC_266_146,(0,3,27):C.UVGC_266_147,(0,3,28):C.UVGC_266_148,(0,3,29):C.UVGC_266_149,(0,3,30):C.UVGC_266_150,(0,3,31):C.UVGC_266_151,(0,3,32):C.UVGC_266_152,(0,1,5):C.UVGC_241_93,(0,2,5):C.UVGC_242_94})

V_561 = CTVertex(name = 'V_561',
                 type = 'UV',
                 particles = [ P.YF3u2__tilde__, P.YF3u2, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3u2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_281_366,(0,3,0):C.UVGC_266_121,(0,3,1):C.UVGC_266_122,(0,3,2):C.UVGC_266_123,(0,3,3):C.UVGC_266_124,(0,3,4):C.UVGC_266_125,(0,3,6):C.UVGC_266_126,(0,3,7):C.UVGC_266_127,(0,3,8):C.UVGC_266_128,(0,3,9):C.UVGC_266_129,(0,3,10):C.UVGC_266_130,(0,3,11):C.UVGC_266_131,(0,3,12):C.UVGC_266_132,(0,3,13):C.UVGC_266_133,(0,3,14):C.UVGC_266_134,(0,3,15):C.UVGC_266_135,(0,3,16):C.UVGC_266_136,(0,3,17):C.UVGC_266_137,(0,3,18):C.UVGC_266_138,(0,3,19):C.UVGC_266_139,(0,3,20):C.UVGC_266_140,(0,3,21):C.UVGC_266_141,(0,3,22):C.UVGC_266_142,(0,3,23):C.UVGC_266_143,(0,3,24):C.UVGC_266_144,(0,3,25):C.UVGC_266_145,(0,3,26):C.UVGC_266_146,(0,3,27):C.UVGC_266_147,(0,3,28):C.UVGC_266_148,(0,3,29):C.UVGC_266_149,(0,3,30):C.UVGC_266_150,(0,3,31):C.UVGC_266_151,(0,3,32):C.UVGC_266_152,(0,1,5):C.UVGC_249_101,(0,2,5):C.UVGC_250_102})

V_562 = CTVertex(name = 'V_562',
                 type = 'UV',
                 particles = [ P.YF3u3__tilde__, P.YF3u3, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3u3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_281_366,(0,3,0):C.UVGC_266_121,(0,3,1):C.UVGC_266_122,(0,3,2):C.UVGC_266_123,(0,3,3):C.UVGC_266_124,(0,3,4):C.UVGC_266_125,(0,3,6):C.UVGC_266_126,(0,3,7):C.UVGC_266_127,(0,3,8):C.UVGC_266_128,(0,3,9):C.UVGC_266_129,(0,3,10):C.UVGC_266_130,(0,3,11):C.UVGC_266_131,(0,3,12):C.UVGC_266_132,(0,3,13):C.UVGC_266_133,(0,3,14):C.UVGC_266_134,(0,3,15):C.UVGC_266_135,(0,3,16):C.UVGC_266_136,(0,3,17):C.UVGC_266_137,(0,3,18):C.UVGC_266_138,(0,3,19):C.UVGC_266_139,(0,3,20):C.UVGC_266_140,(0,3,21):C.UVGC_266_141,(0,3,22):C.UVGC_266_142,(0,3,23):C.UVGC_266_143,(0,3,24):C.UVGC_266_144,(0,3,25):C.UVGC_266_145,(0,3,26):C.UVGC_266_146,(0,3,27):C.UVGC_266_147,(0,3,28):C.UVGC_266_148,(0,3,29):C.UVGC_266_149,(0,3,30):C.UVGC_266_150,(0,3,31):C.UVGC_266_151,(0,3,32):C.UVGC_266_152,(0,1,5):C.UVGC_257_109,(0,2,5):C.UVGC_258_110})

V_563 = CTVertex(name = 'V_563',
                 type = 'UV',
                 particles = [ P.YF3d1__tilde__, P.YF3d1, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3d1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_281_366,(0,3,0):C.UVGC_266_121,(0,3,1):C.UVGC_266_122,(0,3,2):C.UVGC_266_123,(0,3,3):C.UVGC_266_124,(0,3,4):C.UVGC_266_125,(0,3,6):C.UVGC_266_126,(0,3,7):C.UVGC_266_127,(0,3,8):C.UVGC_266_128,(0,3,9):C.UVGC_266_129,(0,3,10):C.UVGC_266_130,(0,3,11):C.UVGC_266_131,(0,3,12):C.UVGC_266_132,(0,3,13):C.UVGC_266_133,(0,3,14):C.UVGC_266_134,(0,3,15):C.UVGC_266_135,(0,3,16):C.UVGC_266_136,(0,3,17):C.UVGC_266_137,(0,3,18):C.UVGC_266_138,(0,3,19):C.UVGC_266_139,(0,3,20):C.UVGC_266_140,(0,3,21):C.UVGC_266_141,(0,3,22):C.UVGC_266_142,(0,3,23):C.UVGC_266_143,(0,3,24):C.UVGC_266_144,(0,3,25):C.UVGC_266_145,(0,3,26):C.UVGC_266_146,(0,3,27):C.UVGC_266_147,(0,3,28):C.UVGC_266_148,(0,3,29):C.UVGC_266_149,(0,3,30):C.UVGC_266_150,(0,3,31):C.UVGC_266_151,(0,3,32):C.UVGC_266_152,(0,1,5):C.UVGC_181_33,(0,2,5):C.UVGC_182_34})

V_564 = CTVertex(name = 'V_564',
                 type = 'UV',
                 particles = [ P.YF3d2__tilde__, P.YF3d2, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3d2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_281_366,(0,3,0):C.UVGC_266_121,(0,3,1):C.UVGC_266_122,(0,3,2):C.UVGC_266_123,(0,3,3):C.UVGC_266_124,(0,3,4):C.UVGC_266_125,(0,3,6):C.UVGC_266_126,(0,3,7):C.UVGC_266_127,(0,3,8):C.UVGC_266_128,(0,3,9):C.UVGC_266_129,(0,3,10):C.UVGC_266_130,(0,3,11):C.UVGC_266_131,(0,3,12):C.UVGC_266_132,(0,3,13):C.UVGC_266_133,(0,3,14):C.UVGC_266_134,(0,3,15):C.UVGC_266_135,(0,3,16):C.UVGC_266_136,(0,3,17):C.UVGC_266_137,(0,3,18):C.UVGC_266_138,(0,3,19):C.UVGC_266_139,(0,3,20):C.UVGC_266_140,(0,3,21):C.UVGC_266_141,(0,3,22):C.UVGC_266_142,(0,3,23):C.UVGC_266_143,(0,3,24):C.UVGC_266_144,(0,3,25):C.UVGC_266_145,(0,3,26):C.UVGC_266_146,(0,3,27):C.UVGC_266_147,(0,3,28):C.UVGC_266_148,(0,3,29):C.UVGC_266_149,(0,3,30):C.UVGC_266_150,(0,3,31):C.UVGC_266_151,(0,3,32):C.UVGC_266_152,(0,1,5):C.UVGC_189_41,(0,2,5):C.UVGC_190_42})

V_565 = CTVertex(name = 'V_565',
                 type = 'UV',
                 particles = [ P.YF3d3__tilde__, P.YF3d3, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3d3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_281_366,(0,3,0):C.UVGC_266_121,(0,3,1):C.UVGC_266_122,(0,3,2):C.UVGC_266_123,(0,3,3):C.UVGC_266_124,(0,3,4):C.UVGC_266_125,(0,3,6):C.UVGC_266_126,(0,3,7):C.UVGC_266_127,(0,3,8):C.UVGC_266_128,(0,3,9):C.UVGC_266_129,(0,3,10):C.UVGC_266_130,(0,3,11):C.UVGC_266_131,(0,3,12):C.UVGC_266_132,(0,3,13):C.UVGC_266_133,(0,3,14):C.UVGC_266_134,(0,3,15):C.UVGC_266_135,(0,3,16):C.UVGC_266_136,(0,3,17):C.UVGC_266_137,(0,3,18):C.UVGC_266_138,(0,3,19):C.UVGC_266_139,(0,3,20):C.UVGC_266_140,(0,3,21):C.UVGC_266_141,(0,3,22):C.UVGC_266_142,(0,3,23):C.UVGC_266_143,(0,3,24):C.UVGC_266_144,(0,3,25):C.UVGC_266_145,(0,3,26):C.UVGC_266_146,(0,3,27):C.UVGC_266_147,(0,3,28):C.UVGC_266_148,(0,3,29):C.UVGC_266_149,(0,3,30):C.UVGC_266_150,(0,3,31):C.UVGC_266_151,(0,3,32):C.UVGC_266_152,(0,1,5):C.UVGC_197_49,(0,2,5):C.UVGC_198_50})

V_566 = CTVertex(name = 'V_566',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.YF3Qu1, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,1):C.UVGC_580_865,(0,1,0):C.UVGC_534_816,(0,1,2):C.UVGC_534_817,(0,2,0):C.UVGC_535_818,(0,2,2):C.UVGC_535_819})

V_567 = CTVertex(name = 'V_567',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.YF3Qu2, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd2] ], [ [P.g, P.YF3Qd2, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,1):C.UVGC_580_865,(0,1,0):C.UVGC_543_824,(0,1,2):C.UVGC_543_825,(0,2,0):C.UVGC_544_826,(0,2,2):C.UVGC_544_827})

V_568 = CTVertex(name = 'V_568',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.YF3Qu3, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,1):C.UVGC_580_865,(0,1,0):C.UVGC_552_831,(0,1,2):C.UVGC_552_832,(0,2,0):C.UVGC_553_833,(0,2,2):C.UVGC_553_834})

V_569 = CTVertex(name = 'V_569',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.YF3Qd1, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,1):C.UVGC_580_865,(0,1,0):C.UVGC_534_816,(0,1,2):C.UVGC_534_817,(0,2,0):C.UVGC_535_818,(0,2,2):C.UVGC_535_819})

V_570 = CTVertex(name = 'V_570',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.YF3Qd2, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd2] ], [ [P.g, P.YF3Qd2, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,1):C.UVGC_580_865,(0,1,0):C.UVGC_543_824,(0,1,2):C.UVGC_543_825,(0,2,0):C.UVGC_544_826,(0,2,2):C.UVGC_544_827})

V_571 = CTVertex(name = 'V_571',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.YF3Qd3, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,1):C.UVGC_580_865,(0,1,0):C.UVGC_552_831,(0,1,2):C.UVGC_552_832,(0,2,0):C.UVGC_553_833,(0,2,2):C.UVGC_553_834})

V_572 = CTVertex(name = 'V_572',
                 type = 'UV',
                 particles = [ P.a, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_299_379})

V_573 = CTVertex(name = 'V_573',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.d, P.YS3d1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YS3d1] ], [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_585_876,(0,0,2):C.UVGC_585_877,(0,0,1):C.UVGC_585_878})

V_574 = CTVertex(name = 'V_574',
                 type = 'UV',
                 particles = [ P.Xm, P.d, P.YS3d1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YS3d1] ], [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_585_876,(0,0,2):C.UVGC_585_877,(0,0,1):C.UVGC_585_878})

V_575 = CTVertex(name = 'V_575',
                 type = 'UV',
                 particles = [ P.g, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_301_381,(0,0,1):C.UVGC_301_382,(0,0,2):C.UVGC_301_383,(0,0,3):C.UVGC_301_384,(0,0,4):C.UVGC_301_385,(0,0,6):C.UVGC_301_386,(0,0,7):C.UVGC_301_387,(0,0,8):C.UVGC_301_388,(0,0,9):C.UVGC_301_389,(0,0,10):C.UVGC_301_390,(0,0,11):C.UVGC_301_391,(0,0,12):C.UVGC_301_392,(0,0,13):C.UVGC_301_393,(0,0,14):C.UVGC_301_394,(0,0,15):C.UVGC_301_395,(0,0,16):C.UVGC_301_396,(0,0,17):C.UVGC_301_397,(0,0,18):C.UVGC_301_398,(0,0,19):C.UVGC_301_399,(0,0,20):C.UVGC_301_400,(0,0,21):C.UVGC_301_401,(0,0,22):C.UVGC_301_402,(0,0,23):C.UVGC_301_403,(0,0,24):C.UVGC_301_404,(0,0,25):C.UVGC_301_405,(0,0,26):C.UVGC_301_406,(0,0,27):C.UVGC_301_407,(0,0,28):C.UVGC_301_408,(0,0,29):C.UVGC_301_409,(0,0,30):C.UVGC_301_410,(0,0,31):C.UVGC_301_411,(0,0,32):C.UVGC_301_412,(0,0,5):C.UVGC_301_413})

V_576 = CTVertex(name = 'V_576',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.Xd, P.YS3d1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YS3d1] ], [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_585_876,(0,0,2):C.UVGC_585_877,(0,0,1):C.UVGC_585_878})

V_577 = CTVertex(name = 'V_577',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.Xm, P.YS3d1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YS3d1] ], [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_585_876,(0,0,2):C.UVGC_585_877,(0,0,1):C.UVGC_585_878})

V_578 = CTVertex(name = 'V_578',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_300_380})

V_579 = CTVertex(name = 'V_579',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_302_414,(0,0,1):C.UVGC_302_415,(0,0,2):C.UVGC_302_416,(0,0,3):C.UVGC_302_417,(0,0,4):C.UVGC_302_418,(0,0,6):C.UVGC_302_419,(0,0,7):C.UVGC_302_420,(0,0,8):C.UVGC_302_421,(0,0,9):C.UVGC_302_422,(0,0,10):C.UVGC_302_423,(0,0,11):C.UVGC_302_424,(0,0,12):C.UVGC_302_425,(0,0,13):C.UVGC_302_426,(0,0,14):C.UVGC_302_427,(0,0,15):C.UVGC_302_428,(0,0,16):C.UVGC_302_429,(0,0,17):C.UVGC_302_430,(0,0,18):C.UVGC_302_431,(0,0,19):C.UVGC_302_432,(0,0,20):C.UVGC_302_433,(0,0,21):C.UVGC_302_434,(0,0,22):C.UVGC_302_435,(0,0,23):C.UVGC_302_436,(0,0,24):C.UVGC_302_437,(0,0,25):C.UVGC_302_438,(0,0,26):C.UVGC_302_439,(0,0,27):C.UVGC_302_440,(0,0,28):C.UVGC_302_441,(0,0,29):C.UVGC_302_442,(0,0,30):C.UVGC_302_443,(0,0,31):C.UVGC_302_444,(0,0,32):C.UVGC_302_445,(0,0,5):C.UVGC_302_446})

V_580 = CTVertex(name = 'V_580',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_305_451,(2,0,1):C.UVGC_305_452,(2,0,2):C.UVGC_305_453,(2,0,3):C.UVGC_305_454,(2,0,4):C.UVGC_305_455,(2,0,6):C.UVGC_305_456,(2,0,7):C.UVGC_305_457,(2,0,8):C.UVGC_305_458,(2,0,9):C.UVGC_305_459,(2,0,10):C.UVGC_305_460,(2,0,11):C.UVGC_305_461,(2,0,12):C.UVGC_305_462,(2,0,13):C.UVGC_305_463,(2,0,14):C.UVGC_305_464,(2,0,15):C.UVGC_305_465,(2,0,16):C.UVGC_305_466,(2,0,17):C.UVGC_305_467,(2,0,18):C.UVGC_305_468,(2,0,19):C.UVGC_305_469,(2,0,20):C.UVGC_305_470,(2,0,21):C.UVGC_305_471,(2,0,22):C.UVGC_305_472,(2,0,23):C.UVGC_305_473,(2,0,24):C.UVGC_305_474,(2,0,25):C.UVGC_305_475,(2,0,26):C.UVGC_305_476,(2,0,27):C.UVGC_305_477,(2,0,28):C.UVGC_305_478,(2,0,29):C.UVGC_305_479,(2,0,30):C.UVGC_305_480,(2,0,31):C.UVGC_305_481,(2,0,32):C.UVGC_305_482,(2,0,5):C.UVGC_305_483,(1,0,0):C.UVGC_305_451,(1,0,1):C.UVGC_305_452,(1,0,2):C.UVGC_305_453,(1,0,3):C.UVGC_305_454,(1,0,4):C.UVGC_305_455,(1,0,6):C.UVGC_305_456,(1,0,7):C.UVGC_305_457,(1,0,8):C.UVGC_305_458,(1,0,9):C.UVGC_305_459,(1,0,10):C.UVGC_305_460,(1,0,11):C.UVGC_305_461,(1,0,12):C.UVGC_305_462,(1,0,13):C.UVGC_305_463,(1,0,14):C.UVGC_305_464,(1,0,15):C.UVGC_305_465,(1,0,16):C.UVGC_305_466,(1,0,17):C.UVGC_305_467,(1,0,18):C.UVGC_305_468,(1,0,19):C.UVGC_305_469,(1,0,20):C.UVGC_305_470,(1,0,21):C.UVGC_305_471,(1,0,22):C.UVGC_305_472,(1,0,23):C.UVGC_305_473,(1,0,24):C.UVGC_305_474,(1,0,25):C.UVGC_305_475,(1,0,26):C.UVGC_305_476,(1,0,27):C.UVGC_305_477,(1,0,28):C.UVGC_305_478,(1,0,29):C.UVGC_305_479,(1,0,30):C.UVGC_305_480,(1,0,31):C.UVGC_305_481,(1,0,32):C.UVGC_305_482,(1,0,5):C.UVGC_305_483,(0,0,3):C.UVGC_304_449,(0,0,5):C.UVGC_304_450})

V_581 = CTVertex(name = 'V_581',
                 type = 'UV',
                 particles = [ P.a, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_312_522})

V_582 = CTVertex(name = 'V_582',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.s, P.YS3d2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YS3d2] ], [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_749_981,(0,0,2):C.UVGC_749_982,(0,0,1):C.UVGC_749_983})

V_583 = CTVertex(name = 'V_583',
                 type = 'UV',
                 particles = [ P.Xm, P.s, P.YS3d2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YS3d2] ], [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_749_981,(0,0,2):C.UVGC_749_982,(0,0,1):C.UVGC_749_983})

V_584 = CTVertex(name = 'V_584',
                 type = 'UV',
                 particles = [ P.g, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_301_381,(0,0,1):C.UVGC_301_382,(0,0,2):C.UVGC_301_383,(0,0,3):C.UVGC_301_384,(0,0,4):C.UVGC_301_385,(0,0,6):C.UVGC_301_386,(0,0,7):C.UVGC_301_387,(0,0,8):C.UVGC_301_388,(0,0,9):C.UVGC_301_389,(0,0,10):C.UVGC_301_390,(0,0,11):C.UVGC_301_391,(0,0,12):C.UVGC_301_392,(0,0,13):C.UVGC_301_393,(0,0,14):C.UVGC_301_394,(0,0,15):C.UVGC_301_395,(0,0,16):C.UVGC_301_396,(0,0,17):C.UVGC_301_397,(0,0,18):C.UVGC_301_398,(0,0,19):C.UVGC_301_399,(0,0,20):C.UVGC_301_400,(0,0,21):C.UVGC_301_401,(0,0,22):C.UVGC_301_402,(0,0,23):C.UVGC_301_403,(0,0,24):C.UVGC_301_404,(0,0,25):C.UVGC_301_405,(0,0,26):C.UVGC_301_406,(0,0,27):C.UVGC_301_407,(0,0,28):C.UVGC_301_408,(0,0,29):C.UVGC_301_409,(0,0,30):C.UVGC_301_410,(0,0,31):C.UVGC_301_411,(0,0,32):C.UVGC_301_412,(0,0,5):C.UVGC_314_524})

V_585 = CTVertex(name = 'V_585',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.Xd, P.YS3d2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YS3d2] ], [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_749_981,(0,0,2):C.UVGC_749_982,(0,0,1):C.UVGC_749_983})

V_586 = CTVertex(name = 'V_586',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.Xm, P.YS3d2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YS3d2] ], [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_749_981,(0,0,2):C.UVGC_749_982,(0,0,1):C.UVGC_749_983})

V_587 = CTVertex(name = 'V_587',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_313_523})

V_588 = CTVertex(name = 'V_588',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_302_414,(0,0,1):C.UVGC_302_415,(0,0,2):C.UVGC_302_416,(0,0,3):C.UVGC_302_417,(0,0,4):C.UVGC_302_418,(0,0,6):C.UVGC_302_419,(0,0,7):C.UVGC_302_420,(0,0,8):C.UVGC_302_421,(0,0,9):C.UVGC_302_422,(0,0,10):C.UVGC_302_423,(0,0,11):C.UVGC_302_424,(0,0,12):C.UVGC_302_425,(0,0,13):C.UVGC_302_426,(0,0,14):C.UVGC_302_427,(0,0,15):C.UVGC_302_428,(0,0,16):C.UVGC_302_429,(0,0,17):C.UVGC_302_430,(0,0,18):C.UVGC_302_431,(0,0,19):C.UVGC_302_432,(0,0,20):C.UVGC_302_433,(0,0,21):C.UVGC_302_434,(0,0,22):C.UVGC_302_435,(0,0,23):C.UVGC_302_436,(0,0,24):C.UVGC_302_437,(0,0,25):C.UVGC_302_438,(0,0,26):C.UVGC_302_439,(0,0,27):C.UVGC_302_440,(0,0,28):C.UVGC_302_441,(0,0,29):C.UVGC_302_442,(0,0,30):C.UVGC_302_443,(0,0,31):C.UVGC_302_444,(0,0,32):C.UVGC_302_445,(0,0,5):C.UVGC_315_525})

V_589 = CTVertex(name = 'V_589',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_305_451,(2,0,1):C.UVGC_305_452,(2,0,2):C.UVGC_305_453,(2,0,3):C.UVGC_305_454,(2,0,4):C.UVGC_305_455,(2,0,6):C.UVGC_305_456,(2,0,7):C.UVGC_305_457,(2,0,8):C.UVGC_305_458,(2,0,9):C.UVGC_305_459,(2,0,10):C.UVGC_305_460,(2,0,11):C.UVGC_305_461,(2,0,12):C.UVGC_305_462,(2,0,13):C.UVGC_305_463,(2,0,14):C.UVGC_305_464,(2,0,15):C.UVGC_305_465,(2,0,16):C.UVGC_305_466,(2,0,17):C.UVGC_305_467,(2,0,18):C.UVGC_305_468,(2,0,19):C.UVGC_305_469,(2,0,20):C.UVGC_305_470,(2,0,21):C.UVGC_305_471,(2,0,22):C.UVGC_305_472,(2,0,23):C.UVGC_305_473,(2,0,24):C.UVGC_305_474,(2,0,25):C.UVGC_305_475,(2,0,26):C.UVGC_305_476,(2,0,27):C.UVGC_305_477,(2,0,28):C.UVGC_305_478,(2,0,29):C.UVGC_305_479,(2,0,30):C.UVGC_305_480,(2,0,31):C.UVGC_305_481,(2,0,32):C.UVGC_305_482,(2,0,5):C.UVGC_318_526,(1,0,0):C.UVGC_305_451,(1,0,1):C.UVGC_305_452,(1,0,2):C.UVGC_305_453,(1,0,3):C.UVGC_305_454,(1,0,4):C.UVGC_305_455,(1,0,6):C.UVGC_305_456,(1,0,7):C.UVGC_305_457,(1,0,8):C.UVGC_305_458,(1,0,9):C.UVGC_305_459,(1,0,10):C.UVGC_305_460,(1,0,11):C.UVGC_305_461,(1,0,12):C.UVGC_305_462,(1,0,13):C.UVGC_305_463,(1,0,14):C.UVGC_305_464,(1,0,15):C.UVGC_305_465,(1,0,16):C.UVGC_305_466,(1,0,17):C.UVGC_305_467,(1,0,18):C.UVGC_305_468,(1,0,19):C.UVGC_305_469,(1,0,20):C.UVGC_305_470,(1,0,21):C.UVGC_305_471,(1,0,22):C.UVGC_305_472,(1,0,23):C.UVGC_305_473,(1,0,24):C.UVGC_305_474,(1,0,25):C.UVGC_305_475,(1,0,26):C.UVGC_305_476,(1,0,27):C.UVGC_305_477,(1,0,28):C.UVGC_305_478,(1,0,29):C.UVGC_305_479,(1,0,30):C.UVGC_305_480,(1,0,31):C.UVGC_305_481,(1,0,32):C.UVGC_305_482,(1,0,5):C.UVGC_318_526,(0,0,3):C.UVGC_304_449,(0,0,5):C.UVGC_304_450})

V_590 = CTVertex(name = 'V_590',
                 type = 'UV',
                 particles = [ P.a, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_325_533})

V_591 = CTVertex(name = 'V_591',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.b, P.YS3d3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YS3d3] ], [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_572_841,(0,0,2):C.UVGC_572_842,(0,0,1):C.UVGC_572_843})

V_592 = CTVertex(name = 'V_592',
                 type = 'UV',
                 particles = [ P.Xm, P.b, P.YS3d3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YS3d3] ], [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_572_841,(0,0,2):C.UVGC_572_842,(0,0,1):C.UVGC_572_843})

V_593 = CTVertex(name = 'V_593',
                 type = 'UV',
                 particles = [ P.g, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_301_381,(0,0,1):C.UVGC_301_382,(0,0,2):C.UVGC_301_383,(0,0,3):C.UVGC_301_384,(0,0,4):C.UVGC_301_385,(0,0,6):C.UVGC_301_386,(0,0,7):C.UVGC_301_387,(0,0,8):C.UVGC_301_388,(0,0,9):C.UVGC_301_389,(0,0,10):C.UVGC_301_390,(0,0,11):C.UVGC_301_391,(0,0,12):C.UVGC_301_392,(0,0,13):C.UVGC_301_393,(0,0,14):C.UVGC_301_394,(0,0,15):C.UVGC_301_395,(0,0,16):C.UVGC_301_396,(0,0,17):C.UVGC_301_397,(0,0,18):C.UVGC_301_398,(0,0,19):C.UVGC_301_399,(0,0,20):C.UVGC_301_400,(0,0,21):C.UVGC_301_401,(0,0,22):C.UVGC_301_402,(0,0,23):C.UVGC_301_403,(0,0,24):C.UVGC_301_404,(0,0,25):C.UVGC_301_405,(0,0,26):C.UVGC_301_406,(0,0,27):C.UVGC_301_407,(0,0,28):C.UVGC_301_408,(0,0,29):C.UVGC_301_409,(0,0,30):C.UVGC_301_410,(0,0,31):C.UVGC_301_411,(0,0,32):C.UVGC_301_412,(0,0,5):C.UVGC_327_535})

V_594 = CTVertex(name = 'V_594',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.Xd, P.YS3d3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YS3d3] ], [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_572_841,(0,0,2):C.UVGC_572_842,(0,0,1):C.UVGC_572_843})

V_595 = CTVertex(name = 'V_595',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.Xm, P.YS3d3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YS3d3] ], [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_572_841,(0,0,2):C.UVGC_572_842,(0,0,1):C.UVGC_572_843})

V_596 = CTVertex(name = 'V_596',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_326_534})

V_597 = CTVertex(name = 'V_597',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_302_414,(0,0,1):C.UVGC_302_415,(0,0,2):C.UVGC_302_416,(0,0,3):C.UVGC_302_417,(0,0,4):C.UVGC_302_418,(0,0,6):C.UVGC_302_419,(0,0,7):C.UVGC_302_420,(0,0,8):C.UVGC_302_421,(0,0,9):C.UVGC_302_422,(0,0,10):C.UVGC_302_423,(0,0,11):C.UVGC_302_424,(0,0,12):C.UVGC_302_425,(0,0,13):C.UVGC_302_426,(0,0,14):C.UVGC_302_427,(0,0,15):C.UVGC_302_428,(0,0,16):C.UVGC_302_429,(0,0,17):C.UVGC_302_430,(0,0,18):C.UVGC_302_431,(0,0,19):C.UVGC_302_432,(0,0,20):C.UVGC_302_433,(0,0,21):C.UVGC_302_434,(0,0,22):C.UVGC_302_435,(0,0,23):C.UVGC_302_436,(0,0,24):C.UVGC_302_437,(0,0,25):C.UVGC_302_438,(0,0,26):C.UVGC_302_439,(0,0,27):C.UVGC_302_440,(0,0,28):C.UVGC_302_441,(0,0,29):C.UVGC_302_442,(0,0,30):C.UVGC_302_443,(0,0,31):C.UVGC_302_444,(0,0,32):C.UVGC_302_445,(0,0,5):C.UVGC_328_536})

V_598 = CTVertex(name = 'V_598',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_305_451,(2,0,1):C.UVGC_305_452,(2,0,2):C.UVGC_305_453,(2,0,3):C.UVGC_305_454,(2,0,4):C.UVGC_305_455,(2,0,6):C.UVGC_305_456,(2,0,7):C.UVGC_305_457,(2,0,8):C.UVGC_305_458,(2,0,9):C.UVGC_305_459,(2,0,10):C.UVGC_305_460,(2,0,11):C.UVGC_305_461,(2,0,12):C.UVGC_305_462,(2,0,13):C.UVGC_305_463,(2,0,14):C.UVGC_305_464,(2,0,15):C.UVGC_305_465,(2,0,16):C.UVGC_305_466,(2,0,17):C.UVGC_305_467,(2,0,18):C.UVGC_305_468,(2,0,19):C.UVGC_305_469,(2,0,20):C.UVGC_305_470,(2,0,21):C.UVGC_305_471,(2,0,22):C.UVGC_305_472,(2,0,23):C.UVGC_305_473,(2,0,24):C.UVGC_305_474,(2,0,25):C.UVGC_305_475,(2,0,26):C.UVGC_305_476,(2,0,27):C.UVGC_305_477,(2,0,28):C.UVGC_305_478,(2,0,29):C.UVGC_305_479,(2,0,30):C.UVGC_305_480,(2,0,31):C.UVGC_305_481,(2,0,32):C.UVGC_305_482,(2,0,5):C.UVGC_331_537,(1,0,0):C.UVGC_305_451,(1,0,1):C.UVGC_305_452,(1,0,2):C.UVGC_305_453,(1,0,3):C.UVGC_305_454,(1,0,4):C.UVGC_305_455,(1,0,6):C.UVGC_305_456,(1,0,7):C.UVGC_305_457,(1,0,8):C.UVGC_305_458,(1,0,9):C.UVGC_305_459,(1,0,10):C.UVGC_305_460,(1,0,11):C.UVGC_305_461,(1,0,12):C.UVGC_305_462,(1,0,13):C.UVGC_305_463,(1,0,14):C.UVGC_305_464,(1,0,15):C.UVGC_305_465,(1,0,16):C.UVGC_305_466,(1,0,17):C.UVGC_305_467,(1,0,18):C.UVGC_305_468,(1,0,19):C.UVGC_305_469,(1,0,20):C.UVGC_305_470,(1,0,21):C.UVGC_305_471,(1,0,22):C.UVGC_305_472,(1,0,23):C.UVGC_305_473,(1,0,24):C.UVGC_305_474,(1,0,25):C.UVGC_305_475,(1,0,26):C.UVGC_305_476,(1,0,27):C.UVGC_305_477,(1,0,28):C.UVGC_305_478,(1,0,29):C.UVGC_305_479,(1,0,30):C.UVGC_305_480,(1,0,31):C.UVGC_305_481,(1,0,32):C.UVGC_305_482,(1,0,5):C.UVGC_331_537,(0,0,3):C.UVGC_304_449,(0,0,5):C.UVGC_304_450})

V_599 = CTVertex(name = 'V_599',
                 type = 'UV',
                 particles = [ P.a, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_338_544})

V_600 = CTVertex(name = 'V_600',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.d, P.YS3Qd1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_586_879,(0,0,2):C.UVGC_586_880,(0,0,1):C.UVGC_586_881})

V_601 = CTVertex(name = 'V_601',
                 type = 'UV',
                 particles = [ P.Xm, P.d, P.YS3Qd1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_586_879,(0,0,2):C.UVGC_586_880,(0,0,1):C.UVGC_586_881})

V_602 = CTVertex(name = 'V_602',
                 type = 'UV',
                 particles = [ P.W__minus__, P.YS3Qd1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,1,0):C.UVGC_651_907,(0,1,2):C.UVGC_651_908,(0,1,1):C.UVGC_651_909,(0,0,0):C.UVGC_163_15,(0,2,2):C.UVGC_164_16})

V_603 = CTVertex(name = 'V_603',
                 type = 'UV',
                 particles = [ P.g, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_301_381,(0,0,1):C.UVGC_301_382,(0,0,2):C.UVGC_301_383,(0,0,3):C.UVGC_301_384,(0,0,4):C.UVGC_301_385,(0,0,6):C.UVGC_301_386,(0,0,7):C.UVGC_301_387,(0,0,8):C.UVGC_301_388,(0,0,9):C.UVGC_301_389,(0,0,10):C.UVGC_301_390,(0,0,11):C.UVGC_301_391,(0,0,12):C.UVGC_301_392,(0,0,13):C.UVGC_301_393,(0,0,14):C.UVGC_301_394,(0,0,15):C.UVGC_301_395,(0,0,16):C.UVGC_301_396,(0,0,17):C.UVGC_301_397,(0,0,18):C.UVGC_301_398,(0,0,19):C.UVGC_301_399,(0,0,20):C.UVGC_301_400,(0,0,21):C.UVGC_301_401,(0,0,22):C.UVGC_301_402,(0,0,23):C.UVGC_301_403,(0,0,24):C.UVGC_301_404,(0,0,25):C.UVGC_301_405,(0,0,26):C.UVGC_301_406,(0,0,27):C.UVGC_301_407,(0,0,28):C.UVGC_301_408,(0,0,29):C.UVGC_301_409,(0,0,30):C.UVGC_301_410,(0,0,31):C.UVGC_301_411,(0,0,32):C.UVGC_301_412,(0,0,5):C.UVGC_340_546})

V_604 = CTVertex(name = 'V_604',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.Xd, P.YS3Qd1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_586_879,(0,0,2):C.UVGC_586_880,(0,0,1):C.UVGC_586_881})

V_605 = CTVertex(name = 'V_605',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.Xm, P.YS3Qd1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_586_879,(0,0,2):C.UVGC_586_880,(0,0,1):C.UVGC_586_881})

V_606 = CTVertex(name = 'V_606',
                 type = 'UV',
                 particles = [ P.W__plus__, P.YS3Qd1, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_650_905,(0,0,2):C.UVGC_650_906,(0,0,1):C.UVGC_580_865,(0,1,0):C.UVGC_651_907,(0,1,2):C.UVGC_652_910,(0,1,1):C.UVGC_651_909})

V_607 = CTVertex(name = 'V_607',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_339_545})

V_608 = CTVertex(name = 'V_608',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_649_904,(0,0,2):C.UVGC_648_901,(0,0,1):C.UVGC_648_903})

V_609 = CTVertex(name = 'V_609',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_302_414,(0,0,1):C.UVGC_302_415,(0,0,2):C.UVGC_302_416,(0,0,3):C.UVGC_302_417,(0,0,4):C.UVGC_302_418,(0,0,6):C.UVGC_302_419,(0,0,7):C.UVGC_302_420,(0,0,8):C.UVGC_302_421,(0,0,9):C.UVGC_302_422,(0,0,10):C.UVGC_302_423,(0,0,11):C.UVGC_302_424,(0,0,12):C.UVGC_302_425,(0,0,13):C.UVGC_302_426,(0,0,14):C.UVGC_302_427,(0,0,15):C.UVGC_302_428,(0,0,16):C.UVGC_302_429,(0,0,17):C.UVGC_302_430,(0,0,18):C.UVGC_302_431,(0,0,19):C.UVGC_302_432,(0,0,20):C.UVGC_302_433,(0,0,21):C.UVGC_302_434,(0,0,22):C.UVGC_302_435,(0,0,23):C.UVGC_302_436,(0,0,24):C.UVGC_302_437,(0,0,25):C.UVGC_302_438,(0,0,26):C.UVGC_302_439,(0,0,27):C.UVGC_302_440,(0,0,28):C.UVGC_302_441,(0,0,29):C.UVGC_302_442,(0,0,30):C.UVGC_302_443,(0,0,31):C.UVGC_302_444,(0,0,32):C.UVGC_302_445,(0,0,5):C.UVGC_341_547})

V_610 = CTVertex(name = 'V_610',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_305_451,(2,0,1):C.UVGC_305_452,(2,0,2):C.UVGC_305_453,(2,0,3):C.UVGC_305_454,(2,0,4):C.UVGC_305_455,(2,0,6):C.UVGC_305_456,(2,0,7):C.UVGC_305_457,(2,0,8):C.UVGC_305_458,(2,0,9):C.UVGC_305_459,(2,0,10):C.UVGC_305_460,(2,0,11):C.UVGC_305_461,(2,0,12):C.UVGC_305_462,(2,0,13):C.UVGC_305_463,(2,0,14):C.UVGC_305_464,(2,0,15):C.UVGC_305_465,(2,0,16):C.UVGC_305_466,(2,0,17):C.UVGC_305_467,(2,0,18):C.UVGC_305_468,(2,0,19):C.UVGC_305_469,(2,0,20):C.UVGC_305_470,(2,0,21):C.UVGC_305_471,(2,0,22):C.UVGC_305_472,(2,0,23):C.UVGC_305_473,(2,0,24):C.UVGC_305_474,(2,0,25):C.UVGC_305_475,(2,0,26):C.UVGC_305_476,(2,0,27):C.UVGC_305_477,(2,0,28):C.UVGC_305_478,(2,0,29):C.UVGC_305_479,(2,0,30):C.UVGC_305_480,(2,0,31):C.UVGC_305_481,(2,0,32):C.UVGC_305_482,(2,0,5):C.UVGC_344_548,(1,0,0):C.UVGC_305_451,(1,0,1):C.UVGC_305_452,(1,0,2):C.UVGC_305_453,(1,0,3):C.UVGC_305_454,(1,0,4):C.UVGC_305_455,(1,0,6):C.UVGC_305_456,(1,0,7):C.UVGC_305_457,(1,0,8):C.UVGC_305_458,(1,0,9):C.UVGC_305_459,(1,0,10):C.UVGC_305_460,(1,0,11):C.UVGC_305_461,(1,0,12):C.UVGC_305_462,(1,0,13):C.UVGC_305_463,(1,0,14):C.UVGC_305_464,(1,0,15):C.UVGC_305_465,(1,0,16):C.UVGC_305_466,(1,0,17):C.UVGC_305_467,(1,0,18):C.UVGC_305_468,(1,0,19):C.UVGC_305_469,(1,0,20):C.UVGC_305_470,(1,0,21):C.UVGC_305_471,(1,0,22):C.UVGC_305_472,(1,0,23):C.UVGC_305_473,(1,0,24):C.UVGC_305_474,(1,0,25):C.UVGC_305_475,(1,0,26):C.UVGC_305_476,(1,0,27):C.UVGC_305_477,(1,0,28):C.UVGC_305_478,(1,0,29):C.UVGC_305_479,(1,0,30):C.UVGC_305_480,(1,0,31):C.UVGC_305_481,(1,0,32):C.UVGC_305_482,(1,0,5):C.UVGC_344_548,(0,0,3):C.UVGC_304_449,(0,0,5):C.UVGC_304_450})

V_611 = CTVertex(name = 'V_611',
                 type = 'UV',
                 particles = [ P.a, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_352_588,(0,1,0):C.UVGC_351_587})

V_612 = CTVertex(name = 'V_612',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.s, P.YS3Qd2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YS3Qd2] ], [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_750_984,(0,0,2):C.UVGC_750_985,(0,0,1):C.UVGC_578_859})

V_613 = CTVertex(name = 'V_613',
                 type = 'UV',
                 particles = [ P.Xm, P.s, P.YS3Qd2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YS3Qd2] ], [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_750_984,(0,0,2):C.UVGC_750_985,(0,0,1):C.UVGC_578_859})

V_614 = CTVertex(name = 'V_614',
                 type = 'UV',
                 particles = [ P.W__minus__, P.YS3Qd2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_684_957,(0,0,2):C.UVGC_684_958,(0,0,1):C.UVGC_651_909,(0,1,0):C.UVGC_683_955,(0,1,2):C.UVGC_683_956,(0,1,1):C.UVGC_580_865})

V_615 = CTVertex(name = 'V_615',
                 type = 'UV',
                 particles = [ P.g, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_301_381,(0,0,1):C.UVGC_301_382,(0,0,2):C.UVGC_301_383,(0,0,3):C.UVGC_301_384,(0,0,4):C.UVGC_301_385,(0,0,6):C.UVGC_301_386,(0,0,7):C.UVGC_301_387,(0,0,8):C.UVGC_301_388,(0,0,9):C.UVGC_301_389,(0,0,10):C.UVGC_301_390,(0,0,11):C.UVGC_301_391,(0,0,12):C.UVGC_301_392,(0,0,13):C.UVGC_301_393,(0,0,14):C.UVGC_301_394,(0,0,15):C.UVGC_301_395,(0,0,16):C.UVGC_301_396,(0,0,17):C.UVGC_301_397,(0,0,18):C.UVGC_301_398,(0,0,19):C.UVGC_301_399,(0,0,20):C.UVGC_301_400,(0,0,21):C.UVGC_301_401,(0,0,22):C.UVGC_301_402,(0,0,23):C.UVGC_301_403,(0,0,24):C.UVGC_301_404,(0,0,25):C.UVGC_301_405,(0,0,26):C.UVGC_301_406,(0,0,27):C.UVGC_301_407,(0,0,28):C.UVGC_301_408,(0,0,29):C.UVGC_301_409,(0,0,30):C.UVGC_301_410,(0,0,31):C.UVGC_301_411,(0,0,32):C.UVGC_301_412,(0,0,5):C.UVGC_355_591,(0,1,0):C.UVGC_266_121,(0,1,1):C.UVGC_266_122,(0,1,2):C.UVGC_266_123,(0,1,3):C.UVGC_266_124,(0,1,4):C.UVGC_266_125,(0,1,6):C.UVGC_266_126,(0,1,7):C.UVGC_266_127,(0,1,8):C.UVGC_266_128,(0,1,9):C.UVGC_266_129,(0,1,10):C.UVGC_266_130,(0,1,11):C.UVGC_266_131,(0,1,12):C.UVGC_266_132,(0,1,13):C.UVGC_266_133,(0,1,14):C.UVGC_266_134,(0,1,15):C.UVGC_266_135,(0,1,16):C.UVGC_266_136,(0,1,17):C.UVGC_266_137,(0,1,18):C.UVGC_266_138,(0,1,19):C.UVGC_266_139,(0,1,20):C.UVGC_266_140,(0,1,21):C.UVGC_266_141,(0,1,22):C.UVGC_266_142,(0,1,23):C.UVGC_266_143,(0,1,24):C.UVGC_266_144,(0,1,25):C.UVGC_266_145,(0,1,26):C.UVGC_266_146,(0,1,27):C.UVGC_266_147,(0,1,28):C.UVGC_266_148,(0,1,29):C.UVGC_266_149,(0,1,30):C.UVGC_266_150,(0,1,31):C.UVGC_266_151,(0,1,32):C.UVGC_266_152,(0,1,5):C.UVGC_354_590})

V_616 = CTVertex(name = 'V_616',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.Xd, P.YS3Qd2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YS3Qd2] ], [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_750_984,(0,0,2):C.UVGC_750_985,(0,0,1):C.UVGC_578_859})

V_617 = CTVertex(name = 'V_617',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.Xm, P.YS3Qd2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YS3Qd2] ], [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_750_984,(0,0,2):C.UVGC_750_985,(0,0,1):C.UVGC_578_859})

V_618 = CTVertex(name = 'V_618',
                 type = 'UV',
                 particles = [ P.W__plus__, P.YS3Qd2, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_682_953,(0,0,2):C.UVGC_682_954,(0,0,1):C.UVGC_580_865,(0,1,0):C.UVGC_685_959,(0,1,2):C.UVGC_685_960,(0,1,1):C.UVGC_651_909})

V_619 = CTVertex(name = 'V_619',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_353_589})

V_620 = CTVertex(name = 'V_620',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_681_952,(0,0,2):C.UVGC_648_901,(0,0,1):C.UVGC_648_903})

V_621 = CTVertex(name = 'V_621',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_302_414,(0,0,1):C.UVGC_302_415,(0,0,2):C.UVGC_302_416,(0,0,3):C.UVGC_302_417,(0,0,4):C.UVGC_302_418,(0,0,6):C.UVGC_302_419,(0,0,7):C.UVGC_302_420,(0,0,8):C.UVGC_302_421,(0,0,9):C.UVGC_302_422,(0,0,10):C.UVGC_302_423,(0,0,11):C.UVGC_302_424,(0,0,12):C.UVGC_302_425,(0,0,13):C.UVGC_302_426,(0,0,14):C.UVGC_302_427,(0,0,15):C.UVGC_302_428,(0,0,16):C.UVGC_302_429,(0,0,17):C.UVGC_302_430,(0,0,18):C.UVGC_302_431,(0,0,19):C.UVGC_302_432,(0,0,20):C.UVGC_302_433,(0,0,21):C.UVGC_302_434,(0,0,22):C.UVGC_302_435,(0,0,23):C.UVGC_302_436,(0,0,24):C.UVGC_302_437,(0,0,25):C.UVGC_302_438,(0,0,26):C.UVGC_302_439,(0,0,27):C.UVGC_302_440,(0,0,28):C.UVGC_302_441,(0,0,29):C.UVGC_302_442,(0,0,30):C.UVGC_302_443,(0,0,31):C.UVGC_302_444,(0,0,32):C.UVGC_302_445,(0,0,5):C.UVGC_356_592})

V_622 = CTVertex(name = 'V_622',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_305_451,(2,0,1):C.UVGC_305_452,(2,0,2):C.UVGC_305_453,(2,0,3):C.UVGC_305_454,(2,0,4):C.UVGC_305_455,(2,0,6):C.UVGC_305_456,(2,0,7):C.UVGC_305_457,(2,0,8):C.UVGC_305_458,(2,0,9):C.UVGC_305_459,(2,0,10):C.UVGC_305_460,(2,0,11):C.UVGC_305_461,(2,0,12):C.UVGC_305_462,(2,0,13):C.UVGC_305_463,(2,0,14):C.UVGC_305_464,(2,0,15):C.UVGC_305_465,(2,0,16):C.UVGC_305_466,(2,0,17):C.UVGC_305_467,(2,0,18):C.UVGC_305_468,(2,0,19):C.UVGC_305_469,(2,0,20):C.UVGC_305_470,(2,0,21):C.UVGC_305_471,(2,0,22):C.UVGC_305_472,(2,0,23):C.UVGC_305_473,(2,0,24):C.UVGC_305_474,(2,0,25):C.UVGC_305_475,(2,0,26):C.UVGC_305_476,(2,0,27):C.UVGC_305_477,(2,0,28):C.UVGC_305_478,(2,0,29):C.UVGC_305_479,(2,0,30):C.UVGC_305_480,(2,0,31):C.UVGC_305_481,(2,0,32):C.UVGC_305_482,(2,0,5):C.UVGC_359_593,(1,0,0):C.UVGC_305_451,(1,0,1):C.UVGC_305_452,(1,0,2):C.UVGC_305_453,(1,0,3):C.UVGC_305_454,(1,0,4):C.UVGC_305_455,(1,0,6):C.UVGC_305_456,(1,0,7):C.UVGC_305_457,(1,0,8):C.UVGC_305_458,(1,0,9):C.UVGC_305_459,(1,0,10):C.UVGC_305_460,(1,0,11):C.UVGC_305_461,(1,0,12):C.UVGC_305_462,(1,0,13):C.UVGC_305_463,(1,0,14):C.UVGC_305_464,(1,0,15):C.UVGC_305_465,(1,0,16):C.UVGC_305_466,(1,0,17):C.UVGC_305_467,(1,0,18):C.UVGC_305_468,(1,0,19):C.UVGC_305_469,(1,0,20):C.UVGC_305_470,(1,0,21):C.UVGC_305_471,(1,0,22):C.UVGC_305_472,(1,0,23):C.UVGC_305_473,(1,0,24):C.UVGC_305_474,(1,0,25):C.UVGC_305_475,(1,0,26):C.UVGC_305_476,(1,0,27):C.UVGC_305_477,(1,0,28):C.UVGC_305_478,(1,0,29):C.UVGC_305_479,(1,0,30):C.UVGC_305_480,(1,0,31):C.UVGC_305_481,(1,0,32):C.UVGC_305_482,(1,0,5):C.UVGC_359_593,(0,0,3):C.UVGC_304_449,(0,0,5):C.UVGC_304_450})

V_623 = CTVertex(name = 'V_623',
                 type = 'UV',
                 particles = [ P.a, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_367_601,(0,1,0):C.UVGC_366_600})

V_624 = CTVertex(name = 'V_624',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.b, P.YS3Qd3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_573_844,(0,0,2):C.UVGC_573_845,(0,0,1):C.UVGC_573_846})

V_625 = CTVertex(name = 'V_625',
                 type = 'UV',
                 particles = [ P.Xm, P.b, P.YS3Qd3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_573_844,(0,0,2):C.UVGC_573_845,(0,0,1):C.UVGC_573_846})

V_626 = CTVertex(name = 'V_626',
                 type = 'UV',
                 particles = [ P.W__minus__, P.YS3Qd3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_715_973,(0,0,2):C.UVGC_715_974,(0,0,1):C.UVGC_651_909,(0,1,0):C.UVGC_714_971,(0,1,2):C.UVGC_714_972,(0,1,1):C.UVGC_580_865})

V_627 = CTVertex(name = 'V_627',
                 type = 'UV',
                 particles = [ P.g, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_301_381,(0,0,1):C.UVGC_301_382,(0,0,2):C.UVGC_301_383,(0,0,3):C.UVGC_301_384,(0,0,4):C.UVGC_301_385,(0,0,6):C.UVGC_301_386,(0,0,7):C.UVGC_301_387,(0,0,8):C.UVGC_301_388,(0,0,9):C.UVGC_301_389,(0,0,10):C.UVGC_301_390,(0,0,11):C.UVGC_301_391,(0,0,12):C.UVGC_301_392,(0,0,13):C.UVGC_301_393,(0,0,14):C.UVGC_301_394,(0,0,15):C.UVGC_301_395,(0,0,16):C.UVGC_301_396,(0,0,17):C.UVGC_301_397,(0,0,18):C.UVGC_301_398,(0,0,19):C.UVGC_301_399,(0,0,20):C.UVGC_301_400,(0,0,21):C.UVGC_301_401,(0,0,22):C.UVGC_301_402,(0,0,23):C.UVGC_301_403,(0,0,24):C.UVGC_301_404,(0,0,25):C.UVGC_301_405,(0,0,26):C.UVGC_301_406,(0,0,27):C.UVGC_301_407,(0,0,28):C.UVGC_301_408,(0,0,29):C.UVGC_301_409,(0,0,30):C.UVGC_301_410,(0,0,31):C.UVGC_301_411,(0,0,32):C.UVGC_301_412,(0,0,5):C.UVGC_370_604,(0,1,0):C.UVGC_266_121,(0,1,1):C.UVGC_266_122,(0,1,2):C.UVGC_266_123,(0,1,3):C.UVGC_266_124,(0,1,4):C.UVGC_266_125,(0,1,6):C.UVGC_266_126,(0,1,7):C.UVGC_266_127,(0,1,8):C.UVGC_266_128,(0,1,9):C.UVGC_266_129,(0,1,10):C.UVGC_266_130,(0,1,11):C.UVGC_266_131,(0,1,12):C.UVGC_266_132,(0,1,13):C.UVGC_266_133,(0,1,14):C.UVGC_266_134,(0,1,15):C.UVGC_266_135,(0,1,16):C.UVGC_266_136,(0,1,17):C.UVGC_266_137,(0,1,18):C.UVGC_266_138,(0,1,19):C.UVGC_266_139,(0,1,20):C.UVGC_266_140,(0,1,21):C.UVGC_266_141,(0,1,22):C.UVGC_266_142,(0,1,23):C.UVGC_266_143,(0,1,24):C.UVGC_266_144,(0,1,25):C.UVGC_266_145,(0,1,26):C.UVGC_266_146,(0,1,27):C.UVGC_266_147,(0,1,28):C.UVGC_266_148,(0,1,29):C.UVGC_266_149,(0,1,30):C.UVGC_266_150,(0,1,31):C.UVGC_266_151,(0,1,32):C.UVGC_266_152,(0,1,5):C.UVGC_369_603})

V_628 = CTVertex(name = 'V_628',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.Xd, P.YS3Qd3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_573_844,(0,0,2):C.UVGC_573_845,(0,0,1):C.UVGC_573_846})

V_629 = CTVertex(name = 'V_629',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.Xm, P.YS3Qd3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_573_844,(0,0,2):C.UVGC_573_845,(0,0,1):C.UVGC_573_846})

V_630 = CTVertex(name = 'V_630',
                 type = 'UV',
                 particles = [ P.W__plus__, P.YS3Qd3, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_713_969,(0,0,2):C.UVGC_713_970,(0,0,1):C.UVGC_580_865,(0,1,0):C.UVGC_716_975,(0,1,2):C.UVGC_716_976,(0,1,1):C.UVGC_651_909})

V_631 = CTVertex(name = 'V_631',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_368_602})

V_632 = CTVertex(name = 'V_632',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_712_968,(0,0,2):C.UVGC_648_901,(0,0,1):C.UVGC_648_903})

V_633 = CTVertex(name = 'V_633',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_302_414,(0,0,1):C.UVGC_302_415,(0,0,2):C.UVGC_302_416,(0,0,3):C.UVGC_302_417,(0,0,4):C.UVGC_302_418,(0,0,6):C.UVGC_302_419,(0,0,7):C.UVGC_302_420,(0,0,8):C.UVGC_302_421,(0,0,9):C.UVGC_302_422,(0,0,10):C.UVGC_302_423,(0,0,11):C.UVGC_302_424,(0,0,12):C.UVGC_302_425,(0,0,13):C.UVGC_302_426,(0,0,14):C.UVGC_302_427,(0,0,15):C.UVGC_302_428,(0,0,16):C.UVGC_302_429,(0,0,17):C.UVGC_302_430,(0,0,18):C.UVGC_302_431,(0,0,19):C.UVGC_302_432,(0,0,20):C.UVGC_302_433,(0,0,21):C.UVGC_302_434,(0,0,22):C.UVGC_302_435,(0,0,23):C.UVGC_302_436,(0,0,24):C.UVGC_302_437,(0,0,25):C.UVGC_302_438,(0,0,26):C.UVGC_302_439,(0,0,27):C.UVGC_302_440,(0,0,28):C.UVGC_302_441,(0,0,29):C.UVGC_302_442,(0,0,30):C.UVGC_302_443,(0,0,31):C.UVGC_302_444,(0,0,32):C.UVGC_302_445,(0,0,5):C.UVGC_371_605})

V_634 = CTVertex(name = 'V_634',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_305_451,(2,0,1):C.UVGC_305_452,(2,0,2):C.UVGC_305_453,(2,0,3):C.UVGC_305_454,(2,0,4):C.UVGC_305_455,(2,0,6):C.UVGC_305_456,(2,0,7):C.UVGC_305_457,(2,0,8):C.UVGC_305_458,(2,0,9):C.UVGC_305_459,(2,0,10):C.UVGC_305_460,(2,0,11):C.UVGC_305_461,(2,0,12):C.UVGC_305_462,(2,0,13):C.UVGC_305_463,(2,0,14):C.UVGC_305_464,(2,0,15):C.UVGC_305_465,(2,0,16):C.UVGC_305_466,(2,0,17):C.UVGC_305_467,(2,0,18):C.UVGC_305_468,(2,0,19):C.UVGC_305_469,(2,0,20):C.UVGC_305_470,(2,0,21):C.UVGC_305_471,(2,0,22):C.UVGC_305_472,(2,0,23):C.UVGC_305_473,(2,0,24):C.UVGC_305_474,(2,0,25):C.UVGC_305_475,(2,0,26):C.UVGC_305_476,(2,0,27):C.UVGC_305_477,(2,0,28):C.UVGC_305_478,(2,0,29):C.UVGC_305_479,(2,0,30):C.UVGC_305_480,(2,0,31):C.UVGC_305_481,(2,0,32):C.UVGC_305_482,(2,0,5):C.UVGC_374_606,(1,0,0):C.UVGC_305_451,(1,0,1):C.UVGC_305_452,(1,0,2):C.UVGC_305_453,(1,0,3):C.UVGC_305_454,(1,0,4):C.UVGC_305_455,(1,0,6):C.UVGC_305_456,(1,0,7):C.UVGC_305_457,(1,0,8):C.UVGC_305_458,(1,0,9):C.UVGC_305_459,(1,0,10):C.UVGC_305_460,(1,0,11):C.UVGC_305_461,(1,0,12):C.UVGC_305_462,(1,0,13):C.UVGC_305_463,(1,0,14):C.UVGC_305_464,(1,0,15):C.UVGC_305_465,(1,0,16):C.UVGC_305_466,(1,0,17):C.UVGC_305_467,(1,0,18):C.UVGC_305_468,(1,0,19):C.UVGC_305_469,(1,0,20):C.UVGC_305_470,(1,0,21):C.UVGC_305_471,(1,0,22):C.UVGC_305_472,(1,0,23):C.UVGC_305_473,(1,0,24):C.UVGC_305_474,(1,0,25):C.UVGC_305_475,(1,0,26):C.UVGC_305_476,(1,0,27):C.UVGC_305_477,(1,0,28):C.UVGC_305_478,(1,0,29):C.UVGC_305_479,(1,0,30):C.UVGC_305_480,(1,0,31):C.UVGC_305_481,(1,0,32):C.UVGC_305_482,(1,0,5):C.UVGC_374_606,(0,0,3):C.UVGC_304_449,(0,0,5):C.UVGC_304_450})

V_635 = CTVertex(name = 'V_635',
                 type = 'UV',
                 particles = [ P.a, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_381_613,(0,1,0):C.UVGC_382_614})

V_636 = CTVertex(name = 'V_636',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.u, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_765_1017,(0,0,2):C.UVGC_765_1018,(0,0,1):C.UVGC_586_881})

V_637 = CTVertex(name = 'V_637',
                 type = 'UV',
                 particles = [ P.Xm, P.u, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_765_1017,(0,0,2):C.UVGC_765_1018,(0,0,1):C.UVGC_586_881})

V_638 = CTVertex(name = 'V_638',
                 type = 'UV',
                 particles = [ P.a, P.W__plus__, P.YS3Qd1, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_653_911,(0,0,2):C.UVGC_653_912,(0,0,1):C.UVGC_653_913})

V_639 = CTVertex(name = 'V_639',
                 type = 'UV',
                 particles = [ P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu1__tilde__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_654_914,(0,0,1):C.UVGC_654_915,(0,0,2):C.UVGC_654_916,(0,0,3):C.UVGC_654_917,(0,0,4):C.UVGC_654_918,(0,0,8):C.UVGC_654_919,(0,0,9):C.UVGC_654_920,(0,0,10):C.UVGC_654_921,(0,0,11):C.UVGC_654_922,(0,0,12):C.UVGC_654_923,(0,0,13):C.UVGC_654_924,(0,0,14):C.UVGC_654_925,(0,0,15):C.UVGC_654_926,(0,0,16):C.UVGC_654_927,(0,0,17):C.UVGC_654_928,(0,0,18):C.UVGC_654_929,(0,0,19):C.UVGC_654_930,(0,0,20):C.UVGC_654_931,(0,0,21):C.UVGC_654_932,(0,0,22):C.UVGC_654_933,(0,0,23):C.UVGC_654_934,(0,0,24):C.UVGC_654_935,(0,0,25):C.UVGC_654_936,(0,0,26):C.UVGC_654_937,(0,0,27):C.UVGC_654_938,(0,0,28):C.UVGC_654_939,(0,0,29):C.UVGC_654_940,(0,0,30):C.UVGC_654_941,(0,0,31):C.UVGC_654_942,(0,0,32):C.UVGC_654_943,(0,0,33):C.UVGC_654_944,(0,0,34):C.UVGC_654_945,(0,0,5):C.UVGC_654_946,(0,0,7):C.UVGC_654_947,(0,0,6):C.UVGC_654_948})

V_640 = CTVertex(name = 'V_640',
                 type = 'UV',
                 particles = [ P.g, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_301_381,(0,0,1):C.UVGC_301_382,(0,0,2):C.UVGC_301_383,(0,0,3):C.UVGC_301_384,(0,0,4):C.UVGC_301_385,(0,0,6):C.UVGC_301_386,(0,0,7):C.UVGC_301_387,(0,0,8):C.UVGC_301_388,(0,0,9):C.UVGC_301_389,(0,0,10):C.UVGC_301_390,(0,0,11):C.UVGC_301_391,(0,0,12):C.UVGC_301_392,(0,0,13):C.UVGC_301_393,(0,0,14):C.UVGC_301_394,(0,0,15):C.UVGC_301_395,(0,0,16):C.UVGC_301_396,(0,0,17):C.UVGC_301_397,(0,0,18):C.UVGC_301_398,(0,0,19):C.UVGC_301_399,(0,0,20):C.UVGC_301_400,(0,0,21):C.UVGC_301_401,(0,0,22):C.UVGC_301_402,(0,0,23):C.UVGC_301_403,(0,0,24):C.UVGC_301_404,(0,0,25):C.UVGC_301_405,(0,0,26):C.UVGC_301_406,(0,0,27):C.UVGC_301_407,(0,0,28):C.UVGC_301_408,(0,0,29):C.UVGC_301_409,(0,0,30):C.UVGC_301_410,(0,0,31):C.UVGC_301_411,(0,0,32):C.UVGC_301_412,(0,0,5):C.UVGC_385_617,(0,1,0):C.UVGC_266_121,(0,1,1):C.UVGC_266_122,(0,1,2):C.UVGC_266_123,(0,1,3):C.UVGC_266_124,(0,1,4):C.UVGC_266_125,(0,1,6):C.UVGC_266_126,(0,1,7):C.UVGC_266_127,(0,1,8):C.UVGC_266_128,(0,1,9):C.UVGC_266_129,(0,1,10):C.UVGC_266_130,(0,1,11):C.UVGC_266_131,(0,1,12):C.UVGC_266_132,(0,1,13):C.UVGC_266_133,(0,1,14):C.UVGC_266_134,(0,1,15):C.UVGC_266_135,(0,1,16):C.UVGC_266_136,(0,1,17):C.UVGC_266_137,(0,1,18):C.UVGC_266_138,(0,1,19):C.UVGC_266_139,(0,1,20):C.UVGC_266_140,(0,1,21):C.UVGC_266_141,(0,1,22):C.UVGC_266_142,(0,1,23):C.UVGC_266_143,(0,1,24):C.UVGC_266_144,(0,1,25):C.UVGC_266_145,(0,1,26):C.UVGC_266_146,(0,1,27):C.UVGC_266_147,(0,1,28):C.UVGC_266_148,(0,1,29):C.UVGC_266_149,(0,1,30):C.UVGC_266_150,(0,1,31):C.UVGC_266_151,(0,1,32):C.UVGC_266_152,(0,1,5):C.UVGC_384_616})

V_641 = CTVertex(name = 'V_641',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.Xd, P.YS3Qu1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_765_1017,(0,0,2):C.UVGC_765_1018,(0,0,1):C.UVGC_586_881})

V_642 = CTVertex(name = 'V_642',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.Xm, P.YS3Qu1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_765_1017,(0,0,2):C.UVGC_765_1018,(0,0,1):C.UVGC_586_881})

V_643 = CTVertex(name = 'V_643',
                 type = 'UV',
                 particles = [ P.a, P.W__minus__, P.YS3Qd1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_653_911,(0,0,2):C.UVGC_653_912,(0,0,1):C.UVGC_653_913})

V_644 = CTVertex(name = 'V_644',
                 type = 'UV',
                 particles = [ P.g, P.W__minus__, P.YS3Qd1__tilde__, P.YS3Qu1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_654_914,(0,0,1):C.UVGC_654_915,(0,0,2):C.UVGC_654_916,(0,0,3):C.UVGC_654_917,(0,0,4):C.UVGC_654_918,(0,0,8):C.UVGC_654_919,(0,0,9):C.UVGC_654_920,(0,0,10):C.UVGC_654_921,(0,0,11):C.UVGC_654_922,(0,0,12):C.UVGC_654_923,(0,0,13):C.UVGC_654_924,(0,0,14):C.UVGC_654_925,(0,0,15):C.UVGC_654_926,(0,0,16):C.UVGC_654_927,(0,0,17):C.UVGC_654_928,(0,0,18):C.UVGC_654_929,(0,0,19):C.UVGC_654_930,(0,0,20):C.UVGC_654_931,(0,0,21):C.UVGC_654_932,(0,0,22):C.UVGC_654_933,(0,0,23):C.UVGC_654_934,(0,0,24):C.UVGC_654_935,(0,0,25):C.UVGC_654_936,(0,0,26):C.UVGC_654_937,(0,0,27):C.UVGC_654_938,(0,0,28):C.UVGC_654_939,(0,0,29):C.UVGC_654_940,(0,0,30):C.UVGC_654_941,(0,0,31):C.UVGC_654_942,(0,0,32):C.UVGC_654_943,(0,0,33):C.UVGC_654_944,(0,0,34):C.UVGC_654_945,(0,0,5):C.UVGC_654_946,(0,0,7):C.UVGC_654_947,(0,0,6):C.UVGC_654_948})

V_645 = CTVertex(name = 'V_645',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_383_615})

V_646 = CTVertex(name = 'V_646',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_648_901,(0,0,2):C.UVGC_648_902,(0,0,1):C.UVGC_648_903})

V_647 = CTVertex(name = 'V_647',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_386_618,(0,0,1):C.UVGC_386_619,(0,0,2):C.UVGC_386_620,(0,0,3):C.UVGC_386_621,(0,0,4):C.UVGC_386_622,(0,0,6):C.UVGC_386_623,(0,0,7):C.UVGC_386_624,(0,0,8):C.UVGC_386_625,(0,0,9):C.UVGC_386_626,(0,0,10):C.UVGC_386_627,(0,0,11):C.UVGC_386_628,(0,0,12):C.UVGC_386_629,(0,0,13):C.UVGC_386_630,(0,0,14):C.UVGC_386_631,(0,0,15):C.UVGC_386_632,(0,0,16):C.UVGC_386_633,(0,0,17):C.UVGC_386_634,(0,0,18):C.UVGC_386_635,(0,0,19):C.UVGC_386_636,(0,0,20):C.UVGC_386_637,(0,0,21):C.UVGC_386_638,(0,0,22):C.UVGC_386_639,(0,0,23):C.UVGC_386_640,(0,0,24):C.UVGC_386_641,(0,0,25):C.UVGC_386_642,(0,0,26):C.UVGC_386_643,(0,0,27):C.UVGC_386_644,(0,0,28):C.UVGC_386_645,(0,0,29):C.UVGC_386_646,(0,0,30):C.UVGC_386_647,(0,0,31):C.UVGC_386_648,(0,0,32):C.UVGC_386_649,(0,0,5):C.UVGC_386_650})

V_648 = CTVertex(name = 'V_648',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_305_451,(2,0,1):C.UVGC_305_452,(2,0,2):C.UVGC_305_453,(2,0,3):C.UVGC_305_454,(2,0,4):C.UVGC_305_455,(2,0,6):C.UVGC_305_456,(2,0,7):C.UVGC_305_457,(2,0,8):C.UVGC_305_458,(2,0,9):C.UVGC_305_459,(2,0,10):C.UVGC_305_460,(2,0,11):C.UVGC_305_461,(2,0,12):C.UVGC_305_462,(2,0,13):C.UVGC_305_463,(2,0,14):C.UVGC_305_464,(2,0,15):C.UVGC_305_465,(2,0,16):C.UVGC_305_466,(2,0,17):C.UVGC_305_467,(2,0,18):C.UVGC_305_468,(2,0,19):C.UVGC_305_469,(2,0,20):C.UVGC_305_470,(2,0,21):C.UVGC_305_471,(2,0,22):C.UVGC_305_472,(2,0,23):C.UVGC_305_473,(2,0,24):C.UVGC_305_474,(2,0,25):C.UVGC_305_475,(2,0,26):C.UVGC_305_476,(2,0,27):C.UVGC_305_477,(2,0,28):C.UVGC_305_478,(2,0,29):C.UVGC_305_479,(2,0,30):C.UVGC_305_480,(2,0,31):C.UVGC_305_481,(2,0,32):C.UVGC_305_482,(2,0,5):C.UVGC_389_651,(1,0,0):C.UVGC_305_451,(1,0,1):C.UVGC_305_452,(1,0,2):C.UVGC_305_453,(1,0,3):C.UVGC_305_454,(1,0,4):C.UVGC_305_455,(1,0,6):C.UVGC_305_456,(1,0,7):C.UVGC_305_457,(1,0,8):C.UVGC_305_458,(1,0,9):C.UVGC_305_459,(1,0,10):C.UVGC_305_460,(1,0,11):C.UVGC_305_461,(1,0,12):C.UVGC_305_462,(1,0,13):C.UVGC_305_463,(1,0,14):C.UVGC_305_464,(1,0,15):C.UVGC_305_465,(1,0,16):C.UVGC_305_466,(1,0,17):C.UVGC_305_467,(1,0,18):C.UVGC_305_468,(1,0,19):C.UVGC_305_469,(1,0,20):C.UVGC_305_470,(1,0,21):C.UVGC_305_471,(1,0,22):C.UVGC_305_472,(1,0,23):C.UVGC_305_473,(1,0,24):C.UVGC_305_474,(1,0,25):C.UVGC_305_475,(1,0,26):C.UVGC_305_476,(1,0,27):C.UVGC_305_477,(1,0,28):C.UVGC_305_478,(1,0,29):C.UVGC_305_479,(1,0,30):C.UVGC_305_480,(1,0,31):C.UVGC_305_481,(1,0,32):C.UVGC_305_482,(1,0,5):C.UVGC_389_651,(0,0,3):C.UVGC_304_449,(0,0,5):C.UVGC_304_450})

V_649 = CTVertex(name = 'V_649',
                 type = 'UV',
                 particles = [ P.a, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_396_690,(0,1,0):C.UVGC_397_691})

V_650 = CTVertex(name = 'V_650',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.c, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_578_857,(0,0,2):C.UVGC_578_858,(0,0,1):C.UVGC_578_859})

V_651 = CTVertex(name = 'V_651',
                 type = 'UV',
                 particles = [ P.Xm, P.c, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_578_857,(0,0,2):C.UVGC_578_858,(0,0,1):C.UVGC_578_859})

V_652 = CTVertex(name = 'V_652',
                 type = 'UV',
                 particles = [ P.a, P.W__plus__, P.YS3Qd2, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_686_961,(0,0,2):C.UVGC_686_962,(0,0,1):C.UVGC_653_913})

V_653 = CTVertex(name = 'V_653',
                 type = 'UV',
                 particles = [ P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu2__tilde__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_654_914,(0,0,1):C.UVGC_654_915,(0,0,2):C.UVGC_654_916,(0,0,3):C.UVGC_654_917,(0,0,4):C.UVGC_654_918,(0,0,8):C.UVGC_654_919,(0,0,9):C.UVGC_654_920,(0,0,10):C.UVGC_654_921,(0,0,11):C.UVGC_654_922,(0,0,12):C.UVGC_654_923,(0,0,13):C.UVGC_654_924,(0,0,14):C.UVGC_654_925,(0,0,15):C.UVGC_654_926,(0,0,16):C.UVGC_654_927,(0,0,17):C.UVGC_654_928,(0,0,18):C.UVGC_654_929,(0,0,19):C.UVGC_654_930,(0,0,20):C.UVGC_654_931,(0,0,21):C.UVGC_654_932,(0,0,22):C.UVGC_654_933,(0,0,23):C.UVGC_654_934,(0,0,24):C.UVGC_654_935,(0,0,25):C.UVGC_654_936,(0,0,26):C.UVGC_654_937,(0,0,27):C.UVGC_654_938,(0,0,28):C.UVGC_654_939,(0,0,29):C.UVGC_654_940,(0,0,30):C.UVGC_654_941,(0,0,31):C.UVGC_654_942,(0,0,32):C.UVGC_654_943,(0,0,33):C.UVGC_654_944,(0,0,34):C.UVGC_654_945,(0,0,5):C.UVGC_687_963,(0,0,7):C.UVGC_687_964,(0,0,6):C.UVGC_654_948})

V_654 = CTVertex(name = 'V_654',
                 type = 'UV',
                 particles = [ P.g, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_301_381,(0,0,1):C.UVGC_301_382,(0,0,2):C.UVGC_301_383,(0,0,3):C.UVGC_301_384,(0,0,4):C.UVGC_301_385,(0,0,6):C.UVGC_301_386,(0,0,7):C.UVGC_301_387,(0,0,8):C.UVGC_301_388,(0,0,9):C.UVGC_301_389,(0,0,10):C.UVGC_301_390,(0,0,11):C.UVGC_301_391,(0,0,12):C.UVGC_301_392,(0,0,13):C.UVGC_301_393,(0,0,14):C.UVGC_301_394,(0,0,15):C.UVGC_301_395,(0,0,16):C.UVGC_301_396,(0,0,17):C.UVGC_301_397,(0,0,18):C.UVGC_301_398,(0,0,19):C.UVGC_301_399,(0,0,20):C.UVGC_301_400,(0,0,21):C.UVGC_301_401,(0,0,22):C.UVGC_301_402,(0,0,23):C.UVGC_301_403,(0,0,24):C.UVGC_301_404,(0,0,25):C.UVGC_301_405,(0,0,26):C.UVGC_301_406,(0,0,27):C.UVGC_301_407,(0,0,28):C.UVGC_301_408,(0,0,29):C.UVGC_301_409,(0,0,30):C.UVGC_301_410,(0,0,31):C.UVGC_301_411,(0,0,32):C.UVGC_301_412,(0,0,5):C.UVGC_400_694,(0,1,0):C.UVGC_266_121,(0,1,1):C.UVGC_266_122,(0,1,2):C.UVGC_266_123,(0,1,3):C.UVGC_266_124,(0,1,4):C.UVGC_266_125,(0,1,6):C.UVGC_266_126,(0,1,7):C.UVGC_266_127,(0,1,8):C.UVGC_266_128,(0,1,9):C.UVGC_266_129,(0,1,10):C.UVGC_266_130,(0,1,11):C.UVGC_266_131,(0,1,12):C.UVGC_266_132,(0,1,13):C.UVGC_266_133,(0,1,14):C.UVGC_266_134,(0,1,15):C.UVGC_266_135,(0,1,16):C.UVGC_266_136,(0,1,17):C.UVGC_266_137,(0,1,18):C.UVGC_266_138,(0,1,19):C.UVGC_266_139,(0,1,20):C.UVGC_266_140,(0,1,21):C.UVGC_266_141,(0,1,22):C.UVGC_266_142,(0,1,23):C.UVGC_266_143,(0,1,24):C.UVGC_266_144,(0,1,25):C.UVGC_266_145,(0,1,26):C.UVGC_266_146,(0,1,27):C.UVGC_266_147,(0,1,28):C.UVGC_266_148,(0,1,29):C.UVGC_266_149,(0,1,30):C.UVGC_266_150,(0,1,31):C.UVGC_266_151,(0,1,32):C.UVGC_266_152,(0,1,5):C.UVGC_399_693})

V_655 = CTVertex(name = 'V_655',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.Xd, P.YS3Qu2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_578_857,(0,0,2):C.UVGC_578_858,(0,0,1):C.UVGC_578_859})

V_656 = CTVertex(name = 'V_656',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.Xm, P.YS3Qu2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_578_857,(0,0,2):C.UVGC_578_858,(0,0,1):C.UVGC_578_859})

V_657 = CTVertex(name = 'V_657',
                 type = 'UV',
                 particles = [ P.a, P.W__minus__, P.YS3Qd2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_686_961,(0,0,2):C.UVGC_686_962,(0,0,1):C.UVGC_653_913})

V_658 = CTVertex(name = 'V_658',
                 type = 'UV',
                 particles = [ P.g, P.W__minus__, P.YS3Qd2__tilde__, P.YS3Qu2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_654_914,(0,0,1):C.UVGC_654_915,(0,0,2):C.UVGC_654_916,(0,0,3):C.UVGC_654_917,(0,0,4):C.UVGC_654_918,(0,0,8):C.UVGC_654_919,(0,0,9):C.UVGC_654_920,(0,0,10):C.UVGC_654_921,(0,0,11):C.UVGC_654_922,(0,0,12):C.UVGC_654_923,(0,0,13):C.UVGC_654_924,(0,0,14):C.UVGC_654_925,(0,0,15):C.UVGC_654_926,(0,0,16):C.UVGC_654_927,(0,0,17):C.UVGC_654_928,(0,0,18):C.UVGC_654_929,(0,0,19):C.UVGC_654_930,(0,0,20):C.UVGC_654_931,(0,0,21):C.UVGC_654_932,(0,0,22):C.UVGC_654_933,(0,0,23):C.UVGC_654_934,(0,0,24):C.UVGC_654_935,(0,0,25):C.UVGC_654_936,(0,0,26):C.UVGC_654_937,(0,0,27):C.UVGC_654_938,(0,0,28):C.UVGC_654_939,(0,0,29):C.UVGC_654_940,(0,0,30):C.UVGC_654_941,(0,0,31):C.UVGC_654_942,(0,0,32):C.UVGC_654_943,(0,0,33):C.UVGC_654_944,(0,0,34):C.UVGC_654_945,(0,0,5):C.UVGC_687_963,(0,0,7):C.UVGC_687_964,(0,0,6):C.UVGC_654_948})

V_659 = CTVertex(name = 'V_659',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_398_692})

V_660 = CTVertex(name = 'V_660',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_648_901,(0,0,2):C.UVGC_680_951,(0,0,1):C.UVGC_648_903})

V_661 = CTVertex(name = 'V_661',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_386_618,(0,0,1):C.UVGC_386_619,(0,0,2):C.UVGC_386_620,(0,0,3):C.UVGC_386_621,(0,0,4):C.UVGC_386_622,(0,0,6):C.UVGC_386_623,(0,0,7):C.UVGC_386_624,(0,0,8):C.UVGC_386_625,(0,0,9):C.UVGC_386_626,(0,0,10):C.UVGC_386_627,(0,0,11):C.UVGC_386_628,(0,0,12):C.UVGC_386_629,(0,0,13):C.UVGC_386_630,(0,0,14):C.UVGC_386_631,(0,0,15):C.UVGC_386_632,(0,0,16):C.UVGC_386_633,(0,0,17):C.UVGC_386_634,(0,0,18):C.UVGC_386_635,(0,0,19):C.UVGC_386_636,(0,0,20):C.UVGC_386_637,(0,0,21):C.UVGC_386_638,(0,0,22):C.UVGC_386_639,(0,0,23):C.UVGC_386_640,(0,0,24):C.UVGC_386_641,(0,0,25):C.UVGC_386_642,(0,0,26):C.UVGC_386_643,(0,0,27):C.UVGC_386_644,(0,0,28):C.UVGC_386_645,(0,0,29):C.UVGC_386_646,(0,0,30):C.UVGC_386_647,(0,0,31):C.UVGC_386_648,(0,0,32):C.UVGC_386_649,(0,0,5):C.UVGC_401_695})

V_662 = CTVertex(name = 'V_662',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_305_451,(2,0,1):C.UVGC_305_452,(2,0,2):C.UVGC_305_453,(2,0,3):C.UVGC_305_454,(2,0,4):C.UVGC_305_455,(2,0,6):C.UVGC_305_456,(2,0,7):C.UVGC_305_457,(2,0,8):C.UVGC_305_458,(2,0,9):C.UVGC_305_459,(2,0,10):C.UVGC_305_460,(2,0,11):C.UVGC_305_461,(2,0,12):C.UVGC_305_462,(2,0,13):C.UVGC_305_463,(2,0,14):C.UVGC_305_464,(2,0,15):C.UVGC_305_465,(2,0,16):C.UVGC_305_466,(2,0,17):C.UVGC_305_467,(2,0,18):C.UVGC_305_468,(2,0,19):C.UVGC_305_469,(2,0,20):C.UVGC_305_470,(2,0,21):C.UVGC_305_471,(2,0,22):C.UVGC_305_472,(2,0,23):C.UVGC_305_473,(2,0,24):C.UVGC_305_474,(2,0,25):C.UVGC_305_475,(2,0,26):C.UVGC_305_476,(2,0,27):C.UVGC_305_477,(2,0,28):C.UVGC_305_478,(2,0,29):C.UVGC_305_479,(2,0,30):C.UVGC_305_480,(2,0,31):C.UVGC_305_481,(2,0,32):C.UVGC_305_482,(2,0,5):C.UVGC_404_696,(1,0,0):C.UVGC_305_451,(1,0,1):C.UVGC_305_452,(1,0,2):C.UVGC_305_453,(1,0,3):C.UVGC_305_454,(1,0,4):C.UVGC_305_455,(1,0,6):C.UVGC_305_456,(1,0,7):C.UVGC_305_457,(1,0,8):C.UVGC_305_458,(1,0,9):C.UVGC_305_459,(1,0,10):C.UVGC_305_460,(1,0,11):C.UVGC_305_461,(1,0,12):C.UVGC_305_462,(1,0,13):C.UVGC_305_463,(1,0,14):C.UVGC_305_464,(1,0,15):C.UVGC_305_465,(1,0,16):C.UVGC_305_466,(1,0,17):C.UVGC_305_467,(1,0,18):C.UVGC_305_468,(1,0,19):C.UVGC_305_469,(1,0,20):C.UVGC_305_470,(1,0,21):C.UVGC_305_471,(1,0,22):C.UVGC_305_472,(1,0,23):C.UVGC_305_473,(1,0,24):C.UVGC_305_474,(1,0,25):C.UVGC_305_475,(1,0,26):C.UVGC_305_476,(1,0,27):C.UVGC_305_477,(1,0,28):C.UVGC_305_478,(1,0,29):C.UVGC_305_479,(1,0,30):C.UVGC_305_480,(1,0,31):C.UVGC_305_481,(1,0,32):C.UVGC_305_482,(1,0,5):C.UVGC_404_696,(0,0,3):C.UVGC_304_449,(0,0,5):C.UVGC_304_450})

V_663 = CTVertex(name = 'V_663',
                 type = 'UV',
                 particles = [ P.a, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_411_703,(0,1,0):C.UVGC_412_704})

V_664 = CTVertex(name = 'V_664',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.t, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_758_1002,(0,0,2):C.UVGC_758_1003,(0,0,1):C.UVGC_573_846})

V_665 = CTVertex(name = 'V_665',
                 type = 'UV',
                 particles = [ P.Xm, P.t, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_758_1002,(0,0,2):C.UVGC_758_1003,(0,0,1):C.UVGC_573_846})

V_666 = CTVertex(name = 'V_666',
                 type = 'UV',
                 particles = [ P.a, P.W__plus__, P.YS3Qd3, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_717_977,(0,0,2):C.UVGC_717_978,(0,0,1):C.UVGC_653_913})

V_667 = CTVertex(name = 'V_667',
                 type = 'UV',
                 particles = [ P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu3__tilde__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_654_914,(0,0,1):C.UVGC_654_915,(0,0,2):C.UVGC_654_916,(0,0,3):C.UVGC_654_917,(0,0,4):C.UVGC_654_918,(0,0,8):C.UVGC_654_919,(0,0,9):C.UVGC_654_920,(0,0,10):C.UVGC_654_921,(0,0,11):C.UVGC_654_922,(0,0,12):C.UVGC_654_923,(0,0,13):C.UVGC_654_924,(0,0,14):C.UVGC_654_925,(0,0,15):C.UVGC_654_926,(0,0,16):C.UVGC_654_927,(0,0,17):C.UVGC_654_928,(0,0,18):C.UVGC_654_929,(0,0,19):C.UVGC_654_930,(0,0,20):C.UVGC_654_931,(0,0,21):C.UVGC_654_932,(0,0,22):C.UVGC_654_933,(0,0,23):C.UVGC_654_934,(0,0,24):C.UVGC_654_935,(0,0,25):C.UVGC_654_936,(0,0,26):C.UVGC_654_937,(0,0,27):C.UVGC_654_938,(0,0,28):C.UVGC_654_939,(0,0,29):C.UVGC_654_940,(0,0,30):C.UVGC_654_941,(0,0,31):C.UVGC_654_942,(0,0,32):C.UVGC_654_943,(0,0,33):C.UVGC_654_944,(0,0,34):C.UVGC_654_945,(0,0,5):C.UVGC_718_979,(0,0,7):C.UVGC_718_980,(0,0,6):C.UVGC_654_948})

V_668 = CTVertex(name = 'V_668',
                 type = 'UV',
                 particles = [ P.g, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_301_381,(0,0,1):C.UVGC_301_382,(0,0,2):C.UVGC_301_383,(0,0,3):C.UVGC_301_384,(0,0,4):C.UVGC_301_385,(0,0,6):C.UVGC_301_386,(0,0,7):C.UVGC_301_387,(0,0,8):C.UVGC_301_388,(0,0,9):C.UVGC_301_389,(0,0,10):C.UVGC_301_390,(0,0,11):C.UVGC_301_391,(0,0,12):C.UVGC_301_392,(0,0,13):C.UVGC_301_393,(0,0,14):C.UVGC_301_394,(0,0,15):C.UVGC_301_395,(0,0,16):C.UVGC_301_396,(0,0,17):C.UVGC_301_397,(0,0,18):C.UVGC_301_398,(0,0,19):C.UVGC_301_399,(0,0,20):C.UVGC_301_400,(0,0,21):C.UVGC_301_401,(0,0,22):C.UVGC_301_402,(0,0,23):C.UVGC_301_403,(0,0,24):C.UVGC_301_404,(0,0,25):C.UVGC_301_405,(0,0,26):C.UVGC_301_406,(0,0,27):C.UVGC_301_407,(0,0,28):C.UVGC_301_408,(0,0,29):C.UVGC_301_409,(0,0,30):C.UVGC_301_410,(0,0,31):C.UVGC_301_411,(0,0,32):C.UVGC_301_412,(0,0,5):C.UVGC_415_707,(0,1,0):C.UVGC_266_121,(0,1,1):C.UVGC_266_122,(0,1,2):C.UVGC_266_123,(0,1,3):C.UVGC_266_124,(0,1,4):C.UVGC_266_125,(0,1,6):C.UVGC_266_126,(0,1,7):C.UVGC_266_127,(0,1,8):C.UVGC_266_128,(0,1,9):C.UVGC_266_129,(0,1,10):C.UVGC_266_130,(0,1,11):C.UVGC_266_131,(0,1,12):C.UVGC_266_132,(0,1,13):C.UVGC_266_133,(0,1,14):C.UVGC_266_134,(0,1,15):C.UVGC_266_135,(0,1,16):C.UVGC_266_136,(0,1,17):C.UVGC_266_137,(0,1,18):C.UVGC_266_138,(0,1,19):C.UVGC_266_139,(0,1,20):C.UVGC_266_140,(0,1,21):C.UVGC_266_141,(0,1,22):C.UVGC_266_142,(0,1,23):C.UVGC_266_143,(0,1,24):C.UVGC_266_144,(0,1,25):C.UVGC_266_145,(0,1,26):C.UVGC_266_146,(0,1,27):C.UVGC_266_147,(0,1,28):C.UVGC_266_148,(0,1,29):C.UVGC_266_149,(0,1,30):C.UVGC_266_150,(0,1,31):C.UVGC_266_151,(0,1,32):C.UVGC_266_152,(0,1,5):C.UVGC_414_706})

V_669 = CTVertex(name = 'V_669',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.Xd, P.YS3Qu3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_758_1002,(0,0,2):C.UVGC_758_1003,(0,0,1):C.UVGC_573_846})

V_670 = CTVertex(name = 'V_670',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.Xm, P.YS3Qu3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_758_1002,(0,0,2):C.UVGC_758_1003,(0,0,1):C.UVGC_573_846})

V_671 = CTVertex(name = 'V_671',
                 type = 'UV',
                 particles = [ P.a, P.W__minus__, P.YS3Qd3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_717_977,(0,0,2):C.UVGC_717_978,(0,0,1):C.UVGC_653_913})

V_672 = CTVertex(name = 'V_672',
                 type = 'UV',
                 particles = [ P.g, P.W__minus__, P.YS3Qd3__tilde__, P.YS3Qu3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_654_914,(0,0,1):C.UVGC_654_915,(0,0,2):C.UVGC_654_916,(0,0,3):C.UVGC_654_917,(0,0,4):C.UVGC_654_918,(0,0,8):C.UVGC_654_919,(0,0,9):C.UVGC_654_920,(0,0,10):C.UVGC_654_921,(0,0,11):C.UVGC_654_922,(0,0,12):C.UVGC_654_923,(0,0,13):C.UVGC_654_924,(0,0,14):C.UVGC_654_925,(0,0,15):C.UVGC_654_926,(0,0,16):C.UVGC_654_927,(0,0,17):C.UVGC_654_928,(0,0,18):C.UVGC_654_929,(0,0,19):C.UVGC_654_930,(0,0,20):C.UVGC_654_931,(0,0,21):C.UVGC_654_932,(0,0,22):C.UVGC_654_933,(0,0,23):C.UVGC_654_934,(0,0,24):C.UVGC_654_935,(0,0,25):C.UVGC_654_936,(0,0,26):C.UVGC_654_937,(0,0,27):C.UVGC_654_938,(0,0,28):C.UVGC_654_939,(0,0,29):C.UVGC_654_940,(0,0,30):C.UVGC_654_941,(0,0,31):C.UVGC_654_942,(0,0,32):C.UVGC_654_943,(0,0,33):C.UVGC_654_944,(0,0,34):C.UVGC_654_945,(0,0,5):C.UVGC_718_979,(0,0,7):C.UVGC_718_980,(0,0,6):C.UVGC_654_948})

V_673 = CTVertex(name = 'V_673',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_413_705})

V_674 = CTVertex(name = 'V_674',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_648_901,(0,0,2):C.UVGC_711_967,(0,0,1):C.UVGC_648_903})

V_675 = CTVertex(name = 'V_675',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_386_618,(0,0,1):C.UVGC_386_619,(0,0,2):C.UVGC_386_620,(0,0,3):C.UVGC_386_621,(0,0,4):C.UVGC_386_622,(0,0,6):C.UVGC_386_623,(0,0,7):C.UVGC_386_624,(0,0,8):C.UVGC_386_625,(0,0,9):C.UVGC_386_626,(0,0,10):C.UVGC_386_627,(0,0,11):C.UVGC_386_628,(0,0,12):C.UVGC_386_629,(0,0,13):C.UVGC_386_630,(0,0,14):C.UVGC_386_631,(0,0,15):C.UVGC_386_632,(0,0,16):C.UVGC_386_633,(0,0,17):C.UVGC_386_634,(0,0,18):C.UVGC_386_635,(0,0,19):C.UVGC_386_636,(0,0,20):C.UVGC_386_637,(0,0,21):C.UVGC_386_638,(0,0,22):C.UVGC_386_639,(0,0,23):C.UVGC_386_640,(0,0,24):C.UVGC_386_641,(0,0,25):C.UVGC_386_642,(0,0,26):C.UVGC_386_643,(0,0,27):C.UVGC_386_644,(0,0,28):C.UVGC_386_645,(0,0,29):C.UVGC_386_646,(0,0,30):C.UVGC_386_647,(0,0,31):C.UVGC_386_648,(0,0,32):C.UVGC_386_649,(0,0,5):C.UVGC_416_708})

V_676 = CTVertex(name = 'V_676',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_305_451,(2,0,1):C.UVGC_305_452,(2,0,2):C.UVGC_305_453,(2,0,3):C.UVGC_305_454,(2,0,4):C.UVGC_305_455,(2,0,6):C.UVGC_305_456,(2,0,7):C.UVGC_305_457,(2,0,8):C.UVGC_305_458,(2,0,9):C.UVGC_305_459,(2,0,10):C.UVGC_305_460,(2,0,11):C.UVGC_305_461,(2,0,12):C.UVGC_305_462,(2,0,13):C.UVGC_305_463,(2,0,14):C.UVGC_305_464,(2,0,15):C.UVGC_305_465,(2,0,16):C.UVGC_305_466,(2,0,17):C.UVGC_305_467,(2,0,18):C.UVGC_305_468,(2,0,19):C.UVGC_305_469,(2,0,20):C.UVGC_305_470,(2,0,21):C.UVGC_305_471,(2,0,22):C.UVGC_305_472,(2,0,23):C.UVGC_305_473,(2,0,24):C.UVGC_305_474,(2,0,25):C.UVGC_305_475,(2,0,26):C.UVGC_305_476,(2,0,27):C.UVGC_305_477,(2,0,28):C.UVGC_305_478,(2,0,29):C.UVGC_305_479,(2,0,30):C.UVGC_305_480,(2,0,31):C.UVGC_305_481,(2,0,32):C.UVGC_305_482,(2,0,5):C.UVGC_419_709,(1,0,0):C.UVGC_305_451,(1,0,1):C.UVGC_305_452,(1,0,2):C.UVGC_305_453,(1,0,3):C.UVGC_305_454,(1,0,4):C.UVGC_305_455,(1,0,6):C.UVGC_305_456,(1,0,7):C.UVGC_305_457,(1,0,8):C.UVGC_305_458,(1,0,9):C.UVGC_305_459,(1,0,10):C.UVGC_305_460,(1,0,11):C.UVGC_305_461,(1,0,12):C.UVGC_305_462,(1,0,13):C.UVGC_305_463,(1,0,14):C.UVGC_305_464,(1,0,15):C.UVGC_305_465,(1,0,16):C.UVGC_305_466,(1,0,17):C.UVGC_305_467,(1,0,18):C.UVGC_305_468,(1,0,19):C.UVGC_305_469,(1,0,20):C.UVGC_305_470,(1,0,21):C.UVGC_305_471,(1,0,22):C.UVGC_305_472,(1,0,23):C.UVGC_305_473,(1,0,24):C.UVGC_305_474,(1,0,25):C.UVGC_305_475,(1,0,26):C.UVGC_305_476,(1,0,27):C.UVGC_305_477,(1,0,28):C.UVGC_305_478,(1,0,29):C.UVGC_305_479,(1,0,30):C.UVGC_305_480,(1,0,31):C.UVGC_305_481,(1,0,32):C.UVGC_305_482,(1,0,5):C.UVGC_419_709,(0,0,3):C.UVGC_304_449,(0,0,5):C.UVGC_304_450})

V_677 = CTVertex(name = 'V_677',
                 type = 'UV',
                 particles = [ P.a, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_426_716,(0,1,0):C.UVGC_427_717})

V_678 = CTVertex(name = 'V_678',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.u, P.YS3u1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YS3u1] ], [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_766_1019,(0,0,2):C.UVGC_766_1020,(0,0,1):C.UVGC_766_1021})

V_679 = CTVertex(name = 'V_679',
                 type = 'UV',
                 particles = [ P.Xm, P.u, P.YS3u1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YS3u1] ], [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_766_1019,(0,0,2):C.UVGC_766_1020,(0,0,1):C.UVGC_766_1021})

V_680 = CTVertex(name = 'V_680',
                 type = 'UV',
                 particles = [ P.g, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_301_381,(0,0,1):C.UVGC_301_382,(0,0,2):C.UVGC_301_383,(0,0,3):C.UVGC_301_384,(0,0,4):C.UVGC_301_385,(0,0,6):C.UVGC_301_386,(0,0,7):C.UVGC_301_387,(0,0,8):C.UVGC_301_388,(0,0,9):C.UVGC_301_389,(0,0,10):C.UVGC_301_390,(0,0,11):C.UVGC_301_391,(0,0,12):C.UVGC_301_392,(0,0,13):C.UVGC_301_393,(0,0,14):C.UVGC_301_394,(0,0,15):C.UVGC_301_395,(0,0,16):C.UVGC_301_396,(0,0,17):C.UVGC_301_397,(0,0,18):C.UVGC_301_398,(0,0,19):C.UVGC_301_399,(0,0,20):C.UVGC_301_400,(0,0,21):C.UVGC_301_401,(0,0,22):C.UVGC_301_402,(0,0,23):C.UVGC_301_403,(0,0,24):C.UVGC_301_404,(0,0,25):C.UVGC_301_405,(0,0,26):C.UVGC_301_406,(0,0,27):C.UVGC_301_407,(0,0,28):C.UVGC_301_408,(0,0,29):C.UVGC_301_409,(0,0,30):C.UVGC_301_410,(0,0,31):C.UVGC_301_411,(0,0,32):C.UVGC_301_412,(0,0,5):C.UVGC_430_720,(0,1,0):C.UVGC_266_121,(0,1,1):C.UVGC_266_122,(0,1,2):C.UVGC_266_123,(0,1,3):C.UVGC_266_124,(0,1,4):C.UVGC_266_125,(0,1,6):C.UVGC_266_126,(0,1,7):C.UVGC_266_127,(0,1,8):C.UVGC_266_128,(0,1,9):C.UVGC_266_129,(0,1,10):C.UVGC_266_130,(0,1,11):C.UVGC_266_131,(0,1,12):C.UVGC_266_132,(0,1,13):C.UVGC_266_133,(0,1,14):C.UVGC_266_134,(0,1,15):C.UVGC_266_135,(0,1,16):C.UVGC_266_136,(0,1,17):C.UVGC_266_137,(0,1,18):C.UVGC_266_138,(0,1,19):C.UVGC_266_139,(0,1,20):C.UVGC_266_140,(0,1,21):C.UVGC_266_141,(0,1,22):C.UVGC_266_142,(0,1,23):C.UVGC_266_143,(0,1,24):C.UVGC_266_144,(0,1,25):C.UVGC_266_145,(0,1,26):C.UVGC_266_146,(0,1,27):C.UVGC_266_147,(0,1,28):C.UVGC_266_148,(0,1,29):C.UVGC_266_149,(0,1,30):C.UVGC_266_150,(0,1,31):C.UVGC_266_151,(0,1,32):C.UVGC_266_152,(0,1,5):C.UVGC_429_719})

V_681 = CTVertex(name = 'V_681',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.Xd, P.YS3u1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YS3u1] ], [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_766_1019,(0,0,2):C.UVGC_766_1020,(0,0,1):C.UVGC_766_1021})

V_682 = CTVertex(name = 'V_682',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.Xm, P.YS3u1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YS3u1] ], [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_766_1019,(0,0,2):C.UVGC_766_1020,(0,0,1):C.UVGC_766_1021})

V_683 = CTVertex(name = 'V_683',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_428_718})

V_684 = CTVertex(name = 'V_684',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_386_618,(0,0,1):C.UVGC_386_619,(0,0,2):C.UVGC_386_620,(0,0,3):C.UVGC_386_621,(0,0,4):C.UVGC_386_622,(0,0,6):C.UVGC_386_623,(0,0,7):C.UVGC_386_624,(0,0,8):C.UVGC_386_625,(0,0,9):C.UVGC_386_626,(0,0,10):C.UVGC_386_627,(0,0,11):C.UVGC_386_628,(0,0,12):C.UVGC_386_629,(0,0,13):C.UVGC_386_630,(0,0,14):C.UVGC_386_631,(0,0,15):C.UVGC_386_632,(0,0,16):C.UVGC_386_633,(0,0,17):C.UVGC_386_634,(0,0,18):C.UVGC_386_635,(0,0,19):C.UVGC_386_636,(0,0,20):C.UVGC_386_637,(0,0,21):C.UVGC_386_638,(0,0,22):C.UVGC_386_639,(0,0,23):C.UVGC_386_640,(0,0,24):C.UVGC_386_641,(0,0,25):C.UVGC_386_642,(0,0,26):C.UVGC_386_643,(0,0,27):C.UVGC_386_644,(0,0,28):C.UVGC_386_645,(0,0,29):C.UVGC_386_646,(0,0,30):C.UVGC_386_647,(0,0,31):C.UVGC_386_648,(0,0,32):C.UVGC_386_649,(0,0,5):C.UVGC_431_721})

V_685 = CTVertex(name = 'V_685',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_305_451,(2,0,1):C.UVGC_305_452,(2,0,2):C.UVGC_305_453,(2,0,3):C.UVGC_305_454,(2,0,4):C.UVGC_305_455,(2,0,6):C.UVGC_305_456,(2,0,7):C.UVGC_305_457,(2,0,8):C.UVGC_305_458,(2,0,9):C.UVGC_305_459,(2,0,10):C.UVGC_305_460,(2,0,11):C.UVGC_305_461,(2,0,12):C.UVGC_305_462,(2,0,13):C.UVGC_305_463,(2,0,14):C.UVGC_305_464,(2,0,15):C.UVGC_305_465,(2,0,16):C.UVGC_305_466,(2,0,17):C.UVGC_305_467,(2,0,18):C.UVGC_305_468,(2,0,19):C.UVGC_305_469,(2,0,20):C.UVGC_305_470,(2,0,21):C.UVGC_305_471,(2,0,22):C.UVGC_305_472,(2,0,23):C.UVGC_305_473,(2,0,24):C.UVGC_305_474,(2,0,25):C.UVGC_305_475,(2,0,26):C.UVGC_305_476,(2,0,27):C.UVGC_305_477,(2,0,28):C.UVGC_305_478,(2,0,29):C.UVGC_305_479,(2,0,30):C.UVGC_305_480,(2,0,31):C.UVGC_305_481,(2,0,32):C.UVGC_305_482,(2,0,5):C.UVGC_434_722,(1,0,0):C.UVGC_305_451,(1,0,1):C.UVGC_305_452,(1,0,2):C.UVGC_305_453,(1,0,3):C.UVGC_305_454,(1,0,4):C.UVGC_305_455,(1,0,6):C.UVGC_305_456,(1,0,7):C.UVGC_305_457,(1,0,8):C.UVGC_305_458,(1,0,9):C.UVGC_305_459,(1,0,10):C.UVGC_305_460,(1,0,11):C.UVGC_305_461,(1,0,12):C.UVGC_305_462,(1,0,13):C.UVGC_305_463,(1,0,14):C.UVGC_305_464,(1,0,15):C.UVGC_305_465,(1,0,16):C.UVGC_305_466,(1,0,17):C.UVGC_305_467,(1,0,18):C.UVGC_305_468,(1,0,19):C.UVGC_305_469,(1,0,20):C.UVGC_305_470,(1,0,21):C.UVGC_305_471,(1,0,22):C.UVGC_305_472,(1,0,23):C.UVGC_305_473,(1,0,24):C.UVGC_305_474,(1,0,25):C.UVGC_305_475,(1,0,26):C.UVGC_305_476,(1,0,27):C.UVGC_305_477,(1,0,28):C.UVGC_305_478,(1,0,29):C.UVGC_305_479,(1,0,30):C.UVGC_305_480,(1,0,31):C.UVGC_305_481,(1,0,32):C.UVGC_305_482,(1,0,5):C.UVGC_434_722,(0,0,3):C.UVGC_304_449,(0,0,5):C.UVGC_304_450})

V_686 = CTVertex(name = 'V_686',
                 type = 'UV',
                 particles = [ P.a, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_441_761,(0,1,0):C.UVGC_442_762})

V_687 = CTVertex(name = 'V_687',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.c, P.YS3u2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YS3u2] ], [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_579_860,(0,0,2):C.UVGC_579_861,(0,0,1):C.UVGC_579_862})

V_688 = CTVertex(name = 'V_688',
                 type = 'UV',
                 particles = [ P.Xm, P.c, P.YS3u2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YS3u2] ], [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_579_860,(0,0,2):C.UVGC_579_861,(0,0,1):C.UVGC_579_862})

V_689 = CTVertex(name = 'V_689',
                 type = 'UV',
                 particles = [ P.g, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_301_381,(0,0,1):C.UVGC_301_382,(0,0,2):C.UVGC_301_383,(0,0,3):C.UVGC_301_384,(0,0,4):C.UVGC_301_385,(0,0,6):C.UVGC_301_386,(0,0,7):C.UVGC_301_387,(0,0,8):C.UVGC_301_388,(0,0,9):C.UVGC_301_389,(0,0,10):C.UVGC_301_390,(0,0,11):C.UVGC_301_391,(0,0,12):C.UVGC_301_392,(0,0,13):C.UVGC_301_393,(0,0,14):C.UVGC_301_394,(0,0,15):C.UVGC_301_395,(0,0,16):C.UVGC_301_396,(0,0,17):C.UVGC_301_397,(0,0,18):C.UVGC_301_398,(0,0,19):C.UVGC_301_399,(0,0,20):C.UVGC_301_400,(0,0,21):C.UVGC_301_401,(0,0,22):C.UVGC_301_402,(0,0,23):C.UVGC_301_403,(0,0,24):C.UVGC_301_404,(0,0,25):C.UVGC_301_405,(0,0,26):C.UVGC_301_406,(0,0,27):C.UVGC_301_407,(0,0,28):C.UVGC_301_408,(0,0,29):C.UVGC_301_409,(0,0,30):C.UVGC_301_410,(0,0,31):C.UVGC_301_411,(0,0,32):C.UVGC_301_412,(0,0,5):C.UVGC_445_765,(0,1,0):C.UVGC_266_121,(0,1,1):C.UVGC_266_122,(0,1,2):C.UVGC_266_123,(0,1,3):C.UVGC_266_124,(0,1,4):C.UVGC_266_125,(0,1,6):C.UVGC_266_126,(0,1,7):C.UVGC_266_127,(0,1,8):C.UVGC_266_128,(0,1,9):C.UVGC_266_129,(0,1,10):C.UVGC_266_130,(0,1,11):C.UVGC_266_131,(0,1,12):C.UVGC_266_132,(0,1,13):C.UVGC_266_133,(0,1,14):C.UVGC_266_134,(0,1,15):C.UVGC_266_135,(0,1,16):C.UVGC_266_136,(0,1,17):C.UVGC_266_137,(0,1,18):C.UVGC_266_138,(0,1,19):C.UVGC_266_139,(0,1,20):C.UVGC_266_140,(0,1,21):C.UVGC_266_141,(0,1,22):C.UVGC_266_142,(0,1,23):C.UVGC_266_143,(0,1,24):C.UVGC_266_144,(0,1,25):C.UVGC_266_145,(0,1,26):C.UVGC_266_146,(0,1,27):C.UVGC_266_147,(0,1,28):C.UVGC_266_148,(0,1,29):C.UVGC_266_149,(0,1,30):C.UVGC_266_150,(0,1,31):C.UVGC_266_151,(0,1,32):C.UVGC_266_152,(0,1,5):C.UVGC_444_764})

V_690 = CTVertex(name = 'V_690',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.Xd, P.YS3u2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YS3u2] ], [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_579_860,(0,0,2):C.UVGC_579_861,(0,0,1):C.UVGC_579_862})

V_691 = CTVertex(name = 'V_691',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.Xm, P.YS3u2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YS3u2] ], [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_579_860,(0,0,2):C.UVGC_579_861,(0,0,1):C.UVGC_579_862})

V_692 = CTVertex(name = 'V_692',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_443_763})

V_693 = CTVertex(name = 'V_693',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_386_618,(0,0,1):C.UVGC_386_619,(0,0,2):C.UVGC_386_620,(0,0,3):C.UVGC_386_621,(0,0,4):C.UVGC_386_622,(0,0,6):C.UVGC_386_623,(0,0,7):C.UVGC_386_624,(0,0,8):C.UVGC_386_625,(0,0,9):C.UVGC_386_626,(0,0,10):C.UVGC_386_627,(0,0,11):C.UVGC_386_628,(0,0,12):C.UVGC_386_629,(0,0,13):C.UVGC_386_630,(0,0,14):C.UVGC_386_631,(0,0,15):C.UVGC_386_632,(0,0,16):C.UVGC_386_633,(0,0,17):C.UVGC_386_634,(0,0,18):C.UVGC_386_635,(0,0,19):C.UVGC_386_636,(0,0,20):C.UVGC_386_637,(0,0,21):C.UVGC_386_638,(0,0,22):C.UVGC_386_639,(0,0,23):C.UVGC_386_640,(0,0,24):C.UVGC_386_641,(0,0,25):C.UVGC_386_642,(0,0,26):C.UVGC_386_643,(0,0,27):C.UVGC_386_644,(0,0,28):C.UVGC_386_645,(0,0,29):C.UVGC_386_646,(0,0,30):C.UVGC_386_647,(0,0,31):C.UVGC_386_648,(0,0,32):C.UVGC_386_649,(0,0,5):C.UVGC_446_766})

V_694 = CTVertex(name = 'V_694',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_305_451,(2,0,1):C.UVGC_305_452,(2,0,2):C.UVGC_305_453,(2,0,3):C.UVGC_305_454,(2,0,4):C.UVGC_305_455,(2,0,6):C.UVGC_305_456,(2,0,7):C.UVGC_305_457,(2,0,8):C.UVGC_305_458,(2,0,9):C.UVGC_305_459,(2,0,10):C.UVGC_305_460,(2,0,11):C.UVGC_305_461,(2,0,12):C.UVGC_305_462,(2,0,13):C.UVGC_305_463,(2,0,14):C.UVGC_305_464,(2,0,15):C.UVGC_305_465,(2,0,16):C.UVGC_305_466,(2,0,17):C.UVGC_305_467,(2,0,18):C.UVGC_305_468,(2,0,19):C.UVGC_305_469,(2,0,20):C.UVGC_305_470,(2,0,21):C.UVGC_305_471,(2,0,22):C.UVGC_305_472,(2,0,23):C.UVGC_305_473,(2,0,24):C.UVGC_305_474,(2,0,25):C.UVGC_305_475,(2,0,26):C.UVGC_305_476,(2,0,27):C.UVGC_305_477,(2,0,28):C.UVGC_305_478,(2,0,29):C.UVGC_305_479,(2,0,30):C.UVGC_305_480,(2,0,31):C.UVGC_305_481,(2,0,32):C.UVGC_305_482,(2,0,5):C.UVGC_449_767,(1,0,0):C.UVGC_305_451,(1,0,1):C.UVGC_305_452,(1,0,2):C.UVGC_305_453,(1,0,3):C.UVGC_305_454,(1,0,4):C.UVGC_305_455,(1,0,6):C.UVGC_305_456,(1,0,7):C.UVGC_305_457,(1,0,8):C.UVGC_305_458,(1,0,9):C.UVGC_305_459,(1,0,10):C.UVGC_305_460,(1,0,11):C.UVGC_305_461,(1,0,12):C.UVGC_305_462,(1,0,13):C.UVGC_305_463,(1,0,14):C.UVGC_305_464,(1,0,15):C.UVGC_305_465,(1,0,16):C.UVGC_305_466,(1,0,17):C.UVGC_305_467,(1,0,18):C.UVGC_305_468,(1,0,19):C.UVGC_305_469,(1,0,20):C.UVGC_305_470,(1,0,21):C.UVGC_305_471,(1,0,22):C.UVGC_305_472,(1,0,23):C.UVGC_305_473,(1,0,24):C.UVGC_305_474,(1,0,25):C.UVGC_305_475,(1,0,26):C.UVGC_305_476,(1,0,27):C.UVGC_305_477,(1,0,28):C.UVGC_305_478,(1,0,29):C.UVGC_305_479,(1,0,30):C.UVGC_305_480,(1,0,31):C.UVGC_305_481,(1,0,32):C.UVGC_305_482,(1,0,5):C.UVGC_449_767,(0,0,3):C.UVGC_304_449,(0,0,5):C.UVGC_304_450})

V_695 = CTVertex(name = 'V_695',
                 type = 'UV',
                 particles = [ P.a, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_456_774,(0,1,0):C.UVGC_457_775})

V_696 = CTVertex(name = 'V_696',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.t, P.YS3u3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YS3u3] ], [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_759_1004,(0,0,2):C.UVGC_759_1005,(0,0,1):C.UVGC_759_1006})

V_697 = CTVertex(name = 'V_697',
                 type = 'UV',
                 particles = [ P.Xm, P.t, P.YS3u3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YS3u3] ], [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_759_1004,(0,0,2):C.UVGC_759_1005,(0,0,1):C.UVGC_759_1006})

V_698 = CTVertex(name = 'V_698',
                 type = 'UV',
                 particles = [ P.g, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_301_381,(0,0,1):C.UVGC_301_382,(0,0,2):C.UVGC_301_383,(0,0,3):C.UVGC_301_384,(0,0,4):C.UVGC_301_385,(0,0,6):C.UVGC_301_386,(0,0,7):C.UVGC_301_387,(0,0,8):C.UVGC_301_388,(0,0,9):C.UVGC_301_389,(0,0,10):C.UVGC_301_390,(0,0,11):C.UVGC_301_391,(0,0,12):C.UVGC_301_392,(0,0,13):C.UVGC_301_393,(0,0,14):C.UVGC_301_394,(0,0,15):C.UVGC_301_395,(0,0,16):C.UVGC_301_396,(0,0,17):C.UVGC_301_397,(0,0,18):C.UVGC_301_398,(0,0,19):C.UVGC_301_399,(0,0,20):C.UVGC_301_400,(0,0,21):C.UVGC_301_401,(0,0,22):C.UVGC_301_402,(0,0,23):C.UVGC_301_403,(0,0,24):C.UVGC_301_404,(0,0,25):C.UVGC_301_405,(0,0,26):C.UVGC_301_406,(0,0,27):C.UVGC_301_407,(0,0,28):C.UVGC_301_408,(0,0,29):C.UVGC_301_409,(0,0,30):C.UVGC_301_410,(0,0,31):C.UVGC_301_411,(0,0,32):C.UVGC_301_412,(0,0,5):C.UVGC_460_778,(0,1,0):C.UVGC_266_121,(0,1,1):C.UVGC_266_122,(0,1,2):C.UVGC_266_123,(0,1,3):C.UVGC_266_124,(0,1,4):C.UVGC_266_125,(0,1,6):C.UVGC_266_126,(0,1,7):C.UVGC_266_127,(0,1,8):C.UVGC_266_128,(0,1,9):C.UVGC_266_129,(0,1,10):C.UVGC_266_130,(0,1,11):C.UVGC_266_131,(0,1,12):C.UVGC_266_132,(0,1,13):C.UVGC_266_133,(0,1,14):C.UVGC_266_134,(0,1,15):C.UVGC_266_135,(0,1,16):C.UVGC_266_136,(0,1,17):C.UVGC_266_137,(0,1,18):C.UVGC_266_138,(0,1,19):C.UVGC_266_139,(0,1,20):C.UVGC_266_140,(0,1,21):C.UVGC_266_141,(0,1,22):C.UVGC_266_142,(0,1,23):C.UVGC_266_143,(0,1,24):C.UVGC_266_144,(0,1,25):C.UVGC_266_145,(0,1,26):C.UVGC_266_146,(0,1,27):C.UVGC_266_147,(0,1,28):C.UVGC_266_148,(0,1,29):C.UVGC_266_149,(0,1,30):C.UVGC_266_150,(0,1,31):C.UVGC_266_151,(0,1,32):C.UVGC_266_152,(0,1,5):C.UVGC_459_777})

V_699 = CTVertex(name = 'V_699',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.Xd, P.YS3u3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YS3u3] ], [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_759_1004,(0,0,2):C.UVGC_759_1005,(0,0,1):C.UVGC_759_1006})

V_700 = CTVertex(name = 'V_700',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.Xm, P.YS3u3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YS3u3] ], [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_759_1004,(0,0,2):C.UVGC_759_1005,(0,0,1):C.UVGC_759_1006})

V_701 = CTVertex(name = 'V_701',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_458_776})

V_702 = CTVertex(name = 'V_702',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_386_618,(0,0,1):C.UVGC_386_619,(0,0,2):C.UVGC_386_620,(0,0,3):C.UVGC_386_621,(0,0,4):C.UVGC_386_622,(0,0,6):C.UVGC_386_623,(0,0,7):C.UVGC_386_624,(0,0,8):C.UVGC_386_625,(0,0,9):C.UVGC_386_626,(0,0,10):C.UVGC_386_627,(0,0,11):C.UVGC_386_628,(0,0,12):C.UVGC_386_629,(0,0,13):C.UVGC_386_630,(0,0,14):C.UVGC_386_631,(0,0,15):C.UVGC_386_632,(0,0,16):C.UVGC_386_633,(0,0,17):C.UVGC_386_634,(0,0,18):C.UVGC_386_635,(0,0,19):C.UVGC_386_636,(0,0,20):C.UVGC_386_637,(0,0,21):C.UVGC_386_638,(0,0,22):C.UVGC_386_639,(0,0,23):C.UVGC_386_640,(0,0,24):C.UVGC_386_641,(0,0,25):C.UVGC_386_642,(0,0,26):C.UVGC_386_643,(0,0,27):C.UVGC_386_644,(0,0,28):C.UVGC_386_645,(0,0,29):C.UVGC_386_646,(0,0,30):C.UVGC_386_647,(0,0,31):C.UVGC_386_648,(0,0,32):C.UVGC_386_649,(0,0,5):C.UVGC_461_779})

V_703 = CTVertex(name = 'V_703',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_305_451,(2,0,1):C.UVGC_305_452,(2,0,2):C.UVGC_305_453,(2,0,3):C.UVGC_305_454,(2,0,4):C.UVGC_305_455,(2,0,6):C.UVGC_305_456,(2,0,7):C.UVGC_305_457,(2,0,8):C.UVGC_305_458,(2,0,9):C.UVGC_305_459,(2,0,10):C.UVGC_305_460,(2,0,11):C.UVGC_305_461,(2,0,12):C.UVGC_305_462,(2,0,13):C.UVGC_305_463,(2,0,14):C.UVGC_305_464,(2,0,15):C.UVGC_305_465,(2,0,16):C.UVGC_305_466,(2,0,17):C.UVGC_305_467,(2,0,18):C.UVGC_305_468,(2,0,19):C.UVGC_305_469,(2,0,20):C.UVGC_305_470,(2,0,21):C.UVGC_305_471,(2,0,22):C.UVGC_305_472,(2,0,23):C.UVGC_305_473,(2,0,24):C.UVGC_305_474,(2,0,25):C.UVGC_305_475,(2,0,26):C.UVGC_305_476,(2,0,27):C.UVGC_305_477,(2,0,28):C.UVGC_305_478,(2,0,29):C.UVGC_305_479,(2,0,30):C.UVGC_305_480,(2,0,31):C.UVGC_305_481,(2,0,32):C.UVGC_305_482,(2,0,5):C.UVGC_464_780,(1,0,0):C.UVGC_305_451,(1,0,1):C.UVGC_305_452,(1,0,2):C.UVGC_305_453,(1,0,3):C.UVGC_305_454,(1,0,4):C.UVGC_305_455,(1,0,6):C.UVGC_305_456,(1,0,7):C.UVGC_305_457,(1,0,8):C.UVGC_305_458,(1,0,9):C.UVGC_305_459,(1,0,10):C.UVGC_305_460,(1,0,11):C.UVGC_305_461,(1,0,12):C.UVGC_305_462,(1,0,13):C.UVGC_305_463,(1,0,14):C.UVGC_305_464,(1,0,15):C.UVGC_305_465,(1,0,16):C.UVGC_305_466,(1,0,17):C.UVGC_305_467,(1,0,18):C.UVGC_305_468,(1,0,19):C.UVGC_305_469,(1,0,20):C.UVGC_305_470,(1,0,21):C.UVGC_305_471,(1,0,22):C.UVGC_305_472,(1,0,23):C.UVGC_305_473,(1,0,24):C.UVGC_305_474,(1,0,25):C.UVGC_305_475,(1,0,26):C.UVGC_305_476,(1,0,27):C.UVGC_305_477,(1,0,28):C.UVGC_305_478,(1,0,29):C.UVGC_305_479,(1,0,30):C.UVGC_305_480,(1,0,31):C.UVGC_305_481,(1,0,32):C.UVGC_305_482,(1,0,5):C.UVGC_464_780,(0,0,3):C.UVGC_304_449,(0,0,5):C.UVGC_304_450})

V_704 = CTVertex(name = 'V_704',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_757_999,(0,0,2):C.UVGC_757_1000,(0,0,1):C.UVGC_757_1001})

V_705 = CTVertex(name = 'V_705',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.YF3Qd1, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_515_808,(0,1,0):C.UVGC_513_806,(0,2,0):C.UVGC_514_807})

V_706 = CTVertex(name = 'V_706',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.YF3Qd2, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_515_808,(0,1,0):C.UVGC_520_810,(0,2,0):C.UVGC_521_811})

V_707 = CTVertex(name = 'V_707',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.YF3Qd3, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_515_808,(0,1,0):C.UVGC_527_813,(0,2,0):C.UVGC_528_814})

V_708 = CTVertex(name = 'V_708',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.YF3Qu1, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_538_822,(0,1,0):C.UVGC_536_820,(0,2,0):C.UVGC_537_821})

V_709 = CTVertex(name = 'V_709',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.YF3Qu2, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_538_822,(0,1,0):C.UVGC_545_828,(0,2,0):C.UVGC_546_829})

V_710 = CTVertex(name = 'V_710',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.YF3Qu3, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_538_822,(0,1,0):C.UVGC_554_835,(0,2,0):C.UVGC_555_836})

V_711 = CTVertex(name = 'V_711',
                 type = 'UV',
                 particles = [ P.YF3d1__tilde__, P.YF3d1, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_498_802,(0,1,0):C.UVGC_183_35,(0,2,0):C.UVGC_184_36})

V_712 = CTVertex(name = 'V_712',
                 type = 'UV',
                 particles = [ P.YF3d2__tilde__, P.YF3d2, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_498_802,(0,1,0):C.UVGC_191_43,(0,2,0):C.UVGC_192_44})

V_713 = CTVertex(name = 'V_713',
                 type = 'UV',
                 particles = [ P.YF3d3__tilde__, P.YF3d3, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_498_802,(0,1,0):C.UVGC_199_51,(0,2,0):C.UVGC_200_52})

V_714 = CTVertex(name = 'V_714',
                 type = 'UV',
                 particles = [ P.YF3u1__tilde__, P.YF3u1, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_561_838,(0,1,0):C.UVGC_243_95,(0,2,0):C.UVGC_244_96})

V_715 = CTVertex(name = 'V_715',
                 type = 'UV',
                 particles = [ P.YF3u2__tilde__, P.YF3u2, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_561_838,(0,1,0):C.UVGC_251_103,(0,2,0):C.UVGC_252_104})

V_716 = CTVertex(name = 'V_716',
                 type = 'UV',
                 particles = [ P.YF3u3__tilde__, P.YF3u3, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_561_838,(0,1,0):C.UVGC_259_111,(0,2,0):C.UVGC_260_112})

V_717 = CTVertex(name = 'V_717',
                 type = 'UV',
                 particles = [ P.Z, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_307_485})

V_718 = CTVertex(name = 'V_718',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_308_486})

V_719 = CTVertex(name = 'V_719',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_309_487,(0,0,1):C.UVGC_309_488,(0,0,2):C.UVGC_309_489,(0,0,3):C.UVGC_309_490,(0,0,4):C.UVGC_309_491,(0,0,6):C.UVGC_309_492,(0,0,7):C.UVGC_309_493,(0,0,8):C.UVGC_309_494,(0,0,9):C.UVGC_309_495,(0,0,10):C.UVGC_309_496,(0,0,11):C.UVGC_309_497,(0,0,12):C.UVGC_309_498,(0,0,13):C.UVGC_309_499,(0,0,14):C.UVGC_309_500,(0,0,15):C.UVGC_309_501,(0,0,16):C.UVGC_309_502,(0,0,17):C.UVGC_309_503,(0,0,18):C.UVGC_309_504,(0,0,19):C.UVGC_309_505,(0,0,20):C.UVGC_309_506,(0,0,21):C.UVGC_309_507,(0,0,22):C.UVGC_309_508,(0,0,23):C.UVGC_309_509,(0,0,24):C.UVGC_309_510,(0,0,25):C.UVGC_309_511,(0,0,26):C.UVGC_309_512,(0,0,27):C.UVGC_309_513,(0,0,28):C.UVGC_309_514,(0,0,29):C.UVGC_309_515,(0,0,30):C.UVGC_309_516,(0,0,31):C.UVGC_309_517,(0,0,32):C.UVGC_309_518,(0,0,5):C.UVGC_309_519})

V_720 = CTVertex(name = 'V_720',
                 type = 'UV',
                 particles = [ P.Z, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_320_528})

V_721 = CTVertex(name = 'V_721',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_321_529})

V_722 = CTVertex(name = 'V_722',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_309_487,(0,0,1):C.UVGC_309_488,(0,0,2):C.UVGC_309_489,(0,0,3):C.UVGC_309_490,(0,0,4):C.UVGC_309_491,(0,0,6):C.UVGC_309_492,(0,0,7):C.UVGC_309_493,(0,0,8):C.UVGC_309_494,(0,0,9):C.UVGC_309_495,(0,0,10):C.UVGC_309_496,(0,0,11):C.UVGC_309_497,(0,0,12):C.UVGC_309_498,(0,0,13):C.UVGC_309_499,(0,0,14):C.UVGC_309_500,(0,0,15):C.UVGC_309_501,(0,0,16):C.UVGC_309_502,(0,0,17):C.UVGC_309_503,(0,0,18):C.UVGC_309_504,(0,0,19):C.UVGC_309_505,(0,0,20):C.UVGC_309_506,(0,0,21):C.UVGC_309_507,(0,0,22):C.UVGC_309_508,(0,0,23):C.UVGC_309_509,(0,0,24):C.UVGC_309_510,(0,0,25):C.UVGC_309_511,(0,0,26):C.UVGC_309_512,(0,0,27):C.UVGC_309_513,(0,0,28):C.UVGC_309_514,(0,0,29):C.UVGC_309_515,(0,0,30):C.UVGC_309_516,(0,0,31):C.UVGC_309_517,(0,0,32):C.UVGC_309_518,(0,0,5):C.UVGC_322_530})

V_723 = CTVertex(name = 'V_723',
                 type = 'UV',
                 particles = [ P.Z, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_333_539})

V_724 = CTVertex(name = 'V_724',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_334_540})

V_725 = CTVertex(name = 'V_725',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_309_487,(0,0,1):C.UVGC_309_488,(0,0,2):C.UVGC_309_489,(0,0,3):C.UVGC_309_490,(0,0,4):C.UVGC_309_491,(0,0,6):C.UVGC_309_492,(0,0,7):C.UVGC_309_493,(0,0,8):C.UVGC_309_494,(0,0,9):C.UVGC_309_495,(0,0,10):C.UVGC_309_496,(0,0,11):C.UVGC_309_497,(0,0,12):C.UVGC_309_498,(0,0,13):C.UVGC_309_499,(0,0,14):C.UVGC_309_500,(0,0,15):C.UVGC_309_501,(0,0,16):C.UVGC_309_502,(0,0,17):C.UVGC_309_503,(0,0,18):C.UVGC_309_504,(0,0,19):C.UVGC_309_505,(0,0,20):C.UVGC_309_506,(0,0,21):C.UVGC_309_507,(0,0,22):C.UVGC_309_508,(0,0,23):C.UVGC_309_509,(0,0,24):C.UVGC_309_510,(0,0,25):C.UVGC_309_511,(0,0,26):C.UVGC_309_512,(0,0,27):C.UVGC_309_513,(0,0,28):C.UVGC_309_514,(0,0,29):C.UVGC_309_515,(0,0,30):C.UVGC_309_516,(0,0,31):C.UVGC_309_517,(0,0,32):C.UVGC_309_518,(0,0,5):C.UVGC_335_541})

V_726 = CTVertex(name = 'V_726',
                 type = 'UV',
                 particles = [ P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_346_550})

V_727 = CTVertex(name = 'V_727',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_347_551})

V_728 = CTVertex(name = 'V_728',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_348_552,(0,0,1):C.UVGC_348_553,(0,0,2):C.UVGC_348_554,(0,0,3):C.UVGC_348_555,(0,0,4):C.UVGC_348_556,(0,0,6):C.UVGC_348_557,(0,0,7):C.UVGC_348_558,(0,0,8):C.UVGC_348_559,(0,0,9):C.UVGC_348_560,(0,0,10):C.UVGC_348_561,(0,0,11):C.UVGC_348_562,(0,0,12):C.UVGC_348_563,(0,0,13):C.UVGC_348_564,(0,0,14):C.UVGC_348_565,(0,0,15):C.UVGC_348_566,(0,0,16):C.UVGC_348_567,(0,0,17):C.UVGC_348_568,(0,0,18):C.UVGC_348_569,(0,0,19):C.UVGC_348_570,(0,0,20):C.UVGC_348_571,(0,0,21):C.UVGC_348_572,(0,0,22):C.UVGC_348_573,(0,0,23):C.UVGC_348_574,(0,0,24):C.UVGC_348_575,(0,0,25):C.UVGC_348_576,(0,0,26):C.UVGC_348_577,(0,0,27):C.UVGC_348_578,(0,0,28):C.UVGC_348_579,(0,0,29):C.UVGC_348_580,(0,0,30):C.UVGC_348_581,(0,0,31):C.UVGC_348_582,(0,0,32):C.UVGC_348_583,(0,0,5):C.UVGC_348_584})

V_729 = CTVertex(name = 'V_729',
                 type = 'UV',
                 particles = [ P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_361_595})

V_730 = CTVertex(name = 'V_730',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_362_596})

V_731 = CTVertex(name = 'V_731',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_348_552,(0,0,1):C.UVGC_348_553,(0,0,2):C.UVGC_348_554,(0,0,3):C.UVGC_348_555,(0,0,4):C.UVGC_348_556,(0,0,6):C.UVGC_348_557,(0,0,7):C.UVGC_348_558,(0,0,8):C.UVGC_348_559,(0,0,9):C.UVGC_348_560,(0,0,10):C.UVGC_348_561,(0,0,11):C.UVGC_348_562,(0,0,12):C.UVGC_348_563,(0,0,13):C.UVGC_348_564,(0,0,14):C.UVGC_348_565,(0,0,15):C.UVGC_348_566,(0,0,16):C.UVGC_348_567,(0,0,17):C.UVGC_348_568,(0,0,18):C.UVGC_348_569,(0,0,19):C.UVGC_348_570,(0,0,20):C.UVGC_348_571,(0,0,21):C.UVGC_348_572,(0,0,22):C.UVGC_348_573,(0,0,23):C.UVGC_348_574,(0,0,24):C.UVGC_348_575,(0,0,25):C.UVGC_348_576,(0,0,26):C.UVGC_348_577,(0,0,27):C.UVGC_348_578,(0,0,28):C.UVGC_348_579,(0,0,29):C.UVGC_348_580,(0,0,30):C.UVGC_348_581,(0,0,31):C.UVGC_348_582,(0,0,32):C.UVGC_348_583,(0,0,5):C.UVGC_363_597})

V_732 = CTVertex(name = 'V_732',
                 type = 'UV',
                 particles = [ P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_376_608})

V_733 = CTVertex(name = 'V_733',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_377_609})

V_734 = CTVertex(name = 'V_734',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_348_552,(0,0,1):C.UVGC_348_553,(0,0,2):C.UVGC_348_554,(0,0,3):C.UVGC_348_555,(0,0,4):C.UVGC_348_556,(0,0,6):C.UVGC_348_557,(0,0,7):C.UVGC_348_558,(0,0,8):C.UVGC_348_559,(0,0,9):C.UVGC_348_560,(0,0,10):C.UVGC_348_561,(0,0,11):C.UVGC_348_562,(0,0,12):C.UVGC_348_563,(0,0,13):C.UVGC_348_564,(0,0,14):C.UVGC_348_565,(0,0,15):C.UVGC_348_566,(0,0,16):C.UVGC_348_567,(0,0,17):C.UVGC_348_568,(0,0,18):C.UVGC_348_569,(0,0,19):C.UVGC_348_570,(0,0,20):C.UVGC_348_571,(0,0,21):C.UVGC_348_572,(0,0,22):C.UVGC_348_573,(0,0,23):C.UVGC_348_574,(0,0,24):C.UVGC_348_575,(0,0,25):C.UVGC_348_576,(0,0,26):C.UVGC_348_577,(0,0,27):C.UVGC_348_578,(0,0,28):C.UVGC_348_579,(0,0,29):C.UVGC_348_580,(0,0,30):C.UVGC_348_581,(0,0,31):C.UVGC_348_582,(0,0,32):C.UVGC_348_583,(0,0,5):C.UVGC_378_610})

V_735 = CTVertex(name = 'V_735',
                 type = 'UV',
                 particles = [ P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_391_653})

V_736 = CTVertex(name = 'V_736',
                 type = 'UV',
                 particles = [ P.W__plus__, P.Z, P.YS3Qd1, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_645_898,(0,0,2):C.UVGC_645_899,(0,0,1):C.UVGC_645_900})

V_737 = CTVertex(name = 'V_737',
                 type = 'UV',
                 particles = [ P.W__minus__, P.Z, P.YS3Qd1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_645_898,(0,0,2):C.UVGC_645_899,(0,0,1):C.UVGC_645_900})

V_738 = CTVertex(name = 'V_738',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_392_654})

V_739 = CTVertex(name = 'V_739',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_393_655,(0,0,1):C.UVGC_393_656,(0,0,2):C.UVGC_393_657,(0,0,3):C.UVGC_393_658,(0,0,4):C.UVGC_393_659,(0,0,6):C.UVGC_393_660,(0,0,7):C.UVGC_393_661,(0,0,8):C.UVGC_393_662,(0,0,9):C.UVGC_393_663,(0,0,10):C.UVGC_393_664,(0,0,11):C.UVGC_393_665,(0,0,12):C.UVGC_393_666,(0,0,13):C.UVGC_393_667,(0,0,14):C.UVGC_393_668,(0,0,15):C.UVGC_393_669,(0,0,16):C.UVGC_393_670,(0,0,17):C.UVGC_393_671,(0,0,18):C.UVGC_393_672,(0,0,19):C.UVGC_393_673,(0,0,20):C.UVGC_393_674,(0,0,21):C.UVGC_393_675,(0,0,22):C.UVGC_393_676,(0,0,23):C.UVGC_393_677,(0,0,24):C.UVGC_393_678,(0,0,25):C.UVGC_393_679,(0,0,26):C.UVGC_393_680,(0,0,27):C.UVGC_393_681,(0,0,28):C.UVGC_393_682,(0,0,29):C.UVGC_393_683,(0,0,30):C.UVGC_393_684,(0,0,31):C.UVGC_393_685,(0,0,32):C.UVGC_393_686,(0,0,5):C.UVGC_393_687})

V_740 = CTVertex(name = 'V_740',
                 type = 'UV',
                 particles = [ P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_406_698})

V_741 = CTVertex(name = 'V_741',
                 type = 'UV',
                 particles = [ P.W__plus__, P.Z, P.YS3Qd2, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_677_949,(0,0,2):C.UVGC_677_950,(0,0,1):C.UVGC_645_900})

V_742 = CTVertex(name = 'V_742',
                 type = 'UV',
                 particles = [ P.W__minus__, P.Z, P.YS3Qd2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_677_949,(0,0,2):C.UVGC_677_950,(0,0,1):C.UVGC_645_900})

V_743 = CTVertex(name = 'V_743',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_407_699})

V_744 = CTVertex(name = 'V_744',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_393_655,(0,0,1):C.UVGC_393_656,(0,0,2):C.UVGC_393_657,(0,0,3):C.UVGC_393_658,(0,0,4):C.UVGC_393_659,(0,0,6):C.UVGC_393_660,(0,0,7):C.UVGC_393_661,(0,0,8):C.UVGC_393_662,(0,0,9):C.UVGC_393_663,(0,0,10):C.UVGC_393_664,(0,0,11):C.UVGC_393_665,(0,0,12):C.UVGC_393_666,(0,0,13):C.UVGC_393_667,(0,0,14):C.UVGC_393_668,(0,0,15):C.UVGC_393_669,(0,0,16):C.UVGC_393_670,(0,0,17):C.UVGC_393_671,(0,0,18):C.UVGC_393_672,(0,0,19):C.UVGC_393_673,(0,0,20):C.UVGC_393_674,(0,0,21):C.UVGC_393_675,(0,0,22):C.UVGC_393_676,(0,0,23):C.UVGC_393_677,(0,0,24):C.UVGC_393_678,(0,0,25):C.UVGC_393_679,(0,0,26):C.UVGC_393_680,(0,0,27):C.UVGC_393_681,(0,0,28):C.UVGC_393_682,(0,0,29):C.UVGC_393_683,(0,0,30):C.UVGC_393_684,(0,0,31):C.UVGC_393_685,(0,0,32):C.UVGC_393_686,(0,0,5):C.UVGC_408_700})

V_745 = CTVertex(name = 'V_745',
                 type = 'UV',
                 particles = [ P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_421_711})

V_746 = CTVertex(name = 'V_746',
                 type = 'UV',
                 particles = [ P.W__plus__, P.Z, P.YS3Qd3, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_708_965,(0,0,2):C.UVGC_708_966,(0,0,1):C.UVGC_645_900})

V_747 = CTVertex(name = 'V_747',
                 type = 'UV',
                 particles = [ P.W__minus__, P.Z, P.YS3Qd3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_708_965,(0,0,2):C.UVGC_708_966,(0,0,1):C.UVGC_645_900})

V_748 = CTVertex(name = 'V_748',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_422_712})

V_749 = CTVertex(name = 'V_749',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_393_655,(0,0,1):C.UVGC_393_656,(0,0,2):C.UVGC_393_657,(0,0,3):C.UVGC_393_658,(0,0,4):C.UVGC_393_659,(0,0,6):C.UVGC_393_660,(0,0,7):C.UVGC_393_661,(0,0,8):C.UVGC_393_662,(0,0,9):C.UVGC_393_663,(0,0,10):C.UVGC_393_664,(0,0,11):C.UVGC_393_665,(0,0,12):C.UVGC_393_666,(0,0,13):C.UVGC_393_667,(0,0,14):C.UVGC_393_668,(0,0,15):C.UVGC_393_669,(0,0,16):C.UVGC_393_670,(0,0,17):C.UVGC_393_671,(0,0,18):C.UVGC_393_672,(0,0,19):C.UVGC_393_673,(0,0,20):C.UVGC_393_674,(0,0,21):C.UVGC_393_675,(0,0,22):C.UVGC_393_676,(0,0,23):C.UVGC_393_677,(0,0,24):C.UVGC_393_678,(0,0,25):C.UVGC_393_679,(0,0,26):C.UVGC_393_680,(0,0,27):C.UVGC_393_681,(0,0,28):C.UVGC_393_682,(0,0,29):C.UVGC_393_683,(0,0,30):C.UVGC_393_684,(0,0,31):C.UVGC_393_685,(0,0,32):C.UVGC_393_686,(0,0,5):C.UVGC_423_713})

V_750 = CTVertex(name = 'V_750',
                 type = 'UV',
                 particles = [ P.Z, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_436_724})

V_751 = CTVertex(name = 'V_751',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_437_725})

V_752 = CTVertex(name = 'V_752',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_438_726,(0,0,1):C.UVGC_438_727,(0,0,2):C.UVGC_438_728,(0,0,3):C.UVGC_438_729,(0,0,4):C.UVGC_438_730,(0,0,6):C.UVGC_438_731,(0,0,7):C.UVGC_438_732,(0,0,8):C.UVGC_438_733,(0,0,9):C.UVGC_438_734,(0,0,10):C.UVGC_438_735,(0,0,11):C.UVGC_438_736,(0,0,12):C.UVGC_438_737,(0,0,13):C.UVGC_438_738,(0,0,14):C.UVGC_438_739,(0,0,15):C.UVGC_438_740,(0,0,16):C.UVGC_438_741,(0,0,17):C.UVGC_438_742,(0,0,18):C.UVGC_438_743,(0,0,19):C.UVGC_438_744,(0,0,20):C.UVGC_438_745,(0,0,21):C.UVGC_438_746,(0,0,22):C.UVGC_438_747,(0,0,23):C.UVGC_438_748,(0,0,24):C.UVGC_438_749,(0,0,25):C.UVGC_438_750,(0,0,26):C.UVGC_438_751,(0,0,27):C.UVGC_438_752,(0,0,28):C.UVGC_438_753,(0,0,29):C.UVGC_438_754,(0,0,30):C.UVGC_438_755,(0,0,31):C.UVGC_438_756,(0,0,32):C.UVGC_438_757,(0,0,5):C.UVGC_438_758})

V_753 = CTVertex(name = 'V_753',
                 type = 'UV',
                 particles = [ P.Z, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_451_769})

V_754 = CTVertex(name = 'V_754',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_452_770})

V_755 = CTVertex(name = 'V_755',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_438_726,(0,0,1):C.UVGC_438_727,(0,0,2):C.UVGC_438_728,(0,0,3):C.UVGC_438_729,(0,0,4):C.UVGC_438_730,(0,0,6):C.UVGC_438_731,(0,0,7):C.UVGC_438_732,(0,0,8):C.UVGC_438_733,(0,0,9):C.UVGC_438_734,(0,0,10):C.UVGC_438_735,(0,0,11):C.UVGC_438_736,(0,0,12):C.UVGC_438_737,(0,0,13):C.UVGC_438_738,(0,0,14):C.UVGC_438_739,(0,0,15):C.UVGC_438_740,(0,0,16):C.UVGC_438_741,(0,0,17):C.UVGC_438_742,(0,0,18):C.UVGC_438_743,(0,0,19):C.UVGC_438_744,(0,0,20):C.UVGC_438_745,(0,0,21):C.UVGC_438_746,(0,0,22):C.UVGC_438_747,(0,0,23):C.UVGC_438_748,(0,0,24):C.UVGC_438_749,(0,0,25):C.UVGC_438_750,(0,0,26):C.UVGC_438_751,(0,0,27):C.UVGC_438_752,(0,0,28):C.UVGC_438_753,(0,0,29):C.UVGC_438_754,(0,0,30):C.UVGC_438_755,(0,0,31):C.UVGC_438_756,(0,0,32):C.UVGC_438_757,(0,0,5):C.UVGC_453_771})

V_756 = CTVertex(name = 'V_756',
                 type = 'UV',
                 particles = [ P.Z, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_466_782})

V_757 = CTVertex(name = 'V_757',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_467_783})

V_758 = CTVertex(name = 'V_758',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_438_726,(0,0,1):C.UVGC_438_727,(0,0,2):C.UVGC_438_728,(0,0,3):C.UVGC_438_729,(0,0,4):C.UVGC_438_730,(0,0,6):C.UVGC_438_731,(0,0,7):C.UVGC_438_732,(0,0,8):C.UVGC_438_733,(0,0,9):C.UVGC_438_734,(0,0,10):C.UVGC_438_735,(0,0,11):C.UVGC_438_736,(0,0,12):C.UVGC_438_737,(0,0,13):C.UVGC_438_738,(0,0,14):C.UVGC_438_739,(0,0,15):C.UVGC_438_740,(0,0,16):C.UVGC_438_741,(0,0,17):C.UVGC_438_742,(0,0,18):C.UVGC_438_743,(0,0,19):C.UVGC_438_744,(0,0,20):C.UVGC_438_745,(0,0,21):C.UVGC_438_746,(0,0,22):C.UVGC_438_747,(0,0,23):C.UVGC_438_748,(0,0,24):C.UVGC_438_749,(0,0,25):C.UVGC_438_750,(0,0,26):C.UVGC_438_751,(0,0,27):C.UVGC_438_752,(0,0,28):C.UVGC_438_753,(0,0,29):C.UVGC_438_754,(0,0,30):C.UVGC_438_755,(0,0,31):C.UVGC_438_756,(0,0,32):C.UVGC_438_757,(0,0,5):C.UVGC_468_784})

V_759 = CTVertex(name = 'V_759',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_310_520})

V_760 = CTVertex(name = 'V_760',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_323_531})

V_761 = CTVertex(name = 'V_761',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_336_542})

V_762 = CTVertex(name = 'V_762',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_349_585})

V_763 = CTVertex(name = 'V_763',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_364_598})

V_764 = CTVertex(name = 'V_764',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_379_611})

V_765 = CTVertex(name = 'V_765',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_394_688})

V_766 = CTVertex(name = 'V_766',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_409_701})

V_767 = CTVertex(name = 'V_767',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_424_714})

V_768 = CTVertex(name = 'V_768',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_439_759})

V_769 = CTVertex(name = 'V_769',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_454_772})

V_770 = CTVertex(name = 'V_770',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_469_785})

V_771 = CTVertex(name = 'V_771',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.YF3Qu1, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_767_1022,(0,0,2):C.UVGC_767_1023,(0,0,1):C.UVGC_589_889})

V_772 = CTVertex(name = 'V_772',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.YF3Qd1, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_589_887,(0,0,2):C.UVGC_589_888,(0,0,1):C.UVGC_589_889})

V_773 = CTVertex(name = 'V_773',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.YF3Qu2, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_581_866,(0,0,2):C.UVGC_581_867,(0,0,1):C.UVGC_581_868})

V_774 = CTVertex(name = 'V_774',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.YF3Qd2, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3Qd2] ], [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_753_991,(0,0,2):C.UVGC_753_992,(0,0,1):C.UVGC_581_868})

V_775 = CTVertex(name = 'V_775',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.YF3Qu3, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_760_1007,(0,0,2):C.UVGC_760_1008,(0,0,1):C.UVGC_576_854})

V_776 = CTVertex(name = 'V_776',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.YF3Qd3, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_576_852,(0,0,2):C.UVGC_576_853,(0,0,1):C.UVGC_576_854})

V_777 = CTVertex(name = 'V_777',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.YF3Qu1, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_767_1022,(0,0,2):C.UVGC_767_1023,(0,0,1):C.UVGC_589_889})

V_778 = CTVertex(name = 'V_778',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.YF3Qd1, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_589_887,(0,0,2):C.UVGC_589_888,(0,0,1):C.UVGC_589_889})

V_779 = CTVertex(name = 'V_779',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.YF3Qu2, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_581_866,(0,0,2):C.UVGC_581_867,(0,0,1):C.UVGC_581_868})

V_780 = CTVertex(name = 'V_780',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.YF3Qd2, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3Qd2] ], [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_753_991,(0,0,2):C.UVGC_753_992,(0,0,1):C.UVGC_581_868})

V_781 = CTVertex(name = 'V_781',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.YF3Qu3, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_760_1007,(0,0,2):C.UVGC_760_1008,(0,0,1):C.UVGC_576_854})

V_782 = CTVertex(name = 'V_782',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.YF3Qd3, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_576_852,(0,0,2):C.UVGC_576_853,(0,0,1):C.UVGC_576_854})

V_783 = CTVertex(name = 'V_783',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_287_371,(0,1,0):C.UVGC_174_26,(0,2,0):C.UVGC_176_28})

V_784 = CTVertex(name = 'V_784',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_287_371,(0,1,0):C.UVGC_156_8,(0,2,0):C.UVGC_158_10})

V_785 = CTVertex(name = 'V_785',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_287_371,(0,1,0):C.UVGC_170_22,(0,2,0):C.UVGC_172_24})

V_786 = CTVertex(name = 'V_786',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_280_365,(0,1,0):C.UVGC_160_12,(0,2,0):C.UVGC_162_14})

V_787 = CTVertex(name = 'V_787',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_280_365,(0,1,0):C.UVGC_166_18,(0,2,0):C.UVGC_168_20})

V_788 = CTVertex(name = 'V_788',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_280_365,(0,1,0):C.UVGC_152_4,(0,2,0):C.UVGC_154_6})

V_789 = CTVertex(name = 'V_789',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_281_366,(0,1,0):C.UVGC_266_121,(0,1,1):C.UVGC_266_122,(0,1,2):C.UVGC_266_123,(0,1,3):C.UVGC_266_124,(0,1,4):C.UVGC_266_125,(0,1,6):C.UVGC_266_126,(0,1,7):C.UVGC_266_127,(0,1,8):C.UVGC_266_128,(0,1,9):C.UVGC_266_129,(0,1,10):C.UVGC_266_130,(0,1,11):C.UVGC_266_131,(0,1,12):C.UVGC_266_132,(0,1,13):C.UVGC_266_133,(0,1,14):C.UVGC_266_134,(0,1,15):C.UVGC_266_135,(0,1,16):C.UVGC_266_136,(0,1,17):C.UVGC_266_137,(0,1,18):C.UVGC_266_138,(0,1,19):C.UVGC_266_139,(0,1,20):C.UVGC_266_140,(0,1,21):C.UVGC_266_141,(0,1,22):C.UVGC_266_142,(0,1,23):C.UVGC_266_143,(0,1,24):C.UVGC_266_144,(0,1,25):C.UVGC_266_145,(0,1,26):C.UVGC_266_146,(0,1,27):C.UVGC_266_147,(0,1,28):C.UVGC_266_148,(0,1,29):C.UVGC_266_149,(0,1,30):C.UVGC_266_150,(0,1,31):C.UVGC_266_151,(0,1,32):C.UVGC_266_152,(0,1,5):C.UVGC_487_797,(0,2,0):C.UVGC_266_121,(0,2,1):C.UVGC_266_122,(0,2,2):C.UVGC_266_123,(0,2,3):C.UVGC_266_124,(0,2,4):C.UVGC_266_125,(0,2,6):C.UVGC_266_126,(0,2,7):C.UVGC_266_127,(0,2,8):C.UVGC_266_128,(0,2,9):C.UVGC_266_129,(0,2,10):C.UVGC_266_130,(0,2,11):C.UVGC_266_131,(0,2,12):C.UVGC_266_132,(0,2,13):C.UVGC_266_133,(0,2,14):C.UVGC_266_134,(0,2,15):C.UVGC_266_135,(0,2,16):C.UVGC_266_136,(0,2,17):C.UVGC_266_137,(0,2,18):C.UVGC_266_138,(0,2,19):C.UVGC_266_139,(0,2,20):C.UVGC_266_140,(0,2,21):C.UVGC_266_141,(0,2,22):C.UVGC_266_142,(0,2,23):C.UVGC_266_143,(0,2,24):C.UVGC_266_144,(0,2,25):C.UVGC_266_145,(0,2,26):C.UVGC_266_146,(0,2,27):C.UVGC_266_147,(0,2,28):C.UVGC_266_148,(0,2,29):C.UVGC_266_149,(0,2,30):C.UVGC_266_150,(0,2,31):C.UVGC_266_151,(0,2,32):C.UVGC_266_152,(0,2,5):C.UVGC_488_798})

V_790 = CTVertex(name = 'V_790',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.c, P.g] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,2):C.UVGC_281_366,(0,1,0):C.UVGC_266_121,(0,1,1):C.UVGC_266_122,(0,1,3):C.UVGC_266_123,(0,1,4):C.UVGC_266_124,(0,1,5):C.UVGC_266_125,(0,1,6):C.UVGC_266_126,(0,1,7):C.UVGC_266_127,(0,1,8):C.UVGC_266_128,(0,1,9):C.UVGC_266_129,(0,1,10):C.UVGC_266_130,(0,1,11):C.UVGC_266_131,(0,1,12):C.UVGC_266_132,(0,1,13):C.UVGC_266_133,(0,1,14):C.UVGC_266_134,(0,1,15):C.UVGC_266_135,(0,1,16):C.UVGC_266_136,(0,1,17):C.UVGC_266_137,(0,1,18):C.UVGC_266_138,(0,1,19):C.UVGC_266_139,(0,1,20):C.UVGC_266_140,(0,1,21):C.UVGC_266_141,(0,1,22):C.UVGC_266_142,(0,1,23):C.UVGC_266_143,(0,1,24):C.UVGC_266_144,(0,1,25):C.UVGC_266_145,(0,1,26):C.UVGC_266_146,(0,1,27):C.UVGC_266_147,(0,1,28):C.UVGC_266_148,(0,1,29):C.UVGC_266_149,(0,1,30):C.UVGC_266_150,(0,1,31):C.UVGC_266_151,(0,1,32):C.UVGC_266_152,(0,1,2):C.UVGC_284_369,(0,2,0):C.UVGC_266_121,(0,2,1):C.UVGC_266_122,(0,2,3):C.UVGC_266_123,(0,2,4):C.UVGC_266_124,(0,2,5):C.UVGC_266_125,(0,2,6):C.UVGC_266_126,(0,2,7):C.UVGC_266_127,(0,2,8):C.UVGC_266_128,(0,2,9):C.UVGC_266_129,(0,2,10):C.UVGC_266_130,(0,2,11):C.UVGC_266_131,(0,2,12):C.UVGC_266_132,(0,2,13):C.UVGC_266_133,(0,2,14):C.UVGC_266_134,(0,2,15):C.UVGC_266_135,(0,2,16):C.UVGC_266_136,(0,2,17):C.UVGC_266_137,(0,2,18):C.UVGC_266_138,(0,2,19):C.UVGC_266_139,(0,2,20):C.UVGC_266_140,(0,2,21):C.UVGC_266_141,(0,2,22):C.UVGC_266_142,(0,2,23):C.UVGC_266_143,(0,2,24):C.UVGC_266_144,(0,2,25):C.UVGC_266_145,(0,2,26):C.UVGC_266_146,(0,2,27):C.UVGC_266_147,(0,2,28):C.UVGC_266_148,(0,2,29):C.UVGC_266_149,(0,2,30):C.UVGC_266_150,(0,2,31):C.UVGC_266_151,(0,2,32):C.UVGC_266_152,(0,2,2):C.UVGC_285_370})

V_791 = CTVertex(name = 'V_791',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_281_366,(0,1,0):C.UVGC_266_121,(0,1,1):C.UVGC_266_122,(0,1,2):C.UVGC_266_123,(0,1,3):C.UVGC_266_124,(0,1,4):C.UVGC_266_125,(0,1,6):C.UVGC_266_126,(0,1,7):C.UVGC_266_127,(0,1,8):C.UVGC_266_128,(0,1,9):C.UVGC_266_129,(0,1,10):C.UVGC_266_130,(0,1,11):C.UVGC_266_131,(0,1,12):C.UVGC_266_132,(0,1,13):C.UVGC_266_133,(0,1,14):C.UVGC_266_134,(0,1,15):C.UVGC_266_135,(0,1,16):C.UVGC_266_136,(0,1,17):C.UVGC_266_137,(0,1,18):C.UVGC_266_138,(0,1,19):C.UVGC_266_139,(0,1,20):C.UVGC_266_140,(0,1,21):C.UVGC_266_141,(0,1,22):C.UVGC_266_142,(0,1,23):C.UVGC_266_143,(0,1,24):C.UVGC_266_144,(0,1,25):C.UVGC_266_145,(0,1,26):C.UVGC_266_146,(0,1,27):C.UVGC_266_147,(0,1,28):C.UVGC_266_148,(0,1,29):C.UVGC_266_149,(0,1,30):C.UVGC_266_150,(0,1,31):C.UVGC_266_151,(0,1,32):C.UVGC_266_152,(0,1,5):C.UVGC_477_790,(0,2,0):C.UVGC_266_121,(0,2,1):C.UVGC_266_122,(0,2,2):C.UVGC_266_123,(0,2,3):C.UVGC_266_124,(0,2,4):C.UVGC_266_125,(0,2,6):C.UVGC_266_126,(0,2,7):C.UVGC_266_127,(0,2,8):C.UVGC_266_128,(0,2,9):C.UVGC_266_129,(0,2,10):C.UVGC_266_130,(0,2,11):C.UVGC_266_131,(0,2,12):C.UVGC_266_132,(0,2,13):C.UVGC_266_133,(0,2,14):C.UVGC_266_134,(0,2,15):C.UVGC_266_135,(0,2,16):C.UVGC_266_136,(0,2,17):C.UVGC_266_137,(0,2,18):C.UVGC_266_138,(0,2,19):C.UVGC_266_139,(0,2,20):C.UVGC_266_140,(0,2,21):C.UVGC_266_141,(0,2,22):C.UVGC_266_142,(0,2,23):C.UVGC_266_143,(0,2,24):C.UVGC_266_144,(0,2,25):C.UVGC_266_145,(0,2,26):C.UVGC_266_146,(0,2,27):C.UVGC_266_147,(0,2,28):C.UVGC_266_148,(0,2,29):C.UVGC_266_149,(0,2,30):C.UVGC_266_150,(0,2,31):C.UVGC_266_151,(0,2,32):C.UVGC_266_152,(0,2,5):C.UVGC_478_791})

V_792 = CTVertex(name = 'V_792',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,3):C.UVGC_281_366,(0,1,0):C.UVGC_266_121,(0,1,1):C.UVGC_266_122,(0,1,2):C.UVGC_266_123,(0,1,4):C.UVGC_266_124,(0,1,5):C.UVGC_266_125,(0,1,6):C.UVGC_266_126,(0,1,7):C.UVGC_266_127,(0,1,8):C.UVGC_266_128,(0,1,9):C.UVGC_266_129,(0,1,10):C.UVGC_266_130,(0,1,11):C.UVGC_266_131,(0,1,12):C.UVGC_266_132,(0,1,13):C.UVGC_266_133,(0,1,14):C.UVGC_266_134,(0,1,15):C.UVGC_266_135,(0,1,16):C.UVGC_266_136,(0,1,17):C.UVGC_266_137,(0,1,18):C.UVGC_266_138,(0,1,19):C.UVGC_266_139,(0,1,20):C.UVGC_266_140,(0,1,21):C.UVGC_266_141,(0,1,22):C.UVGC_266_142,(0,1,23):C.UVGC_266_143,(0,1,24):C.UVGC_266_144,(0,1,25):C.UVGC_266_145,(0,1,26):C.UVGC_266_146,(0,1,27):C.UVGC_266_147,(0,1,28):C.UVGC_266_148,(0,1,29):C.UVGC_266_149,(0,1,30):C.UVGC_266_150,(0,1,31):C.UVGC_266_151,(0,1,32):C.UVGC_266_152,(0,1,3):C.UVGC_291_374,(0,2,0):C.UVGC_266_121,(0,2,1):C.UVGC_266_122,(0,2,2):C.UVGC_266_123,(0,2,4):C.UVGC_266_124,(0,2,5):C.UVGC_266_125,(0,2,6):C.UVGC_266_126,(0,2,7):C.UVGC_266_127,(0,2,8):C.UVGC_266_128,(0,2,9):C.UVGC_266_129,(0,2,10):C.UVGC_266_130,(0,2,11):C.UVGC_266_131,(0,2,12):C.UVGC_266_132,(0,2,13):C.UVGC_266_133,(0,2,14):C.UVGC_266_134,(0,2,15):C.UVGC_266_135,(0,2,16):C.UVGC_266_136,(0,2,17):C.UVGC_266_137,(0,2,18):C.UVGC_266_138,(0,2,19):C.UVGC_266_139,(0,2,20):C.UVGC_266_140,(0,2,21):C.UVGC_266_141,(0,2,22):C.UVGC_266_142,(0,2,23):C.UVGC_266_143,(0,2,24):C.UVGC_266_144,(0,2,25):C.UVGC_266_145,(0,2,26):C.UVGC_266_146,(0,2,27):C.UVGC_266_147,(0,2,28):C.UVGC_266_148,(0,2,29):C.UVGC_266_149,(0,2,30):C.UVGC_266_150,(0,2,31):C.UVGC_266_151,(0,2,32):C.UVGC_266_152,(0,2,3):C.UVGC_292_375})

V_793 = CTVertex(name = 'V_793',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_281_366,(0,1,0):C.UVGC_266_121,(0,1,1):C.UVGC_266_122,(0,1,2):C.UVGC_266_123,(0,1,3):C.UVGC_266_124,(0,1,4):C.UVGC_266_125,(0,1,6):C.UVGC_266_126,(0,1,7):C.UVGC_266_127,(0,1,8):C.UVGC_266_128,(0,1,9):C.UVGC_266_129,(0,1,10):C.UVGC_266_130,(0,1,11):C.UVGC_266_131,(0,1,12):C.UVGC_266_132,(0,1,13):C.UVGC_266_133,(0,1,14):C.UVGC_266_134,(0,1,15):C.UVGC_266_135,(0,1,16):C.UVGC_266_136,(0,1,17):C.UVGC_266_137,(0,1,18):C.UVGC_266_138,(0,1,19):C.UVGC_266_139,(0,1,20):C.UVGC_266_140,(0,1,21):C.UVGC_266_141,(0,1,22):C.UVGC_266_142,(0,1,23):C.UVGC_266_143,(0,1,24):C.UVGC_266_144,(0,1,25):C.UVGC_266_145,(0,1,26):C.UVGC_266_146,(0,1,27):C.UVGC_266_147,(0,1,28):C.UVGC_266_148,(0,1,29):C.UVGC_266_149,(0,1,30):C.UVGC_266_150,(0,1,31):C.UVGC_266_151,(0,1,32):C.UVGC_266_152,(0,1,5):C.UVGC_470_786,(0,2,0):C.UVGC_266_121,(0,2,1):C.UVGC_266_122,(0,2,2):C.UVGC_266_123,(0,2,3):C.UVGC_266_124,(0,2,4):C.UVGC_266_125,(0,2,6):C.UVGC_266_126,(0,2,7):C.UVGC_266_127,(0,2,8):C.UVGC_266_128,(0,2,9):C.UVGC_266_129,(0,2,10):C.UVGC_266_130,(0,2,11):C.UVGC_266_131,(0,2,12):C.UVGC_266_132,(0,2,13):C.UVGC_266_133,(0,2,14):C.UVGC_266_134,(0,2,15):C.UVGC_266_135,(0,2,16):C.UVGC_266_136,(0,2,17):C.UVGC_266_137,(0,2,18):C.UVGC_266_138,(0,2,19):C.UVGC_266_139,(0,2,20):C.UVGC_266_140,(0,2,21):C.UVGC_266_141,(0,2,22):C.UVGC_266_142,(0,2,23):C.UVGC_266_143,(0,2,24):C.UVGC_266_144,(0,2,25):C.UVGC_266_145,(0,2,26):C.UVGC_266_146,(0,2,27):C.UVGC_266_147,(0,2,28):C.UVGC_266_148,(0,2,29):C.UVGC_266_149,(0,2,30):C.UVGC_266_150,(0,2,31):C.UVGC_266_151,(0,2,32):C.UVGC_266_152,(0,2,5):C.UVGC_471_787})

V_794 = CTVertex(name = 'V_794',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.b, P.g] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,1):C.UVGC_281_366,(0,1,0):C.UVGC_266_121,(0,1,2):C.UVGC_266_122,(0,1,3):C.UVGC_266_123,(0,1,4):C.UVGC_266_124,(0,1,5):C.UVGC_266_125,(0,1,6):C.UVGC_266_126,(0,1,7):C.UVGC_266_127,(0,1,8):C.UVGC_266_128,(0,1,9):C.UVGC_266_129,(0,1,10):C.UVGC_266_130,(0,1,11):C.UVGC_266_131,(0,1,12):C.UVGC_266_132,(0,1,13):C.UVGC_266_133,(0,1,14):C.UVGC_266_134,(0,1,15):C.UVGC_266_135,(0,1,16):C.UVGC_266_136,(0,1,17):C.UVGC_266_137,(0,1,18):C.UVGC_266_138,(0,1,19):C.UVGC_266_139,(0,1,20):C.UVGC_266_140,(0,1,21):C.UVGC_266_141,(0,1,22):C.UVGC_266_142,(0,1,23):C.UVGC_266_143,(0,1,24):C.UVGC_266_144,(0,1,25):C.UVGC_266_145,(0,1,26):C.UVGC_266_146,(0,1,27):C.UVGC_266_147,(0,1,28):C.UVGC_266_148,(0,1,29):C.UVGC_266_149,(0,1,30):C.UVGC_266_150,(0,1,31):C.UVGC_266_151,(0,1,32):C.UVGC_266_152,(0,1,1):C.UVGC_277_362,(0,2,0):C.UVGC_266_121,(0,2,2):C.UVGC_266_122,(0,2,3):C.UVGC_266_123,(0,2,4):C.UVGC_266_124,(0,2,5):C.UVGC_266_125,(0,2,6):C.UVGC_266_126,(0,2,7):C.UVGC_266_127,(0,2,8):C.UVGC_266_128,(0,2,9):C.UVGC_266_129,(0,2,10):C.UVGC_266_130,(0,2,11):C.UVGC_266_131,(0,2,12):C.UVGC_266_132,(0,2,13):C.UVGC_266_133,(0,2,14):C.UVGC_266_134,(0,2,15):C.UVGC_266_135,(0,2,16):C.UVGC_266_136,(0,2,17):C.UVGC_266_137,(0,2,18):C.UVGC_266_138,(0,2,19):C.UVGC_266_139,(0,2,20):C.UVGC_266_140,(0,2,21):C.UVGC_266_141,(0,2,22):C.UVGC_266_142,(0,2,23):C.UVGC_266_143,(0,2,24):C.UVGC_266_144,(0,2,25):C.UVGC_266_145,(0,2,26):C.UVGC_266_146,(0,2,27):C.UVGC_266_147,(0,2,28):C.UVGC_266_148,(0,2,29):C.UVGC_266_149,(0,2,30):C.UVGC_266_150,(0,2,31):C.UVGC_266_151,(0,2,32):C.UVGC_266_152,(0,2,1):C.UVGC_278_363})

V_795 = CTVertex(name = 'V_795',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_764_1015,(0,0,2):C.UVGC_764_1016,(0,0,1):C.UVGC_580_865})

V_796 = CTVertex(name = 'V_796',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_580_863,(0,0,2):C.UVGC_580_864,(0,0,1):C.UVGC_580_865})

V_797 = CTVertex(name = 'V_797',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_755_994,(0,0,2):C.UVGC_755_995,(0,0,1):C.UVGC_580_865})

V_798 = CTVertex(name = 'V_798',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_764_1015,(0,0,2):C.UVGC_764_1016,(0,0,1):C.UVGC_580_865})

V_799 = CTVertex(name = 'V_799',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_580_863,(0,0,2):C.UVGC_580_864,(0,0,1):C.UVGC_580_865})

V_800 = CTVertex(name = 'V_800',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_755_994,(0,0,2):C.UVGC_755_995,(0,0,1):C.UVGC_580_865})

V_801 = CTVertex(name = 'V_801',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_492_799,(0,1,0):C.UVGC_493_800})

V_802 = CTVertex(name = 'V_802',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_289_372,(0,1,0):C.UVGC_290_373})

V_803 = CTVertex(name = 'V_803',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_483_793,(0,1,0):C.UVGC_484_794})

V_804 = CTVertex(name = 'V_804',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_296_376,(0,1,0):C.UVGC_297_377})

V_805 = CTVertex(name = 'V_805',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_475_788,(0,1,0):C.UVGC_476_789})

V_806 = CTVertex(name = 'V_806',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_282_367,(0,1,0):C.UVGC_283_368})

V_807 = CTVertex(name = 'V_807',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.u, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_767_1022,(0,0,2):C.UVGC_767_1023,(0,0,1):C.UVGC_589_889})

V_808 = CTVertex(name = 'V_808',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.d, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_589_887,(0,0,2):C.UVGC_589_888,(0,0,1):C.UVGC_589_889})

V_809 = CTVertex(name = 'V_809',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.c, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_581_866,(0,0,2):C.UVGC_581_867,(0,0,1):C.UVGC_581_868})

V_810 = CTVertex(name = 'V_810',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.s, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3Qd2] ], [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_753_991,(0,0,2):C.UVGC_753_992,(0,0,1):C.UVGC_581_868})

V_811 = CTVertex(name = 'V_811',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.t, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_760_1007,(0,0,2):C.UVGC_760_1008,(0,0,1):C.UVGC_576_854})

V_812 = CTVertex(name = 'V_812',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.b, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_576_852,(0,0,2):C.UVGC_576_853,(0,0,1):C.UVGC_576_854})

V_813 = CTVertex(name = 'V_813',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.u, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_767_1022,(0,0,2):C.UVGC_767_1023,(0,0,1):C.UVGC_589_889})

V_814 = CTVertex(name = 'V_814',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.d, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_589_887,(0,0,2):C.UVGC_589_888,(0,0,1):C.UVGC_589_889})

V_815 = CTVertex(name = 'V_815',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.c, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_581_866,(0,0,2):C.UVGC_581_867,(0,0,1):C.UVGC_581_868})

V_816 = CTVertex(name = 'V_816',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.s, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3Qd2] ], [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_753_991,(0,0,2):C.UVGC_753_992,(0,0,1):C.UVGC_581_868})

V_817 = CTVertex(name = 'V_817',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.t, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_760_1007,(0,0,2):C.UVGC_760_1008,(0,0,1):C.UVGC_576_854})

V_818 = CTVertex(name = 'V_818',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.b, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_576_852,(0,0,2):C.UVGC_576_853,(0,0,1):C.UVGC_576_854})

V_819 = CTVertex(name = 'V_819',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.YF3d1, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3d1] ], [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_587_882,(0,0,2):C.UVGC_587_883,(0,0,1):C.UVGC_587_884})

V_820 = CTVertex(name = 'V_820',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.YF3d2, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3d2] ], [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_751_986,(0,0,2):C.UVGC_751_987,(0,0,1):C.UVGC_751_988})

V_821 = CTVertex(name = 'V_821',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.YF3d3, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3d3] ], [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_574_847,(0,0,2):C.UVGC_574_848,(0,0,1):C.UVGC_574_849})

V_822 = CTVertex(name = 'V_822',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.YF3u1, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3u1] ], [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_769_1025,(0,0,2):C.UVGC_769_1026,(0,0,1):C.UVGC_769_1027})

V_823 = CTVertex(name = 'V_823',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.YF3u2, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3u2] ], [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_583_871,(0,0,2):C.UVGC_583_872,(0,0,1):C.UVGC_583_873})

V_824 = CTVertex(name = 'V_824',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.YF3u3, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3u3] ], [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_762_1010,(0,0,2):C.UVGC_762_1011,(0,0,1):C.UVGC_762_1012})

V_825 = CTVertex(name = 'V_825',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.YF3d1, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3d1] ], [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_587_882,(0,0,2):C.UVGC_587_883,(0,0,1):C.UVGC_587_884})

V_826 = CTVertex(name = 'V_826',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.YF3d2, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3d2] ], [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_751_986,(0,0,2):C.UVGC_751_987,(0,0,1):C.UVGC_751_988})

V_827 = CTVertex(name = 'V_827',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.YF3d3, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3d3] ], [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_574_847,(0,0,2):C.UVGC_574_848,(0,0,1):C.UVGC_574_849})

V_828 = CTVertex(name = 'V_828',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.YF3u1, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3u1] ], [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_769_1025,(0,0,2):C.UVGC_769_1026,(0,0,1):C.UVGC_769_1027})

V_829 = CTVertex(name = 'V_829',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.YF3u2, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3u2] ], [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_583_871,(0,0,2):C.UVGC_583_872,(0,0,1):C.UVGC_583_873})

V_830 = CTVertex(name = 'V_830',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.YF3u3, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3u3] ], [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_762_1010,(0,0,2):C.UVGC_762_1011,(0,0,1):C.UVGC_762_1012})

V_831 = CTVertex(name = 'V_831',
                 type = 'UV',
                 particles = [ P.YF3d1__tilde__, P.d, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3d1] ], [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_587_882,(0,0,2):C.UVGC_587_883,(0,0,1):C.UVGC_587_884})

V_832 = CTVertex(name = 'V_832',
                 type = 'UV',
                 particles = [ P.YF3d2__tilde__, P.s, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3d2] ], [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_751_986,(0,0,2):C.UVGC_751_987,(0,0,1):C.UVGC_751_988})

V_833 = CTVertex(name = 'V_833',
                 type = 'UV',
                 particles = [ P.YF3d3__tilde__, P.b, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3d3] ], [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_574_847,(0,0,2):C.UVGC_574_848,(0,0,1):C.UVGC_574_849})

V_834 = CTVertex(name = 'V_834',
                 type = 'UV',
                 particles = [ P.YF3u1__tilde__, P.u, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3u1] ], [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_769_1025,(0,0,2):C.UVGC_769_1026,(0,0,1):C.UVGC_769_1027})

V_835 = CTVertex(name = 'V_835',
                 type = 'UV',
                 particles = [ P.YF3u2__tilde__, P.c, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3u2] ], [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_583_871,(0,0,2):C.UVGC_583_872,(0,0,1):C.UVGC_583_873})

V_836 = CTVertex(name = 'V_836',
                 type = 'UV',
                 particles = [ P.YF3u3__tilde__, P.t, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3u3] ], [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_762_1010,(0,0,2):C.UVGC_762_1011,(0,0,1):C.UVGC_762_1012})

V_837 = CTVertex(name = 'V_837',
                 type = 'UV',
                 particles = [ P.YF3d1__tilde__, P.d, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3d1] ], [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_587_882,(0,0,2):C.UVGC_587_883,(0,0,1):C.UVGC_587_884})

V_838 = CTVertex(name = 'V_838',
                 type = 'UV',
                 particles = [ P.YF3d2__tilde__, P.s, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3d2] ], [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_751_986,(0,0,2):C.UVGC_751_987,(0,0,1):C.UVGC_751_988})

V_839 = CTVertex(name = 'V_839',
                 type = 'UV',
                 particles = [ P.YF3d3__tilde__, P.b, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3d3] ], [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_574_847,(0,0,2):C.UVGC_574_848,(0,0,1):C.UVGC_574_849})

V_840 = CTVertex(name = 'V_840',
                 type = 'UV',
                 particles = [ P.YF3u1__tilde__, P.u, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3u1] ], [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_769_1025,(0,0,2):C.UVGC_769_1026,(0,0,1):C.UVGC_769_1027})

V_841 = CTVertex(name = 'V_841',
                 type = 'UV',
                 particles = [ P.YF3u2__tilde__, P.c, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3u2] ], [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_583_871,(0,0,2):C.UVGC_583_872,(0,0,1):C.UVGC_583_873})

V_842 = CTVertex(name = 'V_842',
                 type = 'UV',
                 particles = [ P.YF3u3__tilde__, P.t, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3u3] ], [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_762_1010,(0,0,2):C.UVGC_762_1011,(0,0,1):C.UVGC_762_1012})

V_843 = CTVertex(name = 'V_843',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF4 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_279_364,(0,1,0):C.UVGC_173_25,(0,2,0):C.UVGC_175_27})

V_844 = CTVertex(name = 'V_844',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF4 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_279_364,(0,1,0):C.UVGC_155_7,(0,2,0):C.UVGC_157_9})

V_845 = CTVertex(name = 'V_845',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,1,0):C.UVGC_482_792,(0,3,0):C.UVGC_279_364,(0,0,0):C.UVGC_169_21,(0,2,0):C.UVGC_171_23})

V_846 = CTVertex(name = 'V_846',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF4 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_279_364,(0,1,0):C.UVGC_159_11,(0,2,0):C.UVGC_161_13})

V_847 = CTVertex(name = 'V_847',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF4 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_279_364,(0,1,0):C.UVGC_165_17,(0,2,0):C.UVGC_167_19})

V_848 = CTVertex(name = 'V_848',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF4 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_279_364,(0,1,0):C.UVGC_151_3,(0,2,0):C.UVGC_153_5})

V_849 = CTVertex(name = 'V_849',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.YF3Qu1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,1,0):C.UVGC_533_815,(0,3,0):C.UVGC_279_364,(0,0,0):C.UVGC_219_71,(0,2,0):C.UVGC_221_73})

V_850 = CTVertex(name = 'V_850',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.YF3Qu2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,1,0):C.UVGC_542_823,(0,3,0):C.UVGC_279_364,(0,0,0):C.UVGC_225_77,(0,2,0):C.UVGC_227_79})

V_851 = CTVertex(name = 'V_851',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.YF3Qu3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,1,0):C.UVGC_551_830,(0,3,0):C.UVGC_279_364,(0,0,0):C.UVGC_231_83,(0,2,0):C.UVGC_233_85})

V_852 = CTVertex(name = 'V_852',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.YF3Qd1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,1,0):C.UVGC_512_805,(0,3,0):C.UVGC_279_364,(0,0,0):C.UVGC_201_53,(0,2,0):C.UVGC_203_55})

V_853 = CTVertex(name = 'V_853',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.YF3Qd2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,1,0):C.UVGC_519_809,(0,3,0):C.UVGC_279_364,(0,0,0):C.UVGC_207_59,(0,2,0):C.UVGC_209_61})

V_854 = CTVertex(name = 'V_854',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.YF3Qd3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,1,0):C.UVGC_526_812,(0,3,0):C.UVGC_279_364,(0,0,0):C.UVGC_213_65,(0,2,0):C.UVGC_215_67})

V_855 = CTVertex(name = 'V_855',
                 type = 'UV',
                 particles = [ P.YF3u1__tilde__, P.YF3u1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,1,0):C.UVGC_560_837,(0,3,0):C.UVGC_279_364,(0,0,0):C.UVGC_237_89,(0,2,0):C.UVGC_239_91})

V_856 = CTVertex(name = 'V_856',
                 type = 'UV',
                 particles = [ P.YF3u2__tilde__, P.YF3u2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,1,0):C.UVGC_565_839,(0,3,0):C.UVGC_279_364,(0,0,0):C.UVGC_245_97,(0,2,0):C.UVGC_247_99})

V_857 = CTVertex(name = 'V_857',
                 type = 'UV',
                 particles = [ P.YF3u3__tilde__, P.YF3u3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,1,0):C.UVGC_570_840,(0,3,0):C.UVGC_279_364,(0,0,0):C.UVGC_253_105,(0,2,0):C.UVGC_255_107})

V_858 = CTVertex(name = 'V_858',
                 type = 'UV',
                 particles = [ P.YF3d1__tilde__, P.YF3d1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,1,0):C.UVGC_497_801,(0,3,0):C.UVGC_279_364,(0,0,0):C.UVGC_177_29,(0,2,0):C.UVGC_179_31})

V_859 = CTVertex(name = 'V_859',
                 type = 'UV',
                 particles = [ P.YF3d2__tilde__, P.YF3d2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,1,0):C.UVGC_502_803,(0,3,0):C.UVGC_279_364,(0,0,0):C.UVGC_185_37,(0,2,0):C.UVGC_187_39})

V_860 = CTVertex(name = 'V_860',
                 type = 'UV',
                 particles = [ P.YF3d3__tilde__, P.YF3d3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,1,0):C.UVGC_507_804,(0,3,0):C.UVGC_279_364,(0,0,0):C.UVGC_193_45,(0,2,0):C.UVGC_195_47})

V_861 = CTVertex(name = 'V_861',
                 type = 'UV',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV4, L.VV5, L.VV6 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_267_153,(0,0,1):C.UVGC_267_154,(0,0,2):C.UVGC_267_155,(0,0,3):C.UVGC_267_156,(0,0,4):C.UVGC_267_157,(0,0,5):C.UVGC_267_158,(0,0,6):C.UVGC_267_159,(0,0,7):C.UVGC_267_160,(0,0,8):C.UVGC_267_161,(0,0,9):C.UVGC_267_162,(0,0,10):C.UVGC_267_163,(0,0,11):C.UVGC_267_164,(0,0,12):C.UVGC_267_165,(0,0,13):C.UVGC_267_166,(0,0,14):C.UVGC_267_167,(0,0,15):C.UVGC_267_168,(0,0,16):C.UVGC_267_169,(0,0,17):C.UVGC_267_170,(0,0,18):C.UVGC_267_171,(0,0,19):C.UVGC_267_172,(0,0,20):C.UVGC_267_173,(0,0,21):C.UVGC_267_174,(0,0,22):C.UVGC_267_175,(0,0,23):C.UVGC_267_176,(0,0,24):C.UVGC_267_177,(0,0,25):C.UVGC_267_178,(0,0,26):C.UVGC_267_179,(0,0,27):C.UVGC_267_180,(0,0,28):C.UVGC_267_181,(0,0,29):C.UVGC_267_182,(0,0,30):C.UVGC_267_183,(0,0,31):C.UVGC_267_184,(0,1,3):C.UVGC_149_1,(0,2,4):C.UVGC_150_2})

V_862 = CTVertex(name = 'V_862',
                 type = 'UV',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_390_652,(0,1,0):C.UVGC_380_612})

V_863 = CTVertex(name = 'V_863',
                 type = 'UV',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_405_697,(0,1,0):C.UVGC_395_689})

V_864 = CTVertex(name = 'V_864',
                 type = 'UV',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_420_710,(0,1,0):C.UVGC_410_702})

V_865 = CTVertex(name = 'V_865',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_345_549,(0,1,0):C.UVGC_337_543})

V_866 = CTVertex(name = 'V_866',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_360_594,(0,1,0):C.UVGC_350_586})

V_867 = CTVertex(name = 'V_867',
                 type = 'UV',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_375_607,(0,1,0):C.UVGC_365_599})

V_868 = CTVertex(name = 'V_868',
                 type = 'UV',
                 particles = [ P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_435_723,(0,1,0):C.UVGC_425_715})

V_869 = CTVertex(name = 'V_869',
                 type = 'UV',
                 particles = [ P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_450_768,(0,1,0):C.UVGC_440_760})

V_870 = CTVertex(name = 'V_870',
                 type = 'UV',
                 particles = [ P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_465_781,(0,1,0):C.UVGC_455_773})

V_871 = CTVertex(name = 'V_871',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_306_484,(0,1,0):C.UVGC_298_378})

V_872 = CTVertex(name = 'V_872',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_319_527,(0,1,0):C.UVGC_311_521})

V_873 = CTVertex(name = 'V_873',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_332_538,(0,1,0):C.UVGC_324_532})

V_874 = CTVertex(name = 'V_874',
                 type = 'UV',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3Qu1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_303_447,(1,0,3):C.UVGC_303_448,(1,0,0):C.UVGC_780_1036,(1,0,5):C.UVGC_780_1037,(1,0,1):C.UVGC_780_1038,(1,0,4):C.UVGC_780_1039,(0,0,2):C.UVGC_303_447,(0,0,3):C.UVGC_303_448,(0,0,0):C.UVGC_780_1036,(0,0,5):C.UVGC_780_1037,(0,0,1):C.UVGC_780_1038,(0,0,4):C.UVGC_780_1039})

V_875 = CTVertex(name = 'V_875',
                 type = 'UV',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3Qu1, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qu1, P.YS3Qu2] ], [ [P.g, P.YS3Qu1, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_853_1102,(1,0,8):C.UVGC_853_1103,(1,0,1):C.UVGC_853_1104,(1,0,7):C.UVGC_853_1105,(1,0,2):C.UVGC_793_1054,(1,0,6):C.UVGC_853_1106,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_852_1097,(0,0,8):C.UVGC_852_1098,(0,0,1):C.UVGC_852_1099,(0,0,7):C.UVGC_852_1100,(0,0,2):C.UVGC_792_1048,(0,0,6):C.UVGC_852_1101})

V_876 = CTVertex(name = 'V_876',
                 type = 'UV',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3Qu2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_303_447,(1,0,3):C.UVGC_303_448,(1,0,0):C.UVGC_780_1036,(1,0,5):C.UVGC_780_1037,(1,0,1):C.UVGC_780_1038,(1,0,4):C.UVGC_780_1039,(0,0,2):C.UVGC_303_447,(0,0,3):C.UVGC_303_448,(0,0,0):C.UVGC_780_1036,(0,0,5):C.UVGC_780_1037,(0,0,1):C.UVGC_780_1038,(0,0,4):C.UVGC_780_1039})

V_877 = CTVertex(name = 'V_877',
                 type = 'UV',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qu1, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qu1, P.YS3Qu3] ], [ [P.g, P.YS3Qu1, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_853_1102,(1,0,8):C.UVGC_853_1103,(1,0,1):C.UVGC_853_1104,(1,0,7):C.UVGC_853_1105,(1,0,2):C.UVGC_793_1054,(1,0,6):C.UVGC_853_1106,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_852_1097,(0,0,8):C.UVGC_852_1098,(0,0,1):C.UVGC_852_1099,(0,0,7):C.UVGC_852_1100,(0,0,2):C.UVGC_792_1048,(0,0,6):C.UVGC_852_1101})

V_878 = CTVertex(name = 'V_878',
                 type = 'UV',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qu2, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qu2], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qu2, P.YS3Qu3] ], [ [P.g, P.YS3Qu2, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qu2, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_853_1102,(1,0,8):C.UVGC_853_1103,(1,0,1):C.UVGC_853_1104,(1,0,7):C.UVGC_853_1105,(1,0,2):C.UVGC_793_1054,(1,0,6):C.UVGC_853_1106,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_852_1097,(0,0,8):C.UVGC_852_1098,(0,0,1):C.UVGC_852_1099,(0,0,7):C.UVGC_852_1100,(0,0,2):C.UVGC_792_1048,(0,0,6):C.UVGC_852_1101})

V_879 = CTVertex(name = 'V_879',
                 type = 'UV',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3__tilde__, P.YS3Qu3, P.YS3Qu3 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_303_447,(1,0,3):C.UVGC_303_448,(1,0,0):C.UVGC_780_1036,(1,0,5):C.UVGC_780_1037,(1,0,1):C.UVGC_780_1038,(1,0,4):C.UVGC_780_1039,(0,0,2):C.UVGC_303_447,(0,0,3):C.UVGC_303_448,(0,0,0):C.UVGC_780_1036,(0,0,5):C.UVGC_780_1037,(0,0,1):C.UVGC_780_1038,(0,0,4):C.UVGC_780_1039})

V_880 = CTVertex(name = 'V_880',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qu1] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,7):C.UVGC_592_896,(1,0,8):C.UVGC_592_897,(1,0,0):C.UVGC_809_1076,(1,0,4):C.UVGC_786_1042,(1,0,11):C.UVGC_847_1093,(1,0,1):C.UVGC_809_1078,(1,0,5):C.UVGC_787_1047,(1,0,10):C.UVGC_847_1094,(1,0,2):C.UVGC_809_1080,(1,0,6):C.UVGC_847_1095,(1,0,9):C.UVGC_847_1096,(0,0,3):C.UVGC_591_892,(0,0,7):C.UVGC_591_893,(0,0,8):C.UVGC_591_894,(0,0,0):C.UVGC_774_1030,(0,0,4):C.UVGC_787_1045,(0,0,11):C.UVGC_846_1088,(0,0,1):C.UVGC_774_1032,(0,0,5):C.UVGC_846_1089,(0,0,10):C.UVGC_846_1090,(0,0,2):C.UVGC_808_1074,(0,0,6):C.UVGC_846_1091,(0,0,9):C.UVGC_846_1092})

V_881 = CTVertex(name = 'V_881',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qd1, P.YS3Qu2] ], [ [P.g, P.YS3Qd1, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_809_1076,(1,0,8):C.UVGC_847_1093,(1,0,1):C.UVGC_809_1078,(1,0,7):C.UVGC_847_1094,(1,0,2):C.UVGC_809_1080,(1,0,6):C.UVGC_847_1096,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_774_1030,(0,0,8):C.UVGC_846_1088,(0,0,1):C.UVGC_774_1032,(0,0,7):C.UVGC_846_1090,(0,0,2):C.UVGC_808_1074,(0,0,6):C.UVGC_846_1092})

V_882 = CTVertex(name = 'V_882',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qd1, P.YS3Qu3] ], [ [P.g, P.YS3Qd1, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_809_1076,(1,0,8):C.UVGC_847_1093,(1,0,1):C.UVGC_809_1078,(1,0,7):C.UVGC_847_1094,(1,0,2):C.UVGC_809_1080,(1,0,6):C.UVGC_847_1096,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_774_1030,(0,0,8):C.UVGC_846_1088,(0,0,1):C.UVGC_774_1032,(0,0,7):C.UVGC_846_1090,(0,0,2):C.UVGC_808_1074,(0,0,6):C.UVGC_846_1092})

V_883 = CTVertex(name = 'V_883',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qd1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1] ], [ [P.g] ], [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_303_447,(1,0,3):C.UVGC_303_448,(1,0,0):C.UVGC_774_1030,(1,0,5):C.UVGC_777_1034,(1,0,1):C.UVGC_774_1032,(1,0,4):C.UVGC_777_1035,(0,0,2):C.UVGC_303_447,(0,0,3):C.UVGC_303_448,(0,0,0):C.UVGC_774_1030,(0,0,5):C.UVGC_777_1034,(0,0,1):C.UVGC_774_1032,(0,0,4):C.UVGC_777_1035})

V_884 = CTVertex(name = 'V_884',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd2, P.YS3Qu1, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu2] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu1, P.YS3Qu2] ] ],
                 couplings = {(1,0,0):C.UVGC_786_1042,(1,0,1):C.UVGC_786_1043,(1,0,2):C.UVGC_786_1044,(0,0,0):C.UVGC_787_1045,(0,0,1):C.UVGC_787_1046,(0,0,2):C.UVGC_787_1047})

V_885 = CTVertex(name = 'V_885',
                 type = 'UV',
                 particles = [ P.YS3Qd1, P.YS3Qd2__tilde__, P.YS3Qu1__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu2] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu1, P.YS3Qu2] ] ],
                 couplings = {(1,0,0):C.UVGC_786_1042,(1,0,1):C.UVGC_786_1043,(1,0,2):C.UVGC_786_1044,(0,0,0):C.UVGC_787_1045,(0,0,1):C.UVGC_787_1046,(0,0,2):C.UVGC_787_1047})

V_886 = CTVertex(name = 'V_886',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3Qd2, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qd2, P.YS3Qu1] ], [ [P.g, P.YS3Qd2, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_809_1076,(1,0,8):C.UVGC_847_1093,(1,0,1):C.UVGC_809_1078,(1,0,7):C.UVGC_847_1094,(1,0,2):C.UVGC_809_1080,(1,0,6):C.UVGC_847_1096,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_774_1030,(0,0,8):C.UVGC_846_1088,(0,0,1):C.UVGC_774_1032,(0,0,7):C.UVGC_846_1090,(0,0,2):C.UVGC_808_1074,(0,0,6):C.UVGC_846_1092})

V_887 = CTVertex(name = 'V_887',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qu2] ], [ [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,7):C.UVGC_592_896,(1,0,8):C.UVGC_592_897,(1,0,0):C.UVGC_809_1076,(1,0,4):C.UVGC_786_1042,(1,0,11):C.UVGC_847_1093,(1,0,1):C.UVGC_809_1078,(1,0,5):C.UVGC_787_1047,(1,0,10):C.UVGC_847_1094,(1,0,2):C.UVGC_809_1080,(1,0,6):C.UVGC_847_1095,(1,0,9):C.UVGC_847_1096,(0,0,3):C.UVGC_591_892,(0,0,7):C.UVGC_591_893,(0,0,8):C.UVGC_591_894,(0,0,0):C.UVGC_774_1030,(0,0,4):C.UVGC_787_1045,(0,0,11):C.UVGC_846_1088,(0,0,1):C.UVGC_774_1032,(0,0,5):C.UVGC_846_1089,(0,0,10):C.UVGC_846_1090,(0,0,2):C.UVGC_808_1074,(0,0,6):C.UVGC_846_1091,(0,0,9):C.UVGC_846_1092})

V_888 = CTVertex(name = 'V_888',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qd2, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qd2, P.YS3Qu3] ], [ [P.g, P.YS3Qd2, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_809_1076,(1,0,8):C.UVGC_847_1093,(1,0,1):C.UVGC_809_1078,(1,0,7):C.UVGC_847_1094,(1,0,2):C.UVGC_809_1080,(1,0,6):C.UVGC_847_1096,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_774_1030,(0,0,8):C.UVGC_846_1088,(0,0,1):C.UVGC_774_1032,(0,0,7):C.UVGC_846_1090,(0,0,2):C.UVGC_808_1074,(0,0,6):C.UVGC_846_1092})

V_889 = CTVertex(name = 'V_889',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qd2] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd1, P.YS3Qd2] ], [ [P.g, P.YS3Qd1, P.YS3Qd2, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_793_1054,(1,0,8):C.UVGC_805_1069,(1,0,1):C.UVGC_793_1056,(1,0,7):C.UVGC_805_1070,(1,0,2):C.UVGC_793_1058,(1,0,6):C.UVGC_805_1071,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_792_1048,(0,0,8):C.UVGC_804_1066,(0,0,1):C.UVGC_792_1050,(0,0,7):C.UVGC_804_1067,(0,0,2):C.UVGC_792_1052,(0,0,6):C.UVGC_804_1068})

V_890 = CTVertex(name = 'V_890',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qd2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_303_447,(1,0,3):C.UVGC_303_448,(1,0,0):C.UVGC_774_1030,(1,0,5):C.UVGC_777_1034,(1,0,1):C.UVGC_774_1032,(1,0,4):C.UVGC_777_1035,(0,0,2):C.UVGC_303_447,(0,0,3):C.UVGC_303_448,(0,0,0):C.UVGC_774_1030,(0,0,5):C.UVGC_777_1034,(0,0,1):C.UVGC_774_1032,(0,0,4):C.UVGC_777_1035})

V_891 = CTVertex(name = 'V_891',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd3, P.YS3Qu1, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu3], [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu1, P.YS3Qu3] ] ],
                 couplings = {(1,0,0):C.UVGC_786_1042,(1,0,1):C.UVGC_786_1043,(1,0,2):C.UVGC_786_1044,(0,0,0):C.UVGC_787_1045,(0,0,1):C.UVGC_787_1046,(0,0,2):C.UVGC_787_1047})

V_892 = CTVertex(name = 'V_892',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd3, P.YS3Qu2, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu3], [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qu2, P.YS3Qu3] ] ],
                 couplings = {(1,0,0):C.UVGC_786_1042,(1,0,1):C.UVGC_786_1043,(1,0,2):C.UVGC_786_1044,(0,0,0):C.UVGC_787_1045,(0,0,1):C.UVGC_787_1046,(0,0,2):C.UVGC_787_1047})

V_893 = CTVertex(name = 'V_893',
                 type = 'UV',
                 particles = [ P.YS3Qd1, P.YS3Qd3__tilde__, P.YS3Qu1__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu3], [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu1, P.YS3Qu3] ] ],
                 couplings = {(1,0,0):C.UVGC_786_1042,(1,0,1):C.UVGC_786_1043,(1,0,2):C.UVGC_786_1044,(0,0,0):C.UVGC_787_1045,(0,0,1):C.UVGC_787_1046,(0,0,2):C.UVGC_787_1047})

V_894 = CTVertex(name = 'V_894',
                 type = 'UV',
                 particles = [ P.YS3Qd2, P.YS3Qd3__tilde__, P.YS3Qu2__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu3], [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qu2, P.YS3Qu3] ] ],
                 couplings = {(1,0,0):C.UVGC_786_1042,(1,0,1):C.UVGC_786_1043,(1,0,2):C.UVGC_786_1044,(0,0,0):C.UVGC_787_1045,(0,0,1):C.UVGC_787_1046,(0,0,2):C.UVGC_787_1047})

V_895 = CTVertex(name = 'V_895',
                 type = 'UV',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3Qd3, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qd3, P.YS3Qu1] ], [ [P.g, P.YS3Qd3, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_809_1076,(1,0,8):C.UVGC_847_1093,(1,0,1):C.UVGC_809_1078,(1,0,7):C.UVGC_847_1094,(1,0,2):C.UVGC_809_1080,(1,0,6):C.UVGC_847_1096,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_774_1030,(0,0,8):C.UVGC_846_1088,(0,0,1):C.UVGC_774_1032,(0,0,7):C.UVGC_846_1090,(0,0,2):C.UVGC_808_1074,(0,0,6):C.UVGC_846_1092})

V_896 = CTVertex(name = 'V_896',
                 type = 'UV',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3Qd3, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qd3, P.YS3Qu2] ], [ [P.g, P.YS3Qd3, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_809_1076,(1,0,8):C.UVGC_847_1093,(1,0,1):C.UVGC_809_1078,(1,0,7):C.UVGC_847_1094,(1,0,2):C.UVGC_809_1080,(1,0,6):C.UVGC_847_1096,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_774_1030,(0,0,8):C.UVGC_846_1088,(0,0,1):C.UVGC_774_1032,(0,0,7):C.UVGC_846_1090,(0,0,2):C.UVGC_808_1074,(0,0,6):C.UVGC_846_1092})

V_897 = CTVertex(name = 'V_897',
                 type = 'UV',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,7):C.UVGC_592_896,(1,0,8):C.UVGC_592_897,(1,0,0):C.UVGC_809_1076,(1,0,4):C.UVGC_786_1042,(1,0,11):C.UVGC_847_1093,(1,0,1):C.UVGC_809_1078,(1,0,5):C.UVGC_787_1047,(1,0,10):C.UVGC_847_1094,(1,0,2):C.UVGC_809_1080,(1,0,6):C.UVGC_847_1095,(1,0,9):C.UVGC_847_1096,(0,0,3):C.UVGC_591_892,(0,0,7):C.UVGC_591_893,(0,0,8):C.UVGC_591_894,(0,0,0):C.UVGC_774_1030,(0,0,4):C.UVGC_787_1045,(0,0,11):C.UVGC_846_1088,(0,0,1):C.UVGC_774_1032,(0,0,5):C.UVGC_846_1089,(0,0,10):C.UVGC_846_1090,(0,0,2):C.UVGC_808_1074,(0,0,6):C.UVGC_846_1091,(0,0,9):C.UVGC_846_1092})

V_898 = CTVertex(name = 'V_898',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd1, P.YS3Qd3] ], [ [P.g, P.YS3Qd1, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_793_1054,(1,0,8):C.UVGC_805_1069,(1,0,1):C.UVGC_793_1056,(1,0,7):C.UVGC_805_1070,(1,0,2):C.UVGC_793_1058,(1,0,6):C.UVGC_805_1071,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_792_1048,(0,0,8):C.UVGC_804_1066,(0,0,1):C.UVGC_792_1050,(0,0,7):C.UVGC_804_1067,(0,0,2):C.UVGC_792_1052,(0,0,6):C.UVGC_804_1068})

V_899 = CTVertex(name = 'V_899',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3Qd2, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd2, P.YS3Qd3] ], [ [P.g, P.YS3Qd2, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_793_1054,(1,0,8):C.UVGC_805_1069,(1,0,1):C.UVGC_793_1056,(1,0,7):C.UVGC_805_1070,(1,0,2):C.UVGC_793_1058,(1,0,6):C.UVGC_805_1071,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_792_1048,(0,0,8):C.UVGC_804_1066,(0,0,1):C.UVGC_792_1050,(0,0,7):C.UVGC_804_1067,(0,0,2):C.UVGC_792_1052,(0,0,6):C.UVGC_804_1068})

V_900 = CTVertex(name = 'V_900',
                 type = 'UV',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3Qd3 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_303_447,(1,0,3):C.UVGC_303_448,(1,0,0):C.UVGC_774_1030,(1,0,5):C.UVGC_777_1034,(1,0,1):C.UVGC_774_1032,(1,0,4):C.UVGC_777_1035,(0,0,2):C.UVGC_303_447,(0,0,3):C.UVGC_303_448,(0,0,0):C.UVGC_774_1030,(0,0,5):C.UVGC_777_1034,(0,0,1):C.UVGC_774_1032,(0,0,4):C.UVGC_777_1035})

V_901 = CTVertex(name = 'V_901',
                 type = 'UV',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qu1, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qu1, P.YS3u1] ], [ [P.g, P.YS3Qu1, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_853_1102,(1,0,8):C.UVGC_857_1110,(1,0,1):C.UVGC_853_1104,(1,0,7):C.UVGC_857_1111,(1,0,2):C.UVGC_793_1054,(1,0,6):C.UVGC_857_1112,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_852_1097,(0,0,8):C.UVGC_856_1107,(0,0,1):C.UVGC_852_1099,(0,0,7):C.UVGC_856_1108,(0,0,2):C.UVGC_792_1048,(0,0,6):C.UVGC_856_1109})

V_902 = CTVertex(name = 'V_902',
                 type = 'UV',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qu2, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qu2], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qu2, P.YS3u1] ], [ [P.g, P.YS3Qu2, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qu2, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_853_1102,(1,0,8):C.UVGC_857_1110,(1,0,1):C.UVGC_853_1104,(1,0,7):C.UVGC_857_1111,(1,0,2):C.UVGC_793_1054,(1,0,6):C.UVGC_857_1112,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_852_1097,(0,0,8):C.UVGC_856_1107,(0,0,1):C.UVGC_852_1099,(0,0,7):C.UVGC_856_1108,(0,0,2):C.UVGC_792_1048,(0,0,6):C.UVGC_856_1109})

V_903 = CTVertex(name = 'V_903',
                 type = 'UV',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu3], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qu3, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qu3], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qu3, P.YS3u1] ], [ [P.g, P.YS3Qu3, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qu3, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_853_1102,(1,0,8):C.UVGC_857_1110,(1,0,1):C.UVGC_853_1104,(1,0,7):C.UVGC_857_1111,(1,0,2):C.UVGC_793_1054,(1,0,6):C.UVGC_857_1112,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_852_1097,(0,0,8):C.UVGC_856_1107,(0,0,1):C.UVGC_852_1099,(0,0,7):C.UVGC_856_1108,(0,0,2):C.UVGC_792_1048,(0,0,6):C.UVGC_856_1109})

V_904 = CTVertex(name = 'V_904',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qd1, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qd1, P.YS3u1] ], [ [P.g, P.YS3Qd1, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_809_1076,(1,0,8):C.UVGC_809_1077,(1,0,1):C.UVGC_809_1078,(1,0,7):C.UVGC_809_1079,(1,0,2):C.UVGC_809_1080,(1,0,6):C.UVGC_809_1081,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_774_1030,(0,0,8):C.UVGC_808_1072,(0,0,1):C.UVGC_774_1032,(0,0,7):C.UVGC_808_1073,(0,0,2):C.UVGC_808_1074,(0,0,6):C.UVGC_808_1075})

V_905 = CTVertex(name = 'V_905',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qd2, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qd2, P.YS3u1] ], [ [P.g, P.YS3Qd2, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_809_1076,(1,0,8):C.UVGC_809_1077,(1,0,1):C.UVGC_809_1078,(1,0,7):C.UVGC_809_1079,(1,0,2):C.UVGC_809_1080,(1,0,6):C.UVGC_809_1081,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_774_1030,(0,0,8):C.UVGC_808_1072,(0,0,1):C.UVGC_774_1032,(0,0,7):C.UVGC_808_1073,(0,0,2):C.UVGC_808_1074,(0,0,6):C.UVGC_808_1075})

V_906 = CTVertex(name = 'V_906',
                 type = 'UV',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qd3, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qd3, P.YS3u1] ], [ [P.g, P.YS3Qd3, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_809_1076,(1,0,8):C.UVGC_809_1077,(1,0,1):C.UVGC_809_1078,(1,0,7):C.UVGC_809_1079,(1,0,2):C.UVGC_809_1080,(1,0,6):C.UVGC_809_1081,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_774_1030,(0,0,8):C.UVGC_808_1072,(0,0,1):C.UVGC_774_1032,(0,0,7):C.UVGC_808_1073,(0,0,2):C.UVGC_808_1074,(0,0,6):C.UVGC_808_1075})

V_907 = CTVertex(name = 'V_907',
                 type = 'UV',
                 particles = [ P.YS3u1__tilde__, P.YS3u1__tilde__, P.YS3u1, P.YS3u1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3u1] ], [ [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_303_447,(1,0,3):C.UVGC_303_448,(1,0,0):C.UVGC_780_1036,(1,0,5):C.UVGC_783_1040,(1,0,1):C.UVGC_780_1038,(1,0,4):C.UVGC_783_1041,(0,0,2):C.UVGC_303_447,(0,0,3):C.UVGC_303_448,(0,0,0):C.UVGC_780_1036,(0,0,5):C.UVGC_783_1040,(0,0,1):C.UVGC_780_1038,(0,0,4):C.UVGC_783_1041})

V_908 = CTVertex(name = 'V_908',
                 type = 'UV',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qu1, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qu1, P.YS3u2] ], [ [P.g, P.YS3Qu1, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_853_1102,(1,0,8):C.UVGC_857_1110,(1,0,1):C.UVGC_853_1104,(1,0,7):C.UVGC_857_1111,(1,0,2):C.UVGC_793_1054,(1,0,6):C.UVGC_857_1112,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_852_1097,(0,0,8):C.UVGC_856_1107,(0,0,1):C.UVGC_852_1099,(0,0,7):C.UVGC_856_1108,(0,0,2):C.UVGC_792_1048,(0,0,6):C.UVGC_856_1109})

V_909 = CTVertex(name = 'V_909',
                 type = 'UV',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qu2, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qu2], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qu2, P.YS3u2] ], [ [P.g, P.YS3Qu2, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qu2, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_853_1102,(1,0,8):C.UVGC_857_1110,(1,0,1):C.UVGC_853_1104,(1,0,7):C.UVGC_857_1111,(1,0,2):C.UVGC_793_1054,(1,0,6):C.UVGC_857_1112,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_852_1097,(0,0,8):C.UVGC_856_1107,(0,0,1):C.UVGC_852_1099,(0,0,7):C.UVGC_856_1108,(0,0,2):C.UVGC_792_1048,(0,0,6):C.UVGC_856_1109})

V_910 = CTVertex(name = 'V_910',
                 type = 'UV',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu3], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qu3, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qu3], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qu3, P.YS3u2] ], [ [P.g, P.YS3Qu3, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qu3, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_853_1102,(1,0,8):C.UVGC_857_1110,(1,0,1):C.UVGC_853_1104,(1,0,7):C.UVGC_857_1111,(1,0,2):C.UVGC_793_1054,(1,0,6):C.UVGC_857_1112,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_852_1097,(0,0,8):C.UVGC_856_1107,(0,0,1):C.UVGC_852_1099,(0,0,7):C.UVGC_856_1108,(0,0,2):C.UVGC_792_1048,(0,0,6):C.UVGC_856_1109})

V_911 = CTVertex(name = 'V_911',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qd1, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qd1, P.YS3u2] ], [ [P.g, P.YS3Qd1, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_809_1076,(1,0,8):C.UVGC_809_1077,(1,0,1):C.UVGC_809_1078,(1,0,7):C.UVGC_809_1079,(1,0,2):C.UVGC_809_1080,(1,0,6):C.UVGC_809_1081,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_774_1030,(0,0,8):C.UVGC_808_1072,(0,0,1):C.UVGC_774_1032,(0,0,7):C.UVGC_808_1073,(0,0,2):C.UVGC_808_1074,(0,0,6):C.UVGC_808_1075})

V_912 = CTVertex(name = 'V_912',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qd2, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qd2, P.YS3u2] ], [ [P.g, P.YS3Qd2, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_809_1076,(1,0,8):C.UVGC_809_1077,(1,0,1):C.UVGC_809_1078,(1,0,7):C.UVGC_809_1079,(1,0,2):C.UVGC_809_1080,(1,0,6):C.UVGC_809_1081,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_774_1030,(0,0,8):C.UVGC_808_1072,(0,0,1):C.UVGC_774_1032,(0,0,7):C.UVGC_808_1073,(0,0,2):C.UVGC_808_1074,(0,0,6):C.UVGC_808_1075})

V_913 = CTVertex(name = 'V_913',
                 type = 'UV',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qd3, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qd3, P.YS3u2] ], [ [P.g, P.YS3Qd3, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_809_1076,(1,0,8):C.UVGC_809_1077,(1,0,1):C.UVGC_809_1078,(1,0,7):C.UVGC_809_1079,(1,0,2):C.UVGC_809_1080,(1,0,6):C.UVGC_809_1081,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_774_1030,(0,0,8):C.UVGC_808_1072,(0,0,1):C.UVGC_774_1032,(0,0,7):C.UVGC_808_1073,(0,0,2):C.UVGC_808_1074,(0,0,6):C.UVGC_808_1075})

V_914 = CTVertex(name = 'V_914',
                 type = 'UV',
                 particles = [ P.YS3u1__tilde__, P.YS3u1, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u1], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3u1, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3u1], [P.g, P.YS3u2] ], [ [P.g, P.YS3u1, P.YS3u2] ], [ [P.g, P.YS3u1, P.YS3u2, P.Z] ], [ [P.g, P.YS3u1, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_853_1102,(1,0,8):C.UVGC_907_1119,(1,0,1):C.UVGC_853_1104,(1,0,7):C.UVGC_907_1120,(1,0,2):C.UVGC_793_1054,(1,0,6):C.UVGC_793_1055,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_852_1097,(0,0,8):C.UVGC_906_1117,(0,0,1):C.UVGC_852_1099,(0,0,7):C.UVGC_906_1118,(0,0,2):C.UVGC_792_1048,(0,0,6):C.UVGC_792_1049})

V_915 = CTVertex(name = 'V_915',
                 type = 'UV',
                 particles = [ P.YS3u2__tilde__, P.YS3u2__tilde__, P.YS3u2, P.YS3u2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3u2] ], [ [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_303_447,(1,0,3):C.UVGC_303_448,(1,0,0):C.UVGC_780_1036,(1,0,5):C.UVGC_783_1040,(1,0,1):C.UVGC_780_1038,(1,0,4):C.UVGC_783_1041,(0,0,2):C.UVGC_303_447,(0,0,3):C.UVGC_303_448,(0,0,0):C.UVGC_780_1036,(0,0,5):C.UVGC_783_1040,(0,0,1):C.UVGC_780_1038,(0,0,4):C.UVGC_783_1041})

V_916 = CTVertex(name = 'V_916',
                 type = 'UV',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qu1, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qu1, P.YS3u3] ], [ [P.g, P.YS3Qu1, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_853_1102,(1,0,8):C.UVGC_857_1110,(1,0,1):C.UVGC_853_1104,(1,0,7):C.UVGC_857_1111,(1,0,2):C.UVGC_793_1054,(1,0,6):C.UVGC_857_1112,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_852_1097,(0,0,8):C.UVGC_856_1107,(0,0,1):C.UVGC_852_1099,(0,0,7):C.UVGC_856_1108,(0,0,2):C.UVGC_792_1048,(0,0,6):C.UVGC_856_1109})

V_917 = CTVertex(name = 'V_917',
                 type = 'UV',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qu2, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qu2], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qu2, P.YS3u3] ], [ [P.g, P.YS3Qu2, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qu2, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_853_1102,(1,0,8):C.UVGC_857_1110,(1,0,1):C.UVGC_853_1104,(1,0,7):C.UVGC_857_1111,(1,0,2):C.UVGC_793_1054,(1,0,6):C.UVGC_857_1112,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_852_1097,(0,0,8):C.UVGC_856_1107,(0,0,1):C.UVGC_852_1099,(0,0,7):C.UVGC_856_1108,(0,0,2):C.UVGC_792_1048,(0,0,6):C.UVGC_856_1109})

V_918 = CTVertex(name = 'V_918',
                 type = 'UV',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu3], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qu3, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qu3], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qu3, P.YS3u3] ], [ [P.g, P.YS3Qu3, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qu3, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_853_1102,(1,0,8):C.UVGC_857_1110,(1,0,1):C.UVGC_853_1104,(1,0,7):C.UVGC_857_1111,(1,0,2):C.UVGC_793_1054,(1,0,6):C.UVGC_857_1112,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_852_1097,(0,0,8):C.UVGC_856_1107,(0,0,1):C.UVGC_852_1099,(0,0,7):C.UVGC_856_1108,(0,0,2):C.UVGC_792_1048,(0,0,6):C.UVGC_856_1109})

V_919 = CTVertex(name = 'V_919',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qd1, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qd1, P.YS3u3] ], [ [P.g, P.YS3Qd1, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_809_1076,(1,0,8):C.UVGC_809_1077,(1,0,1):C.UVGC_809_1078,(1,0,7):C.UVGC_809_1079,(1,0,2):C.UVGC_809_1080,(1,0,6):C.UVGC_809_1081,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_774_1030,(0,0,8):C.UVGC_808_1072,(0,0,1):C.UVGC_774_1032,(0,0,7):C.UVGC_808_1073,(0,0,2):C.UVGC_808_1074,(0,0,6):C.UVGC_808_1075})

V_920 = CTVertex(name = 'V_920',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qd2, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qd2, P.YS3u3] ], [ [P.g, P.YS3Qd2, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_809_1076,(1,0,8):C.UVGC_809_1077,(1,0,1):C.UVGC_809_1078,(1,0,7):C.UVGC_809_1079,(1,0,2):C.UVGC_809_1080,(1,0,6):C.UVGC_809_1081,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_774_1030,(0,0,8):C.UVGC_808_1072,(0,0,1):C.UVGC_774_1032,(0,0,7):C.UVGC_808_1073,(0,0,2):C.UVGC_808_1074,(0,0,6):C.UVGC_808_1075})

V_921 = CTVertex(name = 'V_921',
                 type = 'UV',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qd3, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qd3, P.YS3u3] ], [ [P.g, P.YS3Qd3, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_809_1076,(1,0,8):C.UVGC_809_1077,(1,0,1):C.UVGC_809_1078,(1,0,7):C.UVGC_809_1079,(1,0,2):C.UVGC_809_1080,(1,0,6):C.UVGC_809_1081,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_774_1030,(0,0,8):C.UVGC_808_1072,(0,0,1):C.UVGC_774_1032,(0,0,7):C.UVGC_808_1073,(0,0,2):C.UVGC_808_1074,(0,0,6):C.UVGC_808_1075})

V_922 = CTVertex(name = 'V_922',
                 type = 'UV',
                 particles = [ P.YS3u1__tilde__, P.YS3u1, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u1], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3u1, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3u1], [P.g, P.YS3u3] ], [ [P.g, P.YS3u1, P.YS3u3] ], [ [P.g, P.YS3u1, P.YS3u3, P.Z] ], [ [P.g, P.YS3u1, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_853_1102,(1,0,8):C.UVGC_907_1119,(1,0,1):C.UVGC_853_1104,(1,0,7):C.UVGC_907_1120,(1,0,2):C.UVGC_793_1054,(1,0,6):C.UVGC_793_1055,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_852_1097,(0,0,8):C.UVGC_906_1117,(0,0,1):C.UVGC_852_1099,(0,0,7):C.UVGC_906_1118,(0,0,2):C.UVGC_792_1048,(0,0,6):C.UVGC_792_1049})

V_923 = CTVertex(name = 'V_923',
                 type = 'UV',
                 particles = [ P.YS3u2__tilde__, P.YS3u2, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u2], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3u2, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3u2], [P.g, P.YS3u3] ], [ [P.g, P.YS3u2, P.YS3u3] ], [ [P.g, P.YS3u2, P.YS3u3, P.Z] ], [ [P.g, P.YS3u2, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_853_1102,(1,0,8):C.UVGC_907_1119,(1,0,1):C.UVGC_853_1104,(1,0,7):C.UVGC_907_1120,(1,0,2):C.UVGC_793_1054,(1,0,6):C.UVGC_793_1055,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_852_1097,(0,0,8):C.UVGC_906_1117,(0,0,1):C.UVGC_852_1099,(0,0,7):C.UVGC_906_1118,(0,0,2):C.UVGC_792_1048,(0,0,6):C.UVGC_792_1049})

V_924 = CTVertex(name = 'V_924',
                 type = 'UV',
                 particles = [ P.YS3u3__tilde__, P.YS3u3__tilde__, P.YS3u3, P.YS3u3 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3u3] ], [ [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_303_447,(1,0,3):C.UVGC_303_448,(1,0,0):C.UVGC_780_1036,(1,0,5):C.UVGC_783_1040,(1,0,1):C.UVGC_780_1038,(1,0,4):C.UVGC_783_1041,(0,0,2):C.UVGC_303_447,(0,0,3):C.UVGC_303_448,(0,0,0):C.UVGC_780_1036,(0,0,5):C.UVGC_783_1040,(0,0,1):C.UVGC_780_1038,(0,0,4):C.UVGC_783_1041})

V_925 = CTVertex(name = 'V_925',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3d1, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3d1, P.YS3Qu1] ], [ [P.g, P.YS3d1, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_809_1076,(1,0,8):C.UVGC_841_1085,(1,0,1):C.UVGC_809_1078,(1,0,7):C.UVGC_841_1086,(1,0,2):C.UVGC_809_1080,(1,0,6):C.UVGC_841_1087,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_774_1030,(0,0,8):C.UVGC_840_1082,(0,0,1):C.UVGC_774_1032,(0,0,7):C.UVGC_840_1083,(0,0,2):C.UVGC_808_1074,(0,0,6):C.UVGC_840_1084})

V_926 = CTVertex(name = 'V_926',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3d1, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3d1, P.YS3Qu2] ], [ [P.g, P.YS3d1, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_809_1076,(1,0,8):C.UVGC_841_1085,(1,0,1):C.UVGC_809_1078,(1,0,7):C.UVGC_841_1086,(1,0,2):C.UVGC_809_1080,(1,0,6):C.UVGC_841_1087,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_774_1030,(0,0,8):C.UVGC_840_1082,(0,0,1):C.UVGC_774_1032,(0,0,7):C.UVGC_840_1083,(0,0,2):C.UVGC_808_1074,(0,0,6):C.UVGC_840_1084})

V_927 = CTVertex(name = 'V_927',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3d1, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3d1, P.YS3Qu3] ], [ [P.g, P.YS3d1, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_809_1076,(1,0,8):C.UVGC_841_1085,(1,0,1):C.UVGC_809_1078,(1,0,7):C.UVGC_841_1086,(1,0,2):C.UVGC_809_1080,(1,0,6):C.UVGC_841_1087,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_774_1030,(0,0,8):C.UVGC_840_1082,(0,0,1):C.UVGC_774_1032,(0,0,7):C.UVGC_840_1083,(0,0,2):C.UVGC_808_1074,(0,0,6):C.UVGC_840_1084})

V_928 = CTVertex(name = 'V_928',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qd1] ], [ [P.a, P.g, P.YS3d1, P.YS3Qd1] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qd1] ], [ [P.g, P.YS3d1, P.YS3Qd1] ], [ [P.g, P.YS3d1, P.YS3Qd1, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qd1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_793_1054,(1,0,8):C.UVGC_799_1063,(1,0,1):C.UVGC_793_1056,(1,0,7):C.UVGC_799_1064,(1,0,2):C.UVGC_793_1058,(1,0,6):C.UVGC_799_1065,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_792_1048,(0,0,8):C.UVGC_798_1060,(0,0,1):C.UVGC_792_1050,(0,0,7):C.UVGC_798_1061,(0,0,2):C.UVGC_792_1052,(0,0,6):C.UVGC_798_1062})

V_929 = CTVertex(name = 'V_929',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qd2] ], [ [P.a, P.g, P.YS3d1, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qd2] ], [ [P.g, P.YS3d1, P.YS3Qd2] ], [ [P.g, P.YS3d1, P.YS3Qd2, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_793_1054,(1,0,8):C.UVGC_799_1063,(1,0,1):C.UVGC_793_1056,(1,0,7):C.UVGC_799_1064,(1,0,2):C.UVGC_793_1058,(1,0,6):C.UVGC_799_1065,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_792_1048,(0,0,8):C.UVGC_798_1060,(0,0,1):C.UVGC_792_1050,(0,0,7):C.UVGC_798_1061,(0,0,2):C.UVGC_792_1052,(0,0,6):C.UVGC_798_1062})

V_930 = CTVertex(name = 'V_930',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3d1, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3d1, P.YS3Qd3] ], [ [P.g, P.YS3d1, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_793_1054,(1,0,8):C.UVGC_799_1063,(1,0,1):C.UVGC_793_1056,(1,0,7):C.UVGC_799_1064,(1,0,2):C.UVGC_793_1058,(1,0,6):C.UVGC_799_1065,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_792_1048,(0,0,8):C.UVGC_798_1060,(0,0,1):C.UVGC_792_1050,(0,0,7):C.UVGC_798_1061,(0,0,2):C.UVGC_792_1052,(0,0,6):C.UVGC_798_1062})

V_931 = CTVertex(name = 'V_931',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3d1, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3u1] ], [ [P.g, P.YS3d1, P.YS3u1] ], [ [P.g, P.YS3d1, P.YS3u1, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_809_1076,(1,0,8):C.UVGC_901_1114,(1,0,1):C.UVGC_809_1078,(1,0,7):C.UVGC_901_1115,(1,0,2):C.UVGC_809_1080,(1,0,6):C.UVGC_901_1116,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_774_1030,(0,0,8):C.UVGC_774_1031,(0,0,1):C.UVGC_774_1032,(0,0,7):C.UVGC_774_1033,(0,0,2):C.UVGC_808_1074,(0,0,6):C.UVGC_900_1113})

V_932 = CTVertex(name = 'V_932',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3d1, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3u2] ], [ [P.g, P.YS3d1, P.YS3u2] ], [ [P.g, P.YS3d1, P.YS3u2, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_809_1076,(1,0,8):C.UVGC_901_1114,(1,0,1):C.UVGC_809_1078,(1,0,7):C.UVGC_901_1115,(1,0,2):C.UVGC_809_1080,(1,0,6):C.UVGC_901_1116,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_774_1030,(0,0,8):C.UVGC_774_1031,(0,0,1):C.UVGC_774_1032,(0,0,7):C.UVGC_774_1033,(0,0,2):C.UVGC_808_1074,(0,0,6):C.UVGC_900_1113})

V_933 = CTVertex(name = 'V_933',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3d1, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3u3] ], [ [P.g, P.YS3d1, P.YS3u3] ], [ [P.g, P.YS3d1, P.YS3u3, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_809_1076,(1,0,8):C.UVGC_901_1114,(1,0,1):C.UVGC_809_1078,(1,0,7):C.UVGC_901_1115,(1,0,2):C.UVGC_809_1080,(1,0,6):C.UVGC_901_1116,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_774_1030,(0,0,8):C.UVGC_774_1031,(0,0,1):C.UVGC_774_1032,(0,0,7):C.UVGC_774_1033,(0,0,2):C.UVGC_808_1074,(0,0,6):C.UVGC_900_1113})

V_934 = CTVertex(name = 'V_934',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1__tilde__, P.YS3d1, P.YS3d1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1] ], [ [P.g] ], [ [P.g, P.YS3d1] ], [ [P.g, P.YS3d1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_303_447,(1,0,3):C.UVGC_303_448,(1,0,0):C.UVGC_774_1030,(1,0,5):C.UVGC_774_1031,(1,0,1):C.UVGC_774_1032,(1,0,4):C.UVGC_774_1033,(0,0,2):C.UVGC_303_447,(0,0,3):C.UVGC_303_448,(0,0,0):C.UVGC_774_1030,(0,0,5):C.UVGC_774_1031,(0,0,1):C.UVGC_774_1032,(0,0,4):C.UVGC_774_1033})

V_935 = CTVertex(name = 'V_935',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3d2, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3d2, P.YS3Qu1] ], [ [P.g, P.YS3d2, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_809_1076,(1,0,8):C.UVGC_841_1085,(1,0,1):C.UVGC_809_1078,(1,0,7):C.UVGC_841_1086,(1,0,2):C.UVGC_809_1080,(1,0,6):C.UVGC_841_1087,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_774_1030,(0,0,8):C.UVGC_840_1082,(0,0,1):C.UVGC_774_1032,(0,0,7):C.UVGC_840_1083,(0,0,2):C.UVGC_808_1074,(0,0,6):C.UVGC_840_1084})

V_936 = CTVertex(name = 'V_936',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3d2, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3d2, P.YS3Qu2] ], [ [P.g, P.YS3d2, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_809_1076,(1,0,8):C.UVGC_841_1085,(1,0,1):C.UVGC_809_1078,(1,0,7):C.UVGC_841_1086,(1,0,2):C.UVGC_809_1080,(1,0,6):C.UVGC_841_1087,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_774_1030,(0,0,8):C.UVGC_840_1082,(0,0,1):C.UVGC_774_1032,(0,0,7):C.UVGC_840_1083,(0,0,2):C.UVGC_808_1074,(0,0,6):C.UVGC_840_1084})

V_937 = CTVertex(name = 'V_937',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3d2, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3d2, P.YS3Qu3] ], [ [P.g, P.YS3d2, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_809_1076,(1,0,8):C.UVGC_841_1085,(1,0,1):C.UVGC_809_1078,(1,0,7):C.UVGC_841_1086,(1,0,2):C.UVGC_809_1080,(1,0,6):C.UVGC_841_1087,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_774_1030,(0,0,8):C.UVGC_840_1082,(0,0,1):C.UVGC_774_1032,(0,0,7):C.UVGC_840_1083,(0,0,2):C.UVGC_808_1074,(0,0,6):C.UVGC_840_1084})

V_938 = CTVertex(name = 'V_938',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qd1] ], [ [P.a, P.g, P.YS3d2, P.YS3Qd1] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qd1] ], [ [P.g, P.YS3d2, P.YS3Qd1] ], [ [P.g, P.YS3d2, P.YS3Qd1, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qd1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_793_1054,(1,0,8):C.UVGC_799_1063,(1,0,1):C.UVGC_793_1056,(1,0,7):C.UVGC_799_1064,(1,0,2):C.UVGC_793_1058,(1,0,6):C.UVGC_799_1065,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_792_1048,(0,0,8):C.UVGC_798_1060,(0,0,1):C.UVGC_792_1050,(0,0,7):C.UVGC_798_1061,(0,0,2):C.UVGC_792_1052,(0,0,6):C.UVGC_798_1062})

V_939 = CTVertex(name = 'V_939',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qd2] ], [ [P.a, P.g, P.YS3d2, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qd2] ], [ [P.g, P.YS3d2, P.YS3Qd2] ], [ [P.g, P.YS3d2, P.YS3Qd2, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_793_1054,(1,0,8):C.UVGC_799_1063,(1,0,1):C.UVGC_793_1056,(1,0,7):C.UVGC_799_1064,(1,0,2):C.UVGC_793_1058,(1,0,6):C.UVGC_799_1065,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_792_1048,(0,0,8):C.UVGC_798_1060,(0,0,1):C.UVGC_792_1050,(0,0,7):C.UVGC_798_1061,(0,0,2):C.UVGC_792_1052,(0,0,6):C.UVGC_798_1062})

V_940 = CTVertex(name = 'V_940',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3d2, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3d2, P.YS3Qd3] ], [ [P.g, P.YS3d2, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_793_1054,(1,0,8):C.UVGC_799_1063,(1,0,1):C.UVGC_793_1056,(1,0,7):C.UVGC_799_1064,(1,0,2):C.UVGC_793_1058,(1,0,6):C.UVGC_799_1065,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_792_1048,(0,0,8):C.UVGC_798_1060,(0,0,1):C.UVGC_792_1050,(0,0,7):C.UVGC_798_1061,(0,0,2):C.UVGC_792_1052,(0,0,6):C.UVGC_798_1062})

V_941 = CTVertex(name = 'V_941',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3d2, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3u1] ], [ [P.g, P.YS3d2, P.YS3u1] ], [ [P.g, P.YS3d2, P.YS3u1, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_809_1076,(1,0,8):C.UVGC_901_1114,(1,0,1):C.UVGC_809_1078,(1,0,7):C.UVGC_901_1115,(1,0,2):C.UVGC_809_1080,(1,0,6):C.UVGC_901_1116,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_774_1030,(0,0,8):C.UVGC_774_1031,(0,0,1):C.UVGC_774_1032,(0,0,7):C.UVGC_774_1033,(0,0,2):C.UVGC_808_1074,(0,0,6):C.UVGC_900_1113})

V_942 = CTVertex(name = 'V_942',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3d2, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3u2] ], [ [P.g, P.YS3d2, P.YS3u2] ], [ [P.g, P.YS3d2, P.YS3u2, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_809_1076,(1,0,8):C.UVGC_901_1114,(1,0,1):C.UVGC_809_1078,(1,0,7):C.UVGC_901_1115,(1,0,2):C.UVGC_809_1080,(1,0,6):C.UVGC_901_1116,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_774_1030,(0,0,8):C.UVGC_774_1031,(0,0,1):C.UVGC_774_1032,(0,0,7):C.UVGC_774_1033,(0,0,2):C.UVGC_808_1074,(0,0,6):C.UVGC_900_1113})

V_943 = CTVertex(name = 'V_943',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3d2, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3u3] ], [ [P.g, P.YS3d2, P.YS3u3] ], [ [P.g, P.YS3d2, P.YS3u3, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_809_1076,(1,0,8):C.UVGC_901_1114,(1,0,1):C.UVGC_809_1078,(1,0,7):C.UVGC_901_1115,(1,0,2):C.UVGC_809_1080,(1,0,6):C.UVGC_901_1116,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_774_1030,(0,0,8):C.UVGC_774_1031,(0,0,1):C.UVGC_774_1032,(0,0,7):C.UVGC_774_1033,(0,0,2):C.UVGC_808_1074,(0,0,6):C.UVGC_900_1113})

V_944 = CTVertex(name = 'V_944',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3d2] ], [ [P.a, P.g, P.YS3d1, P.YS3d2] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3d2] ], [ [P.g, P.YS3d1, P.YS3d2] ], [ [P.g, P.YS3d1, P.YS3d2, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3d2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_793_1054,(1,0,8):C.UVGC_793_1055,(1,0,1):C.UVGC_793_1056,(1,0,7):C.UVGC_793_1057,(1,0,2):C.UVGC_793_1058,(1,0,6):C.UVGC_793_1059,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_792_1048,(0,0,8):C.UVGC_792_1049,(0,0,1):C.UVGC_792_1050,(0,0,7):C.UVGC_792_1051,(0,0,2):C.UVGC_792_1052,(0,0,6):C.UVGC_792_1053})

V_945 = CTVertex(name = 'V_945',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2__tilde__, P.YS3d2, P.YS3d2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2] ], [ [P.g] ], [ [P.g, P.YS3d2] ], [ [P.g, P.YS3d2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_303_447,(1,0,3):C.UVGC_303_448,(1,0,0):C.UVGC_774_1030,(1,0,5):C.UVGC_774_1031,(1,0,1):C.UVGC_774_1032,(1,0,4):C.UVGC_774_1033,(0,0,2):C.UVGC_303_447,(0,0,3):C.UVGC_303_448,(0,0,0):C.UVGC_774_1030,(0,0,5):C.UVGC_774_1031,(0,0,1):C.UVGC_774_1032,(0,0,4):C.UVGC_774_1033})

V_946 = CTVertex(name = 'V_946',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3d3, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3d3, P.YS3Qu1] ], [ [P.g, P.YS3d3, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_809_1076,(1,0,8):C.UVGC_841_1085,(1,0,1):C.UVGC_809_1078,(1,0,7):C.UVGC_841_1086,(1,0,2):C.UVGC_809_1080,(1,0,6):C.UVGC_841_1087,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_774_1030,(0,0,8):C.UVGC_840_1082,(0,0,1):C.UVGC_774_1032,(0,0,7):C.UVGC_840_1083,(0,0,2):C.UVGC_808_1074,(0,0,6):C.UVGC_840_1084})

V_947 = CTVertex(name = 'V_947',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3d3, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3d3, P.YS3Qu2] ], [ [P.g, P.YS3d3, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_809_1076,(1,0,8):C.UVGC_841_1085,(1,0,1):C.UVGC_809_1078,(1,0,7):C.UVGC_841_1086,(1,0,2):C.UVGC_809_1080,(1,0,6):C.UVGC_841_1087,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_774_1030,(0,0,8):C.UVGC_840_1082,(0,0,1):C.UVGC_774_1032,(0,0,7):C.UVGC_840_1083,(0,0,2):C.UVGC_808_1074,(0,0,6):C.UVGC_840_1084})

V_948 = CTVertex(name = 'V_948',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3d3, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3d3, P.YS3Qu3] ], [ [P.g, P.YS3d3, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_809_1076,(1,0,8):C.UVGC_841_1085,(1,0,1):C.UVGC_809_1078,(1,0,7):C.UVGC_841_1086,(1,0,2):C.UVGC_809_1080,(1,0,6):C.UVGC_841_1087,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_774_1030,(0,0,8):C.UVGC_840_1082,(0,0,1):C.UVGC_774_1032,(0,0,7):C.UVGC_840_1083,(0,0,2):C.UVGC_808_1074,(0,0,6):C.UVGC_840_1084})

V_949 = CTVertex(name = 'V_949',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qd1] ], [ [P.a, P.g, P.YS3d3, P.YS3Qd1] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qd1] ], [ [P.g, P.YS3d3, P.YS3Qd1] ], [ [P.g, P.YS3d3, P.YS3Qd1, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qd1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_793_1054,(1,0,8):C.UVGC_799_1063,(1,0,1):C.UVGC_793_1056,(1,0,7):C.UVGC_799_1064,(1,0,2):C.UVGC_793_1058,(1,0,6):C.UVGC_799_1065,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_792_1048,(0,0,8):C.UVGC_798_1060,(0,0,1):C.UVGC_792_1050,(0,0,7):C.UVGC_798_1061,(0,0,2):C.UVGC_792_1052,(0,0,6):C.UVGC_798_1062})

V_950 = CTVertex(name = 'V_950',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qd2] ], [ [P.a, P.g, P.YS3d3, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qd2] ], [ [P.g, P.YS3d3, P.YS3Qd2] ], [ [P.g, P.YS3d3, P.YS3Qd2, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_793_1054,(1,0,8):C.UVGC_799_1063,(1,0,1):C.UVGC_793_1056,(1,0,7):C.UVGC_799_1064,(1,0,2):C.UVGC_793_1058,(1,0,6):C.UVGC_799_1065,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_792_1048,(0,0,8):C.UVGC_798_1060,(0,0,1):C.UVGC_792_1050,(0,0,7):C.UVGC_798_1061,(0,0,2):C.UVGC_792_1052,(0,0,6):C.UVGC_798_1062})

V_951 = CTVertex(name = 'V_951',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3d3, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3d3, P.YS3Qd3] ], [ [P.g, P.YS3d3, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_793_1054,(1,0,8):C.UVGC_799_1063,(1,0,1):C.UVGC_793_1056,(1,0,7):C.UVGC_799_1064,(1,0,2):C.UVGC_793_1058,(1,0,6):C.UVGC_799_1065,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_792_1048,(0,0,8):C.UVGC_798_1060,(0,0,1):C.UVGC_792_1050,(0,0,7):C.UVGC_798_1061,(0,0,2):C.UVGC_792_1052,(0,0,6):C.UVGC_798_1062})

V_952 = CTVertex(name = 'V_952',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3d3, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3u1] ], [ [P.g, P.YS3d3, P.YS3u1] ], [ [P.g, P.YS3d3, P.YS3u1, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_809_1076,(1,0,8):C.UVGC_901_1114,(1,0,1):C.UVGC_809_1078,(1,0,7):C.UVGC_901_1115,(1,0,2):C.UVGC_809_1080,(1,0,6):C.UVGC_901_1116,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_774_1030,(0,0,8):C.UVGC_774_1031,(0,0,1):C.UVGC_774_1032,(0,0,7):C.UVGC_774_1033,(0,0,2):C.UVGC_808_1074,(0,0,6):C.UVGC_900_1113})

V_953 = CTVertex(name = 'V_953',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3d3, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3u2] ], [ [P.g, P.YS3d3, P.YS3u2] ], [ [P.g, P.YS3d3, P.YS3u2, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_809_1076,(1,0,8):C.UVGC_901_1114,(1,0,1):C.UVGC_809_1078,(1,0,7):C.UVGC_901_1115,(1,0,2):C.UVGC_809_1080,(1,0,6):C.UVGC_901_1116,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_774_1030,(0,0,8):C.UVGC_774_1031,(0,0,1):C.UVGC_774_1032,(0,0,7):C.UVGC_774_1033,(0,0,2):C.UVGC_808_1074,(0,0,6):C.UVGC_900_1113})

V_954 = CTVertex(name = 'V_954',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3d3, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3u3] ], [ [P.g, P.YS3d3, P.YS3u3] ], [ [P.g, P.YS3d3, P.YS3u3, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_809_1076,(1,0,8):C.UVGC_901_1114,(1,0,1):C.UVGC_809_1078,(1,0,7):C.UVGC_901_1115,(1,0,2):C.UVGC_809_1080,(1,0,6):C.UVGC_901_1116,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_774_1030,(0,0,8):C.UVGC_774_1031,(0,0,1):C.UVGC_774_1032,(0,0,7):C.UVGC_774_1033,(0,0,2):C.UVGC_808_1074,(0,0,6):C.UVGC_900_1113})

V_955 = CTVertex(name = 'V_955',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3d3] ], [ [P.a, P.g, P.YS3d1, P.YS3d3] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3d3] ], [ [P.g, P.YS3d1, P.YS3d3] ], [ [P.g, P.YS3d1, P.YS3d3, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3d3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_793_1054,(1,0,8):C.UVGC_793_1055,(1,0,1):C.UVGC_793_1056,(1,0,7):C.UVGC_793_1057,(1,0,2):C.UVGC_793_1058,(1,0,6):C.UVGC_793_1059,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_792_1048,(0,0,8):C.UVGC_792_1049,(0,0,1):C.UVGC_792_1050,(0,0,7):C.UVGC_792_1051,(0,0,2):C.UVGC_792_1052,(0,0,6):C.UVGC_792_1053})

V_956 = CTVertex(name = 'V_956',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3d3] ], [ [P.a, P.g, P.YS3d2, P.YS3d3] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3d3] ], [ [P.g, P.YS3d2, P.YS3d3] ], [ [P.g, P.YS3d2, P.YS3d3, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3d3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_592_895,(1,0,4):C.UVGC_592_896,(1,0,5):C.UVGC_592_897,(1,0,0):C.UVGC_793_1054,(1,0,8):C.UVGC_793_1055,(1,0,1):C.UVGC_793_1056,(1,0,7):C.UVGC_793_1057,(1,0,2):C.UVGC_793_1058,(1,0,6):C.UVGC_793_1059,(0,0,3):C.UVGC_591_892,(0,0,4):C.UVGC_591_893,(0,0,5):C.UVGC_591_894,(0,0,0):C.UVGC_792_1048,(0,0,8):C.UVGC_792_1049,(0,0,1):C.UVGC_792_1050,(0,0,7):C.UVGC_792_1051,(0,0,2):C.UVGC_792_1052,(0,0,6):C.UVGC_792_1053})

V_957 = CTVertex(name = 'V_957',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3__tilde__, P.YS3d3, P.YS3d3 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3] ], [ [P.g] ], [ [P.g, P.YS3d3] ], [ [P.g, P.YS3d3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_303_447,(1,0,3):C.UVGC_303_448,(1,0,0):C.UVGC_774_1030,(1,0,5):C.UVGC_774_1031,(1,0,1):C.UVGC_774_1032,(1,0,4):C.UVGC_774_1033,(0,0,2):C.UVGC_303_447,(0,0,3):C.UVGC_303_448,(0,0,0):C.UVGC_774_1030,(0,0,5):C.UVGC_774_1031,(0,0,1):C.UVGC_774_1032,(0,0,4):C.UVGC_774_1033})

