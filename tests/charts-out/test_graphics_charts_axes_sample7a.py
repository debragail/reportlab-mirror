#Autogenerated by ReportLab guiedit do not edit
from reportlab.graphics.shapes import _DrawingEditorMixin, Drawing, Group, Line, String
from reportlab.lib.colors import Color, CMYKColor, PCMYKColor

class ExplodedDrawing_Drawing(_DrawingEditorMixin,Drawing):
	def __init__(self,width=400,height=200,*args,**kw):
		Drawing.__init__(self,width,height,*args,**kw)
		self.transform = (1,0,0,1,0,0)
		self.add(Line(50,50,350,50,strokeColor=Color(0,0,0,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None))
		self.add(Line(50,50,50,45,strokeColor=Color(0,0,0,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=10,strokeDashArray=None,strokeOpacity=None))
		self.add(Line(143.75,50,143.75,45,strokeColor=Color(0,0,0,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=10,strokeDashArray=None,strokeOpacity=None))
		self.add(Line(237.5,50,237.5,45,strokeColor=Color(0,0,0,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=10,strokeDashArray=None,strokeOpacity=None))
		self.add(Line(331.25,50,331.25,45,strokeColor=Color(0,0,0,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=10,strokeDashArray=None,strokeOpacity=None))
		v0=self._nn(Group())
		v0.transform = (1,0,0,1,50,45)
		v0.add(String(-5,-10,'10',textAnchor='start',fontName='Times-Roman',fontSize=10,fillColor=Color(0,0,0,1)))
		v0=self._nn(Group())
		v0.transform = (1,0,0,1,143.75,45)
		v0.add(String(-5,-10,'20',textAnchor='start',fontName='Times-Roman',fontSize=10,fillColor=Color(0,0,0,1)))
		v0=self._nn(Group())
		v0.transform = (1,0,0,1,237.5,45)
		v0.add(String(-5,-10,'30',textAnchor='start',fontName='Times-Roman',fontSize=10,fillColor=Color(0,0,0,1)))
		v0=self._nn(Group())
		v0.transform = (1,0,0,1,331.25,45)
		v0.add(String(-5,-10,'40',textAnchor='start',fontName='Times-Roman',fontSize=10,fillColor=Color(0,0,0,1)))
		self.add(Line(350,50,350,175,strokeColor=Color(0,0,0,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None))
		self.add(Line(350,50,345,50,strokeColor=Color(0,0,0,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=10,strokeDashArray=None,strokeOpacity=None))
		self.add(Line(350,81.25,345,81.25,strokeColor=Color(0,0,0,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=10,strokeDashArray=None,strokeOpacity=None))
		self.add(Line(350,112.5,345,112.5,strokeColor=Color(0,0,0,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=10,strokeDashArray=None,strokeOpacity=None))
		self.add(Line(350,143.75,345,143.75,strokeColor=Color(0,0,0,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=10,strokeDashArray=None,strokeOpacity=None))
		self.add(Line(350,175,345,175,strokeColor=Color(0,0,0,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=10,strokeDashArray=None,strokeOpacity=None))
		v0=self._nn(Group())
		v0.transform = (1,0,0,1,345,65.625)
		v0.add(String(-18.88,-4,'Beer',textAnchor='start',fontName='Times-Roman',fontSize=10,fillColor=Color(0,0,0,1)))
		v0=self._nn(Group())
		v0.transform = (1,0,0,1,345,96.875)
		v0.add(String(-21.66,-4,'Wine',textAnchor='start',fontName='Times-Roman',fontSize=10,fillColor=Color(0,0,0,1)))
		v0=self._nn(Group())
		v0.transform = (1,0,0,1,345,128.125)
		v0.add(String(-20.55,-4,'Meat',textAnchor='start',fontName='Times-Roman',fontSize=10,fillColor=Color(0,0,0,1)))
		v0=self._nn(Group())
		v0.transform = (1,0,0,1,345,159.375)
		v0.add(String(-43.89,-4,'Cannelloni',textAnchor='start',fontName='Times-Roman',fontSize=10,fillColor=Color(0,0,0,1)))


if __name__=="__main__": #NORUNTESTS
	ExplodedDrawing_Drawing().save(formats=['pdf'],outDir='.',fnRoot=None)
