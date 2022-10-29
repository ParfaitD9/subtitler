import unittest
from controller import File
from datetime import timedelta


class TestUtils(unittest.TestCase):
    def test_srt_formatting(self):
        self.assertEqual(
            File.as_srt(
                1,
                timedelta(seconds=16, milliseconds=312),
                timedelta(seconds=21),
                "Vas te faire enculer",
            ),
            f"""1
00:00:16,312 --> 00:00:21,000
Vas te faire enculer\n
""",
        )


if __name__ == "__main__":
    unittest.main()
