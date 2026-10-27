import argparse
from core.run_bot import run_bot

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Запуск бота")
    parser.add_argument("--bot", "-b", required=True, help="название папки бота в bots/")
    args = parser.parse_args()
    run_bot(args.bot)