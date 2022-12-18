//Source:  https://codeforgeek.com/unit-testing-nodejs-application-using-mocha/
var supertest = require("supertest");

// This agent refers to PORT where program is runninng.
var server = supertest.agent("http://localhost:8000");

// UNIT test begin
describe('Test zadania 3', function () {
    it('Sprawdzenie pliku', function (done) {
        server
            .get('/submit?path=test.txt')
            .expect('Content-Type', /text\/plain/)
            .expect(200, "To jest plik.\n\nZawartość pliku:\n\nTo jest zawartość pliku testowego\n", done);
    });

    it('Sprawdzenie katalogu', function (done) {
        server
            .get('/submit?path=test')
            .expect('Content-Type', /text\/plain/)
            .expect(200, "To jest katalog.", done);
    });

    it('Błędna ścieżka', function (done) {
        server
            .get('/submit?path=asdasdasdasdasda')
            .expect('Content-Type', /text\/plain/)
            .expect(404, "Plik nie istnieje.", done);
    });
});