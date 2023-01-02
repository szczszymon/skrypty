// Application using the 'Pug' template system
const express = require('express'),
    logger = require('morgan');
const fs = require("fs");
const app = express();
var x = 1;
var y = 2;

// Configuring the application
app.set('views', __dirname + '/views');               // Files with views can be found in the 'views' directory
app.set('view engine', 'pug');                        // Use the 'Pug' template system
app.locals.pretty = app.get('env') === 'development'; // The resulting HTML code will be indented in the development environment

// Determining the contents of the middleware stack
app.use(logger('dev'));                            // Add an HTTP request recorder to the stack — every request will be logged in the console in the 'dev' format
// app.use(express.static(__dirname + '/public')); // Place the built-in middleware 'express.static' — static content (files .css, .js, .jpg, etc.) will be provided from the 'public' directory

// *** Route definitions ***

// The first route
app.get('/', function (req, res) {
    res.render('index', { x: x, y: y, result: x + y }); // Render the 'index' view
});

app.get('/json/:name', function (req, res) {
    // Pobierz nazwę pliku JSON z parametru ścieżki
    const fileName = req.params.name;

    // Wczytaj zawartość pliku JSON o podanej nazwie
    const data = fs.readFileSync(`${fileName}.json`);
    const operations = JSON.parse(data);

    // Oblicz wynik dla każdej operacji
    for (const operation of operations) {
        switch (operation.operation) {
            case '+':
                operation.result = operation.x + operation.y;
                break;
            case '-':
                operation.result = operation.x -operation.y;
                break;
            case '*':
                operation.result = operation.x * operation.y;
                break;
            case '/':
                operation.result = operation.x / operation.y;
                break;
        }
    }

// Wygeneruj tabelę HTML z wynikami operacji
    const table = `<table> <tr> <th>X</th> <th>Operacja</th> <th>Y</th> <th>Wynik</th> </tr> ${operations.map(operation =>`
        <tr>
            <td>${operation.x}</td>
            <td>${operation.operation}</td>
            <td>${operation.y}</td>
            <td>${operation.result}</td>
        </tr>
    `).join('')} </table> `;

    const styl = `<style>
    table, td, th {
    text-align: center;
    border: 1px solid black;
    width: auto;
    }
    
    td {
    padding: 5px;
    }
    </style>`;

    const content = table + styl;

// Wyślij tabelę do przeglądarki
    res.send(content);
});

// The application is to listen on port number 3000
app.listen(3000, function () {
    console.log('The application is available on port 3000');
});