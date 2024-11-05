import os
import pathlib
from typing import List, Dict

def create_file_with_content(path: str, content: str = "") -> None:
    """Create a file with optional content."""
    with open(path, 'w') as f:
        f.write(content)

def create_project_structure():
    # Project root directory
    base_path = pathlib.Path.cwd()
    
    # Define the structure with files and their initial content
    structure: Dict[str, List[str]] = {
        "app": [
            "__init__.py",
            "main.py"
        ],
        "app/api": [
            "__init__.py"
        ],
        "app/api/v1": [
            "__init__.py"
        ],
        "app/api/v1/endpoints": [
            "__init__.py",
            "auth.py",
            "business.py",
            "users.py",
            "products.py",
            "orders.py",
            "suppliers.py",
            "inventory.py"
        ],
        "app/api/v1/dependencies": [
            "__init__.py",
            "auth.py",
            "database.py"
        ],
        "app/core": [
            "__init__.py",
            "config.py",
            "security.py",
            "events.py",
            "exceptions.py"
        ],
        "app/db": [
            "__init__.py",
            "session.py",
            "base.py"
        ],
        "app/db/migrations": [
            "README.md"
        ],
        "app/db/repositories": [
            "__init__.py",
            "base.py",
            "business.py",
            "user.py",
            "product.py"
        ],
        "app/models": [
            "__init__.py"
        ],
        "app/models/domain": [
            "__init__.py"
        ],
        "app/models/schemas": [
            "__init__.py",
            "business.py",
            "user.py",
            "product.py"
        ],
        "app/models/database": [
            "__init__.py",
            "business.py",
            "user.py",
            "product.py"
        ],
        "app/services": [
            "__init__.py"
        ],
        "app/services/auth": [
            "__init__.py",
            "service.py",
            "jwt.py",
            "password.py",
            "permissions.py"
        ],
        "app/services/business": [
            "__init__.py",
            "service.py",
            "validators.py",
            "exceptions.py",
            "utils.py"
        ],
        "app/services/ocr": [
            "__init__.py",
            "service.py",
            "processors.py",
            "validators.py"
        ],
        "app/services/payment": [
            "__init__.py",
            "service.py",
            "providers.py",
            "validators.py"
        ],
        "app/utils": [
            "__init__.py",
            "logging.py",
            "pagination.py",
            "cache.py"
        ],
        "tests": [
            "__init__.py",
            "conftest.py"
        ],
        "tests/api": [
            "__init__.py",
            "test_auth.py",
            "test_business.py"
        ],
        "tests/services": [
            "__init__.py",
            "test_auth_service.py",
            "test_business_service.py"
        ],
        "docs": [
            "README.md"
        ],
        "docs/api": [
            "README.md"
        ],
        "docs/architecture": [
            "README.md"
        ],
        "scripts": [
            "seed_data.py",
            "generate_keys.py"
        ],
        "deployment": [
            "README.md"
        ],
        "deployment/docker": [
            "Dockerfile",
            "docker-compose.yml"
        ],
        "deployment/kubernetes": [
            "deployment.yaml",
            "service.yaml",
            "ingress.yaml"
        ]
    }

    # Root level files
    root_files = {
        ".env.example": "# Environment Variables\nDATABASE_URL=\nSECRET_KEY=\nDEBUG=False",
        ".gitignore": """
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Environment
.env
.venv
venv/
ENV/

# IDE
.idea/
.vscode/
*.swp
*.swo

# Project specific
logs/
*.log
        """,
        "README.md": """
# FastAPI POS System

## Description
Point of Sale system backend built with FastAPI.

## Setup
1. Create virtual environment
2. Install dependencies
3. Set up environment variables
4. Run migrations
5. Start server

## Development
```bash
uvicorn app.main:app --reload
```

## Testing
```bash
pytest
```
        """,
        "requirements.txt": """
fastapi
uvicorn
sqlalchemy
alembic
pydantic
python-jose[cryptography]
passlib[bcrypt]
python-multipart
pytest
httpx
asyncpg
redis
python-dotenv
        """
    }

    # Create directories and files
    for directory, files in structure.items():
        # Create directory
        dir_path = base_path / directory
        dir_path.mkdir(parents=True, exist_ok=True)
        
        # Create files in directory
        for file in files:
            file_path = dir_path / file
            create_file_with_content(file_path)

    # Create root level files
    for file, content in root_files.items():
        file_path = base_path / file
        create_file_with_content(file_path, content)

if __name__ == "__main__":
    create_project_structure()
    print("Project structure created successfully!")
