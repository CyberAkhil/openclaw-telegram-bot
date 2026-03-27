# Contributing to OpenClaw Telegram Bot

Thank you for your interest in contributing to the OpenClaw Telegram Bot project! This document provides guidelines and instructions for contributing.

## Code of Conduct

This project adheres to the Contributor Covenant code of conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to nikhilgumasta1@gmail.com.

## Getting Started

### Prerequisites
- Python 3.9+
- pip
- Git

### Development Setup

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/openclaw-telegram-bot.git`
3. Create a virtual environment: `python -m venv venv`
4. Activate it: `source venv/bin/activate` (or `venv\Scripts\activate` on Windows)
5. Install dependencies: `pip install -r requirements.txt`
6. Create a `.env` file based on `.env.example` and configure it

## Making Changes

### Branch Naming
- Feature: `feature/descriptive-name`
- Bug fix: `bugfix/descriptive-name`
- Documentation: `docs/descriptive-name`

### Commit Messages
Use semantic commit messages:
- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation changes
- `test:` for test additions
- `refactor:` for code refactoring
- `chore:` for maintenance tasks

Example: `feat: add conversation history persistence`

### Code Style
- Follow PEP 8 guidelines
- Use type hints where applicable
- Add docstrings to functions and classes
- Keep functions focused and concise

### Testing
- Write tests for new features
- Ensure existing tests pass: `python -m pytest`
- Aim for >80% code coverage

## Submitting Changes

### Pull Request Process

1. Update documentation if needed
2. Add tests for new functionality
3. Ensure all tests pass
4. Push to your fork
5. Create a Pull Request with:
   - Clear description of changes
   - Reference to related issues
   - Screenshots/examples if applicable

### PR Template
```
## Description
Brief description of the changes.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation

## How Has This Been Tested?
Describe the testing you've done.

## Checklist
- [ ] My code follows the style guidelines
- [ ] I have performed a self-review
- [ ] I have added comments where needed
- [ ] I have updated documentation
- [ ] I have added tests that prove the fix/feature
- [ ] New and existing tests pass
```

## Reporting Issues

### Bug Reports
Include:
- Python version
- Environment details
- Steps to reproduce
- Expected behavior
- Actual behavior
- Error logs

### Feature Requests
Include:
- Use case description
- Expected behavior
- Why this feature would be useful

## Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- GitHub contributors page

## Questions?

Feel free to:
- Open an issue
- Contact maintainers at nikhilgumasta1@gmail.com
- Check existing discussions

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing to making OpenClaw Telegram Bot better!** 🚀
