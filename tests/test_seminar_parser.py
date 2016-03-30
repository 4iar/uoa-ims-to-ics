from ims_to_ics.seminar_parser import get_event_ids, fetch_events_as_ics, extract_event

import unittest
import responses
from unittest import mock

class SeminarParserTestCase(unittest.TestCase):

    @responses.activate
    def test_get_event_ids(self):

        body = """
        <rss version="2.0">
        <channel>
        <item>
            <link>https://www.abdn.ac.uk/ims/seminars/8939/</link>
            <guid isPermaLink="true">https://www.abdn.ac.uk/ims/seminars/8939/</guid>
            <title><![CDATA['Micro molecules - major effects in rheumatic diseases?']]></title>
            <pubDate>Thu, 31 Mar 2016 13:00:00 +0100</pubDate>
            <description><![CDATA[Professor Iain McInnes, Institute of Infection, Immunity & Inflammation, University of Glasgow<br /><b>Venue:</b> Institute of Medical Sciences - Level 7 Conference Room<br /><br />]]></description>
        </item>
        <item>
            <link>https://www.abdn.ac.uk/ims/seminars/9131/</link>
            <guid isPermaLink="true">https://www.abdn.ac.uk/ims/seminars/9131/</guid>
            <title><![CDATA[May Festival Programme Launch ]]></title>
            <pubDate>Mon, 18 Apr 2016 09:30:00 +0100</pubDate>
            <description><![CDATA[<a href="https://www.abdn.ac.uk/ims/seminars/9131/"><img src="https://www.abdn.ac.uk/events/images/thumbs/MAY_FESTIVAL_LOGO__DATE.jpg" alt="" /></a><br />Programme launched and tickets on sale now!<br /><br />]]></description>
        </item>
        <item>
            <link>https://www.abdn.ac.uk/ims/seminars/8941/</link>
            <guid isPermaLink="true">https://www.abdn.ac.uk/ims/seminars/8941/</guid>
            <title><![CDATA['Investigating redox signalling in the human fungal pathogen Cryptococcus neoformans']]></title>
            <pubDate>Tue, 19 Apr 2016 13:00:00 +0100</pubDate>
            <description><![CDATA[Andrew Alspaugh, Department of Medicine - Duke University School of Medicine, Durham, NC, USA<br /><b>Venue:</b> Institute of Medical Sciences - Level 7 Conference Room<br /><br />]]></description>
        </item>
        </channel>
        </rss>
        """
        responses.add(responses.GET, "https://www.abdn.ac.uk/ims/seminars/rss.xml",
                      body=body,
                      content_type="text/xsl")

        self.assertEqual(get_event_ids(), ['8939', '9131', '8941'])

    def test_extract_event(self):
        ics_raw = 'BEGIN:VCALENDAR\r\nCalendar data goes here\nEND:VCALENDAR\r\n'
        ics_extracted = 'Calendar data goes here\n'

        self.assertEqual(extract_event(ics_raw), ics_extracted)

    @mock.patch('ims_to_ics.seminar_parser.get_event_ids')
    @mock.patch('ims_to_ics.seminar_parser.extract_event', side_effect=['clean ics 1\n', 'clean ics 2\n'])
    @responses.activate
    def test_fetch_events_as_ics(self, mock_extract_event, mock_get_event_ids):

        mock_extract_event.return_value = '1234'
        mock_get_event_ids.return_value = ['1', '2']

        responses.add(responses.GET, "https://www.abdn.ac.uk/ims/seminars/ical/1/",
                      body="raw ics 1",
                      content_type="text/calendar")

        responses.add(responses.GET, "https://www.abdn.ac.uk/ims/seminars/ical/2/",
                      body="raw ics 2",
                      content_type="text/calendar")

        ics = "BEGIN:VCALENDAR\r\nclean ics 1\nclean ics 2\nEND:VCALENDAR\r\n"
        self.assertEqual(fetch_events_as_ics(), ics)

        mock_extract_event.assert_called_once('raw ics 1')
        mock_extract_event.assert_called_once('raw ics 2')


if __name__ == "__main__":
    unittest.main()
