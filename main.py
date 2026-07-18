from core.run_bot import run_bot

if __name__ == "__main__":
    name = input("Введите название бота: ").strip()
    if not name:
        raise SystemExit("Имя бота пустое")
    run_bot(name)