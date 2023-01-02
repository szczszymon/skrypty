var supertest = require("supertest");
const {expect} = require("chai");

var chai = require('chai');
chai.use(require('chai-json'));

// This agent refers to PORT where program is runninng.
var server = supertest.agent("http://localhost:3000");

// UNIT test begin
describe('Testy GET /', function() {
    it('respond with html', function(done) {
        server
            .get('/')
            .expect('Content-Type', /html/)
            .expect(200, done);
    });

    it('Test wyniku sumowania', function (done) {
        function testSumy(res) {
            if (res.text != '<p>1 + 2 = 3</p>')
                throw new Error('Wynik sumowania nie jest poprawny')
        }

        server
            .get('/')
            .expect('Content-Type', /html/)
            .expect(200)
            .expect(testSumy)
            .end(done)
    });
});

describe('Testy GET /json/:name', () => {
    it('Sprawdzenie poprawnosci pliku', function (done) {
        expect('./operacje.json').to.be.a.jsonFile().and.contain.jsonWithProps({
            "operation": "+",
            "x": 1,
            "y": 2
        })
        expect('./operacje.json').to.be.a.jsonFile().and.contain.jsonWithProps({
            "operation": "-",
            "x": 10,
            "y": 5
        })
        expect('./operacje.json').to.be.a.jsonFile().and.contain.jsonWithProps({
            "operation": "*",
            "x": 2,
            "y": 3
        })
        expect('./operacje.json').to.be.a.jsonFile().and.contain.jsonWithProps({
            "operation": "/",
            "x": 8,
            "y": 2
        })
        done()
    })

    it('Sprawdzenie poprawności wyników', async () => {
        function testTable(res){
            const lines = res.text.split('\n');
            const tb_res = [[1, 2, 3], [10, 5, 5], [2, 3, 6], [8, 2, 4]];
            let i = 0;

            for (const line of lines) {

                if (line.startsWith('<tr>')) {
                    const cells = line.split('<td>');

                    // Odczytanie tabeli
                    const x = parseInt(cells[1], 10);
                    const y = parseInt(cells[3], 10);
                    const result = parseInt(cells[4], 10);
                    console.log(cells);

                    // Sprawdzenie wyników
                    expect(x).toEqual(tb_res[i][0]);
                    expect(y).toEqual(tb_res[i][1]);
                    expect(result).toEqual(tb_res[i][2]);

                    i++;
                }// if
            }// for
        }//t estTable()

        server
            .get('/json/operacje')
            .expect('Content-Type', /html/)
            .expect(testTable)
            .expect(200);
    });
});