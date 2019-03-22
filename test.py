import utils.datadict
import utils.sapsession
import SL.SL
import utils.DEFAULT
import unittest
import configparser

cfg = configparser.ConfigParser()
cfg.read('config.txt')
test_config = cfg['test']

class datadictTest(unittest.TestCase):

    def setUp(self):

        self.test_dict = utils.datadict.DataDictionnary({"Field1" : "Value1", "Field2" : "Value2"})
        self.new_dict = {"Field1" : "Value3", "Field3" : "Value4"}

    def test_update(self):

        self.test_dict.update_default(self.new_dict)
        self.assertEqual(self.test_dict, {"Field1" : "Value3", "Field2" : "Value2"})

class SapSessionTest(unittest.TestCase):

    "Should be run with correct SAP system running too"

    def setUp(self):
        self.app = utils.sapsession.SapSession(test_config.get('sap_system_name'))
        
    def test_attach(self):
        self.assertTrue(self.app.Session)

    def test_verify(self):
        
        element1 = self.app.verify_gui_element("wnd[0]/tbar[0]/okcd")
        element2 = self.app.verify_gui_element("wnd[0]/tbar[0]/ssqdhJQSLD")

        self.assertTrue(element1)
        self.assertFalse(element2)

class SLTest(unittest.TestCase):
    
    def setUp(self):
        self.app = utils.sapsession.SapSession(test_config.get('sap_system_name'))
        self.source_list = SL.SL.SL(test_config.get('material'),test_config.get('plant'),self.app)
        
    def test_isexist(self):
        tst = self.source_list.is_exist()
        self.assertFalse(tst)

    def test_updata(self):
        new_data = [{'Valid From' : 'Test'}]
        self.source_list.update_data(new_data)
        self.assertEqual(self.source_list.Data[0]['Valid From'], 'Test')

        new_data = [dict(),{'Valid From':'Test2'}]
        self.source_list.update_data(new_data)

        self.assertEqual(self.source_list.Data[0]['Valid From'], 'Test')
        self.assertEqual(self.source_list.Data[1]['Valid From'], 'Test2')

        self.source_list.update_data([{}],reset=True)
        self.assertEqual(self.source_list.Data, [utils.DEFAULT.DEFAULT_SL])

    def test_create_n_extract(self):
        ext = None
        self.source_list.update_data([{'Vendor' : test_config.get('vendor1'), "POrg" : test_config.get('porg1'), "Vendor Plant" : test_config.get('vendor_plant1')}])
        self.source_list.create_sl()
        tst = self.app.verify_transaction_success()
        print(tst)
        self.assertTrue(tst)
        
        ext = self.source_list.extract_sl()[0]
        self.assertEqual(ext, self.source_list.Data)

        self.source_list.update_data([{'Blocked': True},{"Vendor" : test_config.get('vendor2'),"POrg" : test_config.get('porg2'), "Vendor Plant" : test_config.get('vendor_plant2')}])
        self.source_list.update_sl()
        ext = self.source_list.extract_sl()[0]
        self.assertEqual(ext, self.source_list.Data)
        
        self.source_list.delete_sl(delete_all=True)
        tst2 = self.app.verify_transaction_success()
        self.assertTrue(tst2)
        ext = self.source_list.extract_sl()[1]
        self.assertEqual(ext, 0)
        

    
        
        
