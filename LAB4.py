import hashlib, itertools  # Імпортуємо бібліотеки hashlib та itertools для роботи з хешами та ітераціями.

def crack(hash):
    result = hashlib.md5('00078'.encode())  # Створюємо початковий хеш MD5 для порівняння.
    for pin in itertools.product(range(10), repeat=5):  # Запускаємо цикл для створення всіх можливих комбінацій 5-цифрових пін-кодів.
        pin = ''.join(list(map(str, pin)))  # Перетворюємо кортеж у рядок для представлення пін-коду.
        result = hashlib.md5(pin.encode()).hexdigest()  # Обчислюємо MD5-хеш поточного пін-коду.

        if result == hash:  # Порівнюємо обчислений хеш з вхідним хешем.
            return pin  # Якщо хеші збігаються, повертаємо знайдений пін-код.
