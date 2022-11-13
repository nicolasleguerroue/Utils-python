import LTStruct as lts


def main():
	#Parameters

	lt = lts.LTStruct("tmp.asc")
	lt.displayInfos(True)
	# lt.setCursor(10,0) #Center of table drawing
	# lt.addNode("Ve") 		#create first Sallen key
	# lt.wire(lt.right(), 2)
	# lt.addText("This file has been automatically generated", 2, 20)
	# lt.addDoubleSupply(vcc=15.0, vee=15.0, name=["+VCC", "-VCC"], x=0, y=0)
	# lt.setCursor(10,0)

	lt.voltageDivider("ve", "vs", "10k","100k", lt.left())
	# lt.wire(lt.right(),5)
	# lt.voltageDivider("ve2", "vs2", 200,200)
	# lt.wire(lt.right(),5)
	# lt.passiveHighPass("ve3", "vs3", 1000,1000)
	# lt.wire(lt.right(),5)
	# lt.passiveLowPass("ve98", "vs4", "47k",1000)
	# lt.wire(lt.right(), 5)
	# lt.invertingAop("+VCC", "0", 1000, 1000)
	# lt.wire(lt.right(),10)
	# lt.nonInvertingAop("+VCC", "0", 1000, 1000)
	# lt.wire(lt.right(),10)
	# lt.nonInvertingAop("+VCC", "0", 1000, 1000)

	lt.addDirective(".tran 3", 10,50)
	lt.exportFile()
	lt.run()


if __name__ == '__main__':
	main()