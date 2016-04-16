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

class MyFrame1 ( wx.Frame ):
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 473,240 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.Size( 473,240 ), wx.Size( 473,240 ) )
        
        gSizer1 = wx.GridSizer( 4, 3, 0, 0 )
        
        gSizer4 = wx.GridSizer( 1, 2, 0, 0 )
        
        self.m_checkBox1 = wx.CheckBox( self, wx.ID_ANY, u"SELF", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer4.Add( self.m_checkBox1, 0, wx.ALL, 5 )
        
        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"user name", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        self.m_staticText4.Wrap( -1 )
        gSizer4.Add( self.m_staticText4, 0, wx.ALL, 5 )
        
        
        gSizer1.Add( gSizer4, 1, wx.EXPAND, 5 )
        
        gSizer7 = wx.GridSizer( 0, 2, 0, 0 )
        
        self.m_textCtrl7 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
        gSizer7.Add( self.m_textCtrl7, 0, wx.ALL, 5 )
        
        self.m_button1 = wx.Button( self, wx.ID_ANY, u"connect", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
        gSizer7.Add( self.m_button1, 0, wx.ALL, 5 )
        
        
        gSizer1.Add( gSizer7, 1, wx.EXPAND, 5 )
        
        gSizer2 = wx.GridSizer( 1, 2, 0, 0 )
        
        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Status: ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )
        gSizer2.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
        
        self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"NONE", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )
        gSizer2.Add( self.m_staticText6, 0, wx.ALL, 5 )
        
        
        gSizer1.Add( gSizer2, 1, wx.EXPAND, 5 )
        
        gSizer5 = wx.GridSizer( 2, 2, 0, 0 )
        
        self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"USRP", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )
        gSizer5.Add( self.m_staticText8, 0, wx.ALL, 5 )
        
        self.m_radioBtn2 = wx.RadioButton( self, wx.ID_ANY, u"IP", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer5.Add( self.m_radioBtn2, 0, wx.ALL, 5 )
        
        
        gSizer5.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_radioBtn1 = wx.RadioButton( self, wx.ID_ANY, u"SERIAL", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer5.Add( self.m_radioBtn1, 0, wx.ALL, 5 )
        
        
        gSizer1.Add( gSizer5, 1, wx.EXPAND, 5 )
        
        self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,-1 ), 0 )
        gSizer1.Add( self.m_textCtrl2, 0, wx.ALL, 5 )
        
        self.m_button8 = wx.Button( self, wx.ID_ANY, u"Find Device", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_button8, 0, wx.ALL, 5 )
        
        gSizer6 = wx.GridSizer( 2, 2, 0, 0 )
        
        self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"File: ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )
        gSizer6.Add( self.m_staticText10, 0, wx.ALL, 5 )
        
        self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        gSizer6.Add( self.m_textCtrl6, 0, wx.ALL, 5 )
        
        self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Freq (Hz)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )
        gSizer6.Add( self.m_staticText11, 0, wx.ALL, 5 )
        
        self.m_textCtrl9 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer6.Add( self.m_textCtrl9, 0, wx.ALL, 5 )
        
        
        gSizer1.Add( gSizer6, 1, wx.EXPAND, 5 )
        
        
        gSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        gSizer8 = wx.GridSizer( 1, 2, 0, 0 )
        
        self.m_button2 = wx.Button( self, wx.ID_ANY, u"SEARCH", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
        gSizer8.Add( self.m_button2, 0, wx.ALL, 5 )
        
        self.m_button9 = wx.Button( self, wx.ID_ANY, u"START", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
        gSizer8.Add( self.m_button9, 0, wx.ALL, 5 )
        
        
        gSizer1.Add( gSizer8, 1, wx.EXPAND, 5 )
        
        self.m_button3 = wx.Button( self, wx.ID_ANY, u"STOP", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_button3, 0, wx.ALL, 5 )
        
        self.m_button5 = wx.Button( self, wx.ID_ANY, u"SAVE", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_button5, 0, wx.ALL, 5 )
        
        self.m_button6 = wx.Button( self, wx.ID_ANY, u"LOAD", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_button6, 0, wx.ALL, 5 )
        
        
        self.SetSizer( gSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_checkBox1.Bind( wx.EVT_CHECKBOX, self.disable_server )
        self.m_button1.Bind( wx.EVT_BUTTON, self.ssh_connect )
        self.m_button8.Bind( wx.EVT_BUTTON, self.usrp_find )
        self.m_button2.Bind( wx.EVT_BUTTON, self.file_search )
        self.m_button9.Bind( wx.EVT_BUTTON, self.usrp_start )
        self.m_button3.Bind( wx.EVT_BUTTON, self.usrp_abort )
        self.m_button5.Bind( wx.EVT_BUTTON, self.save )
        self.m_button6.Bind( wx.EVT_BUTTON, self.load )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def disable_server( self, event ):
        event.Skip()
    
    def ssh_connect( self, event ):
        event.Skip()
    
    def usrp_find( self, event ):
        event.Skip()
    
    def file_search( self, event ):
        event.Skip()
    
    def usrp_start( self, event ):
        event.Skip()
    
    def usrp_abort( self, event ):
        event.Skip()
    
    def save( self, event ):
        event.Skip()
    
    def load( self, event ):
        event.Skip()
    

