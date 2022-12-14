import time
import unittest

from debounce_function import debounce


class TestDebounceMethod(unittest.TestCase):
    def test_sync(self):
        count = 0

        @debounce(1000)
        def f():
            print("calling sync function")
            nonlocal count
            count = count + 1

        start = int(time.time())

        while (int(time.time()) - start) < 5:
            f()

        self.assertEqual(count, 4)


class TestAsyncDebounceMethod(unittest.IsolatedAsyncioTestCase):
    async def test_async(self):
        count = 0

        @debounce(1000)
        async def f():
            nonlocal count
            count = count + 1
            print("calling async function")

        start = int(time.time())

        while (int(time.time()) - start) < 5:
            await f()

        self.assertEqual(count, 4)


if __name__ == "__main__":
    unittest.main()
