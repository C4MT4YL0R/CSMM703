(
// start the audio server
Server.default = Server.internal.boot;
)

(
// add some synthesis definitions
SynthDef(\ping,{
	arg freq = 440, amp = 0.1;
	var audio = LFTri.ar(freq,mul:amp);
	audio = audio * EnvGen.ar(Env.perc(0.005,0.200));
	Out.ar(0,audio!2);
}).add;
)

// test the synthesis definitions
(instrument:\ping,midinote:60).play;

OSCdef.help

// respond to OSC from Blender
(
OSCdef(\ping, {
	|msg, time, addr, port|
	msg.postln;
	(instrument:\ping,midinote:60).play;
},"/ping");
)








