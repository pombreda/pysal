import unittest
import pysal
from pysal.esda import moran
import numpy as np


class Moran_Tester(unittest.TestCase):
    def setUp(self):
        self.w=pysal.open("../../examples/stl.gal").read()
        f=pysal.open("../../examples/stl_hom.txt")
        self.y=np.array(f.by_col['HR8893'])
    def test_moran(self):
        mi=moran.Moran(self.y,self.w)
        self.assertAlmostEquals(mi.I,0.24365582621771659,7)
        self.assertAlmostEquals(mi.p_norm, 0.00027147862770937614)
    def test_sids(self):
        w=pysal.open("../../examples/sids2.gal").read()
        f=pysal.open("../../examples/sids2.dbf")
        SIDR=np.array(f.by_col("SIDR74"))
        mi=pysal.Moran(SIDR,w)
        self.assertAlmostEquals(mi.I,0.24772519320480135)
        self.assertAlmostEquals(mi.p_norm,0.00011583330781)

class Moran_BV_matrix_Tester(unittest.TestCase):
    def setUp(self):
        f=pysal.open("../../examples/sids2.dbf")
        varnames=['SIDR74','SIDR79','NWR74','NWR79']
        self.names=varnames
        vars=[np.array(f.by_col[var]) for var in varnames]
        self.vars=vars
        self.w=pysal.open("../../examples/sids2.gal").read()
    def test_Moran_BV_Matrix(self):
        res=moran.Moran_BV_matrix(self.vars,self.w,varnames=self.names)
        self.assertAlmostEquals(res[(0,1)].I,0.19362610652874668)
        self.assertAlmostEquals(res[(3,0)].I,0.37701382542927858)
        



suite = unittest.TestSuite()
test_classes = [Moran_Tester,Moran_BV_matrix_Tester]
for i in test_classes:
    a = unittest.TestLoader().loadTestsFromTestCase(i)
    suite.addTest(a)

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite)

