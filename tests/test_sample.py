import unittest
import numpy as np
from numpy import linalg as LA
class TestMethods(unittest.TestCase):

	def test_test(self):
		self.assertTrue(True)

	def test_import(self):
		import mozart as mz
		self.assertTrue(True)

	def test_authors(self):
		import mozart as mz
		authors = ('Yoon-gu Hwang <yz0624@gmail.com>', 'Dong-Wook Shin <dwshin.yonsei@gmail.com>', 'Ji-Yeon Suh <suh91919@gmail.com>')
		self.assertEqual(mz.__author__, authors)

	def test_1d_uniform_mesh(self):
		from mozart.mesh.rectangle import unit_interval
		N = 4
		c4n, n4e = unit_interval(N)
		diff_c4n = c4n - np.linspace(0,1,N)
		diff_n4e = n4e - np.array([[0,1], [1, 2], [2,3]])
		self.assertTrue(LA.norm(diff_c4n) < 1E-8)
		self.assertTrue(LA.norm(diff_n4e) < 1E-8)

	def test_1d_uniform_interval(self):
		from mozart.mesh.rectangle import interval
		a=0
		b=1
		M=4
		N=2
		c4n, n4e, n4db, ind4e = interval(a,b,M,N)
		diff_c4n = c4n - np.linspace(a,b,M*N+1)
		diff_n4e = n4e - np.array([[0,2], [2,4], [4,6], [6,8]])
		diff_n4db = n4db - np.array([0, 8])
		diff_ind4e = ind4e - np.array([[0,1,2], [2,3,4], [4,5,6], [6,7,8]])
		self.assertTrue(LA.norm(diff_c4n) < 1E-8)
		self.assertTrue(LA.norm(diff_n4e) < 1E-8)
		self.assertTrue(LA.norm(diff_n4db) < 1E-8)
		self.assertTrue(LA.norm(diff_ind4e) < 1E-8)

	def test_poisson_square_2d(self):
		from mozart.mesh.rectangle import unit_square
		unit_square(0.1)
		self.assertTrue(True)

	def test_getPoissonMatrix1D(self):
		from mozart.poisson.solve import getMatrix1D
		M1, S1, D1 = getMatrix1D(1)
		diff_M1 = M1 - np.array([[ 2,  1], [ 1, 2]]) / 3.
		diff_S1 = S1 - np.array([[ 1, -1], [-1, 1]]) / 2.
		diff_D1 = D1 - np.array([[-1,  1], [-1, 1]]) / 2.
		M2, S2, D2 = getMatrix1D(2)
		diff_M2 = M2 - np.array([[ 4,  2, -1], [ 2, 16,  2], [-1,  2, 4]]) / 15.
		diff_S2 = S2 - np.array([[ 7, -8,  1], [-8, 16, -8], [ 1, -8, 7]]) / 6.
		diff_D2 = D2 - np.array([[-3,  4, -1], [-1,  0,  1], [ 1, -4, 3]]) / 2.
		self.assertTrue(LA.norm(diff_M1) < 1E-8)
		self.assertTrue(LA.norm(diff_S1) < 1E-8)
		self.assertTrue(LA.norm(diff_D1) < 1E-8)
		self.assertTrue(LA.norm(diff_M2) < 1E-8)
		self.assertTrue(LA.norm(diff_S2) < 1E-8)
		self.assertTrue(LA.norm(diff_D2) < 1E-8)

	def test_nJacobiP(self):
		from mozart.poisson.solve import nJacobiP
		x = np.linspace(-1,1,5)
		P = nJacobiP(x,0,0,0)
		diff_P = P - 0.707106781186548 * np.ones(5,float)
		P2 = nJacobiP(x,0,0,1)
		diff_P2 = P2 - 1.224744871391589*x
		P3 = nJacobiP(x,0,0,2)
		diff_P3 = P3 - np.array([1.581138830084190, -0.197642353760524, -0.790569415042095, -0.197642353760524, 1.581138830084190])
		self.assertTrue(LA.norm(diff_P) < 1E-8)
		self.assertTrue(LA.norm(diff_P2) < 1E-8)
		self.assertTrue(LA.norm(diff_P3) < 1E-8)

	def test_nJacobiGQ(self):
		from mozart.poisson.solve import nJacobiGQ
		x0, w0 = nJacobiGQ(0,0,0)
		diff_x0 = x0 - 0.0
		diff_w0 = w0 - 2.0
		x1, w1 = nJacobiGQ(0,0,1)
		diff_x1 = x1 - np.array([-np.sqrt(1.0/3.0), np.sqrt(1.0/3.0)])
		diff_w1 = w1 - np.array([1.0, 1.0])
		x2, w2 = nJacobiGQ(0,0,2)
		diff_x2 = x2 - np.array([-np.sqrt(3.0/5.0), 0.0, np.sqrt(3.0/5.0)])
		diff_w2 = w2 - np.array([5.0/9.0, 8.0/9.0, 5.0/9.0])
		self.assertTrue(LA.norm(diff_x0) < 1E-8)
		self.assertTrue(LA.norm(diff_w0) < 1E-8)
		self.assertTrue(LA.norm(diff_x1) < 1E-8)
		self.assertTrue(LA.norm(diff_w1) < 1E-8)
		self.assertTrue(LA.norm(diff_x2) < 1E-8)
		self.assertTrue(LA.norm(diff_w2) < 1E-8)

	def test_nJacobiGL(self):
		from mozart.poisson.solve import nJacobiGL
		x0 = nJacobiGL(0,0,0)
		diff_x0 = x0 - 0.0;
		x1 = nJacobiGL(0,0,1)
		diff_x1 = x1 - np.array([-1.0, 1.0])
		x2 = nJacobiGL(0,0,2)
		diff_x2 = x2 - np.array([-1.0, 0.0, 1.0])
		self.assertTrue(LA.norm(diff_x0) < 1E-8)
		self.assertTrue(LA.norm(diff_x1) < 1E-8)
		self.assertTrue(LA.norm(diff_x2) < 1E-8)

	def test_DnJacobiP(self):
		from mozart.poisson.solve import DnJacobiP
		x = np.linspace(-1,1,5)
		dP = DnJacobiP(x,0,0,0)
		diff_dP = dP - np.zeros(5,float)
		dP2 = DnJacobiP(x,0,0,1)
		diff_dP2 = dP2 - 1.224744871391589*np.ones(5,float)
		self.assertTrue(LA.norm(diff_dP) < 1E-8)
		self.assertTrue(LA.norm(diff_dP2) < 1E-8)

	def test_VandermondeM1D(self):
		from mozart.poisson.solve import VandermondeM1D
		r = np.array([-1.0, 1.0])
		V1D = VandermondeM1D(1,r)
		diff_V1D = V1D - np.array([[0.707106781186548, -1.224744871391589], [0.707106781186548, 1.224744871391589]])
		self.assertTrue(LA.norm(diff_V1D) < 1E-8)

	def test_DVandermondeM1D(self):
		from mozart.poisson.solve import DVandermondeM1D
		r = np.array([-1.0, 1.0])
		DVr = DVandermondeM1D(1,r)
		diff_DVr = DVr - np.array([[0.0, 1.224744871391589], [0.0, 1.224744871391589]])
		self.assertTrue(LA.norm(diff_DVr) < 1E-8)

	def test_Dmatrix1D(self):
		from mozart.poisson.solve import Dmatrix1D
		from mozart.poisson.solve import VandermondeM1D
		r = np.array([-1.0, 1.0])
		V = VandermondeM1D(1,r)
		Dr = Dmatrix1D(1,r,V)
		diff_Dr = Dr - np.array([[-0.5, 0.5], [-0.5, 0.5]])
		self.assertTrue(LA.norm(diff_Dr) < 1E-8)

	def test_solve_onedim(self):
		from mozart.mesh.rectangle import unit_interval
		N = 3
		c4n, n4e = unit_interval(N)
		n4Db = [0, N-1]
		f = lambda x: np.ones_like(x)
		u_D = lambda x: np.zeros_like(x)
		from mozart.poisson.solve import one_dim
		x = one_dim(c4n, n4e, n4Db, f, u_D)
		diff_x = x - np.array([0., 0.125, 0.])
		self.assertTrue(LA.norm(diff_x) < 1E-8)

		self.assertTrue(True)

	def test_solve_twodim(self):
		from mozart.poisson.solve import two_dim
		two_dim(None, None, None, None)

		self.assertTrue(True)

	def test_solve_threedim(self):
		from mozart.poisson.solve import three_dim
		three_dim(None, None, None, None)

		self.assertTrue(True)

	def test_benchmark01_sample(self):
		from mozart.poisson.solve import sample
		sample()
		self.assertTrue(True)