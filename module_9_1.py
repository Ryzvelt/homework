def apply_all_func(int_list, *functions):

    results = {}
    for func in functions:
        try:
            results[func.__name__] = func(int_list)
        except Exception as e:
            results[func.__name__] = f"Ошибка при вызове {func.__name__}: {e}"
    return results


if __name__ == "__main__":
    print(apply_all_func([6, 20, 15, 9], max, min))
    print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
    print(apply_all_func([6, 20, 15, 9], max, min, len, sum, sorted))
    print(apply_all_func([6,20,15,9],max,int))