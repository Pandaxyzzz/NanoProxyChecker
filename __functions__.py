import os


class Utils(object):
    @staticmethod
    def clear() -> None:
        os.system("cls||clear")
    @staticmethod
    def title(title: str) -> None:
        if len(title) > 0:
            os.system(f'title NPC • {title}')
        else:
            os.system(f'title NPC')
