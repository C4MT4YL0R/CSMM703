import bge
#progress = 1; instead of fixed, comes from somewhere else

def FirstStar (x,y):
    q = bge.logic.getRandomFloat()*3-5;
    pt1 = [q+x,-5+y,0];
    pt2 = [0+x,5+y,0];
    pt3 = [5+x,5+y,0];
    pt4 = [-7+x,2+y,0];
    pt5 = [7+x,2+y,0];
    colour = [1.0,bge.logic.getRandomFloat(),bge.logic.getRandomFloat()];
    if bge.logic.getRandomFloat() < 0.5:
        bge.render.drawLine(pt1,pt2,colour);
    if bge.logic.getRandomFloat() < 0.5:
        bge.render.drawLine(pt2,pt3,colour);
    if bge.logic.getRandomFloat() < 0.5:
        bge.render.drawLine(pt3,pt4,colour);
    if bge.logic.getRandomFloat() < 0.5:
        bge.render.drawLine(pt4,pt5,colour);
    if bge.logic.getRandomFloat() < 0.5:
        bge.render.drawLine(pt5,pt1,colour);
         
#FirstStar(0,0);

def FirstStarWrapper(m):
    for n in range(0,m+50):
        FirstStar(bge.logic.getRandomFloat()*20-10,bge.logic.getRandomFloat()*20-10);
        
def makeGenerativeArt():
	bge.logic.globalDict['progress'] = 1
	FirstStarWrapper(bge.logic.globalDict['progress']+20);
	FourthStarWrapper(bge.logic.globalDict['progress']+50);
	ThirdStarWrapper(bge.logic.globalDict['progress']+100);
	SecondStarWrapper(bge.logic.globalDict['progress']+200);
  
def SecondStar (x,y):
    q = bge.logic.getRandomFloat()*3-5;
    pt1 = [q+x,-9+y,0];
    pt2 = [2+x,3+y,0];
    pt3 = [4+x,5+y,0];
    pt4 = [7+x,4+y,0];
    pt5 = [7+x,2+y,0];
    colour = [bge.logic.getRandomFloat(),bge.logic.getRandomFloat(),1.0];
    if bge.logic.getRandomFloat() < 0.5:
        bge.render.drawLine(pt1,pt2,colour);
    if bge.logic.getRandomFloat() < 0.5:
        bge.render.drawLine(pt2,pt3,colour);
    if bge.logic.getRandomFloat() < 0.99:
        bge.render.drawLine(pt3,pt4,colour);
    if bge.logic.getRandomFloat() < 0.99:
        bge.render.drawLine(pt4,pt5,colour);
    if bge.logic.getRandomFloat() < 0.99:
        bge.render.drawLine(pt5,pt1,colour);
        
def SecondStarWrapper(m):
    for n in range(0,m):
    	SecondStar(bge.logic.getRandomFloat()*20-10,bge.logic.getRandomFloat()*20-10);
        

        
#SecondStar(0,0);
    
def ThirdStar (x,y):
    q = bge.logic.getRandomFloat()*3-5;
    pt1 = [q+x,2+y,0];
    pt2 = [0+x,1+y,0];
    pt3 = [7+x,1+y,0];
    pt4 = [-7+x,-3+y,0];
    pt5 = [7+x,2+y,0];
    colour = [bge.logic.getRandomFloat(),1.0, bge.logic.getRandomFloat()];
    if bge.logic.getRandomFloat() < 0.99:
        bge.render.drawLine(pt1,pt2,colour);
    if bge.logic.getRandomFloat() < 0.99:
        bge.render.drawLine(pt2,pt3,colour);
    if bge.logic.getRandomFloat() < 0.99:
        bge.render.drawLine(pt3,pt4,colour);
    if bge.logic.getRandomFloat() < 0.99:
        bge.render.drawLine(pt4,pt5,colour);
    if bge.logic.getRandomFloat() < 0.99:
        bge.render.drawLine(pt5,pt1,colour);

def ThirdStarWrapper(m):
    for n in range(0,m):
    	ThirdStar(bge.logic.getRandomFloat()*20-10,bge.logic.getRandomFloat()*20-10);
        

            
#ThirdStar(0,0);

def FourthStar (x,y):
    q = bge.logic.getRandomFloat()*3-5;
    pt1 = [q+x,2+y,0];
    pt2 = [8+x,2+y,0];
    pt3 = [7+x,7+y,0];
    pt4 = [-2+x,-3+y,0];
    pt5 = [7+x,2+y,0];
    colour = [bge.logic.getRandomFloat(),bge.logic.getRandomFloat(), bge.logic.getRandomFloat()];
    if bge.logic.getRandomFloat() < 0.99:
        bge.render.drawLine(pt1,pt2,colour);
    if bge.logic.getRandomFloat() < 0.99:
        bge.render.drawLine(pt2,pt3,colour);
    if bge.logic.getRandomFloat() < 0.99:
        bge.render.drawLine(pt3,pt4,colour);
    if bge.logic.getRandomFloat() < 0.99:
        bge.render.drawLine(pt4,pt5,colour);
    if bge.logic.getRandomFloat() < 0.99:
        bge.render.drawLine(pt5,pt1,colour);
        
def FourthStarWrapper(m):
    for n in range(0,m+20):
    	FourthStar(bge.logic.getRandomFloat()*20-10,bge.logic.getRandomFloat()*20-10);
        
        
                    
#FourthStar(0,0);
