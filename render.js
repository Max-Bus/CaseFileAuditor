const mainProcess = require('electron').remote.require('./main.js');
const dialog = require('electron').remote.dialog;

const inputBtn = document.getElementById('inputBtn');
const outputBtn = document.getElementById('outputBtn');
const diagnosisBtn = document.getElementById('diagnosisBtn')
const inputPathText = document.getElementById('inputPathText')
const outputPathText = document.getElementById('outputPathText')

var inputPath, outputPath;

inputBtn.onclick = selectInput;
outputBtn.onclick = selectOutput;
diagnosisBtn.onclick = runDiagnosisDev;

async function selectInput() {
    dialog.showOpenDialog(require('electron').remote.getCurrentWindow(), {
        buttonLabel: "Select Folder",
        properties: ['openDirectory']
    }).then((data) => {
        inputPath = data.filePaths;
        inputPathText.innerHTML = data.filePaths;
    });
}

async function selectOutput() {
    dialog.showOpenDialog(require('electron').remote.getCurrentWindow(), {
        buttonLabel: "Select Folder",
        properties: ['openDirectory']
    }).then((data) => {
        outputPath = data.filePaths;
        outputPathText.innerHTML = data.filePaths;
    });
}

async function runDiagnosisDev() {
    var python = require('child_process').spawn('python', ['./pyexe/eletest.py', inputPath, outputPath]);
    python.stdout.on('data',function(data){
        console.log("data: ",data.toString('utf8'));
    });
}

async function runDiagnosisBuild() {
    var child = require('child_process').execFile;
    var deconstructedPath = __dirname.split("\\");
    var newPath = "";
    for (var i = 0; i < deconstructedPath.length - 1; i++) {
        newPath += deconstructedPath[i] + "\\";
    }
    newPath += "eletest.exe";

    console.log(__dirname);
    console.log(newPath);

    child(newPath, [inputPath, outputPath], function(err, data) {
        if(err){
           console.error(err);
           return;
        }
     
        console.log(data.toString());
    });
}