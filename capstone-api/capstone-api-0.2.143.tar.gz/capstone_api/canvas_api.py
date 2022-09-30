import time
import json
from configparser import ConfigParser

import pandas as pd
from pick import pick
from pathlib import Path
from urllib.parse import urljoin
from dateutil.parser import isoparse

import requests
from imgcat import imgcat
from oathtool import generate_otp
from requests_html import AsyncHTMLSession

from .class_api import ClassAPI


class CanvasAPI(ClassAPI):
    """Wrapper for Canvas REST API"""

    def __init__(self, course_id=0, reset=False):
        """Configs"""
        config_path = Path(Path.home(), '.config', 'capstone_api')
        cache_path = config_path.joinpath('.cache')
        self.config_file = config_path.joinpath('capstone_api.ini')
        self.cache_file = cache_path.joinpath('course.json')
        self.cache_courses = cache_path.joinpath('courses.json')

        if not config_path.exists():
            config_path.mkdir(parents=True)
        if not cache_path.exists():
            cache_path.mkdir(parents=True)

        if self.config_file.exists():
            config = ConfigParser()
            config.read(self.config_file)
            params = dict(config["canvas"].items())
            self.API_URL = params["api_url"]
            self.API_KEY = params["api_key"]
            self.USERNAME = params["username"]
            self.PASSWORD = params["password"]
            self.OATH_KEY = params["oath_key"]

        if course_id:
            self.setCourseID(course_id=course_id)
        else:
            self.selectCourse(reset=reset, extract=False)

        ClassAPI.__init__(self)

    def get(self, path, data={}):
        """Canvas wrapper for requests.get
        Args:
            path: The endpoint for Canvas API
            data: Payload parameters
        """
        url = urljoin(f'{self.API_URL}/', path.strip('/'))
        data.update({
            "access_token": self.API_KEY,
            "per_page": 100
        })
        r = requests.get(url=url, params=data)
        if 'json' in r.headers.get('Content-Type'):
            return r.json()
        return r.text

    def put(self, path, data={}):
        """Canvas wrapper for requests.put
        Args:
            path: The endpoint for Canvas API
            data: Payload parameters
        """
        url = urljoin(f'{self.API_URL}/', path.strip('/'))
        data.update({
            "access_token": self.API_KEY,
            "per_page": 100
        })
        r = requests.put(url=url, params=data)
        if 'json' in r.headers.get('Content-Type'):
            return r.json()
        return r.text


    def post(self, path, data={}):
        """Canvas wrapper for requests.get
        Args:
            path: The endpoint for Canvas API
            data: Payload parameters
        """
        url = urljoin(f'{self.API_URL}/', path.strip('/'))
        data.update({
            "access_token": self.API_KEY,
            "per_page": 100
        })
        r = requests.post(url=url, params=data)
        if 'json' in r.headers.get('Content-Type'):
            return r.json()
        return r.text

    def getCourses(self, reset=False, **kwargs):
        """
        Get Active Courses

        Args:
            Optional - enrollment_type (str)    - filter courses by enrollment type (teacher, student, ta, observer, designer)
            Optional - enrollment_state (int)   - filter courses by enrollment state (active, invited_or_pending, completed)
            Optional - state (str)              - filter courses by the given state (npublished, available, completed, deleted)
        Returns:
            courses (JSON Array)
        """
        path = f'/courses'

        if reset or not self.cache_courses.exists():
            courses = self.get(path=path, data=kwargs)
            self.courses = sorted(courses, key=lambda x: isoparse(x["start_at"]), reverse=True)
            self.cache_courses.write_text(json.dumps(self.courses, indent=2))
            return self.courses

        self.courses = json.loads(self.cache_courses.read_te6xt())
        return self.courses

    def getCourse(self, **kwargs):
        """
        Get Course Info from CourseID

        Args:
            Optional - course_id (int)  - ID of a given course (use cached if not provieded)
        """
        if kwargs.get('course_id'):
            self.setCourseID(kwargs.pop('course_id'))
            path = f"/courses/{self.COURSE_ID}"
            self.course = self.get(path=path, data=kwargs)
            return self.course

        self.course = self.selectCourse(reset=False, extract=True)
        return self.course

    def setCourseID(self, course_id=-1):
        """Helper Function to Set Course_ID in CanvasAPI Object"""
        self.COURSE_ID = course_id
        return

    def selectCourse(self, reset=False, extract=True):
        """
        Get CourseID from `cache` or `user selection`

        Cache_File: ~/.config/capstone_api/.cache/course.json

        Args:
            Optional - reset (bool)     - re-write the `Cache_File`
        """
        if reset or not self.cache_file.exists():
            # courses = sorted(self.getCourses(), key=lambda x: isoparse(x["start_at"]), reverse=True)
            courses = self.getCourses()
            course_names = [c["name"] for c in courses]
            name, index = pick(title='Select Course: ', options=course_names, indicator='🢧')
            course = courses[index]
            self.cache_file.write_text(json.dumps(course, indent=2))
            self.setCourseID(course_id=course["id"])
        else:
            course = json.loads(self.cache_file.read_text())
            self.setCourseID(course_id=course["id"])
        if extract:
            return course
        return

    def getCourseUsers(self, **kwargs):
        """
        Get List of Users in a Course

        Args:
            Optional - course_id (int)  - ID of a given course
        Returns:
            users (JSON Array)
        """
        if kwargs.get("course_id"):
            self.COURSE_ID = kwargs.pop('course_id')

        path = f"/courses/{self.COURSE_ID}/users"
        return self.get(path=path, data=kwargs)

    def getUserInfo(self, **kwargs):
        """
        Get Information About a Single User

        Args:
            Optional - course_id (int)
            Required - user_id (int)
        Returns:
            user (JSON Object)
        """
        if kwargs.get("course_id"):
            self.COURSE_ID = kwargs.pop('course_id')
        if kwargs.get("user_id"):
            user_id = kwargs.pop('user_id')

        path = f"/api/v1/courses/{self.COURSE_ID}/users/{user_id}"
        return self.get(path=path, data=kwargs)

    def getTeachers(self):
        """Get all Teachers"""
        return self.getCourseUsers(enrollment_type="teacher")

    def getTAs(self):
        """Get all TAs"""
        return self.getCourseUsers(enrollment_type="ta")

    def getStudents(self):
        """Get all Students"""
        # path = f"/courses/{self.COURSE_ID}/users"
        # return self.get(path=path)
        return self.getCourseUsers(enrollment_type="student")

    def getStudent(self, user_id):
        """Get student"""
        path = f"/courses/{self.COURSE_ID}/users/{user_id}"
        return self.get(path=path)

    def getStudentInfo(self, user_id):
        """Get student email address"""
        student = next((s for s in self.getStudents() if s["id"] == user_id), None)
        return student

    def editGroup(self, group_id=0, **kwargs):
        """Edit Group Info"""
        params = {**kwargs}
        path = f'/groups/{group_id}'
        return self.put(path=path, data=params)

    def createGroup(self, name='', group_category_id=0, **kwargs):
        """Create a Group Under Group Category"""
        params = {"name": name}
        if kwargs.get("description"):
            params.update({"description": kwargs["description"]})
        path = f"/group_categories/{group_category_id}/groups"
        return self.post(path=path, data=params)

    def createGroupMembership(self, user_id='', group_id=0, **kwargs):
        """Add a User to a Group"""
        path = f"/groups/{group_id}/memberships"
        params = {"user_id": user_id}
        return self.post(path=path, data=params)

    def getGroupCategories(self, **kwargs):
        """Get all Group Sets (Categories)"""
        if kwargs.get("course_id"):
            self.COURSE_ID = kwargs.pop('course_id')

        path = f"/courses/{self.COURSE_ID}/group_categories"
        group_cats = self.get(path=path)
        if len(group_cats) == 1:
            return group_cats[0]
        return group_cats

    def getGroups(self):
        """Get all groups"""
        path = f"/courses/{self.COURSE_ID}/groups"
        return self.get(path=path)

    def getGroup(self, group_id):
        """Get group"""
        path = f"/groups/{group_id}"
        return self.get(path=path)

    def getGroupStudents(self, group_id):
        """Get group members"""
        path = f"/groups/{group_id}/users"
        return self.get(path=path)

    def getQuizzes(self, **kwargs):
        """
        Get List of all Quizes in a Course

        Args:
            Optional - course_id (int)  - ID of a given course
        Returns:
            users (JSON Array)
        """
        if kwargs.get("course_id"):
            self.COURSE_ID = kwargs.pop('course_id')

        path = f"/courses/{self.COURSE_ID}/quizzes"
        return self.get(path=path, data=kwargs)

    def getQuiz(self, **kwargs):
        """
        Get List of all Quizes in a Course

        Args:
            Optional - quiz_id (int)  - ID of a given quiz
            Optional - title (str)    - Title of a quiz to search for
        Returns:
            users (JSON Array)
        """
        quizzes = self.getQuizzes()

        if kwargs.get("course_id"):
            self.COURSE_ID = kwargs.pop('course_id')

        if kwargs.get("quiz_id"):
            quiz_id = kwargs["quiz_id"]
            self.quiz_id = quiz_id
            return next(filter(lambda x: x["id"] == quiz_id, quizzes))

        if kwargs.get("title"):
            title = kwargs["title"]
            quiz = next(filter(lambda x: title.lower() in x["title"].lower(), quizzes))
            self.quiz_id = quiz["id"]
            return quiz

        path = f"/courses/{self.COURSE_ID}/quizzes"
        return self.get(path=path, data=kwargs)

    def getQuizSubmissions(self, quiz_id,  **kwargs):
        """
        Get List of all Quiz Submissions by quiz_id

        Args:
            Optional - course_id (int)  - ID of a given course
        Returns:
            users (JSON Array)
        """
        if kwargs.get("course_id"):
            self.COURSE_ID = kwargs.pop('course_id')

        self.quiz_id = quiz_id
        path = f"/courses/{self.COURSE_ID}/quizzes/{quiz_id}/submissions"
        return self.get(path=path, data=kwargs).get('quiz_submissions')

    def downloadQuizSubmission(self, submission):
        """
        Download Quiz Submission by submission object

        Args:
            Optional - course_id (int)  - ID of a given course
        Returns:
            users (JSON Array)
        """

        #path = f"/courses/{self.COURSE_ID}/quizzes/{self.quiz_id}/submissions/{submission['id']}"
        #quiz = self.get(path=path, data=kwargs)

        path = submission['result_url']
        params = {"validation_token": submission["validation_token"]}
        return self.get(path=path, data=params)

    def getAssignments(self):
        """Get all assignments for all students"""
        path = f"/courses/{self.COURSE_ID}/assignments"
        return self.get(path=path)

    def getAssignmentGroups(self):
        """Get assignment groups"""
        path = f"/courses/{self.COURSE_ID}/assignment_groups"
        return self.get(path=path)

    def getGroupAssignments(self, assignment_group_id):
        """Get assignments for all assignment groups"""
        path = f"/courses/{self.COURSE_ID}/assignment_groups/{assignment_group_id}"
        return self.get(path=path)

    def getSubmissions(self, assignment_id):
        """Get all student submissions for an assignment"""
        path = f"/courses/{self.COURSE_ID}/assignments/{assignment_id}/submissions"
        return self.get(path=path)

    async def downloadSubmissions(self, assignment_name, download_path):
        """Search assignment by name, then download all submissions"""
        assignment_id = next((a["id"] for a in self.getAssignments() if a["name"] == assignment_name), None)

        url = f"https://udel.instructure.com/courses/{self.COURSE_ID}/assignments/{assignment_id}"
        s = AsyncHTMLSession()
        r = await s.get(url)
        await r.html.arender(keep_page=True)
        await r.html.page.evaluate(f"""document.querySelector('input[name="udelnetid"]').value="{self.USERNAME}";""")
        await r.html.page.evaluate(f"""document.querySelector('input[name="pword"]').value="{self.PASSWORD}";""")
        png = await r.html.page.screenshot()
        imgcat(png)
        await r.html.page.evaluate("""document.querySelector('button[tabindex="3"]').click();""")
        time.sleep(3)

        pages = await r.html.browser.pages()
        oath_page = pages[1]
        pin = generate_otp(self.OATH_KEY)
        await oath_page.evaluate(f"""document.querySelector('input[name="oathKey"]').value="{pin}";""")
        png = await oath_page.screenshot()
        imgcat(png)
        await oath_page.evaluate("""document.querySelector('button[tabindex="6"]').click();""")
        time.sleep(3)

        await oath_page.goto(url)
        png = await oath_page.screenshot()
        imgcat(png)
        time.sleep(20)

        await oath_page.evaluate("""document.querySelector('a[id="download_submission_button"]').click();""")
        png = await oath_page.screenshot()
        imgcat(png)
        time.sleep(5)

        await oath_page._client.send('Page.setDownloadBehavior', {'behavior': 'allow', 'downloadPath': download_path})
        await oath_page.evaluate("""document.querySelector('a[href*="submissions"]').click();""")
        png = await oath_page.screenshot()
        imgcat(png)
        time.sleep(1)

        await pages[1].close()
        await pages[0].close()
        await oath_page.browser.close()
        time.sleep(1)
