from setuptools import find_packages, setup

package_name = 'pkg_ros'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='noam',
    maintainer_email='noam@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                 'pub_lum = pkg_ros.pub_lum:main' ,
                 'sus_lum = pkg_ros.sus_lum:main' ,
                 'pub_temp = pkg_ros.pub_temp:main' ,
                 'sus_temp = pkg_ros.sus_temp:main' ,
                 'pub_presence = pkg_ros.pub_presence:main' ,
                 'sus_presence = pkg_ros.sus_presence:main' ,
                 'client_bp = pkg_ros.bp_portail:main' ,
                 'app = pkg_ros.app:main' ,
        ],
    },
)
