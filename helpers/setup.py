from setuptools import find_packages, setup

package_name = 'helpers'

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
    maintainer='root',
    maintainer_email='root@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'node_q_1_1 = helpers.node_q_1_1:main',
            'node_q_1_2 = helpers.node_q_1_2:main',
            'node_q_4_2 = helpers.node_q_4_2:main'
        ],
    },
)
