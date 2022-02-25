const { getElements } = require("./src/main");

const basePath = process.cwd();
const { startCreating, buildSetup } = require(`${basePath}/src/main.js`);

(() => {
  buildSetup();
  startCreating();
})();
