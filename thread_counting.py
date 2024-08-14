# порівняти рахування за часом потоками і процесами. і подивитись, коли це буде швидше
# потоками рахує значно повільніше!!!!!!!!!!1
import threading
import time

def is_lucky_ticket(ticket):
    half_len = len(ticket) // 2
    first_half = sum(int(digit) for digit in ticket[:half_len])
    second_half = sum(int(digit) for digit in ticket[half_len:])
    return first_half == second_half

def count_lucky_tickets_for_range(start, end, num_digits, result, index):
    count = 0
    for ticket_number in range(start, end):
        ticket = str(ticket_number).zfill(num_digits)  # додає нулі на початку
        if is_lucky_ticket(ticket):
            count += 1
    result[index] = count  #  результат у спільному списку

def count_lucky_tickets(num_digits):
    max_ticket_number = 10 ** num_digits # 10 в 6(num_digit) ступінь- це найбільший можливий номер квитка
    chunk_size = max_ticket_number // 4

    result = [0] * 4  # список для зберігання рез-ів від кожного потоку
    threads = []


    for i in range(4): # створює та запускає потоки
        start = i * chunk_size
        end = (i + 1) * chunk_size
        thread = threading.Thread(target=count_lucky_tickets_for_range, args=(start, end, num_digits, result, i))
        threads.append(thread)
        thread.start()


    for thread in threads: # чекає завершення всіх потоків
        thread.join()

    return sum(result)

if __name__ == "__main__":
    num_digits = 6  # шестизначний номер
    start_time = time.time()
    result = count_lucky_tickets(num_digits)
    end_time = time.time()
    time_for_counting = end_time - start_time
    print(f"amount of lucky tickets for {num_digits}-digits: {result}")
    print(f"time for counting {time_for_counting:.2f} sec")
