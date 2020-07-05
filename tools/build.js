import * as fs from 'fs';
import {execSync} from "child_process";

function rmdir(path: string) {
  try { var files = fs.readdirSync(path); }
  catch(e) { return; }
  if (files.length > 0) {
    for (var i = 0; i < files.length; i++) {
      var filePath = path + '/' + files[i];
      if (fs.statSync(filePath).isFile()) {
        fs.unlinkSync(filePath);
      } else {
	rmdir(filePath);
      }
    }
  }
  fs.rmdirSync(path);
}

function mkdir(path: string) {
  fs.mkdirSync(path);
}

function cldir(path: string) {
  rmdir(path);
  mkdir(path);
}

function exec(cmd: string) {
  execSync(cmd, undefined);
}

function clean() {
  console.log("Cleaning...");
  cldir("./build");
  cldir("./pub");
  cldir("./lib");
}

function compile() {
  console.log("Compiling...");
  exec("node_modules/typescript/bin/tsc");
}

function bundle(debug: boolean) {
  console.log("Bundling...");
  exec("cp ./build/src/lib/* ./lib");
  exec("mv ./build/src/lib ./build/lib");
  exec("cp ./src/pub/lexicon.js ./pub");
  exec("cp ./src/pub/style.css ./pub");
  if (debug) {
    exec("browserify ./build/src/pub/viewer.js -s viewer > ./pub/viewer.js");
  } else {
    exec("browserify ./build/src/pub/viewer.js -s viewer | uglifyjs --screw-ie8 > ./pub/viewer.js");
  }
}

function build(debug: boolean) {
  let t0 = Date.now();
  clean();
  compile();
  bundle(debug);
  console.log("Build completed in " + (Date.now() - t0) + " ms");
}

build(true);