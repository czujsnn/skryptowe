import unittest
import channel_sub

class Test_channel_subcribing(unittest.TestCase):
    global acc1, acc2, ch1, ch2, ch3, ch4

    acc1 = channel_sub.Account("User1")
    acc2 = channel_sub.Account("User2")

    ch1 = channel_sub.Channel("Channel1","...")
    ch2 = channel_sub.Channel("Channel2","aaaaaaaaaaaa")
    ch3 = channel_sub.Channel("Blank Channel","")
    ch4 = channel_sub.Channel("Channel4","unittest")

    acc1.subscribe_to_channel(ch1)
    acc1.subscribe_to_channel(ch2)
    acc1.subscribe_to_channel(ch4)

    def test_subscribe_to_channels(self):

        self.assertEqual(acc1.subscribe_to_channel(ch1), False) # Already subscribe_to_channeld
        self.assertEqual(acc1.subscribe_to_channel(ch3), True)
        self.assertEqual(acc2.subscribe_to_channel(ch4), True)
        with self.assertRaises(Exception):
            self.assertEqual(acc1.subscribe_to_channel("Non existent channel"), False) # There is no channel no. 5

    def test_unsubscribe_to_channels(self):

        self.assertEqual(acc1.unsubscribe_to_channel(ch1), True)
        self.assertEqual(acc2.unsubscribe_to_channel(ch4), True)
        self.assertEqual(acc1.unsubscribe_to_channel(ch2), True)

    def test_change_description_to_channel1(self):

        ch1.update_channel_description(" added description to channel1.")
        self.assertEqual(ch1.channel_description, "... added description to channel1.")

    def test_remove_descriptions(self):

        self.assertEqual(ch1.remove_channel_description(), True)
        self.assertEqual(ch2.remove_channel_description(), True)
        self.assertEqual(ch3.remove_channel_description(), True)
        self.assertNotEqual(ch4.remove_channel_description(), False)


if __name__ == '__main__':
    unittest.main()