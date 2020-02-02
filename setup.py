from setuptools import setup, find_packages

from pyoverchain.core import version

setup(name='pyoverchain',
      version=version.get(),
      description="a python pipeline to generate chain files between different genome assemblies for LiftOver",
      long_description=__doc__,
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: MIT License',
          'Operating System :: Unix',
          'Programming Language :: Python :: 3.6',
          'Topic :: Scientific/Engineering :: Bio-Informatics'
      ],
      keywords='genome bioinformatics assembly BLAT LiftOver',
      author='Tao Zhu',
      author_email='taozhu@mail.bnu.edu.cn',
      url='https://github.com/billzt/pyOverChain',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      python_requires='>=3.6',
      install_requires=[
          'progressbar2'
      ],
      entry_points={
          'console_scripts': [
              'pyoverchain = pyoverchain.cmd.run:main',
          ]
      }
)