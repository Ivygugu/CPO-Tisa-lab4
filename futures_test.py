import unittest

import time

from futures import ThreadPoolExecutor, CancelledError


class MyTestCase(unittest.TestCase):

    def test_done(self):
        def return_future(msg):
            time.sleep(3)
            return msg

        pool = ThreadPoolExecutor(max_workers=2)

        t1 = pool.submit(return_future, 'a')
        t2 = pool.submit(return_future, 'b')

        time.sleep(1)
        self.assertEqual(t1.done(), False)
        self.assertEqual(t2.done(), False)

        time.sleep(8)
        self.assertEqual(t1.done(), True)
        self.assertEqual(t2.done(), True)

    def test_process(self):
        def return_future(msg):
            time.sleep(3)
            return msg

        pool = ThreadPoolExecutor(max_workers=2)

        t1 = pool.submit(return_future, 'a')
        t2 = pool.submit(return_future, 'b')
        t3 = pool.submit(return_future, 'c')
        self.assertEqual(t1.running(), True)
        self.assertEqual(t2.running(), True)
        self.assertEqual(t3.running(), False)

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

    def test_result_sequence(self):
        """
        From this test, job 2 is queue later than job 1, but it get executed
        before job 1. Because priority has been specified as we want to get job 2
        result first.
        """
        exe = ThreadPoolExecutor(max_workers=1)
        jobs = {lambda: time.sleep(3): {'priority': 2, 'args': []},
                lambda: time.sleep(2): {'priority': 1, 'args': []}}
        fs = exe.submit_with_priority(jobs)
        time.sleep(1)
        self.assertEqual(fs[0].running(), True)
        self.assertEqual(fs[1].running(), False)


if __name__ == '__main__':
    unittest.main()
