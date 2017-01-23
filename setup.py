from setuptools import setup, Distribution, find_packages

class BinaryDistribution(Distribution):
	def is_pure(self):
		return False

setup(	name='mozart', version='0.0',
		description='PDE Solver Package',
		url='https://github.com/yoon-gu/mozart-pub/',
		author='Yoon-gu Hwang',
		author_email='yz0624@gmail.com',
		license='MIT',
		packages=find_packages(),
		install_requires=[
			'numpy',
		],
		package_data={
			'' : ['*.so']
		},
		include_package_data=True,
		distclass=BinaryDistribution,
		zip_safe=False)