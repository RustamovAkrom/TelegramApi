import os


account_dir = "apps/account/"
telegram_dir = "apps/telegram/"

create_default_apis = {
    "BASE_DIR": None,
    "APPS_DIR": "apps",
    "APPS": ("account", "telegram"),
}

def main():
    dirname = "apps/{{ dirname }}"
    print(dirname)


if __name__=="__main__":
    main()