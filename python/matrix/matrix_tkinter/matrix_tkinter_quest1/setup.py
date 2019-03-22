import setuptools

setuptools.setup(
    name='matrix_tkinter_quest1',
    version='1.0',
    author='Vadym Kononenko',
    author_email='<Vadym.kononenko@gmail.com>',
    description='eKids python example 1: create a GUI application with a quest through matrix cells',
    url="https://github.com/vadym/examples/python/matrix/matrix_tkinter/matrix_tkinter_quest1",

    packages=setuptools.find_packages(),

    # See: https://pypi.org/classifiers
    classifiers=[
        "Programming Language :: Python :: 3",

        ##
        # License choosing: http://oss-watch.ac.uk/apps/licdiff/
        #
        # 1. Popular and widely used: Yes
        # 2. Licence type: Permissive
        # 3. Jurisdiction: No
        # 4.a Grants patent rights: Yes
        # 4.b Patent retaliation clause: Yes
        # 5. Specifies enhanced attribution: No
        # 6. Addresses privacy loophole: No
        # 7. Includes 'no promotion' feature: Yes
        "License :: OSI Approved :: Apache Software License",

        "Operating System :: OS Independent",
    ],
    package_data={'Markdown': ['*.md']},
    #install_requires=[''],
    entry_points={'console_scripts': ['matrix_tkinter_quest1 = matrix_tkinter_quest1.cli:main']},
)
