# Copyright (c) 2010-2012, GEM Foundation.
#
# OpenQuake is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# OpenQuake is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with OpenQuake.  If not, see <http://www.gnu.org/licenses/>.

import unittest

from nose.plugins.attrib import attr

from openquake.db.models import OqJob

from tests.utils import helpers


class ProbabilisticEventBasedRiskQATest(unittest.TestCase):
    """QA tests for the Probabilistic Event Based Risk calculator."""

    @attr('qa')
    def test_probabilistic_risk(self):
        # The rudimentary beginnings of a QA test for the probabilistic
        # calculator. For now, just run it end-to-end
        # to make sure it doesn't blow up.
        cfg = helpers.demo_file(
            'probabilistic_event_based_risk/config_stest.gem')

        ret_code = helpers.run_job(cfg, ['--output-type=xml'])
        self.assertEqual(0, ret_code)

        job = OqJob.objects.latest('id')
        self.assertEqual('succeeded', job.status)
