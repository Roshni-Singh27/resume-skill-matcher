from resume_parser import extract_resume_text


class MockUploadedFile:

    def __init__(self, content, name):

        self.content = content
        self.name = name

    def read(self):

        return self.content


def test_txt_resume_parser():

    content = b"""
    Roshni Singh

    Python Developer

    Skills:
    Python, SQL, Git

    Education:
    B.Tech Computer Science

    Projects:
    AI Resume Matcher
    """

    file = MockUploadedFile(
        content,
        "resume.txt"
    )

    result = extract_resume_text(
        file
    )

    assert "Python Developer" in result
    assert "Python" in result
    assert "AI Resume Matcher" in result