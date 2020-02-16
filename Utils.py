def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        print("錯誤：請輸入整數")
        return False
