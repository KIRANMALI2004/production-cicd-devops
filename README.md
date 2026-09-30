# Production-Style CI/CD Pipeline

A production-style DevOps project demonstrating automated testing,
containerization, CI/CD, AWS infrastructure, and Infrastructure as Code.

## Technologies

- Python
- Flask
- Pytest
- Git
- GitHub
- GitHub Actions
- Docker
- AWS
- Amazon ECR
- Terraform
- Linux

## Architecture

Developer
    |
    v
GitHub
    |
    v
GitHub Actions
    |
    +----> Automated Tests
    |
    +----> Docker Build
    |
    v
Amazon ECR
    |
    v
AWS Deployment

Terraform manages the AWS infrastructure.

## Application Endpoints

GET /

GET /health

GET /api/info

## Run Locally

Create virtual environment:

```bash
python -m venv .venv