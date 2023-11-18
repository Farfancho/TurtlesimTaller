from setuptools import setup

package_name = 'tortuga_alejo_y_jose'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='farfann',
    maintainer_email='alejofarfanromero@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'taller_aj = tortuga_alejo_y_jose.taller_tortuga:main',
        ],
    },
)
