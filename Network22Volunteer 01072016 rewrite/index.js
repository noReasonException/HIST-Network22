var electron = require('electron');
var app = electron.app;
var BrowserWindow = electron.BrowserWindow;
var exec = require('child_process').exec;

//exec('echo hey'function(error,stdout,stderr){
//console.log....
//})

function greek_flag(){

console.log(
    "%c    %c  %c                     \n" +
    "%c    %c  %c    %c               \n" +
    "%c          %c                 \n" +
    "%c    %c  %c    %c               \n" +
    "%c    %c  %c                     \n" +
    "%c                           \n" +
    "%c                           \n" +
    "%c                           \n" +
    "%c                           \n",
"background: #0072c7", "background: #ffffff", "background: #0072c7",
"background: #0072c7", "background: #ffffff", "background: #0072c7", "background: #ffffff",
"background: #ffffff", "background: #0072c7",
"background: #0072c7", "background: #ffffff", "background: #0072c7", "background: #ffffff",
"background: #0072c7", "background: #ffffff", "background: #0072c7",
"background: #ffffff",
"background: #0072c7",
"background: #ffffff",
"background: #0072c7");
}
app.on('ready',function(){
  var MainWindow = new BrowserWindow({
    width:600,
    height:600

  });
  MainWindow.alwaysOnTop(true);
  MainWindow.setFullScreen(true);
  MainWindow.loadURL('file://' + __dirname + '/SignIn.html');

});
greek_flag();
