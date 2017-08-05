from unittest import TestCase
import pandas as pd
import numpy as np

from general import split


class SplitTest(TestCase):
    def test_python_list(self):
        l = range(20)

        chunks = split(l, 8)

        self.assertEqual(len(chunks), 3)
        self.assertEqual(len(chunks[0]), 8)
        self.assertEqual(len(chunks[1]), 8)
        self.assertEqual(len(chunks[2]), 4)

    def test_pandas_dataframe(self):
        df = pd.DataFrame({'A': np.zeros(20), 'B': np.ones(20)})

        chunks = split(df, 8)
        self.assertEqual(len(chunks), 3)
        self.assertEqual(len(chunks[0]), 8)
        self.assertEqual(len(chunks[1]), 8)
        self.assertEqual(len(chunks[2]), 4)