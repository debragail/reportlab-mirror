#Autogenerated by ReportLab guiedit do not edit
from reportlab.graphics.shapes import _DrawingEditorMixin, Drawing, Group, Rect, String
from reportlab.lib.colors import Color, CMYKColor, PCMYKColor

class ExplodedDrawing_Drawing(_DrawingEditorMixin,Drawing):
	def __init__(self,width=400,height=200,*args,**kw):
		Drawing.__init__(self,width,height,*args,**kw)
		self.transform = (1,0,0,1,0,0)
		self.add(Rect(0,0,100,20,rx=0,ry=0,fillColor=Color(1,1,0,1),fillOpacity=None,strokeColor=Color(0,0,0,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None))
		self.add(String(5,5,'Text in the box',textAnchor='start',fontName='Times-Roman',fontSize=12,fillColor=Color(0,0,0,1)))
		v0=self._nn(Group())
		v0.transform = (1,0,0,1,25,25)
		v0.add(Rect(0,0,100,20,rx=0,ry=0,fillColor=Color(1,1,0,1),fillOpacity=None,strokeColor=Color(0,0,0,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None))
		v0.add(String(5,5,'Text in the box',textAnchor='start',fontName='Times-Roman',fontSize=12,fillColor=Color(0,0,0,1)))
		v0=self._nn(Group())
		v0.transform = (1,0,0,1,25,25)
		v1=v0._nn(Group())
		v1.transform = (1,0,0,1,25,25)
		v1.add(Rect(0,0,100,20,rx=0,ry=0,fillColor=Color(1,1,0,1),fillOpacity=None,strokeColor=Color(0,0,0,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None))
		v1.add(String(5,5,'Text in the box',textAnchor='start',fontName='Times-Roman',fontSize=12,fillColor=Color(0,0,0,1)))
		v0=self._nn(Group())
		v0.transform = (1,0,0,1,25,25)
		v1=v0._nn(Group())
		v1.transform = (1,0,0,1,25,25)
		v2=v1._nn(Group())
		v2.transform = (1,0,0,1,25,25)
		v2.add(Rect(0,0,100,20,rx=0,ry=0,fillColor=Color(1,1,0,1),fillOpacity=None,strokeColor=Color(0,0,0,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None))
		v2.add(String(5,5,'Text in the box',textAnchor='start',fontName='Times-Roman',fontSize=12,fillColor=Color(0,0,0,1)))


if __name__=="__main__": #NORUNTESTS
	ExplodedDrawing_Drawing().save(formats=['pdf'],outDir='.',fnRoot=None)
