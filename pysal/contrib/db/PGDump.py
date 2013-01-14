#!/usr/bin/python
__author__ = "Philip Stephens <philip.stephens@asu.edu "

__all__ = ['db2shape', 'db_table2gal']

from django.contrib.gis.gdal.geomtype import OGRGeomType
from osgeo import ogr
import pysal
import os

class db_object(connstring):
    """Class object that holds connection to database and implements
    methods for interacting with said db."""

    def __init__(connstring):
        """
        Instantiates connection to database.

        Arguments
        ---------
        connstring = A connection string with 4 parameters. Example is 
        "PG: host='localhost' dbname='pysaldb' user='myusername'
        password='my_password'"
        """
        # which connect utility will you use...ogr? sqlalchemy? django.gis?
        self.conn = ogr.Open(connstring)

    def db2shape(input, output):
        """
        dumps a postgis database table to shapefile 

        Arguments
        ---------
        input : the db table

        output : a filename

        Examples
        --------

        Note
        ----

        If a file exists with the same name as 'output', it will be deleted
        before being overwritten.
        """
        layer = self.conn.GetLayerByName(input)
        type = layer.GetGeomType()  # returns an int
        geom_type = OGRGeomType._types[type]  # map int to string description

        # Schema definition of SHP file
        out_driver = ogr.GetDriverByName( 'ESRI Shapefile' )
        if os.path.exists(output):
            out_driver.DeleteDataSource(output)
        out_ds = out_driver.CreateDataSource(output)
        out_srs = None
        out_layer = out_ds.CreateLayer(geom_type, out_srs, type)
        fd = ogr.FieldDefn('name',ogr.OFTString)
        out_layer.CreateField(fd)

        #layer = conn.ExecuteSQL(sql)

        feat = layer.GetNextFeature()
        while feat is not None:
            featDef = ogr.Feature(out_layer.GetLayerDefn())
            featDef.SetGeometry(feat.GetGeometryRef())
            #featDef.SetField('name',feat.TITLE)
            out_layer.CreateFeature(featDef)
            feat.Destroy()
            feat = layer.GetNextFeature()
        conn.Destroy()
        out_ds.Destroy()

    def db_table2gal(input, outfile, weights_type=Contiguity):
        """
        generates a GAL file from a postgis database table 

        Arguments
        ---------
        input : the db table

        output: the file to save output

        weights_type : type of spatial weights calculation, defaults to
        Contiguity

        Examples
        --------
        TBD 

        pseudo
        ------
        connect to db
        simplify
        create topo
        query topogeom  #layer = conn.ExecuteSQL(sql)
        return aswkt or asgeojson (geom.ExportToWkt())
        convert returned to pysal w 
        write w to GAL

        """
        pass


if __name__ == '__main__':
    import nose
    nose.runmodule()
