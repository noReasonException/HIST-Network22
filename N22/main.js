var app = require('app');  //εισαγωγη βιβιοθηκης
var BrowserWindow = require('browser-window');  // βιβλιοθηκη για να ανοιξει window
var exec = require('child_process').exec;



function ConnectToNetwork22(Username , Password){
  console.log('ConnectToNetwork22');
  var command = "python SignIn.py "+username+" "+password;
  console.log(command)
  exec(command,function(error,stdout,stderr){
    console.log(stdout);
  });
}



var mainWindow = null;

app.on('window-all-closed', function() {

  if (process.platform != 'darwin') {
    app.quit();
  }
});

app.on('ready', function() {
  mainWindow = new BrowserWindow({width: 567, height: 1000});
  mainWindow.loadURL('file://' + __dirname + '/SignIn.html');
  mainWindow.setFullScreen = true;
  mainWindow.alwaysOnTop=true;
  mainWindow.openDevTools();

  //μολις το κυριο παραθρο ζητηθει να κλεισει , τοτε εκτελειται η ανωνυμηfunction
  mainWindow.on('closed', function() {
    mainWindow = null;
  });
});
