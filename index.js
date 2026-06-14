const http = require("http");

const REDIRECT_TO = "https://anthonyrohloff.github.io";

http.createServer((req, res) => {
  res.writeHead(301, { Location: REDIRECT_TO });
  res.end();
}).listen(process.env.PORT || 3000);
