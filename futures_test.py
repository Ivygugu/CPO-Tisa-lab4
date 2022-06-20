import unittest

import time

from futures import ThreadPoolExecutor, CancelledError, TimeoutError


class MyTestCase(unittest.TestCase):

    def test_isDone(self):
        def return_future(msg):
            time.sleep(3)
            return msg

        pool = ThreadPoolExecutor(max_workers=2)

        t1 = pool.submit(return_future, 'a')
        t2 = pool.submit(return_future, 'b')

        time.sleep(1)
        self.assertEqual(t1.isDone(), False)
        self.assertEqual(t2.isDone(), False)

        time.sleep(8)
        self.assertEqual(t1.isDone(), True)
        self.assertEqual(t2.isDone(), True)

    def test_InProcess(self):
        def return_future(msg):
            time.sleep(3)
            return msg

        pool = ThreadPoolExecutor(max_workers=2)

        t1 = pool.submit(return_future, 'a')
        t2 = pool.submit(return_future, 'b')
        t3 = pool.submit(return_future, 'c')
        self.assertEqual(t1.inProcess(), True)
        self.assertEqual(t2.inProcess(), True)
        self.assertEqual(t3.inProcess(), False)

    def test_result(self):
        def return_future(msg):
            time.sleep(3)
            return msg

        pool = ThreadPoolExecutor(max_workers=2)
        t1 = pool.submit(return_future, 'a')
        t2 = pool.submit(return_future, 'b')
        self.assertEqual(t1.result(), 'a')
        self.assertEqual(t2.result(), 'b')

        with self.assertRaises(CancelledError):
            pool = ThreadPoolExecutor(max_workers=1)
            t1 = pool.submit(return_future, 'a')
            t2 = pool.submit(return_future, 'b')
            t2.cancel()
            t2.result()

        # error: TimeoutError
        with self.assertRaises(TimeoutError):
            pool = ThreadPoolExecutor(max_workers=1)
            t1 = pool.submit(return_future, 'a')
            t2 = pool.submit(return_future, 'b')
            t1.result(timeout=1)

    def test_cancel(self):
        def return_future(msg):
            time.sleep(3)
            return msg

        pool = ThreadPoolExecutor(max_workers=2)

        t1 = pool.submit(return_future, 'a')
        t2 = pool.submit(return_future, 'b')
        time.sleep(6)
        t3 = pool.submit(return_future, 'c')
        self.assertEqual(t1.cancel(), False)
        self.assertEqual(t2.cancel(), False)
        self.assertEqual(t3.cancel(), None)



if __name__ == '__main__':
    unittest.main()
