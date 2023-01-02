// No use of any template system
const express = require('express'),
    logger = require('morgan');
const app = express();
const fs = require('fs');
const MongoClient = require('mongodb').MongoClient;
var x = 1;
var y = 2;

// Determining the contents of the middleware stack
app.use(logger('dev'));                            // Place an HTTP request recorder on the stack — each request will be logged in the console in 'dev' format
// app.use(express.static(__dirname + '/public')); // Place the built-in middleware 'express.static' — static content (files .css, .js, .jpg, etc.) will be provided from the 'public' directory

// *** Route definitions ***

app.get('/', function(req, res) {
    res.send(`<p>${x} + ${y} = ${x + y}</p>`);
});

const url = 'mongodb://localhost:27017';
const dbName = 'obliczenia';
let db;
const client = new MongoClient(url, { useNewUrlParser: true });
client.connect((err) => {
    if (err) {
        console.error(err);
        process.exit(1);
    }
    db = client.db(dbName);
});

app.get('/calculate/:operation/:x/:y', function(req, res) {
    const operation = req.params.operation;
    const x = parseInt(req.params.x, 10);
    const y = parseInt(req.params.y, 10);

    let result;
    switch (operation) {
        case '+':
            result = x + y;
            break;
        case '-':
            result = x - y;
            break;
        case '*':
            result = x * y;
            break;
        case '/':
            result = x / y;
            break;
    }// switch

    db.collection('obliczenia').insertOne({ operation, x, y });

    res.send(`<p>${x} ${operation} ${y} = ${result}</p>`);
});

app.get('/json/:name', function (req, res) {
    const fileName = req.params.name;

    const data = fs.readFileSync(`${fileName}.json`);
    const operations = JSON.parse(data);

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

    res.send(content);
});

// The first route
app.get('/org', function (req, res) {
    res.send(`
<!DOCTYPE html>
<html lang="en" data-bs-theme="dark">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD"
      crossorigin="anonymous">
    <title>Your first page</title>
    <style>
    table, td, th {
    text-align: center;
    border: 1px solid black;
    width: auto;
    }
    
    td {
    padding: 5px;
    }
    </style>
  </head>
  <body>
    <main class="container">
      <h1>Hello World</h1>
    </main>
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN"
      crossorigin="anonymous">
    </script>
  </body>
</html>
`); // Send a response to the browser
});

// The application is to listen on port number 3000
app.listen(3000, function () {
    console.log('The application is available on port 3000');
});