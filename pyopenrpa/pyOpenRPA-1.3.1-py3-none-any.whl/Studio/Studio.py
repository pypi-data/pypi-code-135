from http.server import BaseHTTPRequestHandler, HTTPServer
import pdb
import pywinauto
import json
import subprocess
import zlib
import os
import sys
import traceback
from . import RobotConnector
from . import JSONNormalize
from ..Tools import Usage
import importlib
#Единый глобальный словарь (За основу взять из Settings.py)
global gSettingsDict
#Call Settings function from argv[1] file
################################################
lSubmoduleFunctionName = "Settings"
lFileFullPath = sys.argv[1]
lModuleName = (lFileFullPath.split("\\")[-1])[0:-3]
lTechSpecification = importlib.util.spec_from_file_location(lModuleName, lFileFullPath)
lTechModuleFromSpec = importlib.util.module_from_spec(lTechSpecification)
lTechSpecificationModuleLoader = lTechSpecification.loader.exec_module(lTechModuleFromSpec)
gSettingsDict = None
if lSubmoduleFunctionName in dir(lTechModuleFromSpec):
    # Run SettingUpdate function in submodule
    gSettingsDict = getattr(lTechModuleFromSpec, lSubmoduleFunctionName)()
#################################################
RobotConnector.mGlobalDict = gSettingsDict
#Init the robot
RobotConnector.UIDesktop.Utils.ProcessBitness.SettingsInit(gSettingsDict["ProcessBitness"])

from pyOpenRPA.Utils.Render import Render
from pyOpenRPA.Tools import CrossOS # https://schedule.readthedocs.io/en/stable/examples.html
lFileStr = CrossOS.PathJoinList(CrossOS.PathSplitList(__file__)[:-2] + ["Resources","Web","orpa","std.xhtml"])
gRender = Render(inTemplatePathStr=lFileStr,inTemplateRefreshBool=True)
from pyOpenRPA import __version__


# HTTP Studio web server class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
    #ResponseContentTypeFile
    def SendResponseContentTypeFile(self,inContentType,inFilePath):
        # Send response status code
        self.send_response(200)
        # Send headers
        self.send_header('Content-type',inContentType)
        self.end_headers()
        lFileObject = open(inFilePath, "rb") 
        # Write content as utf-8 data
        self.wfile.write(lFileObject.read())
        #Закрыть файловый объект
        lFileObject.close()        
    # GET
    def do_GET(self):
        lStudioFolder = "\\".join(__file__.split("\\")[:-1])
        #Мост между файлом и http запросом (новый формат)
        if self.path == "/":
            # Пример использования
            global gRender
            lStr = gRender.Generate(inDataDict={"title":"СТУДИЯ PYOPENRPA", "subtitle":"ПОИСК UIO СЕЛЕКТОРА", "version":__version__})
            # Send response status code
            self.send_response(200)
            # Send headers
            self.send_header('Content-type','text/html')
            self.end_headers()
            # Write content as utf-8 data
            self.wfile.write(bytes(lStr, "utf8"))
        #Мост между файлом и http запросом (новый формат)
        if self.path == '/3rdParty/Semantic-UI-CSS-master/semantic.min.css':
            self.SendResponseContentTypeFile('text/css', os.path.join(lStudioFolder, "..\\Resources\\Web\\Semantic-UI-CSS-master\\semantic.min.css"))
        #Мост между файлом и http запросом (новый формат)
        if self.path == '/3rdParty/Semantic-UI-CSS-master/semantic.min.js':
            self.SendResponseContentTypeFile('application/javascript', os.path.join(lStudioFolder, "..\\Resources\\Web\\Semantic-UI-CSS-master\\semantic.min.js"))
        #Мост между файлом и http запросом (новый формат)
        if self.path == '/3rdParty/jQuery/jquery-3.1.1.min.js':
            self.SendResponseContentTypeFile('application/javascript', os.path.join(lStudioFolder, "..\\Resources\\Web\\jQuery\\jquery-3.1.1.min.js"))
        #Мост между файлом и http запросом (новый формат)
        if self.path == '/3rdParty/Google/LatoItalic.css':
            self.SendResponseContentTypeFile('font/css', os.path.join(lStudioFolder, "..\\Resources\\Web\\Google\\LatoItalic.css"))
        #Мост между файлом и http запросом (новый формат)
        if self.path == '/3rdParty/Semantic-UI-CSS-master/themes/default/assets/fonts/icons.woff2':
            self.SendResponseContentTypeFile('font/woff2', os.path.join(lStudioFolder, "..\\Resources\\Web\\Semantic-UI-CSS-master\\themes\\default\\assets\\fonts\\icons.woff2"))
        #Мост между файлом и http запросом (новый формат)
        if self.path == '/favicon.ico':
            self.SendResponseContentTypeFile('image/x-icon', os.path.join(lStudioFolder, "..\\Resources\\Web\\orpa\\favicon.ico"))
		#Мост между файлом и http запросом (новый формат)
        if self.path == '/pyOpenRPA_logo.png' or self.path == '/orpa/resources/Web/orpa/logo.png':
            self.SendResponseContentTypeFile('image/png', os.path.join(lStudioFolder, "..\\Resources\\Web\\orpa\\logo.png"))
		#Мост между файлом и http запросом (новый формат)
        if self.path == '/pyOpenRPA_logo.png' or self.path == '/orpa/resources/Web/orpa/logo.png':
            self.SendResponseContentTypeFile('image/png', os.path.join(lStudioFolder, "..\\Resources\\Web\\orpa\\logo.png"))
        if self.path == '/orpa/resources/Web/orpa/styleset/home.css': self.SendResponseContentTypeFile('text/css', os.path.join(lStudioFolder, "..\\Resources\\Web\\orpa\\styleset\\home.css"))
        if self.path == '/orpa/resources/Web/orpa/styleset/home.js': self.SendResponseContentTypeFile('application/javascript', os.path.join(lStudioFolder, "..\\Resources\\Web\\orpa\\styleset\\home.js"))
        if self.path == '/orpa/resources/Web/orpa/styleset/bg1.jpg': self.SendResponseContentTypeFile('image/png', os.path.join(lStudioFolder, "..\\Resources\\Web\\orpa\\styleset\\bg1.jpg"))
        if self.path == '/orpa/resources/Web/orpa/styleset/bg2.jpg': self.SendResponseContentTypeFile('image/png', os.path.join(lStudioFolder, "..\\Resources\\Web\\orpa\\styleset\\bg2.jpg"))
        if self.path == '/orpa/resources/Web/orpa/styleset/bg3.jpg': self.SendResponseContentTypeFile('image/png', os.path.join(lStudioFolder, "..\\Resources\\Web\\orpa\\styleset\\bg3.jpg"))
        if self.path == '/orpa/resources/Web/orpa/styleset/bg4.jpg': self.SendResponseContentTypeFile('image/png', os.path.join(lStudioFolder, "..\\Resources\\Web\\orpa\\styleset\\bg4.jpg"))
        if self.path == '/orpa/resources/Web/orpa/styleset/bg5.jpg': self.SendResponseContentTypeFile('image/png', os.path.join(lStudioFolder, "..\\Resources\\Web\\orpa\\styleset\\bg5.jpg"))
        if self.path == '/orpa/resources/Web/orpa/styleset/bg6.jpg': self.SendResponseContentTypeFile('image/png', os.path.join(lStudioFolder, "..\\Resources\\Web\\orpa\\styleset\\bg6.jpg"))
        if self.path == '/orpa/resources/Web/orpa/styleset/bg7.jpg': self.SendResponseContentTypeFile('image/png', os.path.join(lStudioFolder, "..\\Resources\\Web\\orpa\\styleset\\bg7.jpg"))
        if self.path == '/orpa/resources/Web/orpa/styleset/bg8.jpg': self.SendResponseContentTypeFile('image/png', os.path.join(lStudioFolder, "..\\Resources\\Web\\orpa\\styleset\\bg8.jpg"))
        if self.path == '/orpa/resources/Web/orpa/styleset/bg9.jpg': self.SendResponseContentTypeFile('image/png', os.path.join(lStudioFolder, "..\\Resources\\Web\\orpa\\styleset\\bg9.jpg"))
        if self.path == '/orpa/resources/Web/orpa/styleset/bg10.jpg': self.SendResponseContentTypeFile('image/png', os.path.join(lStudioFolder, "..\\Resources\\Web\\orpa\\styleset\\bg10.jpg"))
        if self.path == '/orpa/resources/Web/Semantic-UI-CSS-master/components/site.css': self.SendResponseContentTypeFile('text/css', os.path.join(lStudioFolder, "..\\Resources\\Web\\Semantic-UI-CSS-master\\components\\site.css"))
        if self.path == '/orpa/resources/Web/Semantic-UI-CSS-master/components/reset.css': self.SendResponseContentTypeFile('text/css', os.path.join(lStudioFolder, "..\\Resources\\Web\\Semantic-UI-CSS-master\\components\\reset.css"))
        if self.path == '/orpa/resources/Web/Semantic-UI-CSS-master/components/container.css': self.SendResponseContentTypeFile('text/css', os.path.join(lStudioFolder, "..\\Resources\\Web\\Semantic-UI-CSS-master\\components\\container.css"))
        if self.path == '/orpa/resources/Web/Semantic-UI-CSS-master/components/grid.css': self.SendResponseContentTypeFile('text/css', os.path.join(lStudioFolder, "..\\Resources\\Web\\Semantic-UI-CSS-master\\components\\grid.css"))
        if self.path == '/orpa/resources/Web/Semantic-UI-CSS-master/components/header.css': self.SendResponseContentTypeFile('text/css', os.path.join(lStudioFolder, "..\\Resources\\Web\\Semantic-UI-CSS-master\\components\\header.css"))
        if self.path == '/orpa/resources/Web/Semantic-UI-CSS-master/components/image.css': self.SendResponseContentTypeFile('text/css', os.path.join(lStudioFolder, "..\\Resources\\Web\\Semantic-UI-CSS-master\\components\\image.css"))
        if self.path == '/orpa/resources/Web/Semantic-UI-CSS-master/components/divider.css': self.SendResponseContentTypeFile('text/css', os.path.join(lStudioFolder, "..\\Resources\\Web\\Semantic-UI-CSS-master\\components\\divider.css"))
        if self.path == '/orpa/resources/Web/Semantic-UI-CSS-master/components/menu.css': self.SendResponseContentTypeFile('text/css', os.path.join(lStudioFolder, "..\\Resources\\Web\\Semantic-UI-CSS-master\\components\\menu.css"))
        if self.path == '/orpa/resources/Web/Semantic-UI-CSS-master/components/dropdown.css': self.SendResponseContentTypeFile('text/css', os.path.join(lStudioFolder, "..\\Resources\\Web\\Semantic-UI-CSS-master\\components\\dropdown.css"))
        if self.path == '/orpa/resources/Web/Semantic-UI-CSS-master/components/segment.css': self.SendResponseContentTypeFile('text/css', os.path.join(lStudioFolder, "..\\Resources\\Web\\Semantic-UI-CSS-master\\components\\segment.css"))
        if self.path == '/orpa/resources/Web/Semantic-UI-CSS-master/components/button.css': self.SendResponseContentTypeFile('text/css', os.path.join(lStudioFolder, "..\\Resources\\Web\\Semantic-UI-CSS-master\\components\\button.css"))
        if self.path == '/orpa/resources/Web/Semantic-UI-CSS-master/components/list.css': self.SendResponseContentTypeFile('text/css', os.path.join(lStudioFolder, "..\\Resources\\Web\\Semantic-UI-CSS-master\\components\\list.css"))
        if self.path == '/orpa/resources/Web/Semantic-UI-CSS-master/components/sidebar.css': self.SendResponseContentTypeFile('text/css', os.path.join(lStudioFolder, "..\\Resources\\Web\\Semantic-UI-CSS-master\\components\\sidebar.css"))
        if self.path == '/orpa/resources/Web/Semantic-UI-CSS-master/components/icon.css': self.SendResponseContentTypeFile('text/css', os.path.join(lStudioFolder, "..\\Resources\\Web\\Semantic-UI-CSS-master\\components\\icon.css"))
        if self.path == '/orpa/resources/Web/Semantic-UI-CSS-master/components/transition.css': self.SendResponseContentTypeFile('text/css', os.path.join(lStudioFolder, "..\\Resources\\Web\\Semantic-UI-CSS-master\\components\\transition.css"))
        if self.path == '/orpa/resources/Web/orpa/styleset/sidebar.js': self.SendResponseContentTypeFile('application/javascript', os.path.join(lStudioFolder, "..\\Resources\\Web\\orpa\\styleset\\sidebar.js"))
        if self.path == '/orpa/resources/Web/orpa/styleset/transition.js': self.SendResponseContentTypeFile('application/javascript', os.path.join(lStudioFolder, "..\\Resources\\Web\\orpa\\styleset\\transition.js"))
        if self.path == '/orpa/resources/Web/orpa/styleset/docs.js': self.SendResponseContentTypeFile('application/javascript', os.path.join(lStudioFolder, "..\\Resources\\Web\\orpa\\styleset\\docs.js"))
        if self.path == '/orpa/resources/Web/orpa/styleset/visibility.js': self.SendResponseContentTypeFile('application/javascript', os.path.join(lStudioFolder, "..\\Resources\\Web\\orpa\\styleset\\visibility.js"))
        if self.path == '/orpa/resources/Web/orpa/styleset/highlight.min.js': self.SendResponseContentTypeFile('application/javascript', os.path.join(lStudioFolder, "..\\Resources\\Web\\orpa\\styleset\\highlight.min.js"))
        if self.path == '/orpa/resources/Web/orpa/styleset/less.min.js': self.SendResponseContentTypeFile('application/javascript', os.path.join(lStudioFolder, "..\\Resources\\Web\\orpa\\styleset\\less.min.js"))
        if self.path == '/orpa/resources/Web/orpa/styleset/easing.min.js': self.SendResponseContentTypeFile('application/javascript', os.path.join(lStudioFolder, "..\\Resources\\Web\\orpa\\styleset\\easing.min.js"))
        if self.path == '/metadata.json': self.SendResponseContentTypeFile('application/json', os.path.join(lStudioFolder, "..\\Resources\\Web\\orpa\\\styleset\\metadata.json"))
        if self.path == '/orpa/resources/Web/Semantic-UI-CSS-master/themes/default/assets/fonts/icons.woff2': self.SendResponseContentTypeFile('font/woff2', os.path.join(lStudioFolder, "..\\Resources\\Web\\Semantic-UI-CSS-master\\themes\\default\\assets\\fonts\\icons.woff2"))
        if self.path == '/orpa/resources/Web/Semantic-UI-CSS-master/themes/default/assets/fonts/icons.woff': self.SendResponseContentTypeFile('font/woff', os.path.join(lStudioFolder, "..\\Resources\\Web\\Semantic-UI-CSS-master\\themes\\default\\assets\\fonts\\icons.woff"))
        if self.path == '/orpa/resources/Web/Semantic-UI-CSS-master/themes/default/assets/fonts/icons.ttf': self.SendResponseContentTypeFile('font/ttf', os.path.join(lStudioFolder, "..\\Resources\\Web\\Semantic-UI-CSS-master\\themes\\default\\assets\\fonts\\icons.ttf"))
        if self.path == '/orpa/resources/Web/Semantic-UI-CSS-master/semantic.min.css': self.SendResponseContentTypeFile('text/css', os.path.join(lStudioFolder, "..\\Resources\\Web\\Semantic-UI-CSS-master\\semantic.min.css"))



    # POST
    def do_POST(self):
        #Restart studio
        if self.path == '/RestartStudio':
            #self.shutdown()
			# Send response status code
            self.send_response(200)
            # Send headers
            self.send_header('Content-type','application/json')
            self.end_headers()
            message = json.dumps({"Result":"Restart is in progress!"})
            # Write content as utf-8 data
            self.wfile.write(bytes(message, "utf8"))
            os.execl(sys.executable,os.path.abspath(__file__),*sys.argv)
            sys.exit(0)
        if self.path == '/GUIAction':
            #Обернуть в try, чтобы вернуть ответ, что сообщение не может быть обработано
            #   pdb.set_trace()
            # Send response status code
            self.send_response(200)
            # Send headers
            self.send_header('Content-type','application/json')
            self.end_headers()
            try:
                #ReadRequest
                lInputByteArrayLength = int(self.headers.get('Content-Length'))
                lInputByteArray=self.rfile.read(lInputByteArrayLength)
                #Превращение массива байт в объект
                lInputObject=json.loads(lInputByteArray.decode('utf8'))
                # Send message back to client
                #{'functionName':'', 'argsArray':[]}
                #pdb.set_trace()
                lRequestObject=lInputObject
                #Отправить команду роботу
                lResponseObject=RobotConnector.ActivityRun(lRequestObject)
                #Normalize JSON before send in response
                lResponseObject=JSONNormalize.JSONNormalizeDictList(lResponseObject)
                #Dump DICT LIST in JSON
                message = json.dumps(lResponseObject)
            except Exception as e:
                #Установить флаг ошибки
                lProcessResponse={"Result":None}
                lProcessResponse["ErrorFlag"]=True
                #Зафиксировать traceback
                lProcessResponse["ErrorTraceback"]=traceback.format_exc()
                #Зафиксировать Error message
                lProcessResponse["ErrorMessage"]=str(e)
                #lProcessResponse["ErrorArgs"]=str(e.args)
                message = json.dumps(lProcessResponse)     
            finally:
                # Write content as utf-8 data
                self.wfile.write(bytes(message, "utf8"))
        if self.path == '/GUIActionList':
            #ReadRequest
            lInputByteArrayLength = int(self.headers.get('Content-Length'))
            lInputByteArray=self.rfile.read(lInputByteArrayLength)
            #Превращение массива байт в объект
            lInputObject=json.loads(lInputByteArray.decode('utf8'))
            # Send response status code
            self.send_response(200)
            # Send headers
            self.send_header('Content-type','application/json')
            self.end_headers()
            # Send message back to client
            #{'functionName':'', 'argsArray':[]}
            lRequestObject=lInputObject
            lOutputObject=[]
            #pdb.set_trace()
            lResponseObject=RobotConnector.ActivityListRun(lRequestObject)
            #Сформировать текстовый ответ
            message = json.dumps(lResponseObject)
            # Write content as utf-8 data
            self.wfile.write(bytes(message, "utf8")) 
        return
    
def run():
    inServerAddress = "";
    inPort = gSettingsDict["Server"]["ListenPort"];
    # Server settings
    # Choose port 8080, for port 80, which is normally used for a http server, you need root access
    server_address = (inServerAddress, inPort)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    # Logging
    gSettingsDict["Logger"].info(f"Сервер:: Прослушиваемый URL: {inServerAddress}, Прослушиваемый порт: {inPort}")
    # Запуск адреса в браузере
    os.system(f"explorer http://127.0.0.1:{str(inPort)}")
    Usage.Process(inComponentStr="Studio")
    httpd.serve_forever()
run()
