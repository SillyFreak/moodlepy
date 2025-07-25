from typing import List

from moodle import BaseMoodle
from . import File


class Upload(BaseMoodle):
    def __call__(
        self, *files, itemid: int = 0, filepath: str = "/"
    ) -> List[File]:
        """Uploads files to moodle.

        Args:
            files (file-like-objects, multiple): The files to upload.
            moodlewsrestformat (str, optional): Expected format. Defaults to "json".
            itemid (int, optional): itemid to upload into. Defaults to 0.
            filepath (str, optional): file path under which to upload. Defaults to '/'.

        Returns:
            List[File]: The details for the uploaded files
        """
        data = self.moodle.post_upload(*files, itemid=itemid, filepath=filepath)
        return self._trs(File, data)
