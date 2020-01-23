import unittest
import qenviron


class TestCATPEnvironment():
    
    def test_commit(self):
        env = qenviron.CATPEnvironment()

        env._rewords = [
            1, 3, 4, 1, -4, 2, -8
        ]
        env.commit() 

        self.assertEqual(env.commit(), -1)

if __name__ == "__main__":
    unittest.main()
