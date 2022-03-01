import time
import unittest

from debounce_function import debounce, async_debounce


class TestDebounceMethod(unittest.TestCase):
    def test_foo(self):
        count = 0

        @debounce(5000)
        def f():
            nonlocal count
            count = count = 1

        start = int(time.time())

        while (int(time.time()) - start) < 1:
            f()

        self.assertEqual(count, 1)



if __name__ == "__main__":
    unittest.main()
