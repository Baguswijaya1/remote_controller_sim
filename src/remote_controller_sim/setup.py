from setuptools import find_packages, setup

package_name = 'remote_controller_sim'

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
    maintainer='bagus',
    maintainer_email='bagusanw@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'remote_controller_sim = remote_controller_sim.remote_node:main',
            'drone_motors_node = remote_controller_sim.drone_node:main'
        ],
    },
)
