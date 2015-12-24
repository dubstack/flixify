__author__ = 'SN GUPTA'
import wx

col = [wx.BLACK,wx.RED,wx.GREEN,wx.YELLOW,wx.WHITE]
class DrawPanel(wx.Frame):

    """Draw a line to a panel."""

    def __init__(self,parent, id, title,score):
        wx.Frame.__init__(self, parent, id, title)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.score = score
        self.rcnt = 0

    def OnPaint(self, event=None):
        dc = wx.PaintDC(self)
        dc.Clear()
        for s in self.score:
            self.addRect(s,dc)

    def addRect(self,color,dc):
        dc.SetPen(wx.Pen(col[color], 4))
        dc.DrawLine(self.rcnt,0, self.rcnt, 100)
        print self.rcnt
        self.rcnt = self.rcnt + 1
