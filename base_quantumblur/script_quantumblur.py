# me - this DAT
# scriptOp - the OP which is cooking

import numpy

# press 'Setup Parameters' in the OP to call this function to re-create the parameters.
def onSetupParameters(scriptOp):
	page = scriptOp.appendCustomPage('Custom')
	p = page.appendFloat('Valuea', label='Value A')
	p = page.appendFloat('Valueb', label='Value B')
	return

# called whenever custom pulse parameter is pushed
def onPulse(par):
	return


def onCook(scriptOp):
	a = numpy.random.randint(0, high=255, size=(2, 2, 4), dtype='uint8')
	scriptOp.copyNumpyArray(a)
	return
