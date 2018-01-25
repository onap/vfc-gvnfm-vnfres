# Copyright 2018 ZTE Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import unittest

from rest_framework import status
from rest_framework.test import APIClient


class SwaggerViewTest(unittest.TestCase):
    def setUp(self):
        self.client = APIClient()

    def tearDown(self):
        pass

    def test_swagger_ok(self):
        resp = self.client.get("/api/vnfres/v1/swagger.json", format="json")
        self.assertEqual(resp.status_code, status.HTTP_200_OK, resp.content)