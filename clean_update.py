import os
import shutil

from rich.console import Console
from rich.progress import track

console = Console()


def main():
    with console.status("正在搜寻 .egg-info"):
        egg_info: list = []
        for file in os.listdir():
            if file.endswith(".egg-info"):
                egg_info.append(file)
                console.print(file)
    for file in track(
        ["build", "dist", "logs", *egg_info], description="正在删除"
    ):
        if os.path.isdir(file) and os.access(file, os.W_OK):
            shutil.rmtree(file)


if __name__ == "__main__":
    main()
