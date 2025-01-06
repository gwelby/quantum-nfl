from setuptools import setup, find_packages

setup(
    name="quantum-nfl",
    version="1.0.0",
    description="Advanced Quantum Computing Analysis for NFL Teams and Games",
    author="G. & C.",
    author_email="contact@quantum-nfl.com",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.19.0",
        "scipy>=1.7.0",
        "pandas>=1.3.0",
        "torch>=1.9.0",
        "qiskit>=0.34.0",
        "sphinx>=4.0.0",
        "pytest>=6.0.0",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
)
