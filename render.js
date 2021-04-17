const mainProcess = require('electron').remote.require('./main.js');
const dialog = require('electron').remote.dialog;

const inputBtn = document.getElementById('inputBtn');
const outputBtn = document.getElementById('outputBtn');
const diagnosisBtn = document.getElementById('diagnosisBtn');
const inputPathText = document.getElementById('inputPathText');
const outputPathText = document.getElementById('outputPathText');
const progressText = document.getElementById('progressText');
const diagnosisPreview = document.getElementById('diagnosisPreview');

var inputPath = "", outputPath = "";
var currentlyDiagnosing = false;
var numOfDots = 0;

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
        progressText.innerHTML = "";

        if (inputPath.length === 0 || outputPath.length === 0)
            diagnosisBtn.disabled = true;
        else
            diagnosisBtn.disabled = false;
    });
}

async function selectOutput() {
    dialog.showOpenDialog(require('electron').remote.getCurrentWindow(), {
        buttonLabel: "Select Folder",
        properties: ['openDirectory']
    }).then((data) => {
        outputPath = data.filePaths;
        outputPathText.innerHTML = data.filePaths;
        progressText.innerHTML = "";

        if (inputPath.length === 0 || outputPath.length === 0)
            diagnosisBtn.disabled = true;
        else
            diagnosisBtn.disabled = false;
    });
}

async function runDiagnosisDev() {
    if (inputPath.length === 0 || outputPath.length === 0)
        return;
    if (currentlyDiagnosing)
        return;

    console.log("started diagnosis");
    currentlyDiagnosing = true;
    progressText.innerHTML = "Diagnosing";

    var python = require('child_process').spawn('python', ['./pyexe/eletest.py', inputPath, outputPath]);
    python.stdout.on('data',function(data){
        console.log("data: ",data.toString('utf8'));
        currentlyDiagnosing = false;
        progressText.innerHTML = "Finished";
        diagnosisPreview.innerHTML = data.toString('utf8');
    });

    diagnosisEllipses();
}

async function runDiagnosisBuild() {
    if (inputPath.length === 0 || outputPath.length === 0)
        return;
    if (currentlyDiagnosing)
        return;

    currentlyDiagnosing = true;
    progressText.innerHTML = "Diagnosing";

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

        currentlyDiagnosing = false;
        progressText.innerHTML = "Finished";
        diagnosisPreview.innerHTML = data.toString('utf8');
    });

    diagnosisEllipses();
}

async function diagnosisEllipses () {
    if (currentlyDiagnosing) {
        if (numOfDots === 0) {
            progressText.innerHTML = "Diagnosing";
        } else {
            progressText.innerHTML += ".";
        }

        numOfDots = (numOfDots + 1) % 4;
        setTimeout(() => { diagnosisEllipses(); }, 500);
    } else {
        numOfDots = 0;
    }
}