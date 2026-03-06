from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'py_tut'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        (os.path.join('share', package_name, 'assets'),
         glob('assets/*')),
        ('share/' + package_name, ['package.xml', 'navigationTemplate.mod']),
        (os.path.join('share', 'py_tut', 'launch'),
        glob('launch/*.xml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dalmast',
    maintainer_email='dalmast@dal.ca',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'comm = py_tut.PCBComm:main',
                'wayp = py_tut.WaypointCTRL:main',
                'boat = py_tut.boatClasses:main',
                'ctrl = py_tut.controls:main',
                'navi = py_tut.navigation:main'

        ],
    },
)
