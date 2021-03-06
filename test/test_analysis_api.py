# coding: utf-8

"""
    IdCheck.IO API

    Check identity documents

    OpenAPI spec version: 0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import os
import sys
import unittest

import idcheckio_python_client
from idcheckio_python_client.rest import ApiException
from idcheckio_python_client.apis.analysis_api import AnalysisApi


class TestAnalysisApi(unittest.TestCase):
    """ AnalysisApi unit test stubs """

    def setUp(self):
        self.api = idcheckio_python_client.apis.analysis_api.AnalysisApi()

    def tearDown(self):
        pass

    def test_get_report(self):
        """
        Test case for get_report

        HTTP GET report (demo)
        """
        pass

    def test_get_result(self):
        """
        Test case for get_result

        HTTP GET result
        """
        pass

    def test_get_task(self):
        """
        Test case for get_task

        HTTP GET task
        """
        pass

    def test_post_image(self):
        """
        Test case for post_image

        HTTP POST task image
        """
        pass

    def test_post_mrz(self):
        """
        Test case for post_mrz

        HTTP POST task mrz
        """
        pass


if __name__ == '__main__':
    unittest.main()
