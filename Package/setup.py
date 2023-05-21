from setuptools import setup,find_packages

setup(
        ### 包与作者信息
        name = 'sunflow',
        version = '0.1.1',
        author = 'shihua',
        author_email = "15021408795@163.com",
        python_requires = ">=3.10.9",
        license = "MIT",

        ### 源码与依赖
        packages = find_packages(),
        include_package_data = True,
        description = ' Sunflow is a workflow management tool that provides fast organization of algorithm applications, primarily using pluggy based hook technology.',
        # install_requires = ['pluggy'],

        # ### 包接入点，命令行索引
        # entry_points = {
        #     'console_scripts': [
        #         'fichectl = fiche.cli:fiche'
        #     ]
        # }      
)