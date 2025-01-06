# NFL Quantum Teams Setup Guide

## Prerequisites
- Python 3.10 or higher
- pip package manager
- Git (for version control)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-org/quantum-nfl.git
cd quantum-nfl
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

1. Create environment variables:
```bash
# Linux/Mac
export NFL_DATA_DIR=/path/to/data
export NFL_ENV=development

# Windows
set NFL_DATA_DIR=D:\path\to\data
set NFL_ENV=development
```

2. Initialize the system:
```bash
python -m src.quantum.run_predictions --init
```

## Running Tests
```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_historical_echoes.py

# Run with coverage
pytest --cov=src --cov-report=term-missing
```

## Development Setup

1. Install development dependencies:
```bash
pip install -r requirements-dev.txt
```

2. Set up pre-commit hooks:
```bash
pre-commit install
```

3. Configure your IDE:
- Set Python interpreter to virtual environment
- Enable auto-formatting (black)
- Enable import sorting (isort)

## Troubleshooting

### Common Issues

1. Import Errors
```bash
# Check PYTHONPATH
python -c "import sys; print(sys.path)"
```

2. Data Directory Issues
```bash
# Verify permissions
ls -l $NFL_DATA_DIR
```

3. Memory Issues
```bash
# Increase Python memory limit
export PYTHONMEM=4GB
```

### Getting Help
- Check the documentation in /docs
- Submit issues on GitHub
- Contact the development team
