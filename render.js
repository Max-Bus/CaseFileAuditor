const dialog = require('electron').remote.dialog;

var inputPath, outputPath;

const inputBtn = document.getElementById('inputBtn');
const outputBtn = document.getElementById('outputBtn');
const inputPathText = document.getElementById('inputPathText')
const outputPathText = document.getElementById('outputPathText')

inputBtn.onclick = selectInput;
outputBtn.onclick = selectOutput;

async function selectInput() {
    dialog.showOpenDialog(require('electron').remote.getCurrentWindow(), {
        buttonLabel: "Select Folder",
        properties: ['openDirectory']
    }).then((data) => {
        inputPath = data.filePaths;
        inputPathText.innerHTML = inputPath;
    });
}

async function selectOutput() {
    dialog.showOpenDialog(require('electron').remote.getCurrentWindow(), {
        buttonLabel: "Select Folder",
        properties: ['openDirectory']
    }).then((data) => {
        outputPath = data.filePaths;
        outputPathText.innerHTML = outputPath;
    });
}