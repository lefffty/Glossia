import os
import shutil
import subprocess
from pathlib import Path


class Builder:
    def __init__(self):
        self.app_name = "Glossia"
        self.version = "1.0.0"
        self.main_script = "main.py"

    def clean(self):
        """Очистка предыдущих сборок"""
        folders = ["build", "dist", f"{self.app_name}.spec"]
        for folder in folders:
            if Path(folder).exists():
                if Path(folder).is_dir():
                    shutil.rmtree(folder)
                else:
                    os.remove(folder)

    def install_deps(self):
        """Установка зависимостей"""
        print("Установка зависимостей...")
        subprocess.run([sys.executable, "-m", "pip",
                       "install", "-r", "requirements.txt"])

    def build(self):
        """Сборка exe"""
        print("Начинаем сборку...")

        cmd = [
            "pyinstaller",
            "--onefile",
            "--windowed",
            f"--name={self.app_name}",
            f"--icon=app.ico",
            "--clean",
            self.main_script
        ]

        pyside6_modules = [
            'PySide6.QtCore',
            'PySide6.QtGui',
            'PySide6.QtWidgets',
            'PySide6.QtSql',
        ]

        for module in pyside6_modules:
            cmd.append('--hidden-import={}'.format(module))

        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode == 0:
            print(f"\nСборка завершена успешно!")
            print(f"\tФайл: dist/{self.app_name}.exe")
            print(
                f"\tРазмер: {Path(f'dist/{self.app_name}.exe').stat().st_size / 1024 / 1024:.2f} MB")
        else:
            print(f"\n\tОшибка сборки:")
            print(result.stderr)

    def run(self):
        """Запуск процесса сборки"""
        self.clean()
        self.install_deps()
        self.build()


if __name__ == "__main__":
    import sys
    builder = Builder()
    builder.run()
