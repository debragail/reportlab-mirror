#Autogenerated by ReportLab guiedit do not edit
from reportlab.graphics.shapes import _DrawingEditorMixin, Drawing, Group, Wedge, String
from reportlab.lib.colors import Color, CMYKColor, PCMYKColor

class ExplodedDrawing_Drawing(_DrawingEditorMixin,Drawing):
	def __init__(self,width=400,height=400,*args,**kw):
		Drawing.__init__(self,width,height,*args,**kw)
		self.transform = (1,0,0,1,0,0)
		self.add(Wedge(200,200,90,72.85714,90,yradius=90,annular=False,fillColor=Color(0,.545098,.545098,1),fillOpacity=None,strokeColor=Color(0,0,0,1),strokeWidth=0,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None,radius1=30,yradius1=30))
		self.add(Wedge(200,200,90,38.57143,72.85714,yradius=90,annular=False,fillColor=Color(0,.545098,.545098,1),fillOpacity=None,strokeColor=Color(0,0,0,1),strokeWidth=0,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None,radius1=30,yradius1=30))
		self.add(Wedge(200,200,90,-12.85714,38.57143,yradius=90,annular=False,fillColor=Color(0,.545098,.545098,1),fillOpacity=None,strokeColor=Color(0,0,0,1),strokeWidth=0,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None,radius1=30,yradius1=30))
		self.add(Wedge(200,200,90,-81.42857,-12.85714,yradius=90,annular=False,fillColor=Color(0,.545098,.545098,1),fillOpacity=None,strokeColor=Color(0,0,0,1),strokeWidth=0,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None,radius1=30,yradius1=30))
		self.add(Wedge(200,200,90,-167.1429,-81.42857,yradius=90,annular=False,fillColor=Color(0,.545098,.545098,1),fillOpacity=None,strokeColor=Color(0,0,0,1),strokeWidth=0,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None,radius1=30,yradius1=30))
		self.add(Wedge(200,200,90,-270,-167.1429,yradius=90,annular=False,fillColor=Color(0,.545098,.545098,1),fillOpacity=None,strokeColor=Color(0,0,0,1),strokeWidth=0,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None,radius1=30,yradius1=30))
		self.add(Wedge(200,200,150,-306,-270,yradius=150,annular=False,fillColor=Color(.541176,.168627,.886275,1),fillOpacity=None,strokeColor=Color(0,0,0,1),strokeWidth=0,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None,radius1=90,yradius1=90))
		self.add(Wedge(200,200,150,-378,-306,yradius=150,annular=False,fillColor=Color(.541176,.168627,.886275,1),fillOpacity=None,strokeColor=Color(0,0,0,1),strokeWidth=0,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None,radius1=90,yradius1=90))
		self.add(Wedge(200,200,150,-486,-378,yradius=150,annular=False,fillColor=Color(.541176,.168627,.886275,1),fillOpacity=None,strokeColor=Color(0,0,0,1),strokeWidth=0,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None,radius1=90,yradius1=90))
		self.add(Wedge(200,200,150,-630,-486,yradius=150,annular=False,fillColor=Color(.541176,.168627,.886275,1),fillOpacity=None,strokeColor=Color(0,0,0,1),strokeWidth=0,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None,radius1=90,yradius1=90))
		self.add(String(226.8276,377.9895,'a',textAnchor='middle',fontName='Times-Roman',fontSize=10,fillColor=Color(0,0,0,1)))
		self.add(String(301.3976,348.723,'b',textAnchor='middle',fontName='Times-Roman',fontSize=10,fillColor=Color(0,0,0,1)))
		self.add(String(375.487,240.0538,'c',textAnchor='middle',fontName='Times-Roman',fontSize=10,fillColor=Color(0,0,0,1)))
		self.add(String(322.4311,68.05066,'d',textAnchor='middle',fontName='Times-Roman',fontSize=10,fillColor=Color(0,0,0,1)))
		self.add(String(98.60239,51.27702,'e',textAnchor='middle',fontName='Times-Roman',fontSize=10,fillColor=Color(0,0,0,1)))
		self.add(String(59.27033,312.2282,'f',textAnchor='middle',fontName='Times-Roman',fontSize=10,fillColor=Color(0,0,0,1)))


if __name__=="__main__": #NORUNTESTS
	ExplodedDrawing_Drawing().save(formats=['pdf'],outDir='.',fnRoot=None)
