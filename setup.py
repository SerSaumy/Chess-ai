from setuptools import setup, find_packages

setup(
    name="chess-ai",  
    version="0.1",  
    author="SAUMY",  
    author_email="sersaumy@gmail.com",  
    description="An AI that plays chess using reinforcement learning.",
    long_description=open("README.md").read(),  
    long_description_content_type="text/markdown", 
    url="https://github.com/SerSaumy/Chess-ai",  
    packages=find_packages(), 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  
    install_requires=[  
        "random",  
        "pytest", 
    ],
    entry_points={  
        'console_scripts': [
            'chess-ai=chess_ai.main:main', 
        ],
    },
)
