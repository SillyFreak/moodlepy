from moodle import Moodle
from moodle.upload import File


class TestUpload:
    def test_upload(self, moodle: Moodle):
        files = moodle.upload(
            ('LICENSE', open('LICENSE', 'rb')),
        )
        assert type(files) == list
        assert len(files) == 1
        for f in files:
            assert isinstance(f, File)
            assert f.filename == 'LICENSE'
