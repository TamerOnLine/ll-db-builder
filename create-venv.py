import subprocess
import os
import shutil

def setup_env(env_dir, python_version, requirements_file=None):
    # 🧹 Remove existing environment if it exists
    if os.path.exists(env_dir):
        print(f"\n🧹 Removing existing virtual environment: {env_dir}")
        shutil.rmtree(env_dir)

    # 🆕 Create virtual environment
    print(f"🆕 Creating virtual environment ({env_dir}) with Python {python_version}")
    subprocess.run(["py", f"-{python_version}", "-m", "venv", env_dir], check=True)

    # 🔍 Define paths
    if os.name == "nt":
        pip_path = os.path.join(env_dir, "Scripts", "pip.exe")
        python_path = os.path.join(env_dir, "Scripts", "python.exe")
    else:
        pip_path = os.path.join(env_dir, "bin", "pip")
        python_path = os.path.join(env_dir, "bin", "python")

    # ⬆️ Upgrade pip
    print("⬆️ Upgrading pip...")
    subprocess.run([python_path, "-m", "pip", "install", "--upgrade", "pip"], check=True)

    # 📦 Show versions
    subprocess.run([python_path, "--version"])
    subprocess.run([pip_path, "--version"])

    # 📦 Install requirements
    if requirements_file and os.path.exists(requirements_file):
        print(f"📦 Installing packages from {requirements_file}...")
        subprocess.run([pip_path, "install", "-r", requirements_file], check=True)
    else:
        print(f"⚠️ No {requirements_file} file found or not specified.")

# ✅ إعداد البيئة الأساسية (تشغيل + تطوير)
setup_env("venv", "3.12", "requirements.txt")
#setup_env("venv_dev", "3.12", "Dev_requirements.txt")

# ✅ إعداد بيئة التوثيق (gh-pages)
#setup_env("venv_docs", "3.12", "gh-pages-requirements.txt")
