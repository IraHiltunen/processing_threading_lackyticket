import multiprocessing
from multiprocessing import Pool
import time

# threat - запит до мережі, інпут, аутпут
# process - якісь калькуляції !!!
def is_lucky_ticket(ticket):
    half_len = len(ticket) // 2
    first_half = sum(int(digit) for digit in ticket[:half_len])
    second_half = sum(int(digit) for digit in ticket[half_len:])
    return first_half == second_half


def count_lucky_tickets_for_range(start, end, num_digits):
    count = 0
    for ticket_number in range(start, end):
        ticket = str(ticket_number).zfill(num_digits)  # додаємо нулі на початку
        if is_lucky_ticket(ticket):
            count += 1
    return count


def count_lucky_tickets(num_digits):
    max_ticket_number = 10 ** num_digits # 10 в 6(num_digit) ступінь- це найбільший можливий номер квитка
    chunk_size = max_ticket_number // 4

    # Використовуємо multiprocessing для розпаралелювання
    with multiprocessing.Pool(processes=4) as pool:
        results = [
            pool.apply_async(
                count_lucky_tickets_for_range,
                args=(i * chunk_size, (i + 1) * chunk_size, num_digits)
            )
            for i in range(4)
        ]

        # Збір результатів з усіх процесів
        total_lucky_tickets = sum(result.get() for result in results)

    return total_lucky_tickets


if __name__ == "__main__":
    num_digits = 6  # шестизначний номер
    start_time = time.time()
    result = count_lucky_tickets(num_digits)
    end_time = time.time()
    time_for_counting = end_time - start_time
    print(f"amount of lucky tickets for {num_digits}-digits: {result}")
    print(f"time for counting {time_for_counting:.2f} sec")

