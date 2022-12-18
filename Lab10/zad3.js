const fs = require('fs');
const http = require('http');

function requestListener(request, response) {
    var url = new URL(request.url, `http://${request.headers.host}`);

    if (url.pathname == '/submit') {
        if (request.method == 'GET') {
            let path = url.searchParams.get('path'); // Reading form input

            fs.stat(path, (err, stats) => {
                if (err) {
                    response.writeHead(404, { "Content-Type": "text/plain; charset=utf-8" });
                    response.write("Plik nie istnieje.");
                    response.end();
                    return;
                }// if err

                response.writeHead(200, { "Content-Type": "text/plain; charset=utf-8" });
                if (stats.isFile()){
                    response.write("To jest plik.\n");

                    fs.readFile(path, (err, data) => {
                        response.write("\nZawartość pliku:\n\n" + data);
                        response.end();
                    });
                }// if isFile

                else if (stats.isDirectory()) {
                    response.write("To jest katalog.")
                    response.end();
                }// else if is Directory

                else
                    response.end();
            });// fs.stat
        } // if GET

        else {
            response.write(`This application does not support the ${request.method} method`);
            response.end();
        }// else
    }// if submit

    else { // Generating the form
        response.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
        response.write(`<form method="GET" action="/submit">
	    					<label for="path">Podaj ścieżkę: </label>
	    					<input name="path">
	    					<br><br>
	    					<input type="submit">
	    					<input type="reset">
	    				</form>`);
        response.end();
    }// else form
}// requestListener()

var server = http.createServer(requestListener);
server.listen(8000);
console.log("The server was started on port 8000");
console.log("To stop the server, press 'CTRL + C'");