import os
import importlib
import pytest
import mdahole2

pytest.importorskip('duecredit')


@pytest.mark.skipif((os.environ.get('DUECREDIT_ENABLE', 'no').lower()
                     in ('no', '0', 'false')),
                     reason="duecredit is disabled")
class TestDuecredit:
    def test_duecredit_active(self):
        assert mdahole2.analysis.due.active

    def test_duecredit_collection(self):
        importlib.import_module('mdahole2.analysis.hole')

        dois = [
            "10.1016/s0006-3495(93)81293-1",
            "10.1016/s0263-7855(97)00009-x",
            "10.1016/j.jmb.2013.10.024"
        ]

        for doi in dois:
            assert mdahole2.analysis.due.citations[("mdahole2.analysis.hole", doi)].cites_module
