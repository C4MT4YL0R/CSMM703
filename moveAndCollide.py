import bge

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
		if hitName=="UpArrow":
			obj['dz'] = 0.1;
			obj['dy'] = 0;
			obj['dx'] = 0;
		if hitName=="DownArrow":
			obj['dz'] = -0.1
			obj['dy'] = 0
			obj['dx'] = 0
		if hitName=="LeftXArrow":
			obj['dz'] = 0
			obj['dy'] = 0
			obj['dx'] = 0.1
		if hitName=="RightXArrow":
			obj['dz'] = 0
			obj['dy'] = 0
			obj['dx'] = -0.1
		if hitName=="LeftYArrow":
			obj['dz'] = 0
			obj['dy'] = 0.1
			obj['dx'] = 0
		if hitName=="RightYArrow":
			obj['dz'] = 0
			obj['dy'] = -0.1
			obj['dx'] = 0
