#Autogenerated by ReportLab guiedit do not edit
from reportlab.graphics.shapes import _DrawingEditorMixin, Drawing, Group, Line, String
from reportlab.lib.colors import Color, CMYKColor, PCMYKColor

class ExplodedDrawing_Drawing(_DrawingEditorMixin,Drawing):
	def __init__(self,width=400,height=200,*args,**kw):
		Drawing.__init__(self,width,height,*args,**kw)
		self.transform = (1,0,0,1,0,0)
		self.add(Line(75,75,375,75,strokeColor=Color(0,0,0,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None))
		self.add(Line(75,75,75,70,strokeColor=Color(0,0,0,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=10,strokeDashArray=None,strokeOpacity=None))
		self.add(Line(225,75,225,70,strokeColor=Color(0,0,0,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=10,strokeDashArray=None,strokeOpacity=None))
		self.add(Line(375,75,375,70,strokeColor=Color(0,0,0,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=10,strokeDashArray=None,strokeOpacity=None))
		v0=self._nn(Group())
		v0.transform = (1,0,0,1,150,70)
		v0.add(String(-10,-10,'Ying',textAnchor='start',fontName='Times-Roman',fontSize=10,fillColor=Color(0,0,0,1)))
		v0=self._nn(Group())
		v0.transform = (1,0,0,1,300,70)
		v0.add(String(-10.83,-10,'Yang',textAnchor='start',fontName='Times-Roman',fontSize=10,fillColor=Color(0,0,0,1)))


if __name__=="__main__": #NORUNTESTS
	ExplodedDrawing_Drawing().save(formats=['pdf'],outDir='.',fnRoot=None)
