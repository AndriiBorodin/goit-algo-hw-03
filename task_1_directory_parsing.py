import argparse
from pathlib import Path
import shutil
import sys


"""
приклади використання
python3 task_1_directory_parsing.py test_folder (копіювання в папку я якої запущений скрипт зі створення папки dist)
python3 task_1_directory_parsing.py test_folder sorted_files (копіювання в цільову папку)
"""


def parse_args():
    parser = argparse.ArgumentParser(description="Рекурсивне копіювання та сортування файлів за розширенням.")
    parser.add_argument("source", type=Path, help="Шлях до вихідної директорії")
    parser.add_argument("dest", type=Path, nargs="?", default=Path("dist"),
                        help="Шлях до директорії призначення (за замовчуванням 'dist')")
    return parser.parse_args()


def copy_file(file_path: Path, dest_root: Path):
    try:
        extension = file_path.suffix[1:] if file_path.suffix else "no_extension"
        target_dir = dest_root / extension
        target_dir.mkdir(parents=True, exist_ok=True)
        target_file = target_dir / file_path.name
        shutil.copy2(file_path, target_file)
        print(f"Скопійовано: {file_path} -> {target_file}")

    except OSError as e:
        print(f"Помилка при копіюванні файлу {file_path}: {e}")


def recursive_copy(source_path: Path, dest_path: Path):
    try:
        for item in source_path.iterdir():
            if item.is_dir():
                recursive_copy(item, dest_path)
            elif item.is_file():
                copy_file(item, dest_path)

    except PermissionError:
        print(f"Доступ заборонено: {source_path}")
    except FileNotFoundError:
        print(f"Директорію не знайдено: {source_path}")
    except OSError as e:
        print(f"Помилка доступу до {source_path}: {e}")


def main():
    args = parse_args()
    source = args.source
    dest = args.dest

    if not source.exists() or not source.is_dir():
        print(f"Помилка: Вихідна директорія '{source}' не існує або це не папка.")
        sys.exit(1)

    print(f"Починаємо сортування файлів з '{source}' у '{dest}'...")
    recursive_copy(source, dest)
    print("\nРобота завершена.")


if __name__ == "__main__":
    main()
