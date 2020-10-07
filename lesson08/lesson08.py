class SomeError(Exception):
    def __init__(self, text:None):
        self.text = text

def some_f(cls: SomeError) -> SomeError:
    for num in range(50):
        if num == 15:
            raise SomeError(f"Some error text {num}")
    return cls

    print(num)
