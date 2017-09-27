from unittest import TestCase

from ccdl import CcDownload

class TestCcDownload(TestCase):

 def test_get_new_filename(self):
   ccDl = CcDownload()
   self.assertEqual("test.S02E086.mp4",ccDl.get_new_filename("test","http://www.cc.com/full-episodes/ijy227/the-nightly-show-with-larry-wilmore-april-5--2016---bill-nye-season-2-ep-02086"))
   self.assertEqual("test.S1E002.mp4",ccDl.get_new_filename("test","http://www.cc.com/episodes/i6r4tc/the-opposition-with-jordan-klepper-september-26--2017---neal-katyal-season-1-ep-1002"))
   self.assertEqual("test2.S21E086.mp4",ccDl.get_new_filename("test2","http://www.cc.com/full-episodes/xzj2nq/the-daily-show-with-trevor-noah-april-5--2016---jerrod-carmichael-season-21-ep-21086"))
   self.assertEqual("test2.S21E086.mp4",ccDl.get_new_filename("test2","http://www.cc.com/full-episodes/xzj2nq/the-daily-show-with-trevor-noah-april-5--2016---jerrod-carmichael-season-21-ep-21086/"))


