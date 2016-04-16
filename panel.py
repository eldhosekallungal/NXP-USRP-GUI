# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyPanel1 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        gSizer2 = wx.GridSizer( 1, 1, 0, 0 )
        
        m_listBox1Choices = []
        self.m_listBox1 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 480,280 ), m_listBox1Choices, 0 )
        self.m_listBox1.SetMinSize( wx.Size( 480,280 ) )
        
        gSizer2.Add( self.m_listBox1, 0, wx.ALL, 5 )
        
        
        self.SetSizer( gSizer2 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_listBox1.Bind( wx.EVT_LISTBOX_DCLICK, self.copy )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def copy( self, event ):
        event.Skip()
    

