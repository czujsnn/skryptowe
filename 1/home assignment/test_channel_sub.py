import unittest
import channel_sub

class Test_channel_subcribing(unittest.TestCase):
    global acc1, acc2, ch1, ch2, ch3, ch4

    acc1 = channel_sub.Account("User1")
    acc2 = channel_sub.Account("User2")

    ch1 = channel_sub.Channel("One chan","Blank description in here")
    ch2 = channel_sub.Channel("Two chan","Lorem ipsum dos semit")
    ch3 = channel_sub.Channel("Simple chan","")
    ch4 = channel_sub.Channel("4 chan","Very short desc in here")

    acc1.subscribe_to_channel(ch1)
    acc1.subscribe_to_channel(ch2)
    acc1.subscribe_to_channel(ch4)

    def test_subscribe_to_channelr(self):
        self.assertEqual(acc1.subscribe_to_channel(ch1), False) # Already subscribe_to_channeld
        self.assertEqual(acc1.subscribe_to_channel(ch3), True)
        self.assertEqual(acc2.subscribe_to_channel(ch4), True)
        with self.assertRaises(Exception):
            self.assertEqual(acc1.subscribe_to_channel("channel5"), False) # There is no channel no. 5

    def test_unsubscribe_to_channel(self):
        self.assertEqual(acc1.unsubscribe_to_channel(ch1), True)
        self.assertEqual(acc2.unsubscribe_to_channel(ch4), True)
        self.assertEqual(acc1.unsubscribe_to_channel(ch2), True)

    def test_change_description(self):
        ch1.update_channel_description(" more text XYZ.")
        self.assertEqual(ch1.channel_description, "Blank description in here more text XYZ.")

    def test_remove_description(self):
        self.assertEqual(ch1.remove_channel_description(), True)
        self.assertEqual(ch2.remove_channel_description(), True)
        self.assertEqual(ch3.remove_channel_description(), True)
        self.assertNotEqual(ch4.remove_channel_description(), False)


if __name__ == '__main__':
    unittest.main()