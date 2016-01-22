import unittest

import party


class PartyTests(unittest.TestCase):
    """Tests for my party site."""

    def setUp(self):
        self.client = party.app.test_client()
        
        # Use this to test user's state of RSVP for that session:
        # with self.client.session_transaction() as sess:
        #     sess['rsvp'] = False


        party.app.config['TESTING'] = True

    def test_homepage(self):
        result = self.client.get("/")
        self.assertIn("I'm having a party", result.data)

    def test_no_rsvp_yet(self):
        # FIXME: Add a test to show we haven't RSVP'd yet
        result = self.client.get("/")
        with self.client.session_transaction() as sess:
            if 'rsvp' not in sess:
                self.assertIn("RSVP", result.data)
                self.assertNotIn("Details", result.data)

    def test_rsvp(self):
        result = self.client.post("/rsvp",
                                  data={'name': "Jane", 'email': "jane@jane.com"},
                                  follow_redirects=True)
        # FIXME: check that once we log in we see party details--but not the form!
        self.assertIn("Details", result.data)

    def test_rsvp_mel(self):
        # FIXME: write a test that mel can't invite himself
        pass
        print "FIXME"


if __name__ == "__main__":
    unittest.main()