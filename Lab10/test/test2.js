const assert = require('assert');
const fs = require('fs');

const pathToFile = './test.txt';
const pathToDirectory = './test';

describe('Test zadania 2', () => {
  it('Podana nazwa powinna odpowiadać plikowi', () => {
    let output;
    try {
      const stats = fs.statSync(pathToFile);
      assert.strictEqual(stats.isFile(), true, `${pathToFile} powinien być plikiem`);
      output = fs.readFileSync(pathToFile, 'utf-8');
      assert.strictEqual(output, 'To jest zawartość pliku testowego\n');
    } catch (error) {
      console.error(`Test nie powiódł się: Nie udało się odczytać informacji o pliku ${pathToFile}: ${error}`);
    }
  });

  it('Podana nazwa powinna odpowiadać katalogowi', () => {
    try {
      const stats = fs.statSync(pathToDirectory);
      assert.strictEqual(stats.isDirectory(), true, `${pathToDirectory} powinien być katalogiem`);
    } catch (error) {
      console.error(`Test nie powiódł się: Nie udało się odczytać informacji o katalogu ${pathToDirectory}: ${error}`);
    }
  });
});
