# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.1.0 for Mac OS X ARM (64-bit) (June 16, 2022)
# Date: Fri 22 Mar 2024 18:23:35


from __future__ import division
from object_library import all_particles, Particle
import parameters as Param

import propagators as Prop

a = Particle(pdg_code = 22,
             name = 'a',
             antiname = 'a',
             spin = 3,
             color = 1,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'a',
             antitexname = 'a',
             charge = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

Z = Particle(pdg_code = 23,
             name = 'Z',
             antiname = 'Z',
             spin = 3,
             color = 1,
             mass = Param.MZ,
             width = Param.WZ,
             texname = 'Z',
             antitexname = 'Z',
             charge = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

W__plus__ = Particle(pdg_code = 24,
                     name = 'W+',
                     antiname = 'W-',
                     spin = 3,
                     color = 1,
                     mass = Param.MW,
                     width = Param.WW,
                     texname = 'W+',
                     antitexname = 'W-',
                     charge = 1,
                     GhostNumber = 0,
                     LeptonNumber = 0,
                     Y = 0)

W__minus__ = W__plus__.anti()

g = Particle(pdg_code = 21,
             name = 'g',
             antiname = 'g',
             spin = 3,
             color = 8,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'g',
             antitexname = 'g',
             charge = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

ghA = Particle(pdg_code = 9000001,
               name = 'ghA',
               antiname = 'ghA~',
               spin = -1,
               color = 1,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'ghA',
               antitexname = 'ghA~',
               charge = 0,
               GhostNumber = 1,
               LeptonNumber = 0,
               Y = 0)

ghA__tilde__ = ghA.anti()

ghZ = Particle(pdg_code = 9000002,
               name = 'ghZ',
               antiname = 'ghZ~',
               spin = -1,
               color = 1,
               mass = Param.MZ,
               width = Param.WZ,
               texname = 'ghZ',
               antitexname = 'ghZ~',
               charge = 0,
               GhostNumber = 1,
               LeptonNumber = 0,
               Y = 0)

ghZ__tilde__ = ghZ.anti()

ghWp = Particle(pdg_code = 9000003,
                name = 'ghWp',
                antiname = 'ghWp~',
                spin = -1,
                color = 1,
                mass = Param.MW,
                width = Param.WW,
                texname = 'ghWp',
                antitexname = 'ghWp~',
                charge = 1,
                GhostNumber = 1,
                LeptonNumber = 0,
                Y = 0)

ghWp__tilde__ = ghWp.anti()

ghWm = Particle(pdg_code = 9000004,
                name = 'ghWm',
                antiname = 'ghWm~',
                spin = -1,
                color = 1,
                mass = Param.MW,
                width = Param.WW,
                texname = 'ghWm',
                antitexname = 'ghWm~',
                charge = -1,
                GhostNumber = 1,
                LeptonNumber = 0,
                Y = 0)

ghWm__tilde__ = ghWm.anti()

ghG = Particle(pdg_code = 82,
               name = 'ghG',
               antiname = 'ghG~',
               spin = -1,
               color = 8,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'ghG',
               antitexname = 'ghG~',
               charge = 0,
               GhostNumber = 1,
               LeptonNumber = 0,
               Y = 0)

ghG__tilde__ = ghG.anti()

ve = Particle(pdg_code = 12,
              name = 've',
              antiname = 've~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 've',
              antitexname = 've~',
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 1,
              Y = 0)

ve__tilde__ = ve.anti()

vm = Particle(pdg_code = 14,
              name = 'vm',
              antiname = 'vm~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 'vm',
              antitexname = 'vm~',
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 1,
              Y = 0)

vm__tilde__ = vm.anti()

vt = Particle(pdg_code = 16,
              name = 'vt',
              antiname = 'vt~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 'vt',
              antitexname = 'vt~',
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 1,
              Y = 0)

vt__tilde__ = vt.anti()

e__minus__ = Particle(pdg_code = 11,
                      name = 'e-',
                      antiname = 'e+',
                      spin = 2,
                      color = 1,
                      mass = Param.Me,
                      width = Param.ZERO,
                      texname = 'e-',
                      antitexname = 'e+',
                      charge = -1,
                      GhostNumber = 0,
                      LeptonNumber = 1,
                      Y = 0)

e__plus__ = e__minus__.anti()

mu__minus__ = Particle(pdg_code = 13,
                       name = 'mu-',
                       antiname = 'mu+',
                       spin = 2,
                       color = 1,
                       mass = Param.MMU,
                       width = Param.ZERO,
                       texname = 'mu-',
                       antitexname = 'mu+',
                       charge = -1,
                       GhostNumber = 0,
                       LeptonNumber = 1,
                       Y = 0)

mu__plus__ = mu__minus__.anti()

ta__minus__ = Particle(pdg_code = 15,
                       name = 'ta-',
                       antiname = 'ta+',
                       spin = 2,
                       color = 1,
                       mass = Param.MTA,
                       width = Param.ZERO,
                       texname = 'ta-',
                       antitexname = 'ta+',
                       charge = -1,
                       GhostNumber = 0,
                       LeptonNumber = 1,
                       Y = 0)

ta__plus__ = ta__minus__.anti()

u = Particle(pdg_code = 2,
             name = 'u',
             antiname = 'u~',
             spin = 2,
             color = 3,
             mass = Param.MU,
             width = Param.ZERO,
             texname = 'u',
             antitexname = 'u~',
             charge = 2/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

u__tilde__ = u.anti()

c = Particle(pdg_code = 4,
             name = 'c',
             antiname = 'c~',
             spin = 2,
             color = 3,
             mass = Param.MC,
             width = Param.ZERO,
             texname = 'c',
             antitexname = 'c~',
             charge = 2/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

c__tilde__ = c.anti()

t = Particle(pdg_code = 6,
             name = 't',
             antiname = 't~',
             spin = 2,
             color = 3,
             mass = Param.MT,
             width = Param.WT,
             texname = 't',
             antitexname = 't~',
             charge = 2/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

t__tilde__ = t.anti()

d = Particle(pdg_code = 1,
             name = 'd',
             antiname = 'd~',
             spin = 2,
             color = 3,
             mass = Param.MD,
             width = Param.ZERO,
             texname = 'd',
             antitexname = 'd~',
             charge = -1/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

d__tilde__ = d.anti()

s = Particle(pdg_code = 3,
             name = 's',
             antiname = 's~',
             spin = 2,
             color = 3,
             mass = Param.MS,
             width = Param.ZERO,
             texname = 's',
             antitexname = 's~',
             charge = -1/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

s__tilde__ = s.anti()

b = Particle(pdg_code = 5,
             name = 'b',
             antiname = 'b~',
             spin = 2,
             color = 3,
             mass = Param.MB,
             width = Param.ZERO,
             texname = 'b',
             antitexname = 'b~',
             charge = -1/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

b__tilde__ = b.anti()

H = Particle(pdg_code = 25,
             name = 'H',
             antiname = 'H',
             spin = 1,
             color = 1,
             mass = Param.MH,
             width = Param.WH,
             texname = 'H',
             antitexname = 'H',
             charge = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

G0 = Particle(pdg_code = 250,
              name = 'G0',
              antiname = 'G0',
              spin = 1,
              color = 1,
              mass = Param.MZ,
              width = Param.WZ,
              texname = 'G0',
              antitexname = 'G0',
              goldstone = True,
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 0,
              Y = 0)

G__plus__ = Particle(pdg_code = 251,
                     name = 'G+',
                     antiname = 'G-',
                     spin = 1,
                     color = 1,
                     mass = Param.MW,
                     width = Param.WW,
                     texname = 'G+',
                     antitexname = 'G-',
                     goldstone = True,
                     charge = 1,
                     GhostNumber = 0,
                     LeptonNumber = 0,
                     Y = 0)

G__minus__ = G__plus__.anti()

Xs = Particle(pdg_code = 51,
              name = 'Xs',
              antiname = 'Xs',
              spin = 1,
              color = 1,
              mass = Param.MXs,
              width = Param.ZERO,
              texname = 'Xs',
              antitexname = 'Xs',
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 0,
              Y = 0)

Xm = Particle(pdg_code = 52,
              name = 'Xm',
              antiname = 'Xm',
              spin = 2,
              color = 1,
              mass = Param.MXm,
              width = Param.ZERO,
              texname = 'Xm',
              antitexname = 'Xm',
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 0,
              Y = 0)

Xv = Particle(pdg_code = 53,
              name = 'Xv',
              antiname = 'Xv',
              spin = 3,
              color = 1,
              mass = Param.MXv,
              width = Param.ZERO,
              texname = 'Xv',
              antitexname = 'Xv',
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 0,
              Y = 0)

Xd = Particle(pdg_code = 57,
              name = 'Xd',
              antiname = 'Xd~',
              spin = 2,
              color = 1,
              mass = Param.MXd,
              width = Param.ZERO,
              texname = 'Xd',
              antitexname = 'Xd~',
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 0,
              Y = 0)

Xd__tilde__ = Xd.anti()

Xc = Particle(pdg_code = 56,
              name = 'Xc',
              antiname = 'Xc~',
              spin = 1,
              color = 1,
              mass = Param.MXc,
              width = Param.ZERO,
              texname = 'Xc',
              antitexname = 'Xc~',
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 0,
              Y = 0)

Xc__tilde__ = Xc.anti()

Xw = Particle(pdg_code = 58,
              name = 'Xw',
              antiname = 'Xw~',
              spin = 3,
              color = 1,
              mass = Param.MXw,
              width = Param.ZERO,
              texname = 'Xw',
              antitexname = 'Xw~',
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 0,
              Y = 0)

Xw__tilde__ = Xw.anti()

YS3Qu1 = Particle(pdg_code = 1000002,
                  name = 'YS3Qu1',
                  antiname = 'YS3Qu1~',
                  spin = 1,
                  color = 3,
                  mass = Param.MYS3Qu1,
                  width = Param.WYS3Qu1,
                  texname = 'YS3Qu1',
                  antitexname = 'YS3Qu1~',
                  charge = 2/3,
                  GhostNumber = 0,
                  LeptonNumber = 0,
                  Y = 0)

YS3Qu1__tilde__ = YS3Qu1.anti()

YS3Qu2 = Particle(pdg_code = 1000004,
                  name = 'YS3Qu2',
                  antiname = 'YS3Qu2~',
                  spin = 1,
                  color = 3,
                  mass = Param.MYS3Qu2,
                  width = Param.WYS3Qu2,
                  texname = 'YS3Qu2',
                  antitexname = 'YS3Qu2~',
                  charge = 2/3,
                  GhostNumber = 0,
                  LeptonNumber = 0,
                  Y = 0)

YS3Qu2__tilde__ = YS3Qu2.anti()

YS3Qu3 = Particle(pdg_code = 1000006,
                  name = 'YS3Qu3',
                  antiname = 'YS3Qu3~',
                  spin = 1,
                  color = 3,
                  mass = Param.MYS3Qu3,
                  width = Param.WYS3Qu3,
                  texname = 'YS3Qu3',
                  antitexname = 'YS3Qu3~',
                  charge = 2/3,
                  GhostNumber = 0,
                  LeptonNumber = 0,
                  Y = 0)

YS3Qu3__tilde__ = YS3Qu3.anti()

YS3Qd1 = Particle(pdg_code = 1000001,
                  name = 'YS3Qd1',
                  antiname = 'YS3Qd1~',
                  spin = 1,
                  color = 3,
                  mass = Param.MYS3Qd1,
                  width = Param.WYS3Qd1,
                  texname = 'YS3Qd1',
                  antitexname = 'YS3Qd1~',
                  charge = -1/3,
                  GhostNumber = 0,
                  LeptonNumber = 0,
                  Y = 0)

YS3Qd1__tilde__ = YS3Qd1.anti()

YS3Qd2 = Particle(pdg_code = 1000003,
                  name = 'YS3Qd2',
                  antiname = 'YS3Qd2~',
                  spin = 1,
                  color = 3,
                  mass = Param.MYS3Qd2,
                  width = Param.WYS3Qd2,
                  texname = 'YS3Qd2',
                  antitexname = 'YS3Qd2~',
                  charge = -1/3,
                  GhostNumber = 0,
                  LeptonNumber = 0,
                  Y = 0)

YS3Qd2__tilde__ = YS3Qd2.anti()

YS3Qd3 = Particle(pdg_code = 1000005,
                  name = 'YS3Qd3',
                  antiname = 'YS3Qd3~',
                  spin = 1,
                  color = 3,
                  mass = Param.MYS3Qd3,
                  width = Param.WYS3Qd3,
                  texname = 'YS3Qd3',
                  antitexname = 'YS3Qd3~',
                  charge = -1/3,
                  GhostNumber = 0,
                  LeptonNumber = 0,
                  Y = 0)

YS3Qd3__tilde__ = YS3Qd3.anti()

YS3u1 = Particle(pdg_code = 2000002,
                 name = 'YS3u1',
                 antiname = 'YS3u1~',
                 spin = 1,
                 color = 3,
                 mass = Param.MYS3u1,
                 width = Param.WYS3u1,
                 texname = 'YS3u1',
                 antitexname = 'YS3u1~',
                 charge = 2/3,
                 GhostNumber = 0,
                 LeptonNumber = 0,
                 Y = 2/3)

YS3u1__tilde__ = YS3u1.anti()

YS3u2 = Particle(pdg_code = 2000004,
                 name = 'YS3u2',
                 antiname = 'YS3u2~',
                 spin = 1,
                 color = 3,
                 mass = Param.MYS3u2,
                 width = Param.WYS3u2,
                 texname = 'YS3u2',
                 antitexname = 'YS3u2~',
                 charge = 2/3,
                 GhostNumber = 0,
                 LeptonNumber = 0,
                 Y = 2/3)

YS3u2__tilde__ = YS3u2.anti()

YS3u3 = Particle(pdg_code = 2000006,
                 name = 'YS3u3',
                 antiname = 'YS3u3~',
                 spin = 1,
                 color = 3,
                 mass = Param.MYS3u3,
                 width = Param.WYS3u3,
                 texname = 'YS3u3',
                 antitexname = 'YS3u3~',
                 charge = 2/3,
                 GhostNumber = 0,
                 LeptonNumber = 0,
                 Y = 2/3)

YS3u3__tilde__ = YS3u3.anti()

YS3d1 = Particle(pdg_code = 2000001,
                 name = 'YS3d1',
                 antiname = 'YS3d1~',
                 spin = 1,
                 color = 3,
                 mass = Param.MYS3d1,
                 width = Param.WYS3d1,
                 texname = 'YS3d1',
                 antitexname = 'YS3d1~',
                 charge = -1/3,
                 GhostNumber = 0,
                 LeptonNumber = 0,
                 Y = -1/3)

YS3d1__tilde__ = YS3d1.anti()

YS3d2 = Particle(pdg_code = 2000003,
                 name = 'YS3d2',
                 antiname = 'YS3d2~',
                 spin = 1,
                 color = 3,
                 mass = Param.MYS3d2,
                 width = Param.WYS3d2,
                 texname = 'YS3d2',
                 antitexname = 'YS3d2~',
                 charge = -1/3,
                 GhostNumber = 0,
                 LeptonNumber = 0,
                 Y = -1/3)

YS3d2__tilde__ = YS3d2.anti()

YS3d3 = Particle(pdg_code = 2000005,
                 name = 'YS3d3',
                 antiname = 'YS3d3~',
                 spin = 1,
                 color = 3,
                 mass = Param.MYS3d3,
                 width = Param.WYS3d3,
                 texname = 'YS3d3',
                 antitexname = 'YS3d3~',
                 charge = -1/3,
                 GhostNumber = 0,
                 LeptonNumber = 0,
                 Y = -1/3)

YS3d3__tilde__ = YS3d3.anti()

YS1Lv1 = Particle(pdg_code = 1000012,
                  name = 'YS1Lv1',
                  antiname = 'YS1Lv1~',
                  spin = 1,
                  color = 1,
                  mass = Param.MYS1Lv1,
                  width = Param.WYS1Lv1,
                  texname = 'YS1Lv1',
                  antitexname = 'YS1Lv1~',
                  charge = 0,
                  GhostNumber = 0,
                  LeptonNumber = 0,
                  Y = 0)

YS1Lv1__tilde__ = YS1Lv1.anti()

YS1Lv2 = Particle(pdg_code = 1000014,
                  name = 'YS1Lv2',
                  antiname = 'YS1Lv2~',
                  spin = 1,
                  color = 1,
                  mass = Param.MYS1Lv2,
                  width = Param.WYS1Lv2,
                  texname = 'YS1Lv2',
                  antitexname = 'YS1Lv2~',
                  charge = 0,
                  GhostNumber = 0,
                  LeptonNumber = 0,
                  Y = 0)

YS1Lv2__tilde__ = YS1Lv2.anti()

YS1Lv3 = Particle(pdg_code = 1000016,
                  name = 'YS1Lv3',
                  antiname = 'YS1Lv3~',
                  spin = 1,
                  color = 1,
                  mass = Param.MYS1Lv3,
                  width = Param.WYS1Lv3,
                  texname = 'YS1Lv3',
                  antitexname = 'YS1Lv3~',
                  charge = 0,
                  GhostNumber = 0,
                  LeptonNumber = 0,
                  Y = 0)

YS1Lv3__tilde__ = YS1Lv3.anti()

YS1Le1 = Particle(pdg_code = 1000011,
                  name = 'YS1Le1',
                  antiname = 'YS1Le1~',
                  spin = 1,
                  color = 1,
                  mass = Param.MYS1Le1,
                  width = Param.WYS1Le1,
                  texname = 'YS1Le1',
                  antitexname = 'YS1Le1~',
                  charge = -1,
                  GhostNumber = 0,
                  LeptonNumber = 0,
                  Y = 0)

YS1Le1__tilde__ = YS1Le1.anti()

YS1Le2 = Particle(pdg_code = 1000013,
                  name = 'YS1Le2',
                  antiname = 'YS1Le2~',
                  spin = 1,
                  color = 1,
                  mass = Param.MYS1Le2,
                  width = Param.WYS1Le2,
                  texname = 'YS1Le2',
                  antitexname = 'YS1Le2~',
                  charge = -1,
                  GhostNumber = 0,
                  LeptonNumber = 0,
                  Y = 0)

YS1Le2__tilde__ = YS1Le2.anti()

YS1Le3 = Particle(pdg_code = 1000015,
                  name = 'YS1Le3',
                  antiname = 'YS1Le3~',
                  spin = 1,
                  color = 1,
                  mass = Param.MYS1Le3,
                  width = Param.WYS1Le3,
                  texname = 'YS1Le3',
                  antitexname = 'YS1Le3~',
                  charge = -1,
                  GhostNumber = 0,
                  LeptonNumber = 0,
                  Y = 0)

YS1Le3__tilde__ = YS1Le3.anti()

YS1e1 = Particle(pdg_code = 2000011,
                 name = 'YS1e1',
                 antiname = 'YS1e1~',
                 spin = 1,
                 color = 1,
                 mass = Param.MYS1e1,
                 width = Param.WYS1e1,
                 texname = 'YS1e1',
                 antitexname = 'YS1e1~',
                 charge = -1,
                 GhostNumber = 0,
                 LeptonNumber = 0,
                 Y = -1)

YS1e1__tilde__ = YS1e1.anti()

YS1e2 = Particle(pdg_code = 2000013,
                 name = 'YS1e2',
                 antiname = 'YS1e2~',
                 spin = 1,
                 color = 1,
                 mass = Param.MYS1e2,
                 width = Param.WYS1e2,
                 texname = 'YS1e2',
                 antitexname = 'YS1e2~',
                 charge = -1,
                 GhostNumber = 0,
                 LeptonNumber = 0,
                 Y = -1)

YS1e2__tilde__ = YS1e2.anti()

YS1e3 = Particle(pdg_code = 2000015,
                 name = 'YS1e3',
                 antiname = 'YS1e3~',
                 spin = 1,
                 color = 1,
                 mass = Param.MYS1e3,
                 width = Param.WYS1e3,
                 texname = 'YS1e3',
                 antitexname = 'YS1e3~',
                 charge = -1,
                 GhostNumber = 0,
                 LeptonNumber = 0,
                 Y = -1)

YS1e3__tilde__ = YS1e3.anti()

YF3Qu1 = Particle(pdg_code = 5910002,
                  name = 'YF3Qu1',
                  antiname = 'YF3Qu1~',
                  spin = 2,
                  color = 3,
                  mass = Param.MYF3Qu1,
                  width = Param.WYF3Qu1,
                  texname = 'YF3Qu1',
                  antitexname = 'YF3Qu1~',
                  charge = 2/3,
                  GhostNumber = 0,
                  LeptonNumber = 0,
                  Y = 0)

YF3Qu1__tilde__ = YF3Qu1.anti()

YF3Qu2 = Particle(pdg_code = 5910004,
                  name = 'YF3Qu2',
                  antiname = 'YF3Qu2~',
                  spin = 2,
                  color = 3,
                  mass = Param.MYF3Qu2,
                  width = Param.WYF3Qu2,
                  texname = 'YF3Qu2',
                  antitexname = 'YF3Qu2~',
                  charge = 2/3,
                  GhostNumber = 0,
                  LeptonNumber = 0,
                  Y = 0)

YF3Qu2__tilde__ = YF3Qu2.anti()

YF3Qu3 = Particle(pdg_code = 5910006,
                  name = 'YF3Qu3',
                  antiname = 'YF3Qu3~',
                  spin = 2,
                  color = 3,
                  mass = Param.MYF3Qu3,
                  width = Param.WYF3Qu3,
                  texname = 'YF3Qu3',
                  antitexname = 'YF3Qu3~',
                  charge = 2/3,
                  GhostNumber = 0,
                  LeptonNumber = 0,
                  Y = 0)

YF3Qu3__tilde__ = YF3Qu3.anti()

YF3Qd1 = Particle(pdg_code = 5910001,
                  name = 'YF3Qd1',
                  antiname = 'YF3Qd1~',
                  spin = 2,
                  color = 3,
                  mass = Param.MYF3Qd1,
                  width = Param.WYF3Qd1,
                  texname = 'YF3Qd1',
                  antitexname = 'YF3Qd1~',
                  charge = -1/3,
                  GhostNumber = 0,
                  LeptonNumber = 0,
                  Y = 0)

YF3Qd1__tilde__ = YF3Qd1.anti()

YF3Qd2 = Particle(pdg_code = 5910003,
                  name = 'YF3Qd2',
                  antiname = 'YF3Qd2~',
                  spin = 2,
                  color = 3,
                  mass = Param.MYF3Qd2,
                  width = Param.WYF3Qd2,
                  texname = 'YF3Qd2',
                  antitexname = 'YF3Qd2~',
                  charge = -1/3,
                  GhostNumber = 0,
                  LeptonNumber = 0,
                  Y = 0)

YF3Qd2__tilde__ = YF3Qd2.anti()

YF3Qd3 = Particle(pdg_code = 5910005,
                  name = 'YF3Qd3',
                  antiname = 'YF3Qd3~',
                  spin = 2,
                  color = 3,
                  mass = Param.MYF3Qd3,
                  width = Param.WYF3Qd3,
                  texname = 'YF3Qd3',
                  antitexname = 'YF3Qd3~',
                  charge = -1/3,
                  GhostNumber = 0,
                  LeptonNumber = 0,
                  Y = 0)

YF3Qd3__tilde__ = YF3Qd3.anti()

YF3u1 = Particle(pdg_code = 5920002,
                 name = 'YF3u1',
                 antiname = 'YF3u1~',
                 spin = 2,
                 color = 3,
                 mass = Param.MYF3u1,
                 width = Param.WYF3u1,
                 texname = 'YF3u1',
                 antitexname = 'YF3u1~',
                 charge = 2/3,
                 GhostNumber = 0,
                 LeptonNumber = 0,
                 Y = 2/3)

YF3u1__tilde__ = YF3u1.anti()

YF3u2 = Particle(pdg_code = 5920004,
                 name = 'YF3u2',
                 antiname = 'YF3u2~',
                 spin = 2,
                 color = 3,
                 mass = Param.MYF3u2,
                 width = Param.WYF3u2,
                 texname = 'YF3u2',
                 antitexname = 'YF3u2~',
                 charge = 2/3,
                 GhostNumber = 0,
                 LeptonNumber = 0,
                 Y = 2/3)

YF3u2__tilde__ = YF3u2.anti()

YF3u3 = Particle(pdg_code = 5920006,
                 name = 'YF3u3',
                 antiname = 'YF3u3~',
                 spin = 2,
                 color = 3,
                 mass = Param.MYF3u3,
                 width = Param.WYF3u3,
                 texname = 'YF3u3',
                 antitexname = 'YF3u3~',
                 charge = 2/3,
                 GhostNumber = 0,
                 LeptonNumber = 0,
                 Y = 2/3)

YF3u3__tilde__ = YF3u3.anti()

YF3d1 = Particle(pdg_code = 5920001,
                 name = 'YF3d1',
                 antiname = 'YF3d1~',
                 spin = 2,
                 color = 3,
                 mass = Param.MYF3d1,
                 width = Param.WYF3d1,
                 texname = 'YF3d1',
                 antitexname = 'YF3d1~',
                 charge = -1/3,
                 GhostNumber = 0,
                 LeptonNumber = 0,
                 Y = -1/3)

YF3d1__tilde__ = YF3d1.anti()

YF3d2 = Particle(pdg_code = 5920003,
                 name = 'YF3d2',
                 antiname = 'YF3d2~',
                 spin = 2,
                 color = 3,
                 mass = Param.MYF3d2,
                 width = Param.WYF3d2,
                 texname = 'YF3d2',
                 antitexname = 'YF3d2~',
                 charge = -1/3,
                 GhostNumber = 0,
                 LeptonNumber = 0,
                 Y = -1/3)

YF3d2__tilde__ = YF3d2.anti()

YF3d3 = Particle(pdg_code = 5920005,
                 name = 'YF3d3',
                 antiname = 'YF3d3~',
                 spin = 2,
                 color = 3,
                 mass = Param.MYF3d3,
                 width = Param.WYF3d3,
                 texname = 'YF3d3',
                 antitexname = 'YF3d3~',
                 charge = -1/3,
                 GhostNumber = 0,
                 LeptonNumber = 0,
                 Y = -1/3)

YF3d3__tilde__ = YF3d3.anti()

YF1Lv1 = Particle(pdg_code = 5910012,
                  name = 'YF1Lv1',
                  antiname = 'YF1Lv1~',
                  spin = 2,
                  color = 1,
                  mass = Param.MYF1Lv1,
                  width = Param.WYF1Lv1,
                  texname = 'YF1Lv1',
                  antitexname = 'YF1Lv1~',
                  charge = 0,
                  GhostNumber = 0,
                  LeptonNumber = 0,
                  Y = 0)

YF1Lv1__tilde__ = YF1Lv1.anti()

YF1Lv2 = Particle(pdg_code = 5910014,
                  name = 'YF1Lv2',
                  antiname = 'YF1Lv2~',
                  spin = 2,
                  color = 1,
                  mass = Param.MYF1Lv2,
                  width = Param.WYF1Lv2,
                  texname = 'YF1Lv2',
                  antitexname = 'YF1Lv2~',
                  charge = 0,
                  GhostNumber = 0,
                  LeptonNumber = 0,
                  Y = 0)

YF1Lv2__tilde__ = YF1Lv2.anti()

YF1Lv3 = Particle(pdg_code = 5910016,
                  name = 'YF1Lv3',
                  antiname = 'YF1Lv3~',
                  spin = 2,
                  color = 1,
                  mass = Param.MYF1Lv3,
                  width = Param.WYF1Lv3,
                  texname = 'YF1Lv3',
                  antitexname = 'YF1Lv3~',
                  charge = 0,
                  GhostNumber = 0,
                  LeptonNumber = 0,
                  Y = 0)

YF1Lv3__tilde__ = YF1Lv3.anti()

YF1Le1 = Particle(pdg_code = 5910011,
                  name = 'YF1Le1',
                  antiname = 'YF1Le1~',
                  spin = 2,
                  color = 1,
                  mass = Param.MYF1Le1,
                  width = Param.WYF1Le1,
                  texname = 'YF1Le1',
                  antitexname = 'YF1Le1~',
                  charge = -1,
                  GhostNumber = 0,
                  LeptonNumber = 0,
                  Y = 0)

YF1Le1__tilde__ = YF1Le1.anti()

YF1Le2 = Particle(pdg_code = 5910013,
                  name = 'YF1Le2',
                  antiname = 'YF1Le2~',
                  spin = 2,
                  color = 1,
                  mass = Param.MYF1Le2,
                  width = Param.WYF1Le2,
                  texname = 'YF1Le2',
                  antitexname = 'YF1Le2~',
                  charge = -1,
                  GhostNumber = 0,
                  LeptonNumber = 0,
                  Y = 0)

YF1Le2__tilde__ = YF1Le2.anti()

YF1Le3 = Particle(pdg_code = 5910015,
                  name = 'YF1Le3',
                  antiname = 'YF1Le3~',
                  spin = 2,
                  color = 1,
                  mass = Param.MYF1Le3,
                  width = Param.WYF1Le3,
                  texname = 'YF1Le3',
                  antitexname = 'YF1Le3~',
                  charge = -1,
                  GhostNumber = 0,
                  LeptonNumber = 0,
                  Y = 0)

YF1Le3__tilde__ = YF1Le3.anti()

YF1e1 = Particle(pdg_code = 5920011,
                 name = 'YF1e1',
                 antiname = 'YF1e1~',
                 spin = 2,
                 color = 1,
                 mass = Param.MYF1e1,
                 width = Param.WYF1e1,
                 texname = 'YF1e1',
                 antitexname = 'YF1e1~',
                 charge = -1,
                 GhostNumber = 0,
                 LeptonNumber = 0,
                 Y = -1)

YF1e1__tilde__ = YF1e1.anti()

YF1e2 = Particle(pdg_code = 5920013,
                 name = 'YF1e2',
                 antiname = 'YF1e2~',
                 spin = 2,
                 color = 1,
                 mass = Param.MYF1e2,
                 width = Param.WYF1e2,
                 texname = 'YF1e2',
                 antitexname = 'YF1e2~',
                 charge = -1,
                 GhostNumber = 0,
                 LeptonNumber = 0,
                 Y = -1)

YF1e2__tilde__ = YF1e2.anti()

YF1e3 = Particle(pdg_code = 5920015,
                 name = 'YF1e3',
                 antiname = 'YF1e3~',
                 spin = 2,
                 color = 1,
                 mass = Param.MYF1e3,
                 width = Param.WYF1e3,
                 texname = 'YF1e3',
                 antitexname = 'YF1e3~',
                 charge = -1,
                 GhostNumber = 0,
                 LeptonNumber = 0,
                 Y = -1)

YF1e3__tilde__ = YF1e3.anti()

