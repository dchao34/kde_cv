import sys
import os
import datetime
import tempfile
import subprocess

b1, e1, s1 = 0.0, 0.1, 0.001
b2, e2, s2 = 0.0, 1.0, 0.01

outdir = 'visual/contour'
datadir = 'data'

# optimal for all except continum (approximate).
opt_h1 = [ 2.39e-3, 2.11e-3, 1.21e-3, 1.49e-3, 1.67e-4]
opt_h2 = [ 2.08e-2, 1.69e-2, 1.87e-2, 1.66e-2, 1.34e-2 ]

for i, (h1, h2) in enumerate(zip(opt_h1, opt_h2)):
    sys.stdout.write('Scanning evttype{0}...\n'.format(i+1))
    sys.stdout.flush()
    out2d = outdir + '/evttype{0}.2d.opt.txt'.format(i+1)
    out1d = outdir + '/evttype{0}.1d.opt.txt'.format(i+1)
    in_data = datadir + '/evttype{0}.cv.csv'.format(i+1)

    subprocess.check_call(['./kde_scan', out2d, out1d, in_data,
                           str(h1), str(h2),
                           str(b1), str(e1), str(s1),
                           str(b2), str(e2), str(s2)])