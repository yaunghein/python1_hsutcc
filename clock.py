import time
from datetime import datetime


def get_current_time() -> str:
    """
    get current time in 00:00:00:00 format (including milliseconds)
    """
    now = datetime.now()
    hours, minutes, seconds = now.hour, now.minute, now.second
    milliseconds = str(now.microsecond)[:2]
    formatted_time = f"{hours:02d}:{minutes:02d}:{seconds:02d}:{milliseconds}"
    return formatted_time


def coundown(seconds: int) -> None:
    """
    count the time back from given seconds to 0 seccond
    """
    end_time = time.time() + seconds
    while time.time() < end_time:
        remaining = end_time - time.time()

        mins, secs = divmod(int(remaining), 60)
        hours = mins // 60
        milliseconds = int((remaining - int(remaining)) * 100)

        formatted_time = f"{hours:02d}:{mins:02d}:{secs:02d}:{milliseconds:02d}"
        print(f" {formatted_time}", end="\r")
        time.sleep(0.01)
    return


def start_normal_watch() -> None:
    """
    show the current time in terminal continuously in 00:00:00:00 format (including milliseconds)
    """
    while True:
        current_time = get_current_time()
        print(f" {current_time}", end="\r")
        time.sleep(0.01)


def show_timer_menu() -> None:
    """
    show the options for timer
    """
    print("\n")
    print("="*48)
    print("TIMER MODES\n")
    print("1. (5,3,5,3,5,3)")
    print("2. (10,5,10)")
    print("3. Normal Timer")
    print("4. Back to Main Menu\n")
    print("Warning: Whoever enters invalid input is GAY 🥺!")
    print("="*48)
    return


def work_break_pattern(pattern: tuple[int, ...]) -> None:
    """
    show countdown in terminal according to the input tuple
    odd indices are working sessions
    and even indices are break sesions
    """

    work_count = 0
    break_count = 0

    for i, seconds in enumerate(pattern):
        if i % 2 == 0:
            work_count += 1
        else:
            break_count += 1

    for i, seconds in enumerate(pattern):
        if i % 2 == 0:
            session_num = i // 2 + 1
            print(
                f"\n\nWORK Session {session_num}/{work_count} - {seconds} seconds\n")
        else:
            session_num = i // 2 + 1
            print(
                f"\n\nBREAK Session {session_num}/{break_count} - {seconds} seconds\n")

        coundown(seconds)

    print("All work-break sessions completed!")
    return


def normal_timer() -> None:
    """
     show countdown in terminal according to the input seconds
     from input seconds to 0 seconds
    """
    seconds_input = input("\nEnter seconds to countdown: ")

    if seconds_input.isdigit():
        seconds = int(seconds_input)
        print(f"\nStarting countdown from {seconds} seconds...\n")
        time.sleep(1)
        coundown(seconds)
    else:
        print("You are gay 🫵 - that's not a valid number!")


def start_timer() -> None:
    """
    timer options router,
    show different options for timer and run related functions according to input
    """
    while True:
        show_timer_menu()
        timer_mode = input("\nSelect timer mode (1-4): ").strip()

        if timer_mode == '1':
            print("\nSelected: Work-Break Pattern (5,3,5,3,5,3)")
            time.sleep(1)
            work_break_pattern((5, 3, 5, 3, 5, 3))
        elif timer_mode == '2':
            print("\nSelected: Work-Break Pattern (10,5,10)")
            time.sleep(1)
            work_break_pattern((10, 5, 10))
        elif timer_mode == '3':
            print("\nSelected: Normal Timer")
            normal_timer()
        elif timer_mode == '4':
            print("\nReturning to main menu...\n")
            break
        else:
            print("\nYou are gay 🫵 - Invalid timer mode!\n")
            time.sleep(1)


def show_menu() -> None:
    """
    show main menu
    """
    print("="*48)
    print("CHOOSE YOUR MODE\n")
    print("1. Normal Watch (Current Time)")
    print("2. Timer (Countdown Timer)")
    print("3. ASCII Clock Display")
    print("4. Exit Program\n")
    print("Warning: Whoever enters invalid input is GAY 🥺!")
    print("="*48)
    return


mode = None

while True:
    show_menu()
    mode = input("\nSelect mode (1-4): ").strip()

    if mode == '1':
        print("\nStarting Normal Watch...\n")
        time.sleep(1)
        start_normal_watch()
    elif mode == '2':
        start_timer()
    elif mode == '3':
        print("\nASCII Clock Mode - COMING SOON!")
        print("This feature is under development...\n")
        time.sleep(2)
    elif mode == '4':
        print("\n👋 Adios!\n")
        exit()
    else:
        print("\nYou are gay 🫵 - Invalid choice!")
        time.sleep(3)
