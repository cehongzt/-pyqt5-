from PyQt5.Qt import *
from sklearn.externals import joblib
class Window(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("钢管混凝土柱承载力预测")
            self.setFixedSize(400, 500)

import sys
app=QApplication(sys.argv)

window=Window()
label1=QLabel(window)
label1.setText("Author : hongzt")

label1.setContentsMargins(100,0,0,10)
label1.resize(600,50)
label2=QLabel(window)
label2.move(50,100)
label2.setText("D(mm)")
lined=QLineEdit(window)

lined.move(200,90)
label3=QLabel(window)
label3.move(50,150)
label3.setText("t(mm)")
linet=QLineEdit(window)

linet.move(200,140)
label4=QLabel(window)
label4.move(50,200)
label4.setText("l(mm)")
linel=QLineEdit(window)

linel.move(200,190)
label5=QLabel(window)
label5.move(50,250)
label5.setText("fy(MPa)")
linefy=QLineEdit(window)

linefy.move(200,240)
label6=QLabel(window)
label6.move(50,300)
label6.setText("fc(MPa)")
linefc=QLineEdit(window)
linefc.move(200,290)
btp=QPushButton(window)
btp.setText("预测极限承载力")
btp.move(50,350)
btc=QPushButton(window)
btc.setText("关闭")
btc.move(200,350)
btp.setEnabled(False)
def inp(text):
    if len(text)>0  :
        btp.setEnabled(True)
    else:
        btp.setEnabled(False)

lined.textChanged.connect(inp)
linet.textChanged.connect(inp)
linel.textChanged.connect(inp)
linefy.textChanged.connect(inp)
linefc.textChanged.connect(inp)
lineprediet=QLineEdit(window)
lineprediet.move(50,400)
lined.setToolTip("请输入钢管直径")
linet.setToolTip("请输入钢管厚度")
linel.setToolTip("请输入组合构建长度")
linefy.setToolTip("请输入钢管强度")
linefc.setToolTip("请输入核心混凝土强度")
def contentinput():
    connectd=lined.text()
    connectt=linet.text()
    connectl = linel.text()
    connectfy = linefy.text()
    connectfc= linefc.text()
    a=[[float(connectd),float(connectt),float(connectl),float(connectfy),float(connectfc)]]
    c=predietmodel.predict(a)
    predietmax=str(c)
    lineprediet.setText(predietmax)



predietmodel= joblib.load('tiaocanLgbm.model1')

btp.clicked.connect(contentinput)

#lineprediet.setText(predietmodel.predict([[200,50,300,4,600]]))

btc.clicked.connect(QCoreApplication.instance().quit)



window.show()

sys.exit(app.exec())

