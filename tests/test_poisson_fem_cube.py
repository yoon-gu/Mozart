import numpy as np
import numpy.testing as npt
from numpy import linalg as LA

def test_compute_n4s():
	from mozart.poisson.fem.cube import compute_n4s
	n4e = np.array([[0, 1, 4, 3, 6, 7, 10, 9], [1, 2, 5, 4, 7, 8, 11, 10]])
	n4s = compute_n4s(n4e)
	ref_n4s = np.array([[ 0,  1], [ 1,  2], [ 1,  4], [ 2,  5], [ 4,  3], 
		[ 5,  4], [ 3,  0], [ 0,  6], [ 1,  7], [ 2,  8], [ 4, 10], 
		[ 5, 11], [ 3,  9], [ 6,  7], [ 7,  8], [ 7, 10], [ 8, 11], 
		[10,  9], [11, 10], [ 9,  6]], dtype = int)
	npt.assert_almost_equal(n4s, ref_n4s, decimal=8)

def test_compute_s4e():
	from mozart.poisson.fem.cube import compute_s4e
	n4e = np.array([[0, 1, 4, 3, 6, 7, 10, 9], [1, 2, 5, 4, 7, 8, 11, 10]])
	s4e = compute_s4e(n4e)
	ref_s4e = np.array([[ 0,  2,  4,  6,  7,  8, 10, 12, 13, 15, 17, 19],
				[ 1,  3,  5,  2,  8,  9, 11, 10, 14, 16, 18, 15]], dtype = int)
	npt.assert_almost_equal(s4e, ref_s4e, decimal=8)

def test_compute_n4f():
	from mozart.poisson.fem.cube import compute_n4f
	n4e = np.array([[0, 1, 4, 3, 6, 7, 10, 9], [1, 2, 5, 4, 7, 8, 11, 10]])
	n4f = compute_n4f(n4e)
	ref_n4f = np.array([[ 0,  1,  4,  3], [ 1,  2,  5,  4], [ 0,  1,  7,  6], [ 1,  2,  8,  7], 
				[ 1,  4, 10,  7], [ 2,  5, 11,  8], [ 4,  3,  9, 10], [ 5,  4, 10, 11], 
				[ 3,  0,  6,  9], [ 6,  7, 10,  9], [ 7,  8, 11, 10]], dtype = int)
	npt.assert_almost_equal(n4f, ref_n4f, decimal=8)

def test_compute_f4e():
	from mozart.poisson.fem.cube import compute_f4e
	n4e = np.array([[0, 1, 4, 3, 6, 7, 10, 9], [1, 2, 5, 4, 7, 8, 11, 10]])
	f4e = compute_f4e(n4e)
	ref_f4e = np.array([[ 0,  2,  4,  6,  8,  9],
				[ 1,  3,  5,  7,  4, 10]])
	npt.assert_almost_equal(f4e, ref_f4e, decimal=8)

def test_compute_e4f():
	from mozart.poisson.fem.cube import compute_e4f
	n4e = np.array([[0, 1, 4, 3, 6, 7, 10, 9], [1, 2, 5, 4, 7, 8, 11, 10]])
	e4f = compute_e4f(n4e)
	ref_e4f = np.array([[ 0, -1], [ 0, -1], [ 0, -1], [ 0, -1], [ 0,  1], [ 0, -1], 
				[ 1, -1], [ 1, -1], [ 1, -1], [ 1, -1], [ 1, -1]], dtype = int)
	npt.assert_almost_equal(e4f, ref_e4f, decimal=8)

def test_getIndex():
	from mozart.poisson.fem.cube import getIndex
	c4n = np.array([[0., 0., 0.], [1., 0., 0.], [2., 0., 0.], [0., 1., 0.],
				[1., 1., 0.], [2., 1., 0.], [0., 0., 1.], [1., 0., 1.],
				[2., 0., 1.], [0., 1., 1.], [1., 1., 1.], [2., 1., 1.]])
	n4e = np.array([[0, 1, 4, 3, 6, 7, 10, 9], [1, 2, 5, 4, 7, 8, 11, 10]])
	n4fDb = np.array([[0, 1, 4, 3], [1, 2, 5, 4], [0, 1, 7, 6], [1, 2, 8, 7], [5, 4, 10, 11],
				  [4, 3, 9, 10], [3, 0, 6, 9], [6, 7, 10, 9], [7, 8, 11, 10]])
	n4fNb = np.array([[2, 5, 11, 8]])
	c4nNew, ind4e, ind4Db, ind4Nb = getIndex(3, c4n, n4e, n4fDb, n4fNb)
	ref_c4nNew = np.array([[   0.,   0.,   0.],	[   1.,   0.,   0.], [   2.,   0.,   0.], [   0.,   1.,   0.],
						   [   1.,   1.,   0.],	[   2.,   1.,   0.], [   0.,   0.,   1.], [   1.,   0.,   1.],
						   [   2.,   0.,   1.],	[   0.,   1.,   1.], [   1.,   1.,   1.], [   2.,   1.,   1.],
						   [ 1/3.,   0.,   0.],	[ 2/3.,   0.,   0.], [ 4/3.,   0.,   0.], [ 5/3.,   0.,   0.],
						   [   1., 1/3.,   0.], [   1., 2/3.,   0.], [   2., 1/3.,   0.], [   2., 2/3.,   0.],
						   [ 2/3.,   1.,   0.], [ 1/3.,   1.,   0.], [ 5/3.,   1.,   0.], [ 4/3.,   1.,   0.],
						   [   0., 2/3.,   0.],	[   0., 1/3.,   0.], [   0.,   0., 1/3.], [   0.,   0., 2/3.],
						   [   1.,   0., 1/3.],	[   1.,   0., 2/3.], [   2.,   0., 1/3.], [   2.,   0., 2/3.],
						   [   1.,   1., 1/3.], [   1.,   1., 2/3.], [   2.,   1., 1/3.], [   2.,   1., 2/3.],
						   [   0.,   1., 1/3.],	[   0.,   1., 2/3.], [ 1/3.,   0.,   1.], [ 2/3.,   0.,   1.],
						   [ 4/3.,   0.,   1.],	[ 5/3.,   0.,   1.], [   1., 1/3.,   1.], [   1., 2/3.,   1.],
						   [   2., 1/3.,   1.],	[   2., 2/3.,   1.], [ 2/3.,   1.,   1.], [ 1/3.,   1.,   1.],
						   [ 5/3.,   1.,   1.],	[ 4/3.,   1.,   1.], [   0., 2/3.,   1.], [   0., 1/3.,   1.],
						   [ 1/3., 1/3.,   0.],	[ 2/3., 1/3.,   0.], [ 1/3., 2/3.,   0.], [ 2/3., 2/3.,   0.],
						   [ 4/3., 1/3.,   0.],	[ 5/3., 1/3.,   0.], [ 4/3., 2/3.,   0.], [ 5/3., 2/3.,   0.],
						   [ 1/3.,   0., 1/3.],	[ 2/3.,   0., 1/3.], [ 1/3.,   0., 2/3.], [ 2/3.,   0., 2/3.],
						   [ 4/3.,   0., 1/3.],	[ 5/3.,   0., 1/3.], [ 4/3.,   0., 2/3.], [ 5/3.,   0., 2/3.],
						   [   1., 1/3., 1/3.],	[   1., 2/3., 1/3.], [   1., 1/3., 2/3.], [   1., 2/3., 2/3.],
						   [   2., 1/3., 1/3.],	[   2., 2/3., 1/3.], [   2., 1/3., 2/3.], [   2., 2/3., 2/3.],
						   [ 2/3.,   1., 1/3.],	[ 1/3.,   1., 1/3.], [ 2/3.,   1., 2/3.], [ 1/3.,   1., 2/3.],
						   [ 5/3.,   1., 1/3.],	[ 4/3.,   1., 1/3.], [ 5/3.,   1., 2/3.], [ 4/3.,   1., 2/3.],
						   [   0., 2/3., 1/3.],	[   0., 1/3., 1/3.], [   0., 2/3., 2/3.], [   0., 1/3., 2/3.],
						   [ 1/3., 1/3.,   1.], [ 2/3., 1/3.,   1.], [ 1/3., 2/3.,   1.], [ 2/3., 2/3.,   1.],
						   [ 4/3., 1/3.,   1.],	[ 5/3., 1/3.,   1.], [ 4/3., 2/3.,   1.], [ 5/3., 2/3.,   1.],
						   [ 1/3., 1/3., 1/3.],	[ 2/3., 1/3., 1/3.], [ 1/3., 2/3., 1/3.], [ 2/3., 2/3., 1/3.],
						   [ 1/3., 1/3., 2/3.],	[ 2/3., 1/3., 2/3.], [ 1/3., 2/3., 2/3.], [ 2/3., 2/3., 2/3.],
						   [ 4/3., 1/3., 1/3.],	[ 5/3., 1/3., 1/3.], [ 4/3., 2/3., 1/3.], [ 5/3., 2/3., 1/3.],
						   [ 4/3., 1/3., 2/3.],	[ 5/3., 1/3., 2/3.], [ 4/3., 2/3., 2/3.], [ 5/3., 2/3., 2/3.]], dtype=np.float64)
	ref_ind4e = np.array([[ 0, 12, 13, 1, 25, 52, 53, 16, 24, 54, 55, 17, 3, 21, 20, 4, 26, 60, 61, 28, 85,  96,  
						   97, 68, 84,  98,  99, 69, 36, 77, 76, 32, 27, 62, 63, 29, 87, 100, 101, 70, 86, 102, 
						  103, 71, 37, 79, 78, 33, 6, 38, 39, 7, 51, 88, 89, 42, 50, 90, 91, 43,  9, 47, 46, 10],
						  [ 1, 14, 15, 2, 16, 56, 57, 18, 17, 58, 59, 19, 4, 23, 22, 5, 28, 64, 65, 30, 68, 104, 
						  105, 72, 69, 106, 107, 73, 32, 81, 80, 34, 29, 66, 67, 31, 70, 108, 109, 74, 71, 110, 
						  111, 75, 33, 83, 82, 35, 7, 40, 41, 8, 42, 92, 93, 44, 43, 94, 95, 45, 10, 49, 48, 11]], dtype=int)
	ref_ind4Db = np.array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 
						   24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 
						   46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 
						   76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95], dtype = int)
	ref_ind4Nb = np.array([[ 2, 18, 19, 5, 30, 72, 73, 34, 31, 74, 75, 35, 8, 44, 45, 11]])
	npt.assert_almost_equal(c4nNew, ref_c4nNew, decimal=8)
	npt.assert_almost_equal(ind4e, ref_ind4e, decimal=8)
	npt.assert_almost_equal(ind4Db, ref_ind4Db, decimal=8)
	npt.assert_almost_equal(ind4Nb, ref_ind4Nb, decimal=8)

def test_getPoissonMatrix3D():
	from mozart.poisson.fem.cube import getMatrix
	M_R, M2D_R, Srr_R, Sss_R, Stt_R, Dr_R, Ds_R, Dt_R = getMatrix(1)
	ref_M_R = np.array([[8, 4, 4, 2, 4, 2, 2, 1],
				       [4, 8, 2, 4, 2, 4, 1, 2],
				       [4, 2, 8, 4, 2, 1, 4, 2],
				       [2, 4, 4, 8, 1, 2, 2, 4],
				       [4, 2, 2, 1, 8, 4, 4, 2],
				       [2, 4, 1, 2, 4, 8, 2, 4],
				       [2, 1, 4, 2, 4, 2, 8, 4],
				       [1, 2, 2, 4, 2, 4, 4, 8]]) / 27.
	ref_M2D_R = np.array([[4, 2, 2, 1],  [2, 4, 1, 2],  
						 [2, 1, 4, 2],  [1, 2, 2, 4]]) / 9.
	ref_Srr_R = np.array([[ 4, -4,  2, -2,  2, -2,  1, -1],
						 [-4,  4, -2,  2, -2,  2, -1,  1],
						 [ 2, -2,  4, -4,  1, -1,  2, -2],
						 [-2,  2, -4,  4, -1,  1, -2,  2],
						 [ 2, -2,  1, -1,  4, -4,  2, -2],
						 [-2,  2, -1,  1, -4,  4, -2,  2],
						 [ 1, -1,  2, -2,  2, -2,  4, -4],
						 [-1,  1, -2,  2, -2,  2, -4,  4 ]]) / 18.
	ref_Sss_R = np.array([[ 4,  2, -4, -2,  2,  1, -2, -1],
						 [ 2,  4, -2, -4,  1,  2, -1, -2],
						 [-4, -2,  4,  2, -2, -1,  2,  1],
						 [-2, -4,  2,  4, -1, -2,  1,  2],
						 [ 2,  1, -2, -1,  4,  2, -4, -2],
						 [ 1,  2, -1, -2,  2,  4, -2, -4],
						 [-2, -1,  2,  1, -4, -2,  4,  2],
						 [-1, -2,  1,  2, -2, -4,  2,  4]]) / 18.
	ref_Stt_R = np.array([[ 4,  2,  2,  1, -4, -2, -2, -1],
						 [ 2,  4,  1,  2, -2, -4, -1, -2],
						 [ 2,  1,  4,  2, -2, -1, -4, -2],
						 [ 1,  2,  2,  4, -1, -2, -2, -4],
						 [-4, -2, -2, -1,  4,  2,  2,  1],
						 [-2, -4, -1, -2,  2,  4,  1,  2],
						 [-2, -1, -4, -2,  2,  1,  4,  2],
						 [-1, -2, -2, -4,  1,  2,  2,  4]]) / 18.
	ref_Dr_R = np.array([[-1, 1,  0, 0,  0, 0,  0, 0],
						[-1, 1,  0, 0,  0, 0,  0, 0],
						[ 0, 0, -1, 1,  0, 0,  0, 0],
						[ 0, 0, -1, 1,  0, 0,  0, 0],
						[ 0, 0,  0, 0, -1, 1,  0, 0],
						[ 0, 0,  0, 0, -1, 1,  0, 0],
						[ 0, 0,  0, 0,  0, 0, -1, 1],
						[ 0, 0,  0, 0,  0, 0, -1, 1]]) / 2.
	ref_Ds_R = np.array([[-1,  0, 1, 0,  0,  0, 0, 0],
						[ 0, -1, 0, 1,  0,  0, 0, 0],
						[-1,  0, 1, 0,  0,  0, 0, 0],
						[ 0, -1, 0, 1,  0,  0, 0, 0],
						[ 0,  0, 0, 0, -1,  0, 1, 0],
						[ 0,  0, 0, 0,  0, -1, 0, 1],
						[ 0,  0, 0, 0, -1,  0, 1, 0],
						[ 0,  0, 0, 0,  0, -1, 0, 1]]) / 2.
	ref_Dt_R = np.array([[-1,  0,  0,  0, 1, 0, 0, 0],
						[ 0, -1,  0,  0, 0, 1, 0, 0],
						[ 0,  0, -1,  0, 0, 0, 1, 0],
						[ 0,  0,  0, -1, 0, 0, 0, 1],
						[-1,  0,  0,  0, 1, 0, 0, 0],
						[ 0, -1,  0,  0, 0, 1, 0, 0],
						[ 0,  0, -1,  0, 0, 0, 1, 0],
						[ 0,  0,  0, -1, 0, 0, 0, 1]]) / 2.
	npt.assert_almost_equal(M_R, ref_M_R, decimal=8)
	npt.assert_almost_equal(M2D_R, ref_M2D_R, decimal=8)
	npt.assert_almost_equal(Srr_R, ref_Srr_R, decimal=8)
	npt.assert_almost_equal(Sss_R, ref_Sss_R, decimal=8)
	npt.assert_almost_equal(Stt_R, ref_Stt_R, decimal=8)
	npt.assert_almost_equal(Dr_R, ref_Dr_R, decimal=8)
	npt.assert_almost_equal(Ds_R, ref_Ds_R, decimal=8)
	npt.assert_almost_equal(Dt_R, ref_Dt_R, decimal=8)

def test_solve():
	from mozart.poisson.fem.cube import getIndex, getMatrix, solve
	N = 3
	c4n = np.array([[0., 0., 0.], [1., 0., 0.], [0., 1., 0.], [1., 1., 0.],
					[0., 0., 1.], [1., 0., 1.], [0., 1., 1.], [1., 1., 1.]])
	n4e = np.array([[0, 1, 3, 2, 4, 5, 7, 6]])
	n4fDb = np.array([[0, 1, 3, 2], [0, 1, 5, 4], [2, 0, 4, 6], [4, 5, 7, 6]])
	n4fNb = np.array([[1, 3, 7, 5]])
	c4nNew, ind4e, ind4Db, ind4Nb = getIndex(N, c4n, n4e, n4fDb, n4fNb)
	M_R, M2D_R, Srr_R, Sss_R, Stt_R, Dr_R, Ds_R, Dt_R = getMatrix(N)
	f = (lambda x, y, z: 3 * np.pi**2 * np.sin(np.pi * x) * np.sin(np.pi * y) * np.sin(np.pi * z))
	u_D = (lambda x, y, z: x * 0)
	u_N = (lambda x, y, z: np.pi * np.cos(np.pi * x) * np.sin(np.pi * y) * np.sin(np.pi * z))
	x = solve(c4nNew, n4e, ind4e, ind4Db, ind4Nb, M_R, Srr_R, Sss_R, Stt_R, M2D_R, f, u_D, u_N, N)
	ref_x = np.array([ 0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
					   0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
					   0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
					   0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
					   0.36673102,  0.36673102,  0.        ,  0.        ,  0.        ,
					   0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
					   0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
					   0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
					   0.06209753,  0.1873742 ,  0.06209753,  0.1873742 ,  0.61071588,
					   0.55509583,  0.61071588,  0.55509583,  0.        ,  0.        ,
					   0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
					   0.        ,  0.67471301,  0.69313957,  0.77159936,  0.81732792,
					   0.67471301,  0.69313957,  0.77159936,  0.81732792])

	npt.assert_almost_equal(x, ref_x, decimal=8)

def test_Error():
	from mozart.poisson.fem.cube import getIndex, getMatrix, solve, Error, refineUniformRed
	iter = 3

	f = (lambda x, y, z: 3 * np.pi**2 * np.sin(np.pi * x) * np.sin(np.pi * y) * np.sin(np.pi * z))
	u_D = (lambda x, y, z: x * 0)
	u_exact = (lambda x, y, z: np.sin(np.pi * x) * np.sin(np.pi * y) * np.sin(np.pi * z))
	u_N = (lambda x, y, z: np.pi * np.cos(np.pi * x) * np.sin(np.pi * y) * np.sin(np.pi * z))
	ux = (lambda x, y, z: np.pi * np.cos(np.pi * x) * np.sin(np.pi * y) * np.sin(np.pi * z))
	uy = (lambda x, y, z: np.pi * np.sin(np.pi * x) * np.cos(np.pi * y) * np.sin(np.pi * z))
	uz = (lambda x, y, z: np.pi * np.sin(np.pi * x) * np.sin(np.pi * y) * np.cos(np.pi * z))

	for N in range (1,4):
		c4n = np.array([[0., 0., 0.], [1., 0., 0.], [0., 1., 0.], [1., 1., 0.], 
						[0., 0., 1.], [1., 0., 1.], [0., 1., 1.], [1., 1., 1.]])
		n4e = np.array([[0, 1, 3, 2, 4, 5, 7, 6]])
		n4fDb = np.array([[0, 1, 3, 2], [0, 1, 5, 4], [3, 2, 6, 7], [2, 0, 4, 6], [4, 5, 7, 6]])
		n4fNb = np.array([[1, 3, 7, 5]])

		M_R, M2D_R, Srr_R, Sss_R, Stt_R, Dr_R, Ds_R, Dt_R = getMatrix(N)
		L2error = np.zeros(iter, dtype = np.float64)
		sH1error = np.zeros(iter, dtype = np.float64)
		h = np.zeros(iter, dtype = np.float64)
		for j in range(0,iter):
			c4n, n4e, n4fDb, n4fNb = refineUniformRed(c4n, n4e, n4fDb, n4fNb)
			c4nNew, ind4e, ind4Db, ind4Nb = getIndex(N, c4n, n4e, n4fDb, n4fNb)
			u = solve(c4nNew, n4e, ind4e, ind4Db, ind4Nb, M_R, Srr_R, Sss_R, Stt_R, M2D_R, f, u_D, u_N, N)
			L2error[j], sH1error[j] = Error(c4n, n4e, ind4e, u, u_exact, ux, uy, uz, N, N+3)
			h[j] = 0.5 ** (j+1)

		rateL2 = (np.log(L2error[1:])-np.log(L2error[0:-1]))/(np.log(h[1:])-np.log(h[0:-1]))
		ratesH1 = (np.log(sH1error[1:])-np.log(sH1error[0:-1]))/(np.log(h[1:])-np.log(h[0:-1]))
		npt.assert_array_less(N+1-0.2, rateL2[-1])
		npt.assert_array_less(N-0.2, ratesH1[-1])

def test_refineUniformRed():
	from mozart.poisson.fem.cube import refineUniformRed
	c4n = np.array([[0., 0., 0.], [1., 0., 0.], [0., 1., 0.], [1., 1., 0.], 
					[0., 0., 1.], [1., 0., 1.], [0., 1., 1.], [1., 1., 1.]])
	n4e = np.array([[0, 1, 3, 2, 4, 5, 7, 6]])
	n4fDb = np.array([[0, 1, 3, 2], [0, 1, 5, 4], [3, 2, 6, 7], [2, 0, 4, 6], [4, 5, 7, 6]])
	n4fNb = np.array([[1, 3, 7, 5]])
	c4nNew, n4eNew, n4fDbNew, n4fNbNew = refineUniformRed(c4n, n4e, n4fDb, n4fNb)
	ref_c4n = np.array([[ 0. ,  0. ,  0. ], [ 1. ,  0. ,  0. ], [ 0. ,  1. ,  0. ], [ 1. ,  1. ,  0. ], 
						[ 0. ,  0. ,  1. ], [ 1. ,  0. ,  1. ], [ 0. ,  1. ,  1. ], [ 1. ,  1. ,  1. ], 
						[ 0.5,  0. ,  0. ], [ 1. ,  0.5,  0. ], [ 0.5,  1. ,  0. ], [ 0. ,  0.5,  0. ], 
						[ 0. ,  0. ,  0.5], [ 1. ,  0. ,  0.5], [ 1. ,  1. ,  0.5], [ 0. ,  1. ,  0.5], 
						[ 0.5,  0. ,  1. ], [ 1. ,  0.5,  1. ], [ 0.5,  1. ,  1. ], [ 0. ,  0.5,  1. ], 
						[ 0.5,  0.5,  0. ], [ 0.5,  0. ,  0.5], [ 1. ,  0.5,  0.5], [ 0.5,  1. ,  0.5], 
						[ 0. ,  0.5,  0.5], [ 0.5,  0.5,  1. ], [ 0.5,  0.5,  0.5]], dtype = np.float64)
	ref_n4e = np.array([[ 0,  8, 20, 11, 12, 21, 26, 24], [ 8,  1,  9, 20, 21, 13, 22, 26], 
						[11, 20, 10,  2, 24, 26, 23, 15], [20,  9,  3, 10, 26, 22, 14, 23], 
						[12, 21, 26, 24,  4, 16, 25, 19], [21, 13, 22, 26, 16,  5, 17, 25], 
						[24, 26, 23, 15, 19, 25, 18,  6], [26, 22, 14, 23, 25, 17,  7, 18]], dtype = int)
	ref_n4fDb = np.array([[ 0,  8, 20, 11], [ 8,  1,  9, 20], [11, 20, 10,  2], [20,  9,  3, 10], 
						  [ 0,  8, 21, 12], [ 8,  1, 13, 21], [12, 21, 16,  4], [21, 13,  5, 16], 
						  [ 3, 10, 23, 14], [10,  2, 15, 23], [14, 23, 18,  7], [23, 15,  6, 18], 
						  [ 2, 11, 24, 15], [11,  0, 12, 24], [15, 24, 19,  6], [24, 12,  4, 19], 
						  [ 4, 16, 25, 19], [16,  5, 17, 25], [19, 25, 18,  6], [25, 17,  7, 18]], dtype = int)
	ref_n4fNb = np.array([[ 1,  9, 22, 13], [ 9,  3, 14, 22], [13, 22, 17,  5], [22, 14,  7, 17]], dtype = int)
	npt.assert_almost_equal(c4nNew, ref_c4n, decimal=8)
	npt.assert_almost_equal(n4eNew, ref_n4e, decimal=8)
	npt.assert_almost_equal(n4fDbNew, ref_n4fDb, decimal=8)
	npt.assert_almost_equal(n4fNbNew, ref_n4fNb, decimal=8)