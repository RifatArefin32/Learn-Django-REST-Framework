From the project root `LearnDRP/` directory, where the `env` virtual environment resides, we'll create a `requirements.txt` file.

## Why `requirements.txt`?
- Instead of manually installing each library, a single command `(pip install -r requirements.txt)` installs all the necessary dependencies for the project.
- `requirements.txt` ensures that everyone working on the project uses the same versions of dependencies which avoids compatibility issues.
- Eases Collaboration
- During deployment, the production server can use the requirements.txt file to quickly install all dependencies. 
- (CI/CD) pipelines use `requirements.txt` to set up the application environment in automated workflows.

## Where to Create requirements.txt?
We should create the `requirements.txt` file in the `project_root/` directory, alongside `.git/` and `env/.` This makes the file accessible for :
- Git tracking: It’s version-controlled with our repository.
- Deployment: Tools like Docker or CI/CD pipelines often expect `requirements.txt` in the root directory.
- Team collaboration: Developers working on the same project can install dependencies easily.

## How to create?
```bash
pip freeze > requirements.txt
```