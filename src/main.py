import sys
import tasks


def main(argv):
    if len(argv) < 2:
        print("Команды: add <текст> | list | done <id> | delete <id>")
        return 1
    cmd = argv[1]
    data = tasks.load()

    if cmd == "add" and len(argv) >= 3:
        new_id = tasks.add(data, " ".join(argv[2:]))
        print(f"Добавлена задача #{new_id}")
    elif cmd == "list":
        if not data:
            print("Задач нет")
        for t in data:
            mark = "x" if t["done"] else " "
            print(f"[{mark}] {t['id']}. {t['title']}")
    elif cmd == "done" and len(argv) == 3:
        print("Готово" if tasks.mark_done(data, int(argv[2])) else "Не найдено")
    elif cmd == "delete" and len(argv) == 3:
        print("Удалено" if tasks.delete(data, int(argv[2])) else "Не найдено")
    else:
        print("Неверная команда")
        return 1

    tasks.save(data)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
