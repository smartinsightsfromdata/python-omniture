import unittest
import omniture



class UtilTest(unittest.TestCase):
    def setUp(self):
        fakelist = [{"id":"123", "title":"abc"},{"id":"456","title":"abc"}]

        self.alist = omniture.Value.list("segemnts",fakelist,{})


    def tearDown(self):
        del self.alist

    def test_addressable_list_repr_html_(self):
        """Test the _repr_html_ for AddressableList this is used in ipython """
        outlist = '<table><tr><td><b>ID</b></td><td><b>Title</b></td></tr><tr><td><b>123</b></td><td>abc</td></tr><tr><td><b>456</b></td><td>abc</td></tr></table>'
        self.assertEqual(self.alist._repr_html_(),outlist,\
                         "The _repr_html_ isn't working: {}"\
                         .format(self.alist._repr_html_()))

    def test_addressable_list_str_(self):
        """Test _str_ method """
        outstring = 'ID 123                       | Name: abc \nID 456                       | Name: abc \n'
        self.assertEqual(self.alist.__str__(),outstring,\
                         "The __str__ isn't working: {}"\
                         .format(self.alist.__str__()))

    def test_addressable_list_get_time(self):
        """ Test the custom get item raises a problem when there are duplicate names """
        with self.assertRaises(KeyError):
             self.alist['abc']
