import bge
import Generative
import random

def test():
	moveObject('Moon');
	directObject('Moon');
	
def moveObject(objName):
	scene = bge.logic.getCurrentScene();
	obj = scene.objects[objName];
	curx=obj.position.x;
	cury=obj.position.y;
	curz=obj.position.z;
	obj.worldPosition = [curx+obj['dx'],cury+obj['dy'],curz+obj['dz']];
				
def directObject(objName):
	scene = bge.logic.getCurrentScene();
	obj = scene.objects[objName];
	sensor = obj.sensors['c']; # get the collision sensor
	hitObject = sensor.hitObject; # get the object we hit
	
	if hitObject: # note: we check if this exists, because...
		# when we stop touching an object a collision event with no hitobject happens
		hitName = hitObject.name; # get the name of the object we hit
		print("hit!");
		print("hitName: " + str(hitName));
		Generative.makeGenerativeArt();
		chooseRandomDirection('Moon',random.randint(0,5));
	
def chooseRandomDirection(obj,n):
	scene = bge.logic.getCurrentScene();
	obj = scene.objects[obj];
	if n==0:
		obj['dz'] = 0.01;
		obj['dy'] = 0;
		obj['dx'] = 0;
	elif n==1:
		obj['dz'] = -0.01
		obj['dy'] = 0
		obj['dx'] = 0
	elif n==2:
		obj['dz'] = 0
		obj['dy'] = 0
		obj['dx'] = 0.01
	elif n==3:
		obj['dz'] = 0
		obj['dy'] = 0
		obj['dx'] = -0.01
	elif n==4:
		obj['dz'] = 0
		obj['dy'] = 0.01
		obj['dx'] = 0
	else:
		obj['dz'] = 0
		obj['dy'] = -0.01
		obj['dx'] = 0
