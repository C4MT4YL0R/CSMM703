import Rasterizer
import bge
import Generative

# the main setup function called once at engine launch
def setup():
        print("running setup()");
        bge.logic.globalDict['progress'] = 0;
        screamHopelesslyUntilGodComesBack();
        print("completed setup()");

def draw():
        print("draw()");
        Generative.makeGenerativeArt();

# this next function is just for testing, assumes a keyboard sensor called 'test'
def testProgressIncrement():
        controller = bge.logic.getCurrentController();
        test = controller.sensors['test'];
        if test:
                if test.status==1:
                        x = bge.logic.globalDict['progress'];
                        bge.logic.globalDict['progress'] = x + 1;
	
def loadBlend(status):
	print("Loaded %s" % status.libraryName);
	
def screamHopelesslyUntilGodComesBack():
        print("screamHopelessleyUntilGodComesBack()");
        Rasterizer.showMouse(1);
        controller = bge.logic.getCurrentController();
        owner = controller.owner;
        scene = bge.logic.getCurrentScene();
        objects = scene.objects;
        bge.logic.LibLoad('//bluestar.blend','Scene',async=True).onFinish = loadBlend
        bge.logic.LibLoad('//blackstar.blend','Scene',async=True).onFinish = loadBlend;
        bge.logic.LibLoad('//greenstar.blend','Scene',async=True).onFinish = loadBlend;
        bge.logic.LibLoad('//pinkstar.blend','Scene',async=True).onFinish = loadBlend;
        bge.logic.LibLoad('//yellowstar.blend','Scene',async=True).onFinish = loadBlend;
        bge.logic.LibLoad('//arrow.blend','Scene',async=True).onFinish = loadBlend;
        scene.objects["Camera"].position = [0,0,9];
        import GameLogic as g;
        g.objectSelected = None;
	
def makeSmallStar():
	controller = bge.logic.getCurrentController();
	owner = controller.owner;
	scene = bge.logic.getCurrentScene();
	objects = scene.objects;
	import GameLogic as g;

	sensor = controller.sensors["1"]
	if sensor:
		if sensor.status == 1:
			duh = scene.addObject("Blue star",owner);
			duh.position = [0,0,5];
			g.objectSelected = duh;
			
def makeBigStar():
	controller = bge.logic.getCurrentController();
	owner = controller.owner;
	scene = bge.logic.getCurrentScene();
	objects = scene.objects;
	import GameLogic as g;
		
	sensor = controller.sensors["2"]
	if sensor:
		if sensor.status == 1:
			duh = scene.addObject("Black star",owner);
			duh.position = [0,0,5];
			g.objectSelected = duh;
			
def makeGreenStar():
	controller = bge.logic.getCurrentController();
	owner = controller.owner;
	scene = bge.logic.getCurrentScene();
	objects = scene.objects;
	import GameLogic as g;
		
	sensor = controller.sensors["3"]
	if sensor:
		if sensor.status == 1:
			duh = scene.addObject("Green star",owner);
			duh.position = [0,0,5];
			g.objectSelected = duh;
			
def makePinkStar():
	controller = bge.logic.getCurrentController();
	owner = controller.owner;
	scene = bge.logic.getCurrentScene();
	objects = scene.objects;
	import GameLogic as g;
		
	sensor = controller.sensors["4"]
	if sensor:
		if sensor.status == 1:
			duh = scene.addObject("Pink star",owner);
			duh.position = [0,0,5];
			g.objectSelected = duh;
			
def makeArrow():
	controller = bge.logic.getCurrentController();
	owner = controller.owner;
	scene = bge.logic.getCurrentScene();
	objects = scene.objects;
	import GameLogic as g;
		
	sensor = controller.sensors["5"]
	if sensor:
		if sensor.status == 1:
			duh = scene.addObject("Arrow",owner);
			duh.position = [0,0,5];
			g.objectSelected = duh;
			
def makeYellowStar():
	controller = bge.logic.getCurrentController();
	owner = controller.owner;
	scene = bge.logic.getCurrentScene();
	objects = scene.objects;
	import GameLogic as g;
		
	sensor = controller.sensors["6"]
	if sensor:
		if sensor.status == 1:
			duh = scene.addObject("Yellow star",owner);
			duh.position = [0,0,5];
			g.objectSelected = duh;
			
def justAStepToTheRight():
	import GameLogic as g;
	g.objectSelected.position.x += 0.1;
