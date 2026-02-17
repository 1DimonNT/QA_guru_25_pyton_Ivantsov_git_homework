@echo off
setlocal

echo [1/6] Checking for active Virtual Environment...
if not exist .venv\Scripts\activate.bat (
    echo ERROR: .venv not found! Create it in PyCharm first.
    pause
    exit /b
)

echo [2/6] Installing tools into your environment...
call .venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install black isort flake8 autoflake pre-commit allure-pytest pytest==9.0.2 selenium==4.40.0

echo [3/6] Creating pyproject.toml...
(
echo [tool.black]
echo line-length = 90
echo target-version = ['py311']
echo exclude = '''
echo /^^(
echo     \.git
echo     ^| \.venv
echo     ^| \.idea
echo     ^| __pycache__
echo     ^| allure_results
echo     ^| allure_report
echo ^)/
echo '''
echo.
echo [tool.isort]
echo profile = "black"
echo line_length = 90
echo skip = [".venv", ".idea", "__pycache__", "allure_results", "allure_report"]
) > pyproject.toml

echo [4/6] Creating .pre-commit-config.yaml...
(
echo repos:
echo   - repo: local
echo     hooks:
echo       - id: autoflake
echo         name: autoflake
echo         entry: autoflake
echo         language: system
echo         types: [python]
echo         args: ["--in-place", "--remove-all-unused-imports", "--recursive", "--exclude", ".venv"]
echo       - id: isort
echo         name: isort
echo         entry: isort
echo         language: system
echo         types: [python]
echo       - id: black
echo         name: black
echo         entry: black
echo         language: system
echo         types: [python]
echo       - id: flake8
echo         name: flake8
echo         entry: flake8
echo         language: system
echo         types: [python]
echo         args: ["--max-line-length=120", "--ignore=E203,W503", "--exclude=.venv,venv,.idea"]
) > .pre-commit-config.yaml

echo [5/6] Activating pre-commit hooks...
call pre-commit install

echo [6/6] Running final check and freezing requirements...
call pre-commit run --all-files
pip freeze > requirements.txt

echo -----------------------------------------------
echo SUCCESS: Project configured! requirements.txt updated.
pause
