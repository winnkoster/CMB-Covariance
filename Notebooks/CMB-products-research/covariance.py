# Winn Koster - April 19 - Testing ground for new code
# The covaraince code works, but needs improvements. I don't want to break what I already have, so we duplicate and keep going.

import numpy as np

# Keep these as true. I've only defined these so that I can collapse their respective 'if var_name == True:' statements in Atom (code editor). This way I don't have to look at 150 lines of np.loadtxt()
load_data = True                      # boolean variable, load data or not?
linear_derivatives = True             # linear derivatives?

if load_data == True:                 # Loads all the TT, TE, EE power spectra data from simulations, plus nominal data

    # DEFINE FILE LOCATIONS
    # Nominal Data
    fname_nominal_tt = './nominal/tt.txt'
    fname_axis = './nominal/ell.txt'
    fname_nominal_ee = './nominal/ee.txt'
    fname_nominal_te = './nominal/te.txt'

    # Omega_B
    # TT spec
    fname_high_long_omega_b_tt = './nominal/omega_b-HIGH-LONG/tt.txt'
    fname_high_short_omega_b_tt = './nominal/omega_b-HIGH-SHORT/tt.txt'
    fname_low_long_omega_b_tt = './nominal/omega_b-LOW-LONG/tt.txt'
    fname_low_short_omega_b_tt = './nominal/omega_b-LOW-SHORT/tt.txt'

    # EE spec
    fname_high_long_omega_b_ee = './nominal/omega_b-HIGH-LONG/ee.txt'
    fname_high_short_omega_b_ee = './nominal/omega_b-HIGH-SHORT/ee.txt'
    fname_low_long_omega_b_ee = './nominal/omega_b-LOW-LONG/ee.txt'
    fname_low_short_omega_b_ee = './nominal/omega_b-LOW-SHORT/ee.txt'

    # TE spec
    fname_high_long_omega_b_te = './nominal/omega_b-HIGH-LONG/te.txt'
    fname_high_short_omega_b_te = './nominal/omega_b-HIGH-SHORT/te.txt'
    fname_low_long_omega_b_te = './nominal/omega_b-LOW-LONG/te.txt'
    fname_low_short_omega_b_te = './nominal/omega_b-LOW-SHORT/te.txt'

    # Omega_M
    # TT spec
    fname_high_long_omega_m_tt = './nominal/omega_m-HIGH-LONG/tt.txt'
    fname_high_short_omega_m_tt = './nominal/omega_m-HIGH-SHORT/tt.txt'
    fname_low_long_omega_m_tt = './nominal/omega_m-LOW-LONG/tt.txt'
    fname_low_short_omega_m_tt = './nominal/omega_m-LOW-SHORT/tt.txt'

    # EE spec
    fname_high_long_omega_m_ee = './nominal/omega_m-HIGH-LONG/ee.txt'
    fname_high_short_omega_m_ee = './nominal/omega_m-HIGH-SHORT/ee.txt'
    fname_low_long_omega_m_ee = './nominal/omega_m-LOW-LONG/ee.txt'
    fname_low_short_omega_m_ee = './nominal/omega_m-LOW-SHORT/ee.txt'

    # TE spec
    fname_high_long_omega_m_te = './nominal/omega_m-HIGH-LONG/te.txt'
    fname_high_short_omega_m_te = './nominal/omega_m-HIGH-SHORT/te.txt'
    fname_low_long_omega_m_te = './nominal/omega_m-LOW-LONG/te.txt'
    fname_low_short_omega_m_te = './nominal/omega_m-LOW-SHORT/te.txt'

    # H_0
    # TT spec
    fname_high_long_h_0_tt = './nominal/h_0-HIGH-LONG/tt.txt'
    fname_high_short_h_0_tt = './nominal/h_0-HIGH-SHORT/tt.txt'
    fname_low_long_h_0_tt = './nominal/h_0-LOW-LONG/tt.txt'
    fname_low_short_h_0_tt = './nominal/h_0-LOW-SHORT/tt.txt'

    # EE spec
    fname_high_long_h_0_ee = './nominal/h_0-HIGH-LONG/ee.txt'
    fname_high_short_h_0_ee = './nominal/h_0-HIGH-SHORT/ee.txt'
    fname_low_long_h_0_ee = './nominal/h_0-LOW-LONG/ee.txt'
    fname_low_short_h_0_ee = './nominal/h_0-LOW-SHORT/ee.txt'

    # TE spec
    fname_high_long_h_0_te = './nominal/h_0-HIGH-LONG/te.txt'
    fname_high_short_h_0_te = './nominal/h_0-HIGH-SHORT/te.txt'
    fname_low_long_h_0_te = './nominal/h_0-LOW-LONG/te.txt'
    fname_low_short_h_0_te = './nominal/h_0-LOW-SHORT/te.txt'


    # S = 3200
    # TT spec
    fname_high_long_s3_5_tt = './log_s_3.5/d_0_HIGH-LONG/tt.txt'
    fname_high_short_s3_5_tt = './log_s_3.5/d_0_HIGH-SHORT/tt.txt'
    fname_low_long_s3_5_tt = './log_s_3.5/d_0_LOW-LONG/tt.txt'
    fname_low_short_s3_5_tt = './log_s_3.5/d_0_LOW-SHORT/tt.txt'

    # EE spec
    fname_high_long_s3_5_ee = './log_s_3.5/d_0_HIGH-LONG/ee.txt'
    fname_high_short_s3_5_ee = './log_s_3.5/d_0_HIGH-SHORT/ee.txt'
    fname_low_long_s3_5_ee = './log_s_3.5/d_0_LOW-LONG/ee.txt'
    fname_low_short_s3_5_ee = './log_s_3.5/d_0_LOW-SHORT/ee.txt'

    # TE spec
    fname_high_long_s3_5_te = './log_s_3.5/d_0_HIGH-LONG/te.txt'
    fname_high_short_s3_5_te = './log_s_3.5/d_0_HIGH-SHORT/te.txt'
    fname_low_long_s3_5_te = './log_s_3.5/d_0_LOW-LONG/te.txt'
    fname_low_short_s3_5_te = './log_s_3.5/d_0_LOW-SHORT/te.txt'


    # s = 100000 (e+5)
    # TT spec
    fname_high_long_s5_tt = './log_s_5/d_0_HIGH-LONG/tt.txt'
    fname_high_short_s5_tt = './log_s_5/d_0_HIGH-SHORT/tt.txt'
    fname_low_long_s5_tt = './log_s_5/d_0_LOW-LONG/tt.txt'
    fname_low_short_s5_tt = './log_s_5/d_0_LOW-SHORT/tt.txt'

    # EE spec
    fname_high_long_s5_ee = './log_s_5/d_0_HIGH-LONG/ee.txt'
    fname_high_short_s5_ee = './log_s_5/d_0_HIGH-SHORT/ee.txt'
    fname_low_long_s5_ee = './log_s_5/d_0_LOW-LONG/ee.txt'
    fname_low_short_s5_ee = './log_s_5/d_0_LOW-SHORT/ee.txt'

    # TE spec
    fname_high_long_s5_te = './log_s_5/d_0_HIGH-LONG/te.txt'
    fname_high_short_s5_te = './log_s_5/d_0_HIGH-SHORT/te.txt'
    fname_low_long_s5_te = './log_s_5/d_0_LOW-LONG/te.txt'
    fname_low_short_s5_te = './log_s_5/d_0_LOW-SHORT/te.txt'

    # logS = 6.5
    # TT spec
    fname_high_long_s6_5_tt = './log_s_6.5/d_0_HIGH-LONG/tt.txt'
    fname_high_short_s6_5_tt = './log_s_6.5/d_0_HIGH-SHORT/tt.txt'
    fname_low_long_s6_5_tt = './log_s_6.5/d_0_LOW-LONG/tt.txt'
    fname_low_short_s6_5_tt = './log_s_6.5/d_0_LOW-SHORT/tt.txt'

    # EE spec
    fname_high_long_s6_5_ee = './log_s_6.5/d_0_HIGH-LONG/ee.txt'
    fname_high_short_s6_5_ee = './log_s_6.5/d_0_HIGH-SHORT/ee.txt'
    fname_low_long_s6_5_ee = './log_s_6.5/d_0_LOW-LONG/ee.txt'
    fname_low_short_s6_5_ee = './log_s_6.5/d_0_LOW-SHORT/ee.txt'

    # TE spec
    fname_high_long_s6_5_te = './log_s_6.5/d_0_HIGH-LONG/te.txt'
    fname_high_short_s6_5_te = './log_s_6.5/d_0_HIGH-SHORT/te.txt'
    fname_low_long_s6_5_te = './log_s_6.5/d_0_LOW-LONG/te.txt'
    fname_low_short_s6_5_te = './log_s_6.5/d_0_LOW-SHORT/te.txt'



    # S = 10000000 (e+8)
    # TT spec
    fname_high_long_s8_tt = './log_s_8/d_0_HIGH-LONG/tt.txt'
    fname_high_short_s8_tt = './log_s_8/d_0_HIGH-SHORT/tt.txt'
    fname_low_long_s8_tt = './log_s_8/d_0_LOW-LONG/tt.txt'
    fname_low_short_s8_tt = './log_s_8/d_0_LOW-SHORT/tt.txt'

    # EE spec
    fname_high_long_s8_ee = './log_s_8/d_0_HIGH-LONG/ee.txt'
    fname_high_short_s8_ee = './log_s_8/d_0_HIGH-SHORT/ee.txt'
    fname_low_long_s8_ee = './log_s_8/d_0_LOW-LONG/ee.txt'
    fname_low_short_s8_ee = './log_s_8/d_0_LOW-SHORT/ee.txt'

    # TE spec
    fname_high_long_s8_te = './log_s_8/d_0_HIGH-LONG/te.txt'
    fname_high_short_s8_te = './log_s_8/d_0_HIGH-SHORT/te.txt'
    fname_low_long_s8_te = './log_s_8/d_0_LOW-LONG/te.txt'
    fname_low_short_s8_te = './log_s_8/d_0_LOW-SHORT/te.txt'


    # --------------------------------------------------------------------------

    # LOAD THE DATA FROM FILES
    # Nominal data
    data_nominal_tt = np.loadtxt(fname_nominal_tt,skiprows=1)
    data_nominal_ee = np.loadtxt(fname_nominal_ee,skiprows=1)
    data_nominal_te = np.loadtxt(fname_nominal_te,skiprows=1)
    axis = np.loadtxt(fname_axis,skiprows=1)

    # OMEGA_B
    # TT spec
    data_high_long_omega_b_tt = np.loadtxt(fname_high_long_omega_b_tt,skiprows=1)
    data_low_long_omega_b_tt = np.loadtxt(fname_low_long_omega_b_tt,skiprows=1)
    data_high_short_omega_b_tt = np.loadtxt(fname_high_short_omega_b_tt,skiprows=1)
    data_low_short_omega_b_tt = np.loadtxt(fname_low_short_omega_b_tt,skiprows=1)

    # EE spec
    data_high_long_omega_b_ee = np.loadtxt(fname_high_long_omega_b_ee,skiprows=1)
    data_low_long_omega_b_ee = np.loadtxt(fname_low_long_omega_b_ee,skiprows=1)
    data_high_short_omega_b_ee = np.loadtxt(fname_high_short_omega_b_ee,skiprows=1)
    data_low_short_omega_b_ee = np.loadtxt(fname_low_short_omega_b_ee,skiprows=1)

    # TE spec
    data_high_long_omega_b_te = np.loadtxt(fname_high_long_omega_b_te,skiprows=1)
    data_low_long_omega_b_te = np.loadtxt(fname_low_long_omega_b_te,skiprows=1)
    data_high_short_omega_b_te = np.loadtxt(fname_high_short_omega_b_te,skiprows=1)
    data_low_short_omega_b_te = np.loadtxt(fname_low_short_omega_b_te,skiprows=1)


    # OMEGA_M
    # TT spec
    data_high_long_omega_m_tt = np.loadtxt(fname_high_long_omega_m_tt,skiprows=1)
    data_low_long_omega_m_tt = np.loadtxt(fname_low_long_omega_m_tt,skiprows=1)
    data_high_short_omega_m_tt = np.loadtxt(fname_high_short_omega_m_tt,skiprows=1)
    data_low_short_omega_m_tt = np.loadtxt(fname_low_short_omega_m_tt,skiprows=1)

    # EE spec
    data_high_long_omega_m_ee = np.loadtxt(fname_high_long_omega_m_ee,skiprows=1)
    data_low_long_omega_m_ee = np.loadtxt(fname_low_long_omega_m_ee,skiprows=1)
    data_high_short_omega_m_ee = np.loadtxt(fname_high_short_omega_m_ee,skiprows=1)
    data_low_short_omega_m_ee = np.loadtxt(fname_low_short_omega_m_ee,skiprows=1)

    # TE spec
    data_high_long_omega_m_te = np.loadtxt(fname_high_long_omega_m_te,skiprows=1)
    data_low_long_omega_m_te = np.loadtxt(fname_low_long_omega_m_te,skiprows=1)
    data_high_short_omega_m_te = np.loadtxt(fname_high_short_omega_m_te,skiprows=1)
    data_low_short_omega_m_te = np.loadtxt(fname_low_short_omega_m_te,skiprows=1)


    # h_0
    # TT spec
    data_high_long_h_0_tt = np.loadtxt(fname_high_long_h_0_tt,skiprows=1)
    data_low_long_h_0_tt = np.loadtxt(fname_low_long_h_0_tt,skiprows=1)
    data_high_short_h_0_tt = np.loadtxt(fname_high_short_h_0_tt,skiprows=1)
    data_low_short_h_0_tt = np.loadtxt(fname_low_short_h_0_tt,skiprows=1)

    # EE spec
    data_high_long_h_0_ee = np.loadtxt(fname_high_long_h_0_ee,skiprows=1)
    data_low_long_h_0_ee = np.loadtxt(fname_low_long_h_0_ee,skiprows=1)
    data_high_short_h_0_ee = np.loadtxt(fname_high_short_h_0_ee,skiprows=1)
    data_low_short_h_0_ee = np.loadtxt(fname_low_short_h_0_ee,skiprows=1)

    # TE spec
    data_high_long_h_0_te = np.loadtxt(fname_high_long_h_0_te,skiprows=1)
    data_low_long_h_0_te = np.loadtxt(fname_low_long_h_0_te,skiprows=1)
    data_high_short_h_0_te = np.loadtxt(fname_high_short_h_0_te,skiprows=1)
    data_low_short_h_0_te = np.loadtxt(fname_low_short_h_0_te,skiprows=1)


    # S = 3200
    # TT spec
    data_high_long_s3_5_tt = np.loadtxt(fname_high_long_s3_5_tt,skiprows=1)
    data_low_long_s3_5_tt = np.loadtxt(fname_low_long_s3_5_tt,skiprows=1)
    data_high_short_s3_5_tt = np.loadtxt(fname_high_short_s3_5_tt,skiprows=1)
    data_low_short_s3_5_tt = np.loadtxt(fname_low_short_s3_5_tt,skiprows=1)

    # EE spec
    data_high_long_s3_5_ee = np.loadtxt(fname_high_long_s3_5_ee,skiprows=1)
    data_low_long_s3_5_ee = np.loadtxt(fname_low_long_s3_5_ee,skiprows=1)
    data_high_short_s3_5_ee = np.loadtxt(fname_high_short_s3_5_ee,skiprows=1)
    data_low_short_s3_5_ee = np.loadtxt(fname_low_short_s3_5_ee,skiprows=1)

    # TE spec
    data_high_long_s3_5_te = np.loadtxt(fname_high_long_s3_5_te,skiprows=1)
    data_low_long_s3_5_te = np.loadtxt(fname_low_long_s3_5_te,skiprows=1)
    data_high_short_s3_5_te = np.loadtxt(fname_high_short_s3_5_te,skiprows=1)
    data_low_short_s3_5_te = np.loadtxt(fname_low_short_s3_5_te,skiprows=1)


    # S = 100,000
    # TT spec
    data_high_long_s5_tt = np.loadtxt(fname_high_long_s5_tt,skiprows=1)
    data_low_long_s5_tt = np.loadtxt(fname_low_long_s5_tt,skiprows=1)
    data_high_short_s5_tt = np.loadtxt(fname_high_short_s5_tt,skiprows=1)
    data_low_short_s5_tt = np.loadtxt(fname_low_short_s5_tt,skiprows=1)

    # EE spec
    data_high_long_s5_ee = np.loadtxt(fname_high_long_s5_ee,skiprows=1)
    data_low_long_s5_ee = np.loadtxt(fname_low_long_s5_ee,skiprows=1)
    data_high_short_s5_ee = np.loadtxt(fname_high_short_s5_ee,skiprows=1)
    data_low_short_s5_ee = np.loadtxt(fname_low_short_s5_ee,skiprows=1)

    # TE spec
    data_high_long_s5_te = np.loadtxt(fname_high_long_s5_te,skiprows=1)
    data_low_long_s5_te = np.loadtxt(fname_low_long_s5_te,skiprows=1)
    data_high_short_s5_te = np.loadtxt(fname_high_short_s5_te,skiprows=1)
    data_low_short_s5_te = np.loadtxt(fname_low_short_s5_te,skiprows=1)



    # logS = 6.5
    # TT spec
    data_high_long_s6_5_tt = np.loadtxt(fname_high_long_s6_5_tt,skiprows=1)
    data_low_long_s6_5_tt = np.loadtxt(fname_low_long_s6_5_tt,skiprows=1)
    data_high_short_s6_5_tt = np.loadtxt(fname_high_short_s6_5_tt,skiprows=1)
    data_low_short_s6_5_tt = np.loadtxt(fname_low_short_s6_5_tt,skiprows=1)

    # EE spec
    data_high_long_s6_5_ee = np.loadtxt(fname_high_long_s6_5_ee,skiprows=1)
    data_low_long_s6_5_ee = np.loadtxt(fname_low_long_s6_5_ee,skiprows=1)
    data_high_short_s6_5_ee = np.loadtxt(fname_high_short_s6_5_ee,skiprows=1)
    data_low_short_s6_5_ee = np.loadtxt(fname_low_short_s6_5_ee,skiprows=1)

    # TE spec
    data_high_long_s6_5_te = np.loadtxt(fname_high_long_s6_5_te,skiprows=1)
    data_low_long_s6_5_te = np.loadtxt(fname_low_long_s6_5_te,skiprows=1)
    data_high_short_s6_5_te = np.loadtxt(fname_high_short_s6_5_te,skiprows=1)
    data_low_short_s6_5_te = np.loadtxt(fname_low_short_s6_5_te,skiprows=1)


    # S = 100000000 (e+8)
    # TT spec
    data_high_long_s8_tt = np.loadtxt(fname_high_long_s8_tt,skiprows=1)
    data_low_long_s8_tt = np.loadtxt(fname_low_long_s8_tt,skiprows=1)
    data_high_short_s8_tt = np.loadtxt(fname_high_short_s8_tt,skiprows=1)
    data_low_short_s8_tt = np.loadtxt(fname_low_short_s8_tt,skiprows=1)

    # EE spec
    data_high_long_s8_ee = np.loadtxt(fname_high_long_s8_ee,skiprows=1)
    data_low_long_s8_ee = np.loadtxt(fname_low_long_s8_ee,skiprows=1)
    data_high_short_s8_ee = np.loadtxt(fname_high_short_s8_ee,skiprows=1)
    data_low_short_s8_ee = np.loadtxt(fname_low_short_s8_ee,skiprows=1)

    # TE spec
    data_high_long_s8_te = np.loadtxt(fname_high_long_s8_te,skiprows=1)
    data_low_long_s8_te = np.loadtxt(fname_low_long_s8_te,skiprows=1)
    data_high_short_s8_te = np.loadtxt(fname_high_short_s8_te,skiprows=1)
    data_low_short_s8_te = np.loadtxt(fname_low_short_s8_te,skiprows=1)


    # --------------------------------------------------------------------------
    # All these data files have l_max = 2508. One could add lines to trim the lengths of the data just to make sure, but not needed here
    # eg:   data_high_long_s5 = data_high_long_s5[0:2507]
if linear_derivatives == True:        # Takes linear derivatives for all data loaded. This is hard coded.

    # TT derivatives
    linear_derivatives_long_s5_tt = []
    linear_derivatives_short_s5_tt = []

    linear_derivatives_long_s3_5_tt = []
    linear_derivatives_short_s3_5_tt = []

    linear_derivatives_long_s6_5_tt = []
    linear_derivatives_short_s6_5_tt = []

    linear_derivatives_long_s8_tt = []
    linear_derivatives_short_s8_tt = []

    linear_derivatives_long_omega_b_tt = []
    linear_derivatives_short_omega_b_tt = []

    linear_derivatives_long_omega_m_tt = []
    linear_derivatives_short_omega_m_tt = []

    linear_derivatives_long_h_0_tt = []
    linear_derivatives_short_h_0_tt = []



    # TE derivatives
    linear_derivatives_long_s5_te = []
    linear_derivatives_short_s5_te = []


    linear_derivatives_long_s3_5_te = []
    linear_derivatives_short_s3_5_te = []

    linear_derivatives_long_s6_5_te = []
    linear_derivatives_short_s6_5_te = []

    linear_derivatives_long_s8_te = []
    linear_derivatives_short_s8_te = []

    linear_derivatives_long_omega_b_te = []
    linear_derivatives_short_omega_b_te = []

    linear_derivatives_long_omega_m_te = []
    linear_derivatives_short_omega_m_te = []

    linear_derivatives_long_h_0_te = []
    linear_derivatives_short_h_0_te = []

    # EE derivatives
    linear_derivatives_long_s5_ee = []
    linear_derivatives_short_s5_ee = []

    linear_derivatives_long_s3_5_ee = []
    linear_derivatives_short_s3_5_ee = []

    linear_derivatives_long_s6_5_ee = []
    linear_derivatives_short_s6_5_ee = []

    linear_derivatives_long_s8_ee = []
    linear_derivatives_short_s8_ee = []

    linear_derivatives_long_omega_b_ee = []
    linear_derivatives_short_omega_b_ee = []

    linear_derivatives_long_omega_m_ee = []
    linear_derivatives_short_omega_m_ee = []

    linear_derivatives_long_h_0_ee = []
    linear_derivatives_short_h_0_ee = []


    i = 0
    while i < len(axis):
        linear_derivatives_long_s5_tt.append( (data_high_long_s5_tt[i] - data_low_long_s5_tt[i]) / 2.0e-6 )
        linear_derivatives_short_s5_tt.append( (data_high_short_s5_tt[i] - data_low_short_s5_tt[i]) / 2.0e-7 )
        linear_derivatives_long_s3_5_tt.append( (data_high_long_s3_5_tt[i] - data_low_long_s3_5_tt[i]) / 2.0e-6 )
        linear_derivatives_short_s3_5_tt.append( (data_high_short_s3_5_tt[i] - data_low_short_s3_5_tt[i]) / 2.0e-7 )
        linear_derivatives_long_s8_tt.append( (data_high_long_s8_tt[i] - data_low_long_s8_tt[i]) / 2.0e-6 )
        linear_derivatives_short_s8_tt.append( (data_high_short_s8_tt[i] - data_low_short_s8_tt[i]) / 2.0e-7 )
        linear_derivatives_long_s6_5_tt.append( (data_high_long_s6_5_tt[i] - data_low_long_s6_5_tt[i]) / 2.0e-6 )
        linear_derivatives_short_s6_5_tt.append( (data_high_short_s6_5_tt[i] - data_low_short_s6_5_tt[i]) / 2.0e-7 )
        linear_derivatives_long_omega_b_tt.append( (data_high_long_omega_b_tt[i] - data_low_long_omega_b_tt[i]) / 2.0e-2 )
        linear_derivatives_short_omega_b_tt.append( (data_high_short_omega_b_tt[i] - data_low_short_omega_b_tt[i]) / 2.0e-3 )
        linear_derivatives_long_omega_m_tt.append( (data_high_long_omega_m_tt[i] - data_low_long_omega_m_tt[i]) / 2.0e-2 )
        linear_derivatives_short_omega_m_tt.append( (data_high_short_omega_m_tt[i] - data_low_short_omega_m_tt[i]) / 2.0e-3 )
        linear_derivatives_long_h_0_tt.append( (data_high_long_h_0_tt[i] - data_low_long_h_0_tt[i]) / 2.0e-2 )
        linear_derivatives_short_h_0_tt.append( (data_high_short_h_0_tt[i] - data_low_short_h_0_tt[i]) / 2.0e-3 )


        linear_derivatives_long_s5_ee.append( (data_high_long_s5_ee[i] - data_low_long_s5_ee[i]) / 2.0e-6 )
        linear_derivatives_short_s5_ee.append( (data_high_short_s5_ee[i] - data_low_short_s5_ee[i]) / 2.0e-7 )
        linear_derivatives_long_s3_5_ee.append( (data_high_long_s3_5_ee[i] - data_low_long_s3_5_ee[i]) / 2.0e-6 )
        linear_derivatives_short_s3_5_ee.append( (data_high_short_s3_5_ee[i] - data_low_short_s3_5_ee[i]) / 2.0e-7 )
        linear_derivatives_long_s8_ee.append( (data_high_long_s8_ee[i] - data_low_long_s8_ee[i]) / 2.0e-6 )
        linear_derivatives_short_s8_ee.append( (data_high_short_s8_ee[i] - data_low_short_s8_ee[i]) / 2.0e-7 )
        linear_derivatives_long_s6_5_ee.append( (data_high_long_s6_5_ee[i] - data_low_long_s6_5_ee[i]) / 2.0e-6 )
        linear_derivatives_short_s6_5_ee.append( (data_high_short_s6_5_ee[i] - data_low_short_s6_5_ee[i]) / 2.0e-7 )
        linear_derivatives_long_omega_b_ee.append( (data_high_long_omega_b_ee[i] - data_low_long_omega_b_ee[i]) / 2.0e-2 )
        linear_derivatives_short_omega_b_ee.append( (data_high_short_omega_b_ee[i] - data_low_short_omega_b_ee[i]) / 2.0e-3 )
        linear_derivatives_long_omega_m_ee.append( (data_high_long_omega_m_ee[i] - data_low_long_omega_m_ee[i]) / 2.0e-2 )
        linear_derivatives_short_omega_m_ee.append( (data_high_short_omega_m_ee[i] - data_low_short_omega_m_ee[i]) / 2.0e-3 )
        linear_derivatives_long_h_0_ee.append( (data_high_long_h_0_ee[i] - data_low_long_h_0_ee[i]) / 2.0e-2 )
        linear_derivatives_short_h_0_ee.append( (data_high_short_h_0_ee[i] - data_low_short_h_0_ee[i]) / 2.0e-3 )

        linear_derivatives_long_s5_te.append( (data_high_long_s5_te[i] - data_low_long_s5_te[i]) / 2.0e-6 )
        linear_derivatives_short_s5_te.append( (data_high_short_s5_te[i] - data_low_short_s5_te[i]) / 2.0e-7 )
        linear_derivatives_long_s3_5_te.append( (data_high_long_s3_5_te[i] - data_low_long_s3_5_te[i]) / 2.0e-6 )
        linear_derivatives_short_s3_5_te.append( (data_high_short_s3_5_te[i] - data_low_short_s3_5_te[i]) / 2.0e-7 )
        linear_derivatives_long_s8_te.append( (data_high_long_s8_te[i] - data_low_long_s8_te[i]) / 2.0e-6 )
        linear_derivatives_short_s8_te.append( (data_high_short_s8_te[i] - data_low_short_s8_te[i]) / 2.0e-7 )
        linear_derivatives_long_s6_5_te.append( (data_high_long_s6_5_te[i] - data_low_long_s6_5_te[i]) / 2.0e-6 )
        linear_derivatives_short_s6_5_te.append( (data_high_short_s6_5_te[i] - data_low_short_s6_5_te[i]) / 2.0e-7 )
        linear_derivatives_long_omega_b_te.append( (data_high_long_omega_b_te[i] - data_low_long_omega_b_te[i]) / 2.0e-2 )
        linear_derivatives_short_omega_b_te.append( (data_high_short_omega_b_te[i] - data_low_short_omega_b_te[i]) / 2.0e-3 )
        linear_derivatives_long_omega_m_te.append( (data_high_long_omega_m_te[i] - data_low_long_omega_m_te[i]) / 2.0e-2 )
        linear_derivatives_short_omega_m_te.append( (data_high_short_omega_m_te[i] - data_low_short_omega_m_te[i]) / 2.0e-3 )
        linear_derivatives_long_h_0_te.append( (data_high_long_h_0_te[i] - data_low_long_h_0_te[i]) / 2.0e-2 )
        linear_derivatives_short_h_0_te.append( (data_high_short_h_0_te[i] - data_low_short_h_0_te[i]) / 2.0e-3 )

        i += 1

# List inputs for instrument noise. Format is [ 'name', noise, fwhm, f_sky ]. This preserves some data in global variables for verbose feedback outside of the covariance matrix function calls (this way no hard coding of print statements is required)
default = [ 'DEFAULT values', 54., 5., 1. ]         # default values are Planck 217, but I want them defined seperately. Doesn't hurt anything.
planck_143a = ['Planck 143 GHz A', 37., 7.1, 0.65 ]     # Dan listed two different values (called A and B in this code) for different bolometers in Planck. Unless you've been told otherwise, use the B values, which are a more conservative estimate (more noise)
planck_143b = ['Planck 143 GHz B', 78., 7.1, 0.65 ]
planck_217a = ['Planck 217 GHz A', 54., 5., 0.65 ]        # two noise values are given for planck. I've called the lower one A and the upper one B. Not sure what to make of it right now, so just defining them both
planck_217b = ['Planck 217 GHz B', 119., 5., 0.65 ]
wmap_v = ['WMAP V Band', 434., 21., 0.65]
wmap_w = ['WMAP W Band', 409., 13., 0.65]
act_pol = ['Atacama Cosmology Telescope', 8.9, 1.4, 0.097]
spt_3g = ['South Pole Telescope', 2.5, 1.1, 0.06]
cmb_s4 = ['CMB Stage 4', 1.0, 3.0, 0.50]
cvl_test = ['Cosmic Variance LIMIT (test for convergence)', 0., 0., 1.]

# This function simply generates the cosmic variance for a power spectrum
def cosmic_variance(axis,data):
    return data*np.sqrt( 2. / (2.*axis + 1.) )

# This function emulates arXiv 1505.00639, eqn. 47. It generates an approxomation of instrument noise for a given instrument
def instrument_noise(axis,data,input_source=default):
    # Default values are for Planck at 217 GHz; FWHM = 5.0 [arcmin]     NOISE = 54.0 [uK arcmin]

    # Conversion from uK arcmin into uK radian (for noise)
    # This gets squared below
    noise = input_source[1]
    noise = noise*(np.pi/180.)*(1./60.)    # coordinate conversion. The paper lists

    # Conversion from arcmin into radian (for beam fwhm)
    fwhm = input_source[2]
    fwhm = fwhm*(np.pi/180.)*(1./60.)   # paper gives arcmin, but radians are the SI unit, and I don't belive in doing any kind of math not in SI units. It's the easiest way to mess something up. Don't believe me? ask the not one but two landers we've crashed into mars because of stuff like this

    # need to convert from C_L to D_L so multiple the whole enchelada by (L(L+1)) / 2pi...
    return ((axis*(axis+1.))/(2.*np.pi))*(noise**2.)*np.exp( (axis*(axis+1.)*(fwhm**2.))/(5.545177) )

    # As a reminder, this all follows from 1505.00639 (see table 3 and eqn 47)

# This function combines the cosmic_variance() and instrument_noise() functions, adding their squares and taking a sqare root. Error contributions are uncorrelated, so nothing fancy
def combined_noise(axis,data,input_source=default):
    return np.sqrt( instrument_noise(axis,data,input_source)**2. + cosmic_variance(axis,data)**2. )

# This function is intended to emulate arXiv 0911.3105, eqn. 27 (on page 21)
# 3/26/18: we are removing the BB components entirely. I thought leaving them as zero would be fine, but it makes the matrix non-invertable down the road.
# ...Since we're not actually using them, it's easier to dump them entirely. They'll be commented out.
# ...I have, however, left the default bb_spec option in the function arguments. It's nice if we ever want to uncomment bb modes, and isn't hurting anyone
# 4/21/18: apparently, the functions don't take a bb_spec argument anymore. I can't remember taking that out, but I must havve when I got it working as a 3x3 matrix instead of a 4x4...
def covariance_matrix(axis, tt_spec, te_spec, ee_spec):
    # Function requires an ell axis, as well as a tt, te, ee spectra with the same length as the axis. bb spec is optional, and will set to zero if not given
    C_L = np.zeros( (len(axis),3,3), dtype=float )          # creates a 3d array for the covariance of dimensions 3x3x(number of ell's). For any given C_L, we need a rank 2 tensor


    # With our array generated in the desired shape, we now use a loop to populate each matrix
    # This is a perfectly diagonal matrix, so we could probably skip some of the steps below. For the first pass, however, I'd like to make everything explicit. We can worry about optimization later
    i = 0
    while i < len(axis):
        f = 2. / (2.*axis[i] + 1.)                     # Define the pre factor for each C_L
        C_L[i][0][0] = f*tt_spec[i]**2.
        C_L[i][0][1] = f*te_spec[i]**2.
        C_L[i][0][2] = f*tt_spec[i]*te_spec[i]
        #C_L[i][0][3] = 0
        C_L[i][1][0] = f*te_spec[i]**2.
        C_L[i][1][1] = f*ee_spec[i]**2.
        C_L[i][1][2] = f*ee_spec[i]*te_spec[i]
        #C_L[i][1][3] = 0.
        C_L[i][2][0] = f*tt_spec[i]*te_spec[i]
        C_L[i][2][1] = f*ee_spec[i]*te_spec[i]
        C_L[i][2][2] = f*0.5*( (te_spec[i]**2.) + (tt_spec[i]*ee_spec[i]) )
        #C_L[i][2][3] = 0.
        #C_L[i][3][0] = 0.
        #C_L[i][3][1] = 0.
        #C_L[i][3][2] = 0.
        #C_L[i][3][3] = f*bb_spec[i]**2.

        i += 1

    return C_L

# This function will insert the instrument error sources into the matrix and return uncertainty accordingly. covariance_matrix() returns matrix with ONLY cosmic variance, while covariance_mateix_err() returns matrix with cosmic variance AND instrument noise
def covariance_matrix_err(axis, tt_spec, te_spec, ee_spec, input_source=default):
    # Function requires an ell axis, as well as a tt, te, ee spectra with the same length as the axis. bb spec is optional, and will set to zero if not given
    C_L = np.zeros( (len(axis),3,3), dtype=float )          # creates a 3d array for the covariance of dimensions 4x4x(number of ell's). For any given C_L, we need a rank 2 tensor

    f_sky = input_source[3]  # we only need to defined f_sky within THIS function. noise and fwhm are passed on to the combined_noise (which in turn passes on), but aren't touched here

    print(' ')
    print('Running covariance_matrix_err() function...')
    print('------------INPUTS------------')
    print('Instrument Used: '+str(input_source[0]))
    print('Noise Input [uK arcmin]: '+str(input_source[1]))
    print('Instrument FWHM [arcmin]: '+str(input_source[2]))
    print('Sky Fraction (f_sky): '+str(input_source[3]))
    #print('DEFAULT values are for Planck at 217 GHz;     FWHM = 5.0 [arcmin] and NOISE = 54.0 [uK arcmin]')

    tt_error = combined_noise(axis,tt_spec,input_source)
    te_error = np.zeros( len(axis), dtype='float' )        # no instrument (new) noise for te spectrum, cosmic var is already in C_L matrix
    ee_error = combined_noise(axis,ee_spec,input_source)

    # With our array generated in the desired shape, we now use a loop to populate each matrix
    # This is a perfectly diagonal matrix, so we could probably skip some of the steps below. For the first pass, however, I'd like to make everything explicit. We can worry about optimization later
    i = 0
    while i < len(axis):
        f = 2. / (2.*axis[i] + 1.)                     # Define the pre factor for each C_L
        C_L[i][0][0] = f*(tt_spec[i]+tt_error[i])**2.
        C_L[i][0][1] = f*(te_spec[i]+te_error[i])**2.
        C_L[i][0][2] = f*(tt_spec[i]+tt_error[i])*(te_spec[i]+te_error[i])
        #C_L[i][0][3] = 0.      # bb info, left commented for completeness, but will never be used
        C_L[i][1][0] = f*(te_spec[i]+te_error[i])**2.
        C_L[i][1][1] = f*(ee_spec[i]+ee_error[i])**2.
        C_L[i][1][2] = f*(ee_spec[i]+ee_error[i])*(te_spec[i]+te_error[i])
        #C_L[i][1][3] = 0.      # bb info, left commented for completeness, but will never be used
        C_L[i][2][0] = f*(tt_spec[i]+tt_error[i])*(te_spec[i]+te_error[i])
        C_L[i][2][1] = f*(ee_spec[i]+ee_error[i])*(te_spec[i]+te_error[i])
        C_L[i][2][2] = f*0.5*( ((te_spec[i]+te_error[i])**2.) + ((tt_spec[i]+tt_error[i])*(ee_spec[i]+ee_error[i])) )
        #C_L[i][2][3] = 0.      # bb info, left commented for completeness, but will never be used
        #C_L[i][3][0] = 0.      # bb info, left commented for completeness, but will never be used
        #C_L[i][3][1] = 0.      # bb info, left commented for completeness, but will never be used
        #C_L[i][3][2] = 0.      # bb info, left commented for completeness, but will never be used
        #C_L[i][3][3] = f*bb_spec[i]**2.        # bb info, left commented for completeness, but will never be used

        i += 1

    C_L = C_L*(1./f_sky)    # adds the correction factor for an f_sky less than one. Note that for f_sky =1, nothing happens. from 0911.3105 eq. 29

    return C_L

# Defining the fisher information function. Could use this function multiuple times to populate a fisher matrix. This  function is intended to emulate arXiv 0911.3105, eqn. 26 (on page 20)
# This function takes an axis, power spectra, and derivatives for parameters i and j. For i=j, this simplifies in theory (not programmed). Also takes a covariance matrix.
def fisher_information(axis, tt_spec, te_spec, ee_spec, tt_derivatives_i, te_derivatives_i, ee_derivatives_i, tt_derivatives_j, te_derivatives_j, ee_derivatives_j ):
    # We're forming a 4x4xL matrix again, but I'm avoiding using super pythonic loops for the same reason as before: accuracy is more important than optimization.
    # ... there are only sixteen entries, so I'm writing each one explicitly. To be honest the 3d array scares me, and the indexing can be a challenge.

    C_L = covariance_matrix(axis, tt_spec, te_spec, ee_spec)       # references previous function
    C_L_inv = np.zeros( (len(axis),3,3), dtype=float )                      # just an empty array

    # Need to take the inverses of C_L matrices at all L values. Best way to do this is loop. matrix is not invertible if we keep BB modes (too many zeros, then Det = 0 and it all breaks)
    i=0
    while i < len(axis):
        C_L_inv[i] = np.linalg.inv(C_L[i])
        i+=1

    # This takes the format entry_X_Y to link up with eqn. 26. The X derivatives go with param_i, and the Y derivatives go with param_j
    entry_tt_tt = 0.
    entry_tt_te = 0.
    entry_tt_ee = 0.
    entry_tt_bb = 0.
    entry_te_tt = 0.
    entry_te_te = 0.
    entry_te_ee = 0.
    entry_te_bb = 0.
    entry_ee_tt = 0.
    entry_ee_te = 0.
    entry_ee_ee = 0.
    entry_ee_bb = 0.
    entry_bb_tt = 0.
    entry_bb_te = 0.
    entry_bb_ee = 0.
    entry_bb_bb = 0.

    i=0
    while i < len(axis):        # once again, BB modes are commented out but not removed entirely.
        entry_tt_tt += tt_derivatives_i[i]*tt_derivatives_j[i]*(C_L_inv[i][0][0])
        entry_tt_te += tt_derivatives_i[i]*te_derivatives_j[i]*(C_L_inv[i][0][1])
        entry_tt_ee += tt_derivatives_i[i]*ee_derivatives_j[i]*(C_L_inv[i][0][2])
        #entry_tt_bb += tt_derivatives_i[i]*bb_derivatives_j[i]*(C_L_inv[i][0][3])      # possible div by zero issues
        entry_te_tt += te_derivatives_i[i]*tt_derivatives_j[i]*(C_L_inv[i][1][0])
        entry_te_te += te_derivatives_i[i]*te_derivatives_j[i]*(C_L_inv[i][1][1])
        entry_te_ee += te_derivatives_i[i]*ee_derivatives_j[i]*(C_L_inv[i][1][2])
        #entry_te_bb += te_derivatives_i[i]*bb_derivatives_j[i]*(C_L_inv[i][1][3])      # possible div by zero issues
        entry_ee_tt += ee_derivatives_i[i]*tt_derivatives_j[i]*(C_L_inv[i][2][0])
        entry_ee_te += ee_derivatives_i[i]*te_derivatives_j[i]*(C_L_inv[i][2][1])
        entry_ee_ee += ee_derivatives_i[i]*ee_derivatives_j[i]*(C_L_inv[i][2][2])
        #entry_ee_bb += ee_derivatives_i[i]*bb_derivatives_j[i]*(C_L_inv[i][2][3])      # possible div by zero issues
        #entry_bb_tt += bb_derivatives_i[i]*tt_derivatives_j[i]*(C_L_inv[i][3][0])      # possible div by zero issues
        #entry_bb_te += bb_derivatives_i[i]*te_derivatives_j[i]*(C_L_inv[i][3][1])      # possible div by zero issues
        #entry_bb_ee += bb_derivatives_i[i]*ee_derivatives_j[i]*(C_L_inv[i][3][2])      # possible div by zero issues
        #entry_bb_bb += bb_derivatives_i[i]*bb_derivatives_j[i]*(C_L_inv[i][3][3])      # possible div by zero issues

        i += 1

    information = entry_tt_tt + entry_tt_te + entry_tt_ee + entry_tt_bb + entry_te_tt + entry_te_te + entry_te_ee + entry_te_bb + entry_ee_tt + entry_ee_te + entry_ee_ee + entry_ee_bb + entry_bb_tt + entry_bb_te + entry_bb_ee + entry_bb_bb

    return information

# same deal, uses noise
def fisher_information1(axis, tt_spec, te_spec, ee_spec, tt_derivatives_i, te_derivatives_i, ee_derivatives_i, tt_derivatives_j, te_derivatives_j, ee_derivatives_j ):
    # We're forming a 4x4xL matrix again, but I'm avoiding using super pythonic loops for the same reason as before: accuracy is more important than optimization.
    # ... there are only sixteen entries, so I'm writing each one explicitly. To be honest the 3d array scares me, and the indexing can be a challenge.

    C_L = covariance_matrix_err(axis, tt_spec, te_spec, ee_spec)       # references previous function
    C_L_inv = np.zeros( (len(axis),3,3), dtype=float )                      # just an empty array

    # Need to take the inverses of C_L matrices at all L values. Best way to do this is loop
    i=0
    while i < len(axis):
        C_L_inv[i] = np.linalg.inv(C_L[i])
        i+=1

    # This takes the format entry_X_Y to link up with eqn. 26. The X derivatives go with param_i, and the Y derivatives go with param_j
    entry_tt_tt = 0.
    entry_tt_te = 0.
    entry_tt_ee = 0.
    entry_tt_bb = 0.
    entry_te_tt = 0.
    entry_te_te = 0.
    entry_te_ee = 0.
    entry_te_bb = 0.
    entry_ee_tt = 0.
    entry_ee_te = 0.
    entry_ee_ee = 0.
    entry_ee_bb = 0.
    entry_bb_tt = 0.
    entry_bb_te = 0.
    entry_bb_ee = 0.
    entry_bb_bb = 0.

    i=0
    while i < len(axis):
        entry_tt_tt += tt_derivatives_i[i]*tt_derivatives_j[i]*(C_L_inv[i][0][0])
        entry_tt_te += tt_derivatives_i[i]*te_derivatives_j[i]*(C_L_inv[i][0][1])
        entry_tt_ee += tt_derivatives_i[i]*ee_derivatives_j[i]*(C_L_inv[i][0][2])
        #entry_tt_bb += tt_derivatives_i[i]*bb_derivatives_j[i]*(C_L_inv[i][0][3])      # possible div by zero issues
        entry_te_tt += te_derivatives_i[i]*tt_derivatives_j[i]*(C_L_inv[i][1][0])
        entry_te_te += te_derivatives_i[i]*te_derivatives_j[i]*(C_L_inv[i][1][1])
        entry_te_ee += te_derivatives_i[i]*ee_derivatives_j[i]*(C_L_inv[i][1][2])
        #entry_te_bb += te_derivatives_i[i]*bb_derivatives_j[i]*(C_L_inv[i][1][3])      # possible div by zero issues
        entry_ee_tt += ee_derivatives_i[i]*tt_derivatives_j[i]*(C_L_inv[i][2][0])
        entry_ee_te += ee_derivatives_i[i]*te_derivatives_j[i]*(C_L_inv[i][2][1])
        entry_ee_ee += ee_derivatives_i[i]*ee_derivatives_j[i]*(C_L_inv[i][2][2])
        #entry_ee_bb += ee_derivatives_i[i]*bb_derivatives_j[i]*(C_L_inv[i][2][3])      # possible div by zero issues
        #entry_bb_tt += bb_derivatives_i[i]*tt_derivatives_j[i]*(C_L_inv[i][3][0])      # possible div by zero issues
        #entry_bb_te += bb_derivatives_i[i]*te_derivatives_j[i]*(C_L_inv[i][3][1])      # possible div by zero issues
        #entry_bb_ee += bb_derivatives_i[i]*ee_derivatives_j[i]*(C_L_inv[i][3][2])      # possible div by zero issues
        #entry_bb_bb += bb_derivatives_i[i]*bb_derivatives_j[i]*(C_L_inv[i][3][3])      # possible div by zero issues

        i += 1

    information = entry_tt_tt + entry_tt_te + entry_tt_ee + entry_tt_bb + entry_te_tt + entry_te_te + entry_te_ee + entry_te_bb + entry_ee_tt + entry_ee_te + entry_ee_ee + entry_ee_bb + entry_bb_tt + entry_bb_te + entry_bb_ee + entry_bb_bb

    return information

def fisher_information_total(axis, tt_spec, te_spec, ee_spec, tt_derivatives_i, te_derivatives_i, ee_derivatives_i, tt_derivatives_j, te_derivatives_j, ee_derivatives_j, input_source=default ):
    # We're forming a 4x4xL matrix again, but I'm avoiding using super pythonic loops for the same reason as before: accuracy is more important than optimization.
    # ... there are only sixteen entries, so I'm writing each one explicitly. To be honest the 3d array scares me, and the indexing can be a challenge.

    #print('Noise Input [uK arcmin]: '+str(noise))
    #print('Instrument FWHM [arcmin]'+str(fwhm))

    C_L = covariance_matrix_err(axis, tt_spec, te_spec, ee_spec, input_source)       # references previous function
    C_L_inv = np.zeros( (len(axis),3,3), dtype=float )                           # just an empty array

    # Need to take the inverses of C_L matrices at all L values. Best way to do this is loop
    i=0
    while i < len(axis):
        C_L_inv[i] = np.linalg.inv(C_L[i])
        i+=1

    # This takes the format entry_X_Y to link up with eqn. 26. The X derivatives go with param_i, and the Y derivatives go with param_j
    entry_tt_tt = 0.
    entry_tt_te = 0.
    entry_tt_ee = 0.
    entry_tt_bb = 0.
    entry_te_tt = 0.
    entry_te_te = 0.
    entry_te_ee = 0.
    entry_te_bb = 0.
    entry_ee_tt = 0.
    entry_ee_te = 0.
    entry_ee_ee = 0.
    entry_ee_bb = 0.
    entry_bb_tt = 0.
    entry_bb_te = 0.
    entry_bb_ee = 0.
    entry_bb_bb = 0.

    i=0
    while i < len(axis):
        entry_tt_tt += tt_derivatives_i[i]*tt_derivatives_j[i]*(C_L_inv[i][0][0])
        entry_tt_te += tt_derivatives_i[i]*te_derivatives_j[i]*(C_L_inv[i][0][1])
        entry_tt_ee += tt_derivatives_i[i]*ee_derivatives_j[i]*(C_L_inv[i][0][2])
        #entry_tt_bb += tt_derivatives_i[i]*bb_derivatives_j[i]*(C_L_inv[i][0][3])      # possible div by zero issues
        entry_te_tt += te_derivatives_i[i]*tt_derivatives_j[i]*(C_L_inv[i][1][0])
        entry_te_te += te_derivatives_i[i]*te_derivatives_j[i]*(C_L_inv[i][1][1])
        entry_te_ee += te_derivatives_i[i]*ee_derivatives_j[i]*(C_L_inv[i][1][2])
        #entry_te_bb += te_derivatives_i[i]*bb_derivatives_j[i]*(C_L_inv[i][1][3])      # possible div by zero issues
        entry_ee_tt += ee_derivatives_i[i]*tt_derivatives_j[i]*(C_L_inv[i][2][0])
        entry_ee_te += ee_derivatives_i[i]*te_derivatives_j[i]*(C_L_inv[i][2][1])
        entry_ee_ee += ee_derivatives_i[i]*ee_derivatives_j[i]*(C_L_inv[i][2][2])
        #entry_ee_bb += ee_derivatives_i[i]*bb_derivatives_j[i]*(C_L_inv[i][2][3])      # possible div by zero issues
        #entry_bb_tt += bb_derivatives_i[i]*tt_derivatives_j[i]*(C_L_inv[i][3][0])      # possible div by zero issues
        #entry_bb_te += bb_derivatives_i[i]*te_derivatives_j[i]*(C_L_inv[i][3][1])      # possible div by zero issues
        #entry_bb_ee += bb_derivatives_i[i]*ee_derivatives_j[i]*(C_L_inv[i][3][2])      # possible div by zero issues
        #entry_bb_bb += bb_derivatives_i[i]*bb_derivatives_j[i]*(C_L_inv[i][3][3])      # possible div by zero issues

        i += 1

    # Instead of returning a single scalar (the previous code did this), we will return a list containing the F_ij, the sigma_ij, and the inputs used...
    # information[0] : fisher information
    # information[1] : fisher constraint
    # information[2] : instrument name
    # information[3] : instrument noise
    # information[4] : instroment fwhm
    # information[5] : instrument f_sky

    information = []
    information.append( entry_tt_tt + entry_tt_te + entry_tt_ee + entry_tt_bb + entry_te_tt + entry_te_te + entry_te_ee + entry_te_bb + entry_ee_tt + entry_ee_te + entry_ee_ee + entry_ee_bb + entry_bb_tt + entry_bb_te + entry_bb_ee + entry_bb_bb )
    information.append( np.abs(information[0])**(-1./2.) )
    information.append( input_source[0] )
    information.append( input_source[1] )
    information.append( input_source[2] )
    information.append( input_source[3] )


    return information


# LOG S = 3.5    LONG
fisher_information_result = fisher_information_total(axis, data_high_long_s3_5_tt, data_high_long_s3_5_te, data_high_long_s3_5_ee, linear_derivatives_long_s3_5_tt, linear_derivatives_long_s3_5_te, linear_derivatives_long_s3_5_ee, linear_derivatives_long_s3_5_tt, linear_derivatives_long_s3_5_te, linear_derivatives_long_s3_5_ee, cmb_s4)

print(' ')
print('------------COVARIANCE RESULT------------')
print('Log(s) = 3.5, Derivatives=Long. This print line and this line only is HARD CODED so double check it. ') # I'd LOVE a way to make this smarter and modular, so I don't have to write it every time
print('Instrument Used: '+str(fisher_information_result[2]))
print('Noise Input [uK arcmin]: '+str(fisher_information_result[3]))
print('Instrument FWHM [arcmin]: '+str(fisher_information_result[4]))
print('Sky Fraction (f_sky): '+str(fisher_information_result[5]))
print('Fisher Information Result: '+str(fisher_information_result[0]))
print('Best Constraint: '+str(fisher_information_result[1]))
print('------------')
print(' ')



# LOG S = 3.5    SHORT
fisher_info_short_3_5 = fisher_information_total(axis, data_high_short_s3_5_tt, data_high_short_s3_5_te, data_high_short_s3_5_ee, linear_derivatives_short_s3_5_tt, linear_derivatives_short_s3_5_te, linear_derivatives_short_s3_5_ee, linear_derivatives_short_s3_5_tt, linear_derivatives_short_s3_5_te, linear_derivatives_short_s3_5_ee, cmb_s4)

print(' ')
print('------------COVARIANCE RESULT------------')
print('Log(s) = 3.5, Derivatives=Short. This print line and this line only is HARD CODED so double check it. ')
print('Instrument Used: '+str(fisher_info_short_3_5[2]))
print('Noise Input [uK arcmin]: '+str(fisher_info_short_3_5[3]))
print('Instrument FWHM [arcmin]: '+str(fisher_info_short_3_5[4]))
print('Sky Fraction (f_sky): '+str(fisher_info_short_3_5[5]))
print('Fisher Information Result: '+str(fisher_info_short_3_5[0]))
print('Best Constraint: '+str(fisher_info_short_3_5[1]))
print('------------')
print(' ')


# LOG S = 5.0    LONG
fisher_info_long_5 = fisher_information_total(axis, data_high_long_s5_tt, data_high_long_s5_te, data_high_long_s5_ee, linear_derivatives_long_s5_tt, linear_derivatives_long_s5_te, linear_derivatives_long_s5_ee, linear_derivatives_long_s5_tt, linear_derivatives_long_s5_te, linear_derivatives_long_s5_ee, cmb_s4)

print(' ')
print('------------COVARIANCE RESULT------------')
print('Log(s) = 5.0, Derivatives=Long. This print line and this line only is HARD CODED so double check it. ')
print('Instrument Used: '+str(fisher_info_long_5[2]))
print('Noise Input [uK arcmin]: '+str(fisher_info_long_5[3]))
print('Instrument FWHM [arcmin]: '+str(fisher_info_long_5[4]))
print('Sky Fraction (f_sky): '+str(fisher_info_long_5[5]))
print('Fisher Information Result: '+str(fisher_info_long_5[0]))
print('Best Constraint: '+str(fisher_info_long_5[1]))
print('------------')
print(' ')


# LOG S = 5.0    SHORT
fisher_info_short_5 = fisher_information_total(axis, data_high_short_s5_tt, data_high_short_s5_te, data_high_short_s5_ee, linear_derivatives_short_s5_tt, linear_derivatives_short_s5_te, linear_derivatives_short_s5_ee, linear_derivatives_short_s5_tt, linear_derivatives_short_s5_te, linear_derivatives_short_s5_ee, cmb_s4)

print(' ')
print('------------COVARIANCE RESULT------------')
print('Log(s) = 5.0, Derivatives=Short. This print line and this line only is HARD CODED so double check it. ')
print('Instrument Used: '+str(fisher_info_short_5[2]))
print('Noise Input [uK arcmin]: '+str(fisher_info_short_5[3]))
print('Instrument FWHM [arcmin]: '+str(fisher_info_short_5[4]))
print('Sky Fraction (f_sky): '+str(fisher_info_short_5[5]))
print('Fisher Information Result: '+str(fisher_info_short_5[0]))
print('Best Constraint: '+str(fisher_info_short_5[1]))
print('------------')
print(' ')


# LOG S = 6.5    LONG
fisher_info_long_6_5 = fisher_information_total(axis, data_high_long_s6_5_tt, data_high_long_s6_5_te, data_high_long_s6_5_ee, linear_derivatives_long_s6_5_tt, linear_derivatives_long_s6_5_te, linear_derivatives_long_s6_5_ee, linear_derivatives_long_s6_5_tt, linear_derivatives_long_s6_5_te, linear_derivatives_long_s6_5_ee, cvl_test)

print(' ')
print('------------COVARIANCE RESULT------------')
print('Log(s) = 6.5, Derivatives=Long. This print line and this line only is HARD CODED so double check it. ')
print('Instrument Used: '+str(fisher_info_long_6_5[2]))
print('Noise Input [uK arcmin]: '+str(fisher_info_long_6_5[3]))
print('Instrument FWHM [arcmin]: '+str(fisher_info_long_6_5[4]))
print('Sky Fraction (f_sky): '+str(fisher_info_long_6_5[5]))
print('Fisher Information Result: '+str(fisher_info_long_6_5[0]))
print('Best Constraint: '+str(fisher_info_long_6_5[1]))
print('------------')
print(' ')



# LOG S = 3.5    SHORT
fisher_info_short_6_5 = fisher_information_total(axis, data_high_short_s6_5_tt, data_high_short_s6_5_te, data_high_short_s6_5_ee, linear_derivatives_short_s6_5_tt, linear_derivatives_short_s6_5_te, linear_derivatives_short_s6_5_ee, linear_derivatives_short_s6_5_tt, linear_derivatives_short_s6_5_te, linear_derivatives_short_s6_5_ee, cvl_test)

print(' ')
print('------------COVARIANCE RESULT------------')
print('Log(s) = 6.5, Derivatives=Short. This print line and this line only is HARD CODED so double check it. ')
print('Instrument Used: '+str(fisher_info_short_6_5[2]))
print('Noise Input [uK arcmin]: '+str(fisher_info_short_6_5[3]))
print('Instrument FWHM [arcmin]: '+str(fisher_info_short_6_5[4]))
print('Sky Fraction (f_sky): '+str(fisher_info_short_6_5[5]))
print('Fisher Information Result: '+str(fisher_info_short_6_5[0]))
print('Best Constraint: '+str(fisher_info_short_6_5[1]))
print('------------')
print(' ')


# LOG S = 8.0    LONG
fisher_info_long_8 = fisher_information_total(axis, data_high_long_s8_tt, data_high_long_s8_te, data_high_long_s8_ee, linear_derivatives_long_s8_tt, linear_derivatives_long_s8_te, linear_derivatives_long_s8_ee, linear_derivatives_long_s8_tt, linear_derivatives_long_s8_te, linear_derivatives_long_s8_ee, cmb_s4)

print(' ')
print('------------COVARIANCE RESULT------------')
print('Log(s) = 8.0, Derivatives=Long. This print line and this line only is HARD CODED so double check it. ')
print('Instrument Used: '+str(fisher_info_long_8[2]))
print('Noise Input [uK arcmin]: '+str(fisher_info_long_8[3]))
print('Instrument FWHM [arcmin]: '+str(fisher_info_long_8[4]))
print('Sky Fraction (f_sky): '+str(fisher_info_long_8[5]))
print('Fisher Information Result: '+str(fisher_info_long_8[0]))
print('Best Constraint: '+str(fisher_info_long_8[1]))
print('------------')
print(' ')


# LOG S = 8.0    SHORT
fisher_info_short_8 = fisher_information_total(axis, data_high_short_s8_tt, data_high_short_s8_te, data_high_short_s8_ee, linear_derivatives_short_s8_tt, linear_derivatives_short_s8_te, linear_derivatives_short_s8_ee, linear_derivatives_short_s8_tt, linear_derivatives_short_s8_te, linear_derivatives_short_s8_ee, cmb_s4)

print(' ')
print('------------COVARIANCE RESULT------------')
print('Log(s) = 8.0, Derivatives=Short. This print line and this line only is HARD CODED so double check it. ')
print('Instrument Used: '+str(fisher_info_short_8[2]))
print('Noise Input [uK arcmin]: '+str(fisher_info_short_8[3]))
print('Instrument FWHM [arcmin]: '+str(fisher_info_short_8[4]))
print('Sky Fraction (f_sky): '+str(fisher_info_short_8[5]))
print('Fisher Information Result: '+str(fisher_info_short_8[0]))
print('Best Constraint: '+str(fisher_info_short_8[1]))
print('------------')
print(' ')


# LOG S = 8.0    SHORT
additional = fisher_information_total(axis, data_nominal_tt, data_nominal_te, data_nominal_ee, linear_derivatives_long_s8_tt, linear_derivatives_long_s8_te, linear_derivatives_long_s8_ee, linear_derivatives_long_h_0_tt, linear_derivatives_long_h_0_te, linear_derivatives_long_h_0_ee, planck_217b)

print(' ')
print('------------COVARIANCE RESULT------------')
print('Extra one for fun. This print line and this line only is HARD CODED so double check it. ')
print('Instrument Used: '+str(additional[2]))
print('Noise Input [uK arcmin]: '+str(additional[3]))
print('Instrument FWHM [arcmin]: '+str(additional[4]))
print('Sky Fraction (f_sky): '+str(additional[5]))
print('Fisher Information Result: '+str(additional[0]))
print('Best Constraint: '+str(additional[1]))
print('------------')
print(' ')














'''
# WMAP W Band is FWHM=21 arcmin, noise=434 uK
wmap_w_info = fisher_information_total(axis, data_high_long_s3_5_tt, data_high_long_s3_5_te, data_high_long_s3_5_ee, linear_derivatives_long_s5_tt, linear_derivatives_long_s5_te, linear_derivatives_long_s5_ee, linear_derivatives_long_s5_tt, linear_derivatives_long_s5_te, linear_derivatives_long_s5_ee, wmap_v)

print(' ')
print('------------COVARIANCE RESULT------------')
print('Instrument Used: '+str(wmap_w_info[2]))
print('Noise Input [uK arcmin]: '+str(wmap_w_info[3]))
print('Instrument FWHM [arcmin]: '+str(wmap_w_info[4]))
print('Sky Fraction (f_sky): '+str(wmap_w_info[5]))
print('Fisher Information Result: '+str(wmap_w_info[0]))
print('Best Constraint: '+str(wmap_w_info[1]))
print('------------')
print(' ')

cvl_test_info = fisher_information_total(axis, data_high_long_s3_5_tt, data_high_long_s3_5_te, data_high_long_s3_5_ee, linear_derivatives_long_s5_tt, linear_derivatives_long_s5_te, linear_derivatives_long_s5_ee, linear_derivatives_long_s5_tt, linear_derivatives_long_s5_te, linear_derivatives_long_s5_ee, cvl_test)

print(' ')
print('------------COVARIANCE RESULT------------')
print('Instrument Used: '+str(cvl_test_info[2]))
print('Noise Input [uK arcmin]: '+str(cvl_test_info[3]))
print('Instrument FWHM [arcmin]: '+str(cvl_test_info[4]))
print('Sky Fraction (f_sky): '+str(cvl_test_info[5]))
print('Fisher Information Result: '+str(cvl_test_info[0]))
print('Best Constraint: '+str(cvl_test_info[1]))
print('------------')
print(' ')
'''
