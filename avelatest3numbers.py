from collections import deque
class RollingAverage:
    """Track the average of the latest values in constant time."""

    def __init__(self, window_size: int) -> None:
        if not isinstance(window_size, int) or isinstance(window_size, bool):
            raise TypeError("window_size must be an integer")
        if window_size <= 0:
            raise ValueError("window_size must be greater than 0")

        self.window_size = window_size
        self.numbers: deque[float] = deque()
        self.total = 0.0

    def add_number(self, number: float) -> float:
        if not isinstance(number, (int, float)) or isinstance(number, bool):
            raise TypeError("number must be numeric")

        if len(self.numbers) == self.window_size:
            self.total -= self.numbers.popleft()

        self.numbers.append(number)
        self.total += number
        return self.total / len(self.numbers)


if __name__ == "__main__":
    try:
        rolling_average = RollingAverage(window_size=3)

        for number in [1, 2, 3, 4, 5, 6, 7]:
            average = rolling_average.add_number(number)
            print(f"{list(rolling_average.numbers)} Average = {average}")
    except (TypeError, ValueError) as error:
        print(f"Error: {error}")
